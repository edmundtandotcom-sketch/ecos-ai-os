/**
 * REI Google Ads Script v9.0
 * ─────────────────────────────────────────────────────────────────────────────
 * Runs INSIDE Google Ads UI → Tools & Settings → Bulk Actions → Scripts
 * Pulls campaign data for Today, Yesterday, 7D, 14D, 30D, All Time, AND
 * a full day-by-day history tab so the dashboard can show any custom date range.
 *
 * SETUP (one-time, ~5 minutes):
 *   1. In Google Ads → Tools & Settings → Bulk Actions → Scripts → + New Script
 *   2. Paste this entire file
 *   3. Confirm MASTER_SHEET_ID matches your Google Sheet ID
 *   4. Click ▶ Preview to authorise (approve both Google Sheets & Google Ads access)
 *   5. Click ▶ Run once (historical pull from HISTORY_START_DATE to today)
 *   6. Click "Create schedule" → Daily → 6:00 AM SGT → Save
 *
 * WHAT THIS WRITES (to Master Sheet):
 *   Google_Campaigns_Today      — campaign spend for TODAY
 *   Google_Campaigns_Yesterday  — campaign spend for YESTERDAY
 *   Google_Campaigns_L7D        — campaign spend for LAST_7_DAYS
 *   Google_Campaigns_L14D       — campaign spend for LAST_14_DAYS
 *   Google_Campaigns_L30D       — campaign spend for LAST_30_DAYS
 *   Google_Campaigns_AllTime    — campaign spend for ALL_TIME
 *   Google_Campaigns            — legacy tab (LAST_30_DAYS, backward-compat)
 *   Google_AdGroups             — ad group metrics (LAST_30_DAYS)
 *   Google_Ads                  — ad metrics + creative thumbs + hook rate
 *   Google_Campaigns_Daily      ← NEW: one row per campaign per day from
 *                                  HISTORY_START_DATE to today. Used by
 *                                  dashboard custom date range picker.
 *
 * v8 CHANGES vs v7:
 *   - Adds HISTORY_START_DATE config (default: 2025-09-01)
 *   - Adds syncDailyHistory() — segments CAMPAIGN_PERFORMANCE_REPORT by Date
 *     and writes one row per campaign per day into Google_Campaigns_Daily tab
 *   - All existing period tabs unchanged
 */

// ─── CONFIGURATION ───────────────────────────────────────────────────────────
var CONFIG = {
  MASTER_SHEET_ID:    '167C_gZsN5RtImBFArt5hXcUqMAHlfJFqX52f0rN_pWk',
  SGD_RATE:           1.35,        // Applied only when account currency is NOT SGD
  INCLUDE_PAUSED:     true,        // Include paused campaigns in output
  HISTORY_START_DATE: '20250901',  // Daily history start (YYYYMMDD) — 1 Sep 2025
};

