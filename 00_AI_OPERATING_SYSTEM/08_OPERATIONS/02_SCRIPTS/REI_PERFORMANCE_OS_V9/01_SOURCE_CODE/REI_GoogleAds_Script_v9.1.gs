/**
 * REI Google Ads Script v9.1
 * ─────────────────────────────────────────────────────────────────────────────
 * Runs INSIDE Google Ads → Tools → Bulk actions → Scripts.
 * Writes Google spend into the REI Performance OS v9 master sheet.
 *
 * WHY v9.1 REPLACES v9.0
 * v9.0 was written against AWQL ("FROM CAMPAIGN_PERFORMANCE_REPORT"), the old
 * AdWords API reporting language. Google removed it when that API sunset in 2022,
 * so v9.0 throws on its very first report call and can never have worked. Every
 * query here is GAQL, which is what Google Ads scripts accept today.
 *
 * v9.0 also wrote nine tabs. The v9 dashboard reads exactly one of them
 * (Google_Campaigns_Daily) plus Daily_Performance_Fact, so the other seven are
 * dropped. Less to break, and the run finishes in well under a minute.
 *
 * SETUP (one-time, ~3 minutes)
 *   1. Google Ads → Tools → Bulk actions → Scripts → + New script
 *   2. Name it "REI Performance OS v9 sync"
 *   3. Delete the placeholder code and paste this entire file
 *   4. Click Authorise, and approve both Google Ads and Google Sheets access
 *   5. Click Preview. Read the log — it must end with "Sync complete"
 *   6. Click Run
 *   7. Click "Create schedule" → Daily → 06:00 → Save
 *
 * The dashboard's own nightly sync runs at 05:00 SGT, so 06:00 here means Google
 * data lands after it. That is deliberate: the dashboard re-reads this tab on
 * every page open, so same-day figures still appear without waiting a full cycle.
 */

var CONFIG = {
  MASTER_SHEET_ID:    '167C_gZsN5RtImBFArt5hXcUqMAHlfJFqX52f0rN_pWk',
  HISTORY_START_DATE: '2025-09-01',   // GAQL wants YYYY-MM-DD, not YYYYMMDD
  SGD_RATE:           1.35            // applied only when the account is not already SGD
};

function main() {
  var ss       = SpreadsheetApp.openById(CONFIG.MASTER_SHEET_ID);
  var currency = AdsApp.currentAccount().getCurrencyCode().toUpperCase();
  var isSGD    = (currency === 'SGD');

  Logger.log('=== REI Google Ads sync v9.1 ===');
  Logger.log('Account  : ' + AdsApp.currentAccount().getName());
  Logger.log('Currency : ' + currency + (isSGD ? ' (no conversion)' : ' -> SGD @ ' + CONFIG.SGD_RATE));

  var written = syncDailyHistory(ss, isSGD);
  if (written === 0) {
    // Zero rows almost always means the query ran against the wrong account or the
    // date window predates the account. Say so rather than silently wiping the tab.
    Logger.log('WARNING: no rows returned. Check that this script is attached to the ad');
    Logger.log('account that actually spends, and that HISTORY_START_DATE is early enough.');
    return;
  }
  bridgeIntoDailyPerformanceFact(ss);
  Logger.log('=== Sync complete: ' + written + ' campaign-days ===');
}

/**
 * One row per campaign per day, from HISTORY_START_DATE to today.
 *
 * Campaign status is deliberately NOT filtered. Removed campaigns still spent real
 * money, and excluding them would quietly understate historical spend — which is the
 * exact class of bug that had the dashboard disagreeing with the ad platforms.
 */
function syncDailyHistory(ss, isSGD) {
  var today = Utilities.formatDate(new Date(), 'Asia/Singapore', 'yyyy-MM-dd');
  var query =
    'SELECT segments.date, campaign.id, campaign.name, campaign.advertising_channel_type, ' +
    'campaign.status, campaign_budget.amount_micros, metrics.cost_micros, ' +
    'metrics.impressions, metrics.clicks, metrics.conversions, metrics.conversions_value, ' +
    'metrics.ctr, metrics.average_cpc ' +
    'FROM campaign ' +
    "WHERE segments.date BETWEEN '" + CONFIG.HISTORY_START_DATE + "' AND '" + today + "'";

  var headers = ['date', 'campaignId', 'campaign', 'campaignType', 'status',
                 'dailyBudget', 'spend', 'impressions', 'clicks', 'conversions',
                 'conversionValue', 'ctr', 'avgCpc', 'roas', 'platform', 'updatedAt'];

  var rows = [];
  var now  = new Date().toISOString();
  var iter = AdsApp.report(query).rows();

  while (iter.hasNext()) {
    var r    = iter.next();
    var cost = money(r['metrics.cost_micros'], isSGD);
    var cval = money(r['metrics.conversions_value'], isSGD, true);   // value is NOT in micros
    var conv = num(r['metrics.conversions']);

    rows.push([
      r['segments.date'],
      r['campaign.id'],
      r['campaign.name'],
      r['campaign.advertising_channel_type'],
      status(r['campaign.status']),
      money(r['campaign_budget.amount_micros'], isSGD).toFixed(2),
      cost.toFixed(2),
      Math.round(num(r['metrics.impressions'])),
      Math.round(num(r['metrics.clicks'])),
      conv.toFixed(1),
      cval.toFixed(2),
      (num(r['metrics.ctr']) * 100).toFixed(2),        // GAQL returns a fraction
      money(r['metrics.average_cpc'], isSGD).toFixed(4),
      (cost > 0 ? cval / cost : 0).toFixed(2),
      'Google',
      now
    ]);
  }

  writeTab(ss, 'Google_Campaigns_Daily', headers, rows);
  Logger.log('Daily history: ' + rows.length + ' rows (' + CONFIG.HISTORY_START_DATE + ' -> ' + today + ')');
  return rows.length;
}