// ─── MAIN ────────────────────────────────────────────────────────────────────
function main() {
  var ss       = SpreadsheetApp.openById(CONFIG.MASTER_SHEET_ID);
  var currency = AdsApp.currentAccount().getCurrencyCode().toUpperCase();
  var isSGD    = (currency === 'SGD');

  Logger.log('=== REI Google Ads Sync v8 ===');
  Logger.log('Account  : ' + AdsApp.currentAccount().getName());
  Logger.log('Currency : ' + currency + (isSGD ? ' (no conversion)' : ' → SGD @ ' + CONFIG.SGD_RATE));

  Logger.log('--- Syncing campaigns: TODAY → Google_Campaigns_Today');
  syncCampaigns(ss, isSGD, 'TODAY', 'Google_Campaigns_Today');

  Logger.log('--- Syncing campaigns: YESTERDAY → Google_Campaigns_Yesterday');
  syncCampaigns(ss, isSGD, 'YESTERDAY', 'Google_Campaigns_Yesterday');

  Logger.log('--- Syncing campaigns: LAST_7_DAYS → Google_Campaigns_L7D');
  syncCampaigns(ss, isSGD, 'LAST_7_DAYS', 'Google_Campaigns_L7D');

  Logger.log('--- Syncing campaigns: LAST_14_DAYS → Google_Campaigns_L14D');
  syncCampaigns(ss, isSGD, 'LAST_14_DAYS', 'Google_Campaigns_L14D');

  Logger.log('--- Syncing campaigns: LAST_30_DAYS → Google_Campaigns_L30D');
  syncCampaigns(ss, isSGD, 'LAST_30_DAYS', 'Google_Campaigns_L30D');

  Logger.log('--- Syncing campaigns: ALL_TIME → Google_Campaigns_AllTime');
  syncCampaigns(ss, isSGD, 'ALL_TIME', 'Google_Campaigns_AllTime');

  // Legacy tab for backward compatibility
  syncCampaigns(ss, isSGD, 'LAST_30_DAYS', 'Google_Campaigns');

  Logger.log('--- Syncing ad groups and ads (LAST_30_DAYS)');
  syncAdGroups(ss, isSGD);
  syncAds(ss, isSGD);

  // ← NEW in v8: write daily history for custom date range support
  Logger.log('--- Syncing daily history: ' + CONFIG.HISTORY_START_DATE + ' → today');
  syncDailyHistory(ss, isSGD);

  Logger.log('--- Bridging Google daily history into Daily_Performance_Fact');
  syncDailyPerformanceFact(ss);

  Logger.log('=== Sync complete: ' + new Date().toISOString() + ' ===');
}

// ─── DAILY HISTORY (NEW v8) ───────────────────────────────────────────────────
/**
 * Writes Google_Campaigns_Daily: one row per campaign per day from
 * HISTORY_START_DATE through today. The dashboard reads this tab when the
 * user selects a custom date range and aggregates matching date rows.
 *
 * Columns match syncCampaigns() headers (same field order) EXCEPT:
 *   - 'date' column holds the actual segment date (not today's date)
 *   - This is what allows the dashboard to filter by any arbitrary range.
 *
 * NOTE: This overwrites the tab on every run. With ~300 days × ~10 campaigns
 * that's ~3,000 rows — well within Sheets limits. Runtime: ~30–60 seconds.
 */
function syncDailyHistory(ss, isSGD) {
  var startDate = CONFIG.HISTORY_START_DATE;        // e.g. '20250901'
  var endDate   = Utilities.formatDate(new Date(), 'Asia/Singapore', 'yyyyMMdd');
  var during    = startDate + ',' + endDate;

  var headers = [
    'date', 'campaignId', 'campaign', 'campaignType', 'status',
    'dailyBudget', 'spend', 'impressions', 'clicks', 'conversions', 'conversionValue',
    'ctr', 'avgCpc', 'roas', 'platform', 'updatedAt'
  ];

  // Adding 'Date' to SELECT auto-segments the report by day in AWQL.
  var report = AdsApp.report(
    'SELECT CampaignId, CampaignName, AdvertisingChannelType, CampaignStatus, ' +
    'Amount, Cost, Impressions, Clicks, Conversions, ConversionValue, Ctr, AverageCpc, Date ' +
    'FROM CAMPAIGN_PERFORMANCE_REPORT ' +
    'WHERE CampaignStatus IN [ENABLED, PAUSED] ' +
    'DURING ' + during
  );

  var rows = [];
  var now  = new Date().toISOString();
  var iter = report.rows();

  while (iter.hasNext()) {
    var r    = iter.next();
    var cost = toSGD(parseMetric(r['Cost']), isSGD);
    var bud  = toSGD(parseMetric(r['Amount']), isSGD);
    var conv = parseMetric(r['Conversions']);
    var cval = toSGD(parseMetric(r['ConversionValue']), isSGD);
    var roas = cost > 0 ? (cval / cost) : 0;
    var ctr  = parsePercent(r['Ctr']);
    var cpc  = toSGD(parseMetric(r['AverageCpc']), isSGD);

    // r['Date'] is the segment date in YYYY-MM-DD format (e.g. '2025-09-01')
    rows.push([
      r['Date'],                               // actual day — not today
      r['CampaignId'],
      r['CampaignName'],
      r['AdvertisingChannelType'],
      normaliseStatus(r['CampaignStatus']),
      bud.toFixed(2),
      cost.toFixed(2),
      Math.round(parseMetric(r['Impressions'])),
      Math.round(parseMetric(r['Clicks'])),
      conv.toFixed(1),
      cval.toFixed(2),
      ctr.toFixed(2),
      cpc.toFixed(4),
      roas.toFixed(2),
      'Google',
      now
    ]);
  }

  writeTab(ss, 'Google_Campaigns_Daily', headers, rows);
  Logger.log('Daily history synced: ' + rows.length + ' rows (' + startDate + ' → ' + endDate + ')');
}

// ─── HELPER: CURRENCY ────────────────────────────────────────────────────────
function toSGD(amount, isSGD) {
  return isSGD ? amount : amount * CONFIG.SGD_RATE;
}

// Google report values can contain commas and percentage signs.
function parseMetric(value) {
  if (typeof value === 'number') return isFinite(value) ? value : 0;
  var cleaned = String(value == null ? '' : value)
    .replace(/,/g, '')
    .replace(/%/g, '')
    .trim();
  if (!cleaned || cleaned === '--') return 0;
  var parsed = Number(cleaned);
  return isFinite(parsed) ? parsed : 0;
}

// Returns display percentage units: '0.65%' -> 0.65 and 0.0065 -> 0.65.
function parsePercent(value) {
  var raw    = String(value == null ? '' : value);
  var parsed = parseMetric(value);
  return raw.indexOf('%') >= 0 ? parsed : parsed * 100;
}

function singaporeDate() {
  return Utilities.formatDate(new Date(), 'Asia/Singapore', 'yyyy-MM-dd');
}

// ─── HELPER: STATUS NORMALISE ─────────────────────────────────────────────────
function normaliseStatus(s) {
  s = (s || '').toUpperCase();
  if (s === 'ENABLED')  return 'Active';
  if (s === 'PAUSED')   return 'Paused';
  if (s === 'REMOVED')  return 'Archived';
  return s || 'Unknown';
}

// ─── HELPER: EXTRACT YOUTUBE VIDEO ID ────────────────────────────────────────
function extractYouTubeId(url) {
  if (!url) return '';
  var m = url.match(/(?:youtube\.com\/(?:watch\?v=|shorts\/|embed\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})/);
  return m ? m[1] : '';
}

function ytThumb(videoId) {
  return videoId ? 'https://i.ytimg.com/vi/' + encodeURIComponent(videoId) + '/hqdefault.jpg' : '';
}

// ─── HELPER: DETECT FORMAT FROM GOOGLE AD TYPE ───────────────────────────────
function detectGoogleFormat(adType) {
  var t = (adType || '').toUpperCase();
  if (t.includes('VIDEO')   || t.includes('YOUTUBE'))          return 'Video';
  if (t.includes('RESPONSIVE_DISPLAY') || t.includes('IMAGE')) return 'Image';
  if (t.includes('RESPONSIVE_SEARCH')  || t.includes('RSA'))   return 'RSA';
  if (t.includes('EXPANDED_TEXT')      || t.includes('TEXT'))  return 'Text';
  if (t.includes('CALL'))                                       return 'Call';
  return 'Other';
}