/**
 * Copy Google days into Daily_Performance_Fact, the table the dashboard reads.
 *
 * Existing non-Google rows are carried across untouched — this tab also holds every
 * Meta row, and rebuilding it without them would erase the Meta history.
 */
function bridgeIntoDailyPerformanceFact(ss) {
  var source = ss.getSheetByName('Google_Campaigns_Daily');
  if (!source || source.getLastRow() < 2) return;

  var values  = source.getDataRange().getValues();
  var srcHead = values.shift().map(String);
  var idx = {};
  srcHead.forEach(function (h, i) { idx[h] = i; });

  var target = ['date', 'platform', 'accountId', 'campaignId', 'campaignName', 'adSetId',
                'adSetName', 'adId', 'adName', 'objective', 'status', 'spend', 'impressions',
                'reach', 'clicks', 'linkClicks', 'leads', 'conversions', 'conversionValue',
                'ctr', 'cpc', 'cpl', 'sourceUpdatedAt', 'syncRunId'];

  var fact = ss.getSheetByName('Daily_Performance_Fact') || ss.insertSheet('Daily_Performance_Fact');
  var byKey = {};

  if (fact.getLastRow() > 1) {
    var existing = fact.getDataRange().getValues();
    var exHead   = existing.shift().map(String);
    existing.forEach(function (row) {
      var o = {};
      exHead.forEach(function (h, i) { o[h] = row[i]; });
      if (String(o.platform) !== 'Google') {
        byKey[[o.date, o.platform, o.campaignId, o.adSetId, o.adId].join('|')] = o;
      }
    });
  }

  var runId      = 'google-' + Utilities.formatDate(new Date(), 'Asia/Singapore', 'yyyyMMdd-HHmmss');
  var customerId = AdsApp.currentAccount().getCustomerId();

  values.forEach(function (r) {
    var spend = num(r[idx.spend]);
    var conv  = num(r[idx.conversions]);
    var o = {
      date: r[idx.date], platform: 'Google', accountId: customerId,
      campaignId: r[idx.campaignId], campaignName: r[idx.campaign],
      adSetId: '', adSetName: '', adId: '', adName: '',
      objective: r[idx.campaignType], status: r[idx.status],
      spend: spend, impressions: num(r[idx.impressions]), reach: 0,
      clicks: num(r[idx.clicks]), linkClicks: num(r[idx.clicks]),
      leads: conv, conversions: conv, conversionValue: num(r[idx.conversionValue]),
      ctr: num(r[idx.ctr]), cpc: num(r[idx.avgCpc]), cpl: conv ? spend / conv : 0,
      sourceUpdatedAt: r[idx.updatedAt] || new Date().toISOString(), syncRunId: runId
    };
    byKey[[o.date, o.platform, o.campaignId, o.adSetId, o.adId].join('|')] = o;
  });

  var out = [target];
  Object.keys(byKey).sort().forEach(function (k) {
    var o = byKey[k];
    out.push(target.map(function (h) { return o[h] === undefined ? '' : o[h]; }));
  });

  fact.clearContents();
  fact.getRange(1, 1, out.length, target.length).setValues(out);
  fact.setFrozenRows(1);
  Logger.log('Daily_Performance_Fact rebuilt: ' + (out.length - 1) + ' rows');
}

// ── helpers ──────────────────────────────────────────────────────────────────

/** GAQL returns money in micros. conversions_value is the one exception. */
function money(value, isSGD, alreadyWhole) {
  var n = num(value);
  var amount = alreadyWhole ? n : n / 1000000;
  return isSGD ? amount : amount * CONFIG.SGD_RATE;
}

function num(value) {
  if (typeof value === 'number') return isFinite(value) ? value : 0;
  var cleaned = String(value == null ? '' : value).replace(/,/g, '').replace(/%/g, '').trim();
  if (!cleaned || cleaned === '--') return 0;
  var parsed = Number(cleaned);
  return isFinite(parsed) ? parsed : 0;
}

function status(s) {
  s = String(s || '').toUpperCase();
  if (s === 'ENABLED') return 'Active';
  if (s === 'PAUSED')  return 'Paused';
  if (s === 'REMOVED') return 'Archived';
  return s || 'Unknown';
}

function writeTab(ss, tabName, headers, dataRows) {
  var sheet = ss.getSheetByName(tabName) || ss.insertSheet(tabName);
  sheet.clearContents();
  var all = [headers].concat(dataRows || []);
  sheet.getRange(1, 1, all.length, headers.length).setValues(all);
  sheet.setFrozenRows(1);
  sheet.getRange(1, 1, 1, headers.length)
    .setFontWeight('bold').setBackground('#34a853').setFontColor('#ffffff');
}