// ─── CAMPAIGNS (period tabs) ─────────────────────────────────────────────────
function syncCampaigns(ss, isSGD, dateRange, tabName) {
  dateRange = dateRange || 'LAST_30_DAYS';
  tabName   = tabName   || 'Google_Campaigns';

  var headers = [
    'date', 'campaignId', 'campaign', 'campaignType', 'status',
    'dailyBudget', 'spend', 'impressions', 'clicks', 'conversions', 'conversionValue',
    'ctr', 'avgCpc', 'roas', 'platform', 'updatedAt'
  ];

  var report = AdsApp.report(
    'SELECT CampaignId, CampaignName, AdvertisingChannelType, CampaignStatus, ' +
    'Amount, Cost, Impressions, Clicks, Conversions, ConversionValue, Ctr, AverageCpc ' +
    'FROM CAMPAIGN_PERFORMANCE_REPORT ' +
    'WHERE CampaignStatus IN [ENABLED, PAUSED] ' +
    'DURING ' + dateRange
  );

  var rows  = [];
  var today = singaporeDate();
  var iter  = report.rows();

  while (iter.hasNext()) {
    var r    = iter.next();
    var cost = toSGD(parseMetric(r['Cost']), isSGD);
    var bud  = toSGD(parseMetric(r['Amount']), isSGD);
    var conv = parseMetric(r['Conversions']);
    var cval = toSGD(parseMetric(r['ConversionValue']), isSGD);
    var roas = cost > 0 ? (cval / cost) : 0;
    var ctr  = parsePercent(r['Ctr']);
    var cpc  = toSGD(parseMetric(r['AverageCpc']), isSGD);

    rows.push([
      today,
      r['CampaignId'],
      r['CampaignName'],
      r['AdvertisingChannelType'],
      normaliseStatus(r['CampaignStatus']),
      bud.toFixed(2),
      cost.toFixed(2),
      Math.round(parseMetric(r['Impressions'])),
      Math.round(parseMetric(r['Clicks'])),
      conv.toFixed(1),
      cval.toFixed(2),
      ctr.toFixed(2),
      cpc.toFixed(4),
      roas.toFixed(2),
      'Google',
      new Date().toISOString()
    ]);
  }

  writeTab(ss, tabName, headers, rows);
  Logger.log('Campaigns synced (' + dateRange + '): ' + rows.length + ' → ' + tabName);
}

// ─── AD GROUPS ───────────────────────────────────────────────────────────────
function syncAdGroups(ss, isSGD) {
  var headers = [
    'date', 'adGroupId', 'adGroup', 'campaignId', 'campaign', 'adGroupType', 'status',
    'spend', 'impressions', 'clicks', 'conversions', 'ctr', 'avgCpc', 'platform', 'updatedAt'
  ];

  var report = AdsApp.report(
    'SELECT AdGroupId, AdGroupName, CampaignId, CampaignName, AdGroupType, AdGroupStatus, ' +
    'Cost, Impressions, Clicks, Conversions, Ctr, AverageCpc ' +
    'FROM ADGROUP_PERFORMANCE_REPORT ' +
    'WHERE AdGroupStatus IN [ENABLED, PAUSED] ' +
    'DURING LAST_30_DAYS'
  );

  var rows  = [];
  var today = singaporeDate();
  var iter  = report.rows();

  while (iter.hasNext()) {
    var r    = iter.next();
    var cost = toSGD(parseMetric(r['Cost']), isSGD);
    var ctr  = parsePercent(r['Ctr']);
    var cpc  = toSGD(parseMetric(r['AverageCpc']), isSGD);

    rows.push([
      today,
      r['AdGroupId'],
      r['AdGroupName'],
      r['CampaignId'],
      r['CampaignName'],
      r['AdGroupType'] || '',
      normaliseStatus(r['AdGroupStatus']),
      cost.toFixed(2),
      Math.round(parseMetric(r['Impressions'])),
      Math.round(parseMetric(r['Clicks'])),
      parseMetric(r['Conversions']),
      ctr.toFixed(2),
      cpc.toFixed(4),
      'Google',
      new Date().toISOString()
    ]);
  }

  writeTab(ss, 'Google_AdGroups', headers, rows);
  Logger.log('Ad Groups synced: ' + rows.length);
}

// ─── ADS WITH CREATIVES ───────────────────────────────────────────────────────
function syncAds(ss, isSGD) {
  var videoMap = buildVideoMap();
  Logger.log('Video map built: ' + Object.keys(videoMap).length + ' video ads found');

  var headers = [
    'date', 'adId', 'adName', 'adGroupId', 'adGroup', 'campaignId', 'campaign',
    'adType', 'format', 'status', 'finalUrl',
    'impressions', 'clicks', 'spend', 'conversions', 'ctr', 'avgCpc',
    'videoId', 'thumbUrl', 'hookrate', 'adText',
    'platform', 'updatedAt'
  ];

  var report = AdsApp.report(
    'SELECT Id, AdGroupId, AdGroupName, CampaignId, CampaignName, ' +
    'AdType, Status, Headline, HeadlinePart1, HeadlinePart2, Description1, ' +
    'CreativeFinalUrls, ' +
    'Cost, Impressions, Clicks, Conversions, Ctr, AverageCpc ' +
    'FROM AD_PERFORMANCE_REPORT ' +
    'WHERE Status IN [ENABLED, PAUSED] ' +
    'DURING LAST_30_DAYS'
  );

  var rows  = [];
  var today = singaporeDate();
  var iter  = report.rows();

  while (iter.hasNext()) {
    var r    = iter.next();
    var adId = r['Id'];
    var cost = toSGD(parseMetric(r['Cost']), isSGD);
    var ctr  = parsePercent(r['Ctr']);
    var cpc  = toSGD(parseMetric(r['AverageCpc']), isSGD);
    var adType = r['AdType'] || '';

    var adText = [
      r['HeadlinePart1'] || r['Headline'] || '',
      r['HeadlinePart2'] || ''
    ].filter(Boolean).slice(0, 2).join(' | ');
    if (!adText && r['Description1']) adText = r['Description1'];

    var finalUrl = '';
    try {
      var raw     = r['CreativeFinalUrls'] || '';
      var cleaned = raw.replace(/[\[\]']/g, '').trim();
      finalUrl    = cleaned.split(',')[0].trim();
    } catch(e) { finalUrl = ''; }

    var vid      = videoMap['ag:' + r['AdGroupId']] || videoMap[adId] || {};
    var videoId  = vid.videoId  || '';
    var hookrate = vid.hookrate || 0;

    if (!videoId && finalUrl) videoId = extractYouTubeId(finalUrl);
    var thumbUrl = ytThumb(videoId);
    var format   = detectGoogleFormat(adType);

    rows.push([
      today,
      adId,
      r['AdGroupName'] + ' — ' + (adText || adId).slice(0, 50),
      r['AdGroupId'],
      r['AdGroupName'],
      r['CampaignId'],
      r['CampaignName'],
      adType,
      format,
      normaliseStatus(r['Status']),
      finalUrl,
      Math.round(parseMetric(r['Impressions'])),
      Math.round(parseMetric(r['Clicks'])),
      cost.toFixed(2),
      parseMetric(r['Conversions']),
      ctr.toFixed(2),
      cpc.toFixed(4),
      videoId,
      thumbUrl,
      hookrate.toFixed(2),
      adText,
      'Google',
      new Date().toISOString()
    ]);
  }

  writeTab(ss, 'Google_Ads', headers, rows);
  Logger.log('Ads synced: ' + rows.length);
}

// ─── VIDEO MAP ────────────────────────────────────────────────────────────────
function buildVideoMap() {
  var map = {};
  try {
    var report = AdsApp.report(
      'SELECT AdGroupId, AdGroupName, CampaignId, VideoId, VideoTitle, ' +
      'VideoQuartile25Rate, VideoQuartile50Rate, VideoViews, Impressions ' +
      'FROM VIDEO_PERFORMANCE_REPORT ' +
      'DURING LAST_30_DAYS'
    );
    var iter = report.rows();
    while (iter.hasNext()) {
      var r        = iter.next();
      var ytId     = r['VideoId']   || '';
      var agId     = r['AdGroupId'] || '';
      var q25      = parsePercent(r['VideoQuartile25Rate']);
      var views    = Math.round(parseMetric(r['VideoViews']));
      var impr     = Math.round(parseMetric(r['Impressions']));
      var hookrate = q25;
      var key      = agId + '|' + ytId;
      var videoData = { videoId: ytId, hookrate: hookrate, videoViews: views, impressions: impr };
      map[key] = videoData;
      var groupKey = 'ag:' + agId;
      if (!map[groupKey] || impr > (map[groupKey].impressions || 0)) map[groupKey] = videoData;
      if (ytId && !map[ytId]) map[ytId] = { videoId: ytId, hookrate: hookrate, videoViews: views };
    }
  } catch (e) {
    Logger.log('buildVideoMap warning: ' + e.message + ' — video thumbnails may be skipped');
  }
  return map;
}

// ─── WRITE TAB ───────────────────────────────────────────────────────────────
function writeTab(ss, tabName, headers, dataRows) {
  var sheet = ss.getSheetByName(tabName);
  if (!sheet) sheet = ss.insertSheet(tabName);
  sheet.clearContents();
  if (!dataRows || dataRows.length === 0) {
    sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  } else {
    var all = [headers].concat(dataRows);
    sheet.getRange(1, 1, all.length, headers.length).setValues(all);
  }
  sheet.setFrozenRows(1);
  sheet.getRange(1, 1, 1, headers.length)
    .setFontWeight('bold')
    .setBackground('#34a853')
    .setFontColor('#ffffff');
  Logger.log('  Wrote ' + dataRows.length + ' rows → ' + tabName);
}


// ─── V9 DAILY FACT BRIDGE ────────────────────────────────────────────────────
function syncDailyPerformanceFact(ss) {
  var source = ss.getSheetByName('Google_Campaigns_Daily');
  if (!source || source.getLastRow() < 2) return;
  var values = source.getDataRange().getValues();
  var headers = values.shift().map(function(h){ return String(h); });
  var idx = {}; headers.forEach(function(h,i){ idx[h]=i; });
  var targetHeaders = ['date','platform','accountId','campaignId','campaignName','adSetId','adSetName','adId','adName','objective','status','spend','impressions','reach','clicks','linkClicks','leads','conversions','conversionValue','ctr','cpc','cpl','sourceUpdatedAt','syncRunId'];
  var fact = ss.getSheetByName('Daily_Performance_Fact') || ss.insertSheet('Daily_Performance_Fact');
  var existing = fact.getLastRow()>1 ? fact.getDataRange().getValues() : [targetHeaders];
  var existingHeaders = existing.shift().map(function(h){return String(h);});
  var rowsByKey = {};
  existing.forEach(function(r){
    var o={}; existingHeaders.forEach(function(h,i){o[h]=r[i];});
    if(String(o.platform)!=='Google') rowsByKey[[o.date,o.platform,o.campaignId,o.adSetId,o.adId].join('|')]=o;
  });
  var runId='google-'+Utilities.formatDate(new Date(),'Asia/Singapore','yyyyMMdd-HHmmss');
  values.forEach(function(r){
    var spend=parseMetric(r[idx.spend]), conv=parseMetric(r[idx.conversions]);
    var o={date:r[idx.date],platform:'Google',accountId:AdsApp.currentAccount().getCustomerId(),campaignId:r[idx.campaignId],campaignName:r[idx.campaign],adSetId:'',adSetName:'',adId:'',adName:'',objective:r[idx.campaignType],status:r[idx.status],spend:spend,impressions:parseMetric(r[idx.impressions]),reach:0,clicks:parseMetric(r[idx.clicks]),linkClicks:parseMetric(r[idx.clicks]),leads:conv,conversions:conv,conversionValue:parseMetric(r[idx.conversionValue]),ctr:parseMetric(r[idx.ctr]),cpc:parseMetric(r[idx.avgCpc]),cpl:conv?spend/conv:0,sourceUpdatedAt:r[idx.updatedAt]||new Date().toISOString(),syncRunId:runId};
    rowsByKey[[o.date,o.platform,o.campaignId,o.adSetId,o.adId].join('|')]=o;
  });
  var out=[targetHeaders]; Object.keys(rowsByKey).sort().forEach(function(k){var o=rowsByKey[k];out.push(targetHeaders.map(function(h){return o[h]===undefined?'':o[h];}));});
  fact.clearContents(); fact.getRange(1,1,out.length,targetHeaders.length).setValues(out); fact.setFrozenRows(1);
}
