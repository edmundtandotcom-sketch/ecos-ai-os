/**
 * File version: Apps Script v8.43
 * REI Creative Intelligence — Apps Script v8.24
 *
 * v8.30 Leads table header fix:
 *  - Lead table column header now pins directly under the frozen Leads panel.
 *  - Removes the overflow/sticky conflict that could place the header between lead rows.
 *
 * v8.29 UI polish:
 *  - Leads Quality/Urgency filters moved into the Leads header row to save vertical space.
 *  - Leads KPI cards made compact so the full funnel fits across the dashboard width.
 *  - Leads table now uses full page scroll instead of a small inner vertical scroll frame.
 *
 * v8.28 updates:
 *  - Adds Booked Call as its own GHL/dashboard pipeline stage between Responded and Appointment.
 *  - Lead KPI card clicks now match card counts using cumulative stage filters for the selected period.
 *  - Leads cards now show Lead → Responded → Booked Call → Appointment → Strategy Session → Closed.
 *  - CEO/Overview cards separate Booked Calls from Appointments.
 *
 * v8.27 hotfix:
 *  - Loads sheet data first on page load / Sync Now, then refreshes Meta/GHL in background.
 *  - Prevents a slow Meta/GHL API call from leaving the dashboard empty.
 *
 * v8.26 hotfix:
 *  - Fixes blank dashboard caused by Apps Script template escaping a YouTube regex.
 *
 * v8.25 fixes:
 *  - Meta Today/Yesterday spend uses explicit Singapore calendar dates instead of native preset drift.
 *  - Browser merge now replaces period-scoped Meta/Google rows, preventing stale spend on short periods.
 *  - Sync Meta button respects the selected date period.
 *  - CEO/Overview cards use Strategy Sessions and Cost / Strategy Session instead of Qualified.
 *  - Leads default to latest received date; Campaigns/Ad Sets/Creatives default-sort for media buying.
 *  - Leads page control area sticks while only the lead table scrolls.
 *  - YouTube playback fallback no longer opens broken IDs automatically; it prefers real source links.
 *
 * v8.24 fixes:
 *  - Meta Today/Yesterday now use Meta native account-day presets instead of fragile custom time_range.
 *  - All sheet/lead date parsing is forced to Asia/Singapore for midnight-safe lead counts.
 *  - Google/YouTube thumbnail clicks open the direct YouTube watch page instead of fragile embeds.
 *
 * v8.23 fixes:
 *  - Today/yesterday lead counts use Singapore opt-in date and force GHL refresh on period change.
 *  - GHL → dashboard pipeline pull maps pipelineStageId directly and uses correct funnel stage ranking.
 *  - Sticky header/filter/tab offsets auto-calculate after wrapping.
 *  - YouTube lightbox also extracts video IDs from thumbnail URLs.
 *
 * v8.22 fixes:
 *  - Auto GHL refresh while dashboard is open (poll + refocus refresh) and helper trigger.
 *  - Urgency Timeline field added to leads with sorting/filtering and settings playbook.
 *  - Combined CEO Overview, sticky tab bar, and stronger Google video thumbnail fallback.
 *
 * v8.21 fixes:
 *  - Singapore-safe date normalisation prevents June 22 leads displaying as June 21.
 *  - Actual GHL Meta/Google leads drive CEO KPIs and CPL; pixel conversions stay diagnostic.
 *  - Google spend follows Today/Yesterday/7/14/30/All-time period tabs from Google Ads v3.
 *  - Lead attribution IDs are enriched to real ad and campaign names.
 *  - Quality, Closed status, deal value, and notes persist back to GHL_Leads.
 *  - Google video thumbnails play in an embedded YouTube lightbox.
 *
 * v8.3 fixes:
 *  F1. PERIOD BUTTONS — clicking 7d/14d/30d now triggers syncmeta with that
 *      datePreset then reloads from sheets. Default = last_7d.
 *  F2. LP DEDUPLICATION — within-tab dedup by normalised phone + spam filter.
 *  F3. CEO CAMPAIGN FUNNEL — uses Meta API lead count; fuzzy name matching;
 *      shows 0 instead of — for funnel stages; same fix in Campaigns table.
 *  F4. KILL SIGNAL — fires on: (a) no leads + min spend, OR (b) low hook +
 *      high CPL once spend threshold met. Previous logic only killed on ld===0.
 *  F5. LIGHTBOX — Meta CDN videos play via Facebook embed iframe (videoId).
 *      Image lightbox has min-width. Placeholder thumbnail clicks to play
 *      video if videoId exists.
 *  F6. GOOGLE ADS MAPPING — mergeApiData() remaps sheet column names
 *      (adName→name, campaign→campaignName, adGroup→adsetName, conversions→leads,
 *      avgCpc→cpc etc) so Google Ads data appears correctly in all tabs.
 *
 * v8.2 changes:
 *  12. DASHBOARD SERVED DIRECTLY — doGet() with no action param serves REI_Dashboard_v11.html.
 *      Auto-syncs Meta on load. URL is self-detected. Web App URL settings field removed.
 *  13. SORT — Meta API calls sorted by updated_time_descending (latest 50 always).
 *
 * v8.1 additions:
 *  10. META VIDEO THUMBNAILS — resolveMetaVideoThumbnails() fetches picture URL
 *      via /{video_id}?fields=picture,thumbnails for ads where thumbnail_url is empty.
 *  11. GOOGLE ADS SCHEMA — Google_Ads/Campaigns/AdGroups tabs updated to match
 *      REI_GoogleAds_Script.gs output: thumbUrl, videoId, hookrate, adText, format,
 *      dailyBudget, platform, updatedAt, adGroupType columns added.
 *
 * v8 changes:
 *   1. CURRENCY FIX — detect ad account currency; apply SGD_RATE ONLY if account
 *      is in USD. If already SGD (most SG advertisers), spend is used as-is.
 *      This was the primary cause of figures being ~35% higher than Ads Manager.
 *   2. LEAD COUNTING FIX — standardised to `||` at ALL levels (campaign/adset/ad).
 *      Using `+` at ad level double-counted form leads + pixel leads.
 *   3. SHEET-FIRST ARCHITECTURE — `action=getfromsheets` reads all data from
 *      pre-populated Meta_* sheets. Dashboard no longer calls Meta API on demand.
 *   4. SYNC ENDPOINT — `action=syncmeta` triggers a fresh Meta API pull and
 *      writes to Meta_Campaigns / Meta_AdSets / Meta_Ads / Meta_Leads tabs.
 *   5. SETUP ENDPOINT — `action=setup` creates all required sheet tabs with
 *      correct column schemas (Meta_*, Google_*, GHL_Leads, Referrals_Organic).
 *   6. HOURLY AUTO-SYNC — setupHourlyTrigger() installs a time-driven trigger.
 *   7. FULL FUNNEL — computeFunnelByCampaign() aggregates GHL lead statuses
 *      (Responded, Appt, SS, Qualified, Closed/Revenue) per campaign name.
 *   8. LEAD QUALITY — reads `quality` column from GHL_Leads tab (Real/Junk/Fake).
 *   9. GOOGLE ADS TABS — setupDataTabs() creates Google_Campaigns, Google_AdGroups,
 *      Google_Ads tabs ready to receive the Google Ads scheduled report.
 *
 * SECURITY: Meta token stored via storeSecrets() → PropertiesService.getScriptProperties()
 *           NEVER write token into any spreadsheet cell.
 *
 * Deploy → New deployment → Web App → Execute as Me → Anyone
 */

// ─── CONFIGURATION ────────────────────────────────────────────────────────────
const MASTER_SHEET_ID = PropertiesService.getScriptProperties().getProperty('SHEET_ID')
  || '1Wp3zxkQkB7WzlqOaAQENzwJIKjEqzJ42628Q6JCoU0Y';

const LP_LEADS_SHEET_ID = '1y7XHCCvdcxjYkaQhi2ZnFfMsOukdNRN_Rwf7abvDygM';

const META_API_VER = 'v19.0';
const SGD_RATE     = 1.35; // Only applied when ad account currency is USD
const GHL_API_BASE = 'https://services.leadconnectorhq.com';

// ─── ENTRY POINT ──────────────────────────────────────────────────────────────
function doGet(e) {
  // Serve dashboard HTML when accessed with no action parameter
  if (!e || !e.parameter || !e.parameter.action) {
    return HtmlService.createHtmlOutput(getDashboardHtml(ScriptApp.getService().getUrl()))
      .setTitle('REI Media Buyer Dashboard v8.43')
      .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
  }

  const action     = e.parameter.action.toLowerCase();

  // Serve JS as external file — bypasses GAS inline-script CSP restriction
  if (action === 'getscript') {
    return ContentService.createTextOutput(getDashboardJs())
      .setMimeType(ContentService.MimeType.JAVASCRIPT);
  }

  let datePreset = e.parameter.datePreset || 'last_7d';
  const requestedDatePreset = datePreset;
  // v8.24: Today/Yesterday should match Meta Ads Manager's account-day preset.
  // The prior custom Singapore time_range path was fragile and caused incorrect spend on short periods.
  const token      = PropertiesService.getScriptProperties().getProperty('META_ACCESS_TOKEN');

  let result;
  try {
    if (action === 'storetoken') {
      result = { ok: false, error: 'Use storeSecrets() from Script Editor to store token.' };

    } else if (action === 'getghlleads') {
      result = fetchGHLLeads();

    } else if (action === 'syncghl') {
      // v8.15: fetch GHL pipeline leads → write to GHL_Leads sheet → return count
      result = fetchGHLLeads();

    } else if (action === 'updateghl') {
      // v8.14: bidirectional — update GHL opportunity stage from dashboard
      result = updateGHLOpportunity(e.parameter.ghlId, e.parameter.status, e.parameter.dealValue);

    } else if (action === 'updatequality') {
      result = updateLeadQuality(e.parameter.ghlId, e.parameter.quality);

    } else if (action === 'updatelead') {
      result = updateLeadRecord(e.parameter.ghlId, e.parameter.status, e.parameter.quality,
        e.parameter.dealValue, e.parameter.notes, e.parameter.urgencyTimeline);

    } else if (action === 'deletelead') {
      result = deleteLeadRecord(e.parameter.ghlId);

    } else if (action === 'getfromsheets') {
      // PRIMARY PATH — reads all data from pre-populated sheets (fast, no API call)
      // v8.19: accept preset so Google Ads data is read from the matching period tab
      const sheetPreset = (e.parameter.preset || 'last_7_days').toLowerCase();
      result = fetchAllDataFromSheets(sheetPreset);

    } else if (action === 'syncmeta') {
      // Triggered by dashboard "Sync Now" button — pulls fresh Meta API data → writes to sheets
      if (!token) throw new Error('META_ACCESS_TOKEN not set. Run storeSecrets() from Script Editor.');
      const data = fetchAllData(token, datePreset, requestedDatePreset);
      writeToSheet(data);
      result = {
        ok: true,
        syncedAt: new Date().toISOString(),
        campaigns: data.campaigns.length,
        adsets: data.adsets.length,
        ads: data.ads.length
      };

    } else if (action === 'setup') {
      // Creates all required sheet tabs
      setupDataTabs();
      result = { ok: true, msg: 'All tabs created/verified.' };

    } else if (action === 'getdata') {
      // Legacy direct-API path (kept for backward compatibility)
      if (!token) throw new Error('META_ACCESS_TOKEN not set.');
      result = fetchAllData(token, datePreset, requestedDatePreset);

    } else {
      result = { error: 'Unknown action: ' + action };
    }
  } catch (err) {
    result = { error: err.message, stack: err.stack };
  }

  return ContentService
    .createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}

function deleteLeadRecord(ghlId) {
  if (!ghlId) return { ok: false, error: 'ghlId missing' };
  var sheetDeleted = false;
  try {
    var ss2 = SpreadsheetApp.openById(MASTER_SHEET_ID);
    var sh = ss2.getSheetByName('GHL_Leads');
    if (sh) {
      var rows = sh.getDataRange().getValues();
      var hdrs2 = rows[0].map(function(h){ return String(h).trim().toLowerCase(); });
      var col = hdrs2.indexOf('ghlid');
      if (col >= 0) {
        for (var ri = rows.length - 1; ri >= 1; ri--) {
          if (String(rows[ri][col]) === String(ghlId)) {
            sh.deleteRow(ri + 1);
            sheetDeleted = true;
            break;
          }
        }
      }
    }
  } catch(ex) { Logger.log('deleteLeadRecord sheet err: ' + ex.message); }
  var ghlDeleted = false;
  var apiKey2 = PropertiesService.getScriptProperties().getProperty('GHL_API_KEY');
  if (apiKey2) {
    try {
      var delRes = UrlFetchApp.fetch(GHL_API_BASE + '/contacts/' + ghlId, {
        method: 'DELETE',
        headers: { 'Authorization': 'Bearer ' + apiKey2, 'Version': '2021-07-28' },
        muteHttpExceptions: true
      });
      var code = delRes.getResponseCode();
      ghlDeleted = (code === 200 || code === 204);
    } catch(ex2) { Logger.log('deleteLeadRecord GHL err: ' + ex2.message); }
  }
  return { ok: true, sheetDeleted: sheetDeleted, ghlDeleted: ghlDeleted };
}

// ─── GHL WEBHOOK RECEIVER (POST) ──────────────────────────────────────────────
function doPost(e) {
  try {
    const raw     = e.postData ? e.postData.contents : '{}';
    const payload = JSON.parse(raw);

    const contact = payload.contact || payload.body || payload;
    const id      = contact.id || contact.contactId || payload.id || '';
    const fname   = contact.firstName || '';
    const lname   = contact.lastName  || '';
    const name    = contact.name || contact.contactName || (fname + (lname ? ' ' + lname : '')).trim() || '';
    const email   = contact.email || '';
    const phone   = contact.phone  || '';

    const attrs       = contact.attributions || [];
    const adAttr      = attrs.find(a => a.utmAdId) || attrs[0] || {};
    const sourceAdId  = adAttr.utmAdId   || '';
    const sourceAdName= adAttr.utmContent || adAttr.utmCampaign || '';
    const platformRaw = (adAttr.utmSource || adAttr.medium || contact.source || '').toLowerCase();
    const platform    = platformRaw.includes('facebook') || platformRaw.includes('meta') ? 'Meta'
                      : platformRaw.includes('google') ? 'Google' : 'Other';
    const campaignName= adAttr.utmCampaign || '';
    const tagsArr     = contact.tags || [];
    const tagsStr     = tagsArr.join(' ').toLowerCase();
    let proptype = '';
    if (tagsStr.includes('newlaunch') || tagsStr.includes('new launch')) proptype = 'New Launch';
    else if (tagsStr.includes('familylegacy') || tagsStr.includes('family legacy')) proptype = 'Family Legacy';
    else proptype = contact.source || '';

    const dateAdded = Utilities.formatDate(new Date(contact.dateAdded || new Date().toISOString()), 'Asia/Singapore', 'yyyy-MM-dd');

    const lead = {
      ghlId: id, name, contact: email || phone, phone, email,
      sourceAdId, sourceAdName, platform, campaignName,
      status: 'New', proptype, quality: '', date: dateAdded,
      tags: tagsArr.join(', '), source: contact.source || 'GHL Webhook',
      responded: '', appointment: '', strategySession: '', qualified: '',
      dealValue: '', notes: '', urgencyTimeline: ''
    };

    if (!name && !email && !phone) {
      return ContentService.createTextOutput(JSON.stringify({ ok: true, skipped: true }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    const ss    = SpreadsheetApp.openById(MASTER_SHEET_ID);
    let sheet   = ss.getSheetByName('GHL_Leads');
    if (!sheet) {
      sheet = ss.insertSheet('GHL_Leads');
      sheet.appendRow(GHL_LEADS_HEADERS);
    }

    let updated = false;
    if (id) {
      const data  = sheet.getDataRange().getValues();
      const hdrs  = data[0].map(h => String(h).trim().toLowerCase());
      const idCol = hdrs.indexOf('ghlid');
      if (idCol >= 0) {
        for (let i = 1; i < data.length; i++) {
          if (String(data[i][idCol]) === id) {
            const existingRow = {};
            GHL_LEADS_HEADERS.forEach((h, idx) => { existingRow[h] = data[i][idx]; });
            ['quality','dealValue','urgencyTimeline','notes'].forEach(h => {
              if ((lead[h] === '' || lead[h] == null) && existingRow[h] !== '' && existingRow[h] != null) lead[h] = existingRow[h];
            });
            sheet.getRange(i + 1, 1, 1, GHL_LEADS_HEADERS.length)
              .setValues([GHL_LEADS_HEADERS.map(h => lead[h] !== undefined ? lead[h] : '')]);
            updated = true;
            break;
          }
        }
      }
    }
    if (!updated) sheet.appendRow(GHL_LEADS_HEADERS.map(h => lead[h] !== undefined ? lead[h] : ''));

    Logger.log('GHL webhook: ' + (updated ? 'updated' : 'added') + ' ' + name);
    return ContentService.createTextOutput(JSON.stringify({ ok: true, action: updated ? 'updated' : 'added' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    Logger.log('doPost error: ' + err.message);
    return ContentService.createTextOutput(JSON.stringify({ ok: false, error: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// GHL_Leads column schema (expanded with funnel + quality columns)
const GHL_LEADS_HEADERS = [
  'ghlId','name','contact','phone','email','sourceAdId','sourceAdName',
  'platform','campaignName','status','quality','proptype','date',
  'responded','appointment','strategySession','qualified','dealValue','urgencyTimeline',
  'tags','source','notes'
];

// ─── STORE SECRETS + MENU ─────────────────────────────────────────────────────
function storeSecrets() {
  const ui  = SpreadsheetApp.getUi();
  const res = ui.prompt('Store Meta Access Token', 'Paste your token (never stored in sheet):', ui.ButtonSet.OK_CANCEL);
  if (res.getSelectedButton() !== ui.Button.OK) return;
  const tok = res.getResponseText().trim();
  if (!tok) { ui.alert('Empty token — nothing stored.'); return; }
  PropertiesService.getScriptProperties().setProperty('META_ACCESS_TOKEN', tok);
  ui.alert('Token stored securely in Script Properties ✓');
}

function storeGHLKey() {
  const ui  = SpreadsheetApp.getUi();
  const res = ui.prompt('Store GHL API Key', 'Paste your GHL Private Integration key:', ui.ButtonSet.OK_CANCEL);
  if (res.getSelectedButton() !== ui.Button.OK) return;
  const key = res.getResponseText().trim();
  if (!key) { ui.alert('Empty key — nothing stored.'); return; }
  PropertiesService.getScriptProperties().setProperty('GHL_API_KEY', key);
  ui.alert('GHL API key stored ✓');
}

function storeGHLLocationId() {
  const ui      = SpreadsheetApp.getUi();
  const current = PropertiesService.getScriptProperties().getProperty('GHL_LOCATION_ID') || '';
  const res     = ui.prompt('Store GHL Location ID', `Current: ${current || 'none'}\nPaste Location ID:`, ui.ButtonSet.OK_CANCEL);
  if (res.getSelectedButton() !== ui.Button.OK) return;
  const id = res.getResponseText().trim();
  if (!id) { ui.alert('Empty — nothing changed.'); return; }
  PropertiesService.getScriptProperties().setProperty('GHL_LOCATION_ID', id);
  ui.alert('GHL Location ID stored ✓');
}

function storeSheetId() {
  const ui  = SpreadsheetApp.getUi();
  const res = ui.prompt('Store Sheet ID', 'Paste the Master Sheet ID:', ui.ButtonSet.OK_CANCEL);
  if (res.getSelectedButton() !== ui.Button.OK) return;
  PropertiesService.getScriptProperties().setProperty('SHEET_ID', res.getResponseText().trim());
  ui.alert('Sheet ID stored ✓');
}

function onOpen() {
  SpreadsheetApp.getUi().createMenu('REI Menu')
    .addItem('Store Meta Token',        'storeSecrets')
    .addItem('Store Sheet ID',          'storeSheetId')
    .addItem('Store GHL API Key',       'storeGHLKey')
    .addItem('Store GHL Location ID',   'storeGHLLocationId')
    .addSeparator()
    .addItem('Sync Meta Now',           'syncMetaNow')
    .addItem('Setup All Sheet Tabs',    'setupDataTabs')
    .addSeparator()
    .addItem('Start Auto-Sync (Meta hourly + GHL 5-min)',  'setupHourlyTrigger')
    .addItem('Stop Auto-Sync',          'removeTrigger')
    .addToUi();
}

// ─── MAIN DATA FETCH (API path — used by syncmeta) ────────────────────────────
function fetchAllData(token, datePreset, requestedDatePreset) {
  const adAccountId = getAdAccountId(token);
  const currency    = getAccountCurrency(token, adAccountId); // v8: detect currency
  const metaDateSpec= buildMetaDateSpec(requestedDatePreset || datePreset);

  const campaigns = fetchCampaigns(token, adAccountId, metaDateSpec, currency);
  const adsets    = fetchAdSets(token, adAccountId, metaDateSpec, campaigns, currency);
  const ads       = fetchAds(token, adAccountId, metaDateSpec, adsets, currency);
  resolveMetaVideoThumbnails(token, ads); // v8.1: fill missing video thumbnails
  const leads     = fetchMetaLeads(token, adAccountId, metaDateSpec);
  const googleData= fetchGoogleAdsFromSheet(requestedDatePreset || datePreset);

  return {
    campaigns, adsets, ads, leads,
    googleCampaigns: googleData.campaigns,
    googleAdGroups:  googleData.adGroups,
    googleAds:       googleData.ads,
    syncedAt:  new Date().toISOString(),
    datePreset: metaDateSpec.label || datePreset,
    currency
  };
}

function singaporeIsoToday() {
  return Utilities.formatDate(new Date(), 'Asia/Singapore', 'yyyy-MM-dd');
}

function shiftIsoDateSgt(iso, days) {
  const base = new Date(String(iso) + 'T00:00:00+08:00');
  return Utilities.formatDate(new Date(base.getTime() + days * 24 * 60 * 60 * 1000), 'Asia/Singapore', 'yyyy-MM-dd');
}

function buildMetaDateSpec(preset) {
  const p = String(preset || 'last_7d').toLowerCase();
  const today = singaporeIsoToday();
  if (p === 'today') return { since: today, until: today, label: 'today' };
  if (p === 'yesterday') {
    const y = shiftIsoDateSgt(today, -1);
    return { since: y, until: y, label: 'yesterday' };
  }
  if (p === 'last_7d' || p === 'last_7_days') return { since: shiftIsoDateSgt(today, -6), until: today, label: 'last_7d' };
  if (p === 'last_14d' || p === 'last_14_days') return { since: shiftIsoDateSgt(today, -13), until: today, label: 'last_14d' };
  if (p === 'last_30d' || p === 'last_30_days') return { since: shiftIsoDateSgt(today, -29), until: today, label: 'last_30d' };
  if (p.startsWith('sgt:')) {
    const parts = p.slice(4).split(':');
    return { since: parts[0], until: parts[1] || parts[0], label: p };
  }
  if (p === 'all_time' || p === 'maximum') return { preset: 'maximum', label: 'maximum' };
  return { preset: p, label: p };
}

function metaInsightsFields(baseFields, dateSpec, insightFields) {
  if (dateSpec && dateSpec.since && dateSpec.until) {
    return `${baseFields},insights.time_range({"since":"${dateSpec.since}","until":"${dateSpec.until}"}){${insightFields}}`;
  }
  return `${baseFields},insights.date_preset(${(dateSpec && dateSpec.preset) || 'last_7d'}){${insightFields}}`;
}

// ─── SHEET-FIRST DATA FETCH (primary dashboard path) ─────────────────────────
/**
 * Reads all data from pre-populated sheets.
 * Dashboard calls action=getfromsheets — no Meta API call.
 */
function fetchAllDataFromSheets(preset) {
  // v8.19: preset drives which Google_Campaigns_* tab to read
  const ss = SpreadsheetApp.openById(MASTER_SHEET_ID);

  const campaigns = readSheetTab(ss, 'Meta_Campaigns');
  const adsets    = readSheetTab(ss, 'Meta_AdSets');
  const ads       = readSheetTab(ss, 'Meta_Ads');
  const googleData= fetchGoogleAdsFromSheet(preset);
  const leadsData = readGHLLeadsFromSheet();
  const leadRows  = leadsData.leads || [];
  enrichLeadAttribution(leadRows, ads, campaigns, googleData.ads, googleData.campaigns);

  // Compute funnel metrics after IDs have been enriched to campaign names.
  const funnel = computeFunnelByCampaign(leadRows);

  // Attach funnel data to campaigns
  campaigns.forEach(c => {
    const f = funnel[normaliseName(c.name || c.campaignName || '')] || {};
    c.responded     = f.responded     || 0;
    c.bookedCalls   = f.bookedCalls   || 0;
    c.appointments  = f.appointments  || 0;
    c.strategySessions= f.strategySessions || 0;
    c.qualified     = f.qualified     || 0;
    c.revenue       = f.revenue       || 0;
    c.costPerRespond= c.spend > 0 && c.responded > 0  ? c.spend / c.responded : 0;
    c.costPerAppt   = c.spend > 0 && c.appointments > 0? c.spend / c.appointments : 0;
    c.costPerSS     = c.spend > 0 && c.strategySessions > 0 ? c.spend / c.strategySessions : 0;
    c.roas          = c.spend > 0 && c.revenue > 0 ? c.revenue / c.spend : 0;
  });

  // Sync timestamp from Meta_Campaigns tab (last Updated At value)
  let syncedAt = '';
  try {
    const metaSheet = ss.getSheetByName('Meta_Campaigns');
    if (metaSheet) {
      const lastRow = metaSheet.getLastRow();
      if (lastRow > 1) {
        const headerRow = metaSheet.getRange(1, 1, 1, metaSheet.getLastColumn()).getValues()[0];
        const updatedIdx= headerRow.findIndex(h => String(h).toLowerCase().includes('updated'));
        if (updatedIdx >= 0) {
          syncedAt = String(metaSheet.getRange(lastRow, updatedIdx + 1).getValue());
        }
      }
    }
  } catch(e) { /* ignore */ }

  return {
    campaigns, adsets, ads,
    leads:          leadRows,
    leadsBreakdown: leadsData.breakdown || {},
    googleCampaigns:googleData.campaigns,
    googleAdGroups: googleData.adGroups,
    googleAds:      googleData.ads,
    googlePeriodLabel: googleData.periodLabel,
    googleDetailPeriodLabel: googleData.detailPeriodLabel,
    googleWarning:  googleData.warning || '',
    syncedAt:       syncedAt || new Date().toISOString(),
    source:         'sheets'
  };
}

function readSheetTab(ss, tabName) {
  try {
    const sheet = ss.getSheetByName(tabName);
    if (!sheet) return [];
    const data  = sheet.getDataRange().getValues();
    if (data.length < 2) return [];
    const hdrs  = data[0].map(h => String(h || '').trim());
    return data.slice(1)
      .filter(row => row.some(c => c !== '' && c !== null))
      .map(row => {
        const obj = {};
        hdrs.forEach((h, i) => { if (h) obj[h] = row[i] !== undefined ? row[i] : ''; });
        return obj;
      });
  } catch (err) {
    Logger.log('readSheetTab(' + tabName + ') error: ' + err.message);
    return [];
  }
}

// ─── FUNNEL COMPUTATION ───────────────────────────────────────────────────────
/**
 * Groups GHL leads by campaign name and counts each funnel stage.
 * Returns: { normalisedCampaignName: { responded, appointments, strategySessions, qualified, revenue } }
 */
function computeFunnelByCampaign(leads) {
  const funnel = {};

  const STAGE_RANKS = {
    'new': 0, 'contacted': 1, 'responded': 2,
    'booked call': 3, 'booked': 3,
    'appt set': 4, 'appt verified': 4, 'appointment': 4,
    'potential': 5, 'qualified': 5, 'appt qualified': 5,
    'strategy session': 6, 'ss': 6,
    'closed': 7, 'won': 7,
    'lost': -1
  };

  leads.forEach(lead => {
    const camp = normaliseName(lead.campaignName || lead.sourceAdName || '');
    if (!camp) return;
    if (!funnel[camp]) {
      funnel[camp] = { responded: 0, bookedCalls: 0, appointments: 0, strategySessions: 0, qualified: 0, revenue: 0 };
    }

    const statusRaw = (lead.status || lead.responded || '').toLowerCase().trim();
    const rank = STAGE_RANKS[statusRaw] ?? -1;

    if (rank >= 2) funnel[camp].responded++;
    if (rank >= 3) funnel[camp].bookedCalls++;
    if (rank >= 4) funnel[camp].appointments++;
    if (rank >= 5) funnel[camp].qualified++;
    if (rank >= 6) funnel[camp].strategySessions++;
    if (rank === 7) {
      // Add deal value to revenue if available
      const val = parseFloat(String(lead.dealValue || lead.revenue || '0').replace(/[^0-9.]/g, '')) || 0;
      funnel[camp].revenue += val;
    }
  });

  return funnel;
}

function normaliseName(s) {
  return String(s || '').toLowerCase().trim().replace(/\s+/g, ' ');
}

// ─── AD ACCOUNT ───────────────────────────────────────────────────────────────
function getAdAccountId(token) {
  const stored = PropertiesService.getScriptProperties().getProperty('META_AD_ACCOUNT_ID');
  if (stored) return stored;
  const r = apiGet(token, '/me/adaccounts', { fields: 'id,name', limit: 1 });
  if (!r.data || !r.data.length) throw new Error('No ad accounts found for this token');
  const id = r.data[0].id;
  PropertiesService.getScriptProperties().setProperty('META_AD_ACCOUNT_ID', id);
  return id;
}

/**
 * v8: Detect ad account currency.
 * Returns 'SGD', 'USD', or whatever the account uses.
 * Cached in Script Properties so we only call once.
 */
function getAccountCurrency(token, accountId) {
  const cached = PropertiesService.getScriptProperties().getProperty('META_ACCOUNT_CURRENCY');
  if (cached) return cached;
  try {
    const r = apiGet(token, `/${accountId}`, { fields: 'currency' });
    const cur = (r.currency || 'USD').toUpperCase();
    PropertiesService.getScriptProperties().setProperty('META_ACCOUNT_CURRENCY', cur);
    Logger.log('Meta account currency: ' + cur);
    return cur;
  } catch (e) {
    Logger.log('Currency detect failed, assuming USD: ' + e.message);
    return 'USD';
  }
}

/**
 * v8: Convert spend to SGD only if the account is in USD.
 * Fixes the ~35% over-reporting for SGD accounts.
 */
function toSGD(amount, currency) {
  const n = parseFloat(amount || 0);
  return currency === 'USD' ? n * SGD_RATE : n;
}

// ─── CAMPAIGNS ────────────────────────────────────────────────────────────────
function fetchCampaigns(token, accountId, dateSpec, currency) {
  const fields = [
    'id','name','objective','status','daily_budget','lifetime_budget',
    'effective_status','start_time','stop_time'
  ].join(',');
  const insightFields = 'spend,impressions,clicks,cpm,ctr,reach,actions';

  const r = apiGet(token, `/${accountId}/campaigns`, {
    fields: metaInsightsFields(fields, dateSpec, insightFields),
    limit: 200,
    sort: JSON.stringify(['updated_time_descending']),
    effective_status: JSON.stringify(['ACTIVE','PAUSED','ARCHIVED'])
  });

  return (r.data || []).map(c => {
    const ins   = c.insights?.data?.[0] || {};
    const spend = toSGD(ins.spend, currency); // v8: currency-aware conversion
    // v8: use || consistently (not + which double-counts form + pixel leads)
    const leads = extractAction(ins.actions,'lead') || extractAction(ins.actions,'onsite_conversion.lead_grouped');
    return {
      metaId:      c.id,
      name:        c.name,
      platform:    'Meta',
      objective:   c.objective || '',
      status:      normaliseStatus(c.effective_status || c.status),
      budget:      toSGD(parseFloat(c.daily_budget || c.lifetime_budget || 0) / 100, currency),
      spend:       parseFloat(spend.toFixed(2)),
      leads:       leads,
      cpl:         leads > 0 ? parseFloat((spend / leads).toFixed(2)) : 0,
      impressions: parseInt(ins.impressions || 0),
      clicks:      parseInt(ins.clicks || 0),
      ctr:         parseFloat(ins.ctr || 0),
      reach:       parseInt(ins.reach || 0),
      updatedAt:   new Date().toISOString()
    };
  });
}

// ─── AD SETS ──────────────────────────────────────────────────────────────────
function fetchAdSets(token, accountId, dateSpec, campaigns, currency) {
  const fields = [
    'id','name','campaign_id','effective_status','status',
    'daily_budget','lifetime_budget','targeting'
  ].join(',');
  const insightFields = 'spend,impressions,clicks,cpm,ctr,actions';

  const r = apiGet(token, `/${accountId}/adsets`, {
    fields: metaInsightsFields(fields, dateSpec, insightFields),
    limit: 200,
    sort: JSON.stringify(['updated_time_descending'])
  });

  return (r.data || []).map(a => {
    const ins   = a.insights?.data?.[0] || {};
    const spend = toSGD(ins.spend, currency);
    const leads = extractAction(ins.actions,'lead') || extractAction(ins.actions,'onsite_conversion.lead_grouped');
    const camp  = campaigns.find(c => c.metaId === a.campaign_id);
    return {
      metaId:       a.id,
      name:         a.name,
      platform:     'Meta',
      campaignId:   a.campaign_id,
      campaignName: camp?.name || '',
      status:       normaliseStatus(a.effective_status || a.status),
      budget:       toSGD(parseFloat(a.daily_budget || a.lifetime_budget || 0) / 100, currency),
      spend:        parseFloat(spend.toFixed(2)),
      leads:        leads,
      cpl:          leads > 0 ? parseFloat((spend / leads).toFixed(2)) : 0,
      audience:     extractAudience(a.targeting),
      updatedAt:    new Date().toISOString()
    };
  });
}

// ─── ADS (CREATIVES) ──────────────────────────────────────────────────────────
function fetchAds(token, accountId, dateSpec, adsets, currency) {
  const fields = [
    'id','name','adset_id','campaign_id','effective_status','status',
    'permalink_url',
    'creative{id,name,thumbnail_url,object_story_spec,video_id,image_url,call_to_action_type}'
  ].join(',');
  const insightFields = [
    'spend','impressions','clicks','ctr','cpc','cpm','actions',
    'video_p25_watched_actions','video_p50_watched_actions',
    'video_p75_watched_actions','video_p95_watched_actions'
  ].join(',');

  const r = apiGet(token, `/${accountId}/ads`, {
    fields: metaInsightsFields(fields, dateSpec, insightFields),
    limit: 200,
    sort: JSON.stringify(['updated_time_descending'])
  });

  return (r.data || []).map(ad => {
    const ins        = ad.insights?.data?.[0] || {};
    const cr         = ad.creative || {};
    const impressions= parseInt(ins.impressions || 0);
    const spend      = toSGD(ins.spend, currency);
    const clicks     = parseInt(ins.clicks || 0);
    // v8: use || (not +) to avoid double-counting form leads + pixel leads
    const leads      = extractAction(ins.actions,'lead') || extractAction(ins.actions,'onsite_conversion.lead_grouped');
    const p25        = extractVideoAction(ins.video_p25_watched_actions);
    const hookRate   = impressions > 0 ? (p25 / impressions) * 100 : 0;
    const cpl        = leads > 0 ? spend / leads : 0;
    const cpc        = clicks > 0 ? spend / clicks : 0;
    const as         = adsets.find(a => a.metaId === ad.adset_id);

    return {
      metaId:      ad.id,
      name:        ad.name,
      platform:    'Meta',
      adsetId:     ad.adset_id,
      adsetName:   as?.name || '',
      campaignId:  ad.campaign_id,
      campaignName:as?.campaignName || '',
      status:      normaliseStatus(ad.effective_status || ad.status),
      format:      detectFormatFromCreative(cr, ad.name),
      thumbUrl:    cr.thumbnail_url || '',
      videoId:     cr.video_id || '',
      imageUrl:    cr.image_url || '',
      hookrate:    parseFloat(hookRate.toFixed(2)),
      ctr:         parseFloat(ins.ctr || 0),
      cpc:         parseFloat(cpc.toFixed(2)),
      cpm:         parseFloat(ins.cpm || 0),
      spend:       parseFloat(spend.toFixed(2)),
      impressions, clicks, leads,
      cpl:         parseFloat(cpl.toFixed(2)),
      p25, p50:    extractVideoAction(ins.video_p50_watched_actions),
      p75:         extractVideoAction(ins.video_p75_watched_actions),
      p95:         extractVideoAction(ins.video_p95_watched_actions),
      adPermalink: ad.permalink_url || '',
      updatedAt:   new Date().toISOString()
    };
  });
}

// ─── META VIDEO THUMBNAIL RESOLUTION ──────────────────────────────────────────
/**
 * v8.1: For video ads where creative.thumbnail_url was empty but video_id is present,
 * resolve the thumbnail by calling /{video_id}?fields=picture,thumbnails.
 * Mutates the ads array in-place. Called after fetchAds().
 */
function resolveMetaVideoThumbnails(token, ads) {
  const needsResolve = ads.filter(ad => !ad.thumbUrl && ad.videoId);
  if (!needsResolve.length) return;
  Logger.log('Resolving thumbnails for ' + needsResolve.length + ' video ads...');
  const BATCH = 20;
  for (let i = 0; i < needsResolve.length; i += BATCH) {
    needsResolve.slice(i, i + BATCH).forEach(ad => {
      try {
        const r = apiGet(token, '/' + ad.videoId, { fields: 'picture,thumbnails,source' });
        if (r.picture) {
          ad.thumbUrl = r.picture;
        } else if (r.thumbnails && r.thumbnails.data && r.thumbnails.data[0]) {
          ad.thumbUrl = r.thumbnails.data[0].uri || r.thumbnails.data[0].url || '';
        }
        if (r.source) ad.videoSrc = r.source; // v8.12: direct MP4 URL for in-dashboard playback
      } catch (e) {
        Logger.log('Thumbnail resolve failed for videoId ' + ad.videoId + ': ' + e.message);
      }
    });
    if (i + BATCH < needsResolve.length) Utilities.sleep(300);
  }
  Logger.log('Thumbnail resolution complete: ' +
    needsResolve.filter(a => a.thumbUrl).length + '/' + needsResolve.length + ' resolved.');
}

// ─── META LEAD ADS ────────────────────────────────────────────────────────────
function fetchMetaLeads(token, accountId, dateSpec) {
  const allLeads = [];
  try {
    const formsR = apiGet(token, `/${accountId}/leadgen_forms`, {
      fields: 'id,name,status,leads_count', limit: 200
    });
    (formsR.data || []).forEach(form => {
      if (parseInt(form.leads_count) === 0) return;
      try {
        const leadsR = apiGet(token, `/${form.id}/leads`, {
          fields: 'id,created_time,field_data,ad_id,ad_name,adset_id,campaign_id',
          limit: 200
        });
        (leadsR.data || []).forEach(l => {
          const leadDate = l.created_time ? Utilities.formatDate(new Date(l.created_time), 'Asia/Singapore', 'yyyy-MM-dd') : '';
          if (dateSpec && dateSpec.since && dateSpec.until && (!leadDate || leadDate < dateSpec.since || leadDate > dateSpec.until)) return;
          const fds = {};
          (l.field_data || []).forEach(f => { fds[f.name.toLowerCase()] = (f.values || [])[0] || ''; });
          allLeads.push({
            metaLeadId:  l.id,
            formId:      form.id,
            formName:    form.name,
            sourceAdId:  l.ad_id   || '',
            sourceAdName:l.ad_name || '',
            adsetId:     l.adset_id    || '',
            campaignId:  l.campaign_id || '',
            name:        (fds.full_name || fds.first_name || '') + (fds.last_name ? ' ' + fds.last_name : ''),
            contact:     fds.phone_number || fds.email || '',
            email:       fds.email        || '',
            phone:       fds.phone_number || '',
            date:        leadDate,
            status:      'New',
            platform:    'Meta'
          });
        });
      } catch (err) {
        Logger.log('Lead fetch error for form ' + form.id + ': ' + err.message);
      }
    });
  } catch (err) {
    Logger.log('Meta leads fetch error: ' + err.message);
  }
  return allLeads;
}

// ─── GOOGLE ADS FROM SHEET ────────────────────────────────────────────────────
function fetchGoogleAdsFromSheet(preset) {
  const p = String(preset || 'last_7d').toLowerCase();
  const periods = {
    today:       { tab: 'Google_Campaigns_Today',     label: 'Today' },
    yesterday:   { tab: 'Google_Campaigns_Yesterday', label: 'Yesterday' },
    last_7d:     { tab: 'Google_Campaigns_L7D',       label: 'Last 7 days' },
    last_7_days: { tab: 'Google_Campaigns_L7D',       label: 'Last 7 days' },
    last_14d:    { tab: 'Google_Campaigns_L14D',      label: 'Last 14 days' },
    last_14_days:{ tab: 'Google_Campaigns_L14D',      label: 'Last 14 days' },
    last_30d:    { tab: 'Google_Campaigns_L30D',      label: 'Last 30 days' },
    last_30_days:{ tab: 'Google_Campaigns_L30D',      label: 'Last 30 days' },
    all_time:    { tab: 'Google_Campaigns_AllTime',   label: 'All time' },
    maximum:     { tab: 'Google_Campaigns_AllTime',   label: 'All time' }
  };
  const period = periods[p] || null;
  const result = {
    campaigns: [], adGroups: [], ads: [],
    periodLabel: period ? period.label : 'Custom range',
    detailPeriodLabel: 'Last 30 days',
    warning: ''
  };
  try {
    const ss = SpreadsheetApp.openById(MASTER_SHEET_ID);
    if (period) {
      const campSheet = getSheetSafe(ss, period.tab);
      if (campSheet) {
        const rows = campSheet.getDataRange().getValues();
        result.campaigns = rows.slice(1).filter(r => r[0]).map(r => rowToObj(rows[0], r, 'Google'));
      } else {
        result.warning = period.tab + ' is missing. Run REI_GoogleAds_Script_v6 before using this period.';
        Logger.log(result.warning);
      }
    } else {
      result.warning = 'Google spend is unavailable for a custom range; choose a preset period.';
    }
    const agSheet = getSheetSafe(ss, 'Google_AdGroups');
    if (agSheet) {
      const rows = agSheet.getDataRange().getValues();
      result.adGroups = rows.slice(1).filter(r => r[0]).map(r => rowToObj(rows[0], r, 'Google'));
    }
    const adSheet = getSheetSafe(ss, 'Google_Ads');
    if (adSheet) {
      const rows = adSheet.getDataRange().getValues();
      result.ads = rows.slice(1).filter(r => r[0]).map(r => rowToObj(rows[0], r, 'Google'));
    }
  } catch (err) {
    result.warning = 'Google Ads sheet read error: ' + err.message;
    Logger.log(result.warning);
  }
  return result;
}

function getSheetSafe(ss, name) { try { return ss.getSheetByName(name); } catch(e) { return null; } }
function rowToObj(headers, row, platform) {
  const obj = { platform };
  headers.forEach((h, i) => { if (h) obj[h] = row[i] !== '' ? row[i] : null; });
  return obj;
}

function enrichLeadAttribution(leads, metaAds, metaCampaigns, googleAds, googleCampaigns) {
  const byAdId = {}, byCampaignId = {};
  function clean(v) { return String(v == null ? '' : v).trim(); }
  function numeric(v) { return /^\d{8,}$/.test(clean(v)); }
  (metaCampaigns || []).forEach(c => {
    const id = clean(c.metaId || c.campaignId);
    if (id) byCampaignId[id] = { name: clean(c.name || c.campaign), platform: 'Meta' };
  });
  (googleCampaigns || []).forEach(c => {
    const id = clean(c.campaignId || c.googleId);
    if (id) byCampaignId[id] = { name: clean(c.campaign || c.name), platform: 'Google' };
  });
  (metaAds || []).forEach(a => {
    const id = clean(a.metaId || a.adId);
    if (id) byAdId[id] = { name: clean(a.name || a.ad), campaignName: clean(a.campaignName), campaignId: clean(a.campaignId), platform: 'Meta' };
  });
  (googleAds || []).forEach(a => {
    const id = clean(a.adId || a.googleId);
    if (id) byAdId[id] = { name: clean(a.ad || a.name), campaignName: clean(a.campaign || a.campaignName), campaignId: clean(a.campaignId), platform: 'Google' };
  });
  (leads || []).forEach(l => {
    let adId = clean(l.sourceAdId);
    if (!adId && numeric(l.sourceAdName)) adId = clean(l.sourceAdName);
    const ad = byAdId[adId];
    if (ad) {
      l.sourceAdId = adId;
      if (!clean(l.sourceAdName) || numeric(l.sourceAdName)) l.sourceAdName = ad.name;
      if (!clean(l.campaignName) || numeric(l.campaignName)) l.campaignName = ad.campaignName;
      l.platform = ad.platform;
    }
    const campaign = byCampaignId[clean(l.campaignId)];
    if (campaign) {
      if (!clean(l.campaignName) || numeric(l.campaignName)) l.campaignName = campaign.name;
      if (!clean(l.platform)) l.platform = campaign.platform;
    }
    const source = clean(l.source).toLowerCase();
    if (!clean(l.platform) && source.includes('google')) l.platform = 'Google';
    if (!clean(l.platform) && (source.includes('facebook') || source.includes('instagram') || source.includes('meta'))) l.platform = 'Meta';
    if (/^google$/i.test(clean(l.platform))) l.platform = 'Google';
    if (/^(meta|facebook|instagram)$/i.test(clean(l.platform))) l.platform = 'Meta';
  });
}

// ─── MANUAL SYNC ──────────────────────────────────────────────────────────────
function syncMetaNow() {
  const token = PropertiesService.getScriptProperties().getProperty('META_ACCESS_TOKEN');
  if (!token) { SpreadsheetApp.getUi().alert('No token stored. Run "Store Meta Token" first.'); return; }
  try {
    const data = fetchAllData(token, 'last_7d');
    writeToSheet(data);
    SpreadsheetApp.getUi().alert(
      `Sync complete ✓\n${data.campaigns.length} campaigns · ${data.adsets.length} adsets · ${data.ads.length} ads`
    );
  } catch (err) {
    SpreadsheetApp.getUi().alert('Sync failed: ' + err.message);
  }
}

// ─── WRITE TO MASTER SHEET ────────────────────────────────────────────────────
function writeToSheet(data) {
  const ss = SpreadsheetApp.openById(MASTER_SHEET_ID);

  writeTab(ss, 'Meta_Campaigns', data.campaigns, [
    'metaId','name','platform','objective','status','budget','spend',
    'leads','cpl','impressions','clicks','ctr','reach','updatedAt'
  ]);
  writeTab(ss, 'Meta_AdSets', data.adsets, [
    'metaId','name','campaignId','campaignName','platform','status','budget',
    'spend','leads','cpl','audience','updatedAt'
  ]);
  writeTab(ss, 'Meta_Ads', data.ads, [
    'metaId','name','adsetId','adsetName','campaignId','campaignName','platform',
    'status','format','thumbUrl','videoId','imageUrl','videoSrc','hookrate','ctr','cpc','cpm',
    'spend','impressions','clicks','leads','cpl',
    'p25','p50','p75','p95','adPermalink','updatedAt'
  ]);
  if (data.leads && data.leads.length) {
    writeTab(ss, 'Meta_Leads', data.leads, [
      'metaLeadId','formId','formName','sourceAdId','sourceAdName',
      'adsetId','campaignId','name','contact','email','phone','date','status','platform'
    ]);
  }
}

function writeTab(ss, tabName, rows, headers) {
  let sheet = ss.getSheetByName(tabName);
  if (!sheet) sheet = ss.insertSheet(tabName);
  sheet.clearContents();
  if (!rows || !rows.length) {
    sheet.getRange(1,1,1,headers.length).setValues([headers]);
    return;
  }
  const data = [headers, ...rows.map(r => headers.map(h => r[h] !== undefined ? r[h] : ''))];
  sheet.getRange(1, 1, data.length, headers.length).setValues(data);
  sheet.setFrozenRows(1);
  // Bold header
  sheet.getRange(1, 1, 1, headers.length).setFontWeight('bold')
       .setBackground('#1a73e8').setFontColor('#ffffff');
}

// ─── SETUP ALL SHEET TABS ─────────────────────────────────────────────────────
/**
 * Creates all required tabs with correct column schemas.
 * Safe to run multiple times — only creates tabs that don't exist.
 * Run via: REI Menu → Setup All Sheet Tabs  OR  action=setup
 */
function setupDataTabs() {
  const ss = SpreadsheetApp.openById(MASTER_SHEET_ID);
  const tabs = {
    'Meta_Campaigns': [
      'metaId','name','platform','objective','status','budget','spend',
      'leads','cpl','impressions','clicks','ctr','reach','updatedAt'
    ],
    'Meta_AdSets': [
      'metaId','name','campaignId','campaignName','platform','status','budget',
      'spend','leads','cpl','audience','updatedAt'
    ],
    'Meta_Ads': [
      'metaId','name','adsetId','adsetName','campaignId','campaignName','platform',
      'status','format','thumbUrl','videoId','imageUrl','videoSrc','hookrate','ctr','cpc','cpm',
      'spend','impressions','clicks','leads','cpl',
      'p25','p50','p75','p95','adPermalink','updatedAt'
    ],
    'Meta_Leads': [
      'metaLeadId','formId','formName','sourceAdId','sourceAdName',
      'adsetId','campaignId','name','contact','email','phone','date','status','platform'
    ],
    // Google Ads tabs — populated by REI_GoogleAds_Script.gs (Google Ads UI → Bulk Actions → Scripts)
    'Google_Campaigns': [
      'date','campaignId','campaign','campaignType','status',
      'dailyBudget','spend','impressions','clicks','conversions','conversionValue',
      'ctr','avgCpc','roas','platform','updatedAt'
    ],
    'Google_AdGroups': [
      'date','adGroupId','adGroup','campaignId','campaign','adGroupType','status',
      'spend','impressions','clicks','conversions','ctr','avgCpc','platform','updatedAt'
    ],
    'Google_Ads': [
      'date','adId','adName','adGroupId','adGroup','campaignId','campaign',
      'adType','format','status','finalUrl',
      'impressions','clicks','spend','conversions','ctr','avgCpc',
      'videoId','thumbUrl','hookrate','adText',
      'platform','updatedAt'
    ],
    // GHL Leads — populated by webhook + manual export
    'GHL_Leads': GHL_LEADS_HEADERS,
    // Referrals & Organic
    'Referrals_Organic': [
      'Date','Name','Phone','Email','Source','Property Interest','Referred By','Remarks'
    ]
  };

  const COLORS = {
    'Meta_Campaigns': '#1877f2', 'Meta_AdSets': '#1877f2', 'Meta_Ads': '#1877f2', 'Meta_Leads': '#1877f2',
    'Google_Campaigns': '#34a853', 'Google_AdGroups': '#34a853', 'Google_Ads': '#34a853',
    'GHL_Leads': '#ea4335', 'Referrals_Organic': '#fbbc04'
  };

  Object.entries(tabs).forEach(([name, headers]) => {
    let sheet = getSheetSafe(ss, name);
    if (!sheet) {
      sheet = ss.insertSheet(name);
      Logger.log('Created tab: ' + name);
    }
    // Only write headers if empty
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(headers);
      sheet.setFrozenRows(1);
    }
    // Style header row
    const color = COLORS[name] || '#333333';
    sheet.getRange(1, 1, 1, headers.length)
      .setFontWeight('bold').setBackground(color).setFontColor('#ffffff');
  });

  Logger.log('setupDataTabs complete');
}

// ─── HOURLY AUTO-SYNC TRIGGER ─────────────────────────────────────────────────
function setupHourlyTrigger() {
  // Remove existing REI sync triggers first
  removeTrigger(false);
  ScriptApp.newTrigger('syncMetaScheduled')
    .timeBased()
    .everyHours(1)
    .create();
  ScriptApp.newTrigger('syncGHLScheduled')
    .timeBased()
    .everyMinutes(5)
    .create();
  const ui = SpreadsheetApp.getUi();
  if (ui) ui.alert('Auto-sync enabled.\nMeta refreshes hourly. GHL pipeline refreshes every 5 minutes.');
  Logger.log('Auto-sync triggers created for Meta and GHL');
}

function removeTrigger(showAlert) {
  const triggers = ScriptApp.getProjectTriggers();
  triggers.forEach(t => {
    const fn = t.getHandlerFunction();
    if (fn === 'syncMetaScheduled' || fn === 'syncGHLScheduled') ScriptApp.deleteTrigger(t);
  });
  if (showAlert !== false) {
    const ui = SpreadsheetApp.getUi();
    if (ui) ui.alert('Auto-sync stopped.');
  }
  Logger.log('Auto-sync triggers removed');
}

/** Called by the hourly trigger — silent sync to sheets */
function syncMetaScheduled() {
  const token = PropertiesService.getScriptProperties().getProperty('META_ACCESS_TOKEN');
  if (!token) { Logger.log('syncMetaScheduled: No META_ACCESS_TOKEN stored.'); return; }
  try {
    const data = fetchAllData(token, 'last_30d'); // 30-day window for scheduled sync
    writeToSheet(data);
    Logger.log(`syncMetaScheduled: ${data.campaigns.length} campaigns, ${data.ads.length} ads — ${new Date().toISOString()}`);
  } catch (err) {
    Logger.log('syncMetaScheduled error: ' + err.message);
  }
}

/** Called by the 5-minute trigger — keeps GHL_Leads fresh even if nobody clicks Sync Intelia. */
function syncGHLScheduled() {
  try {
    const result = fetchGHLLeads();
    Logger.log(`syncGHLScheduled: ${(result && result.total) || 0} GHL leads — ${new Date().toISOString()}`);
  } catch (err) {
    Logger.log('syncGHLScheduled error: ' + err.message);
  }
}

// ─── GHL LEADS FETCH (API path) ───────────────────────────────────────────────
function fetchGHLLeads() {
  const apiKey = PropertiesService.getScriptProperties().getProperty('GHL_API_KEY');
  if (!apiKey) {
    Logger.log('GHL_API_KEY not set — reading from GHL_Leads sheet tab (fallback mode)');
    return readGHLLeadsFromSheet();
  }
  // v8.17: warn if key looks like a Location ID (short alphanumeric ~20 chars, not a JWT/bearer)
  if (apiKey.length < 40 && /^[a-zA-Z0-9]{10,30}$/.test(apiKey)) {
    Logger.log('WARNING: GHL_API_KEY looks like a Location ID (' + apiKey + '), not a Private Integration key. ' +
               'Go to GHL → Settings → Integrations → Private Integrations → Create New → copy the API Key.');
    return { leads: [], total: 0, error: 'GHL_API_KEY appears to be a Location ID, not a Private Integration key. See Apps Script logs for instructions.' };
  }

  const locationId = PropertiesService.getScriptProperties().getProperty('GHL_LOCATION_ID')
    || 'cyeYxFVQE1l73kO6S6Lx';

  const headers = {
    'Authorization': 'Bearer ' + apiKey,
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  };

  const allContacts = [];
  let startAfter = null, startAfterId = null, page = 0;
  while (page < 20) {
    let url = `${GHL_API_BASE}/contacts/?locationId=${locationId}&limit=100`;
    if (startAfter) url += `&startAfter=${startAfter}&startAfterId=${encodeURIComponent(startAfterId)}`;
    const res  = UrlFetchApp.fetch(url, { headers, muteHttpExceptions: true });
    const body = JSON.parse(res.getContentText());
    if (!body.contacts || body.contacts.length === 0) break;
    allContacts.push(...body.contacts);
    if (!body.meta?.nextPage) break;
    startAfter   = body.meta.startAfter;
    startAfterId = body.meta.startAfterId;
    page++;
    Utilities.sleep(200);
  }

  Logger.log(`GHL: fetched ${allContacts.length} contacts total`);

  const pipelineId = 'BdutTA7xHUrNoPpWc5Nu';
  const stageMap   = buildStageMap(apiKey, locationId, pipelineId);

  // v8.18 FIX: only map contacts that are IN the pipeline (stageMap keys = pipeline contactIds)
  // Previously used all contacts → 815 results. Now: only the ~367 pipeline members.
  const pipelineContactIds = new Set(Object.keys(stageMap));
  const leads = allContacts
    .filter(c => c.id && pipelineContactIds.has(c.id))
    .map(c => mapContactToLead(c, stageMap));

  Logger.log(`GHL: ${leads.length} pipeline leads (filtered from ${allContacts.length} total contacts)`);

  // v8.15: persist leads to GHL_Leads sheet so action=getfromsheets picks them up
  try { writeGHLLeadsToSheet(leads); } catch(e) { Logger.log('writeGHLLeadsToSheet: '+e.message); }

  return { leads, total: leads.length, synced: new Date().toISOString() };
}

// v8.15: Write GHL leads array to GHL_Leads sheet tab (creates tab if absent)
function writeGHLLeadsToSheet(leads) {
  if (!leads || leads.length === 0) return;
  const ss = SpreadsheetApp.openById(MASTER_SHEET_ID);
  let sheet = ss.getSheetByName('GHL_Leads');
  if (!sheet) sheet = ss.insertSheet('GHL_Leads');

  const preserved = {};
  try {
    const existing = sheet.getDataRange().getValues();
    if (existing.length > 1) {
      const hdrs = existing[0].map(h => String(h).toLowerCase().trim());
      const idIdx = hdrs.indexOf('ghlid');
      const keep = ['quality', 'dealvalue', 'urgencytimeline', 'notes'];
      for (let i = 1; idIdx >= 0 && i < existing.length; i++) {
        const id = String(existing[i][idIdx] || '').trim();
        if (!id) continue;
        preserved[id] = {};
        keep.forEach(k => {
          const idx = hdrs.indexOf(k);
          if (idx >= 0 && existing[i][idx] !== '') preserved[id][k] = existing[i][idx];
        });
      }
    }
  } catch (e) { Logger.log('writeGHLLeadsToSheet preserve read error: ' + e.message); }

  sheet.clearContents();
  const rows = leads.map(l => {
    const prior = preserved[l.ghlId] || {};
    if (!l.quality && prior.quality) l.quality = prior.quality;
    if ((l.dealValue === '' || l.dealValue == null) && prior.dealvalue !== undefined) l.dealValue = prior.dealvalue;
    if (!l.urgencyTimeline && prior.urgencytimeline) l.urgencyTimeline = prior.urgencytimeline;
    if (!l.notes && prior.notes) l.notes = prior.notes;
    return GHL_LEADS_HEADERS.map(h => l[h] !== undefined ? String(l[h]) : '');
  });
  sheet.getRange(1, 1, 1, GHL_LEADS_HEADERS.length).setValues([GHL_LEADS_HEADERS]);
  if (rows.length) sheet.getRange(2, 1, rows.length, GHL_LEADS_HEADERS.length).setValues(rows);
  Logger.log('writeGHLLeadsToSheet: wrote ' + leads.length + ' leads; manual quality/revenue/notes preserved');
}

// ─── v8.20: UPDATE QUALITY IN GHL_LEADS SHEET ────────────────────────────────
function updateLeadQuality(ghlId, quality) {
  return updateLeadRecord(ghlId, null, quality, null, null);
}

function updateLeadRecord(ghlId, status, quality, dealValue, notes, urgencyTimeline) {
  if (!ghlId) return { ok: false, error: 'ghlId required' };
  const q = quality == null ? null : String(quality).toUpperCase();
  if (q !== null && !['', 'A', 'B', 'C'].includes(q)) return { ok: false, error: 'Invalid quality' };
  const st = status == null ? null : String(status);
  const allowedStatuses = ['New','Contacted','Responded','Booked Call','Appointment','Appt Qualified','Strategy Session','Closed','Lost'];
  if (st !== null && !allowedStatuses.includes(st)) return { ok: false, error: 'Invalid status' };
  const urgency = urgencyTimeline == null ? null : String(urgencyTimeline);
  const allowedUrgencies = ['', 'No Timeline', 'Exploring This Year', 'Decision In 30 Days', 'Shortlisting Now'];
  if (urgency !== null && !allowedUrgencies.includes(urgency)) return { ok: false, error: 'Invalid urgency timeline' };
  let value = null;
  if (dealValue != null && String(dealValue).trim() !== '') {
    value = Number(String(dealValue).replace(/[^0-9.-]/g, ''));
    if (!isFinite(value) || value < 0) return { ok: false, error: 'Invalid deal value' };
  } else if (dealValue !== null) value = '';
  try {
    const ss = SpreadsheetApp.openById(MASTER_SHEET_ID);
    const sheet = ss.getSheetByName('GHL_Leads');
    if (!sheet) return { ok: false, error: 'GHL_Leads sheet not found' };
    const data = sheet.getDataRange().getValues();
    const hdrs = data[0].map(h => String(h).toLowerCase().trim());
    const idIdx = hdrs.indexOf('ghlid');
    if (idIdx < 0) return { ok: false, error: 'ghlId column not found' };
    GHL_LEADS_HEADERS.forEach(h => {
      const key = String(h).toLowerCase().trim();
      if (!hdrs.includes(key)) {
        sheet.getRange(1, hdrs.length + 1).setValue(h);
        hdrs.push(key);
      }
    });
    for (let i = 1; i < data.length; i++) {
      if (String(data[i][idIdx]).trim() !== String(ghlId).trim()) continue;
      const updates = { status: st, quality: q, dealvalue: value, urgencytimeline: urgency, notes: notes };
      Object.keys(updates).forEach(key => {
        if (updates[key] === null || updates[key] === undefined) return;
        const col = hdrs.indexOf(key);
        if (col >= 0) sheet.getRange(i + 1, col + 1).setValue(updates[key]);
      });
      return { ok: true, ghlId: String(ghlId), status: st, quality: q, dealValue: value, urgencyTimeline: urgency };
    }
    return { ok: false, error: 'Lead not found: ' + ghlId };
  } catch (e) {
    Logger.log('updateLeadRecord error: ' + e.message);
    return { ok: false, error: e.message };
  }
}

function mapGhlStageNameToDashboardStatus(name) {
  const key = String(name || '').toLowerCase().trim();
  const MAP = {
    'new lead': 'New', 'new': 'New', 'signup': 'New',
    'attempting contact': 'Contacted', 'contacted': 'Contacted', 'nurture': 'Contacted',
    'responded': 'Responded',
    'booked call': 'Booked Call', 'booked calls': 'Booked Call', 'book call': 'Booked Call',
    'call booked': 'Booked Call', 'booking': 'Booked Call', 'booked': 'Booked Call',
    'booked appointment': 'Booked Call', 'appointment booked': 'Booked Call', 'diagnosis call booked': 'Booked Call',
    'appointment': 'Appointment',
    'strategy session booked': 'Strategy Session', 'strategy session': 'Strategy Session',
    'implementation opportunity': 'Appt Qualified', 'attended': 'Appt Qualified', 'appt qualified': 'Appt Qualified',
    'close': 'Closed', 'closed': 'Closed', 'won': 'Closed',
    'unqualified': 'Lost', 'lost': 'Lost'
  };
  return MAP[key] || '';
}

function getPipelineStageStatusById(apiKey, locationId, pipelineId) {
  const out = {};
  try {
    const headers = { 'Authorization': 'Bearer ' + apiKey, 'Version': '2021-07-28' };
    const url = `${GHL_API_BASE}/opportunities/pipelines?locationId=${locationId}`;
    const res = UrlFetchApp.fetch(url, { headers, muteHttpExceptions: true });
    const body = JSON.parse(res.getContentText());
    const pipelines = body.pipelines || body.data || [];
    const pipe = pipelines.find(p => String(p.id || p.pipelineId || '') === String(pipelineId)) || pipelines[0];
    ((pipe && pipe.stages) || []).forEach(st => {
      const id = st.id || st.stageId || '';
      const status = mapGhlStageNameToDashboardStatus(st.name || st.title || '');
      if (id && status) out[id] = status;
    });
  } catch (e) {
    Logger.log('getPipelineStageStatusById warning: ' + e.message);
  }
  return out;
}

function buildStageMap(apiKey, locationId, pipelineId) {
  const headers = { 'Authorization': 'Bearer ' + apiKey, 'Version': '2021-07-28' };

  // v8.14: full mapping — GHL stage names (lowercase) → dashboard FUNNEL_STAGES values
  // 1-To-1 Pipeline actual stages: New Lead, Responded, Appointment, Strategy Session,
  //   Close, Nurture, Unqualified, Won, Lost
  const STAGE_STATUS = {
    'new lead':               'New',
    'new':                    'New',
    'signup':                 'New',
    'attempting contact':     'Contacted',
    'contacted':              'Contacted',
    'nurture':                'Contacted',
    'responded':              'Responded',
    'booked call':            'Booked Call',
    'booked calls':           'Booked Call',
    'book call':              'Booked Call',
    'call booked':            'Booked Call',
    'booking':                'Booked Call',
    'booked':                 'Booked Call',
    'booked appointment':     'Booked Call',
    'appointment booked':     'Booked Call',
    'diagnosis call booked':  'Booked Call',
    'appointment':            'Appointment',
    'strategy session booked':'Strategy Session',
    'strategy session':       'Strategy Session',
    'implementation opportunity': 'Appt Qualified',
    'attended':               'Appt Qualified',
    'appt qualified':         'Appt Qualified',
    'close':                  'Closed',
    'closed':                 'Closed',
    'won':                    'Closed',
    'unqualified':            'Lost',
    'lost':                   'Lost'
  };
  const STAGE_ID_STATUS = Object.assign({}, getPipelineStageStatusById(apiKey, locationId, pipelineId), {
    '29567d9f-bddf-485d-85dc-da928856d1e7': 'New',
    'ddc85555-52a5-4e98-8361-2eb74d84a8ec': 'Responded',
    'baf695fb-be5c-4f5b-8596-4193beca03c6': 'Appointment',
    '9881c6e9-2350-43b4-8518-5f8899b86a7e': 'Strategy Session',
    '9c4607fd-a265-4ab4-8acf-705b2fd18ff6': 'Closed',
    '0829d917-331f-4ee2-a240-ee99d97a6a28': 'Lost'
  });

  const map = {};
  let page  = 1;
  while (page <= 5) {
    const url = `${GHL_API_BASE}/opportunities/search?location_id=${locationId}&pipeline_id=${pipelineId}&limit=100&page=${page}`;
    try {
      const res  = UrlFetchApp.fetch(url, { headers, muteHttpExceptions: true });
      const body = JSON.parse(res.getContentText());
      const opps = body.opportunities || [];
      if (opps.length === 0) break;
      opps.forEach(opp => {
        const stageName = (opp.stage?.name || '').toLowerCase().trim();
        const stageId   = opp.pipelineStageId || opp.pipeline_stage_id || opp.stageId || opp.stage?.id || '';
        const oppStatus = String(opp.status || '').toLowerCase().trim();
        const status    = oppStatus === 'won' ? 'Closed' : oppStatus === 'lost' ? 'Lost' : (STAGE_ID_STATUS[stageId] || STAGE_STATUS[stageName] || 'New');
        // v8.20 FIX: GHL API returns contact ID as opp.contact?.id OR opp.contactId (direct property)
        const cid       = opp.contact?.id || opp.contactId || '';
        if (!cid) return; // skip if no contact ID
        const existing  = map[cid];
        // v8.19: store {status, date} so mapContactToLead uses opp createdAt as lead entry date
        const oppDate   = opp.createdAt ? Utilities.formatDate(new Date(opp.createdAt), 'Asia/Singapore', 'yyyy-MM-dd') : '';
        const entry     = { status, date: oppDate };
        if (!existing || statusRank(status) > statusRank(existing.status || existing)) map[cid] = entry;
      });
      if (!body.meta?.nextPage) break;
      page++;
      Utilities.sleep(100);
    } catch (e) {
      Logger.log('buildStageMap error: ' + e.message);
      break;
    }
  }
  Logger.log(`GHL: stage map built for ${Object.keys(map).length} contacts`);
  return map;
}

function statusRank(s) {
  if (s === 'Lost') return -1;
  const order = ['New','Contacted','Responded','Booked Call','Appointment','Appt Qualified','Strategy Session','Closed','Lost'];
  const i = order.indexOf(s);
  return i >= 0 ? i : 0;
}

// ─── v8.14: BIDIRECTIONAL GHL SYNC ────────────────────────────────────────────
// Called by action=updateghl  (dashboard status change → GHL opportunity stage)
// Pipeline: 1-To-1 Pipeline (BdutTA7xHUrNoPpWc5Nu)
function updateGHLOpportunity(ghlContactId, dashStatus, dealValue) {
  const apiKey = PropertiesService.getScriptProperties().getProperty('GHL_API_KEY');
  if (!apiKey)       return { ok: false, error: 'GHL_API_KEY not set' };
  if (!ghlContactId) return { ok: false, error: 'ghlId missing' };
  if (!dashStatus)   return { ok: false, error: 'status missing' };

  // Dashboard status → GHL stage ID  (1-To-1 Pipeline stages fetched 2026-06-22)
  const STAGE_IDS = {
    'New':              '29567d9f-bddf-485d-85dc-da928856d1e7',  // New Lead
    'Contacted':        '29567d9f-bddf-485d-85dc-da928856d1e7',  // v8.19 FIX: New Lead (was wrongly mapped to Responded)
    'Responded':        'ddc85555-52a5-4e98-8361-2eb74d84a8ec',  // Responded
    'Appointment':      'baf695fb-be5c-4f5b-8596-4193beca03c6',  // Appointment
    'Appt Qualified':   '9881c6e9-2350-43b4-8518-5f8899b86a7e',  // Strategy Session (closest)
    'Strategy Session': '9881c6e9-2350-43b4-8518-5f8899b86a7e',  // Strategy Session
    'Closed':           '9c4607fd-a265-4ab4-8acf-705b2fd18ff6',  // Close
    'Lost':             '0829d917-331f-4ee2-a240-ee99d97a6a28'   // Lost
  };

  const pipelineId = 'BdutTA7xHUrNoPpWc5Nu';
  const locationId = PropertiesService.getScriptProperties().getProperty('GHL_LOCATION_ID') || 'cyeYxFVQE1l73kO6S6Lx';
  const dynamicStageIds = {};
  const dynamicStatusById = getPipelineStageStatusById(apiKey, locationId, pipelineId);
  Object.keys(dynamicStatusById).forEach(id => {
    const st = dynamicStatusById[id];
    if (st && !dynamicStageIds[st]) dynamicStageIds[st] = id;
  });
  const stageId = dynamicStageIds[dashStatus] || STAGE_IDS[dashStatus];
  if (!stageId) return { ok: false, error: 'Unrecognised status: ' + dashStatus };

  const headers    = { 'Authorization': 'Bearer ' + apiKey, 'Version': '2021-07-28', 'Content-Type': 'application/json' };

  // Find the opportunity for this contact in the 1-To-1 pipeline
  try {
    const searchUrl = `${GHL_API_BASE}/opportunities/search?location_id=${locationId}&pipeline_id=${pipelineId}&contact_id=${ghlContactId}&limit=1`;
    const sr  = UrlFetchApp.fetch(searchUrl, { headers, muteHttpExceptions: true });
    const sb  = JSON.parse(sr.getContentText());
    const opp = (sb.opportunities || [])[0];

    if (!opp) {
      Logger.log(`updateghl: no opportunity found for contact ${ghlContactId}`);
      return { ok: false, error: 'No opportunity found for this contact in the 1-To-1 pipeline' };
    }

    const updateUrl = `${GHL_API_BASE}/opportunities/${opp.id}`;
    const payloadObj = { pipelineId, pipelineStageId: stageId };
    const money = dealValue != null && String(dealValue).trim() !== '' ? Number(String(dealValue).replace(/[^0-9.-]/g, '')) : null;
    if (money != null && isFinite(money) && money >= 0) payloadObj.monetaryValue = money;
    const payload   = JSON.stringify(payloadObj);
    const res       = UrlFetchApp.fetch(updateUrl, { method: 'PUT', headers, payload, muteHttpExceptions: true });
    const rb        = JSON.parse(res.getContentText());

    if (res.getResponseCode() === 200) {
      Logger.log(`updateghl: ${ghlContactId} → ${dashStatus} (stageId ${stageId})`);
      return { ok: true, opportunityId: opp.id, status: dashStatus, stageId };
    } else {
      Logger.log(`updateghl: PUT failed (${res.getResponseCode()}): ${res.getContentText()}`);
      return { ok: false, error: rb.message || 'GHL update failed', code: res.getResponseCode() };
    }
  } catch (e) {
    Logger.log('updateGHLOpportunity error: ' + e.message);
    return { ok: false, error: e.message };
  }
}

function mapContactToLead(c, stageMap) {
  const name = c.contactName || [c.firstName, c.lastName].filter(Boolean).join(' ') || '';
  const attrs   = c.attributions || [];
  const adAttr  = attrs.find(a => a.utmAdId) || attrs[0] || {};
  const lastAttr= attrs.find(a => a.isLast) || attrs[attrs.length - 1] || {};

  const sourceAdId   = adAttr.utmAdId   || '';
  const sourceAdName = adAttr.utmContent || adAttr.utmCampaign || '';
  const platform     = (adAttr.utmSource || adAttr.adSource || adAttr.medium || 'unknown').toLowerCase();
  const campaignName = adAttr.utmCampaign || lastAttr.utmCampaign || '';

  // v8.19: stageMap now holds {status, date} objects (date = opp.createdAt = when lead entered pipeline)
  const stageEntry = stageMap[c.id] || null;
  let status = stageEntry ? (stageEntry.status || stageEntry) : null;
  const hasCalendar = attrs.some(a => String(a.medium || a.source || '').toLowerCase().includes('calendar'));
  if (!status) {
    status = hasCalendar ? 'Booked Call' : 'New';
  }
  // v8.23: lead date = contact opt-in date in Singapore time; pipeline stage date is not the lead date.
  const oppDate = stageEntry && stageEntry.date ? stageEntry.date : '';
  const contactDate = c.dateAdded ? Utilities.formatDate(new Date(c.dateAdded), 'Asia/Singapore', 'yyyy-MM-dd') : '';

  let proptype = '';
  const tagsStr = (c.tags || []).join(' ').toLowerCase();
  if (tagsStr.includes('newlaunch') || c.source?.toLowerCase().includes('new launch')) proptype = 'New Launch';
  else if (tagsStr.includes('familylegacy') || c.source?.toLowerCase().includes('family')) proptype = 'Family Legacy';
  else if (c.source) proptype = c.source;

  return {
    ghlId:        c.id,
    name,
    contact:      c.email || c.phone || '',
    phone:        c.phone  || '',
    email:        c.email  || '',
    sourceAdId,   sourceAdName,
    platform:     platform.includes('facebook') || platform.includes('meta') ? 'Meta'
                : platform.includes('google') || platform.includes('yt') ? 'Google'
                : (sourceAdId || campaignName) ? 'Meta' : 'Other', // v8.17: has ad attribution → Meta
    campaignName,
    status,
    quality:      '', // manually set in GHL_Leads sheet: Real / Junk / Fake
    proptype,
    date:         contactDate || oppDate,
    responded:    status !== 'Lost' && statusRank(status) >= statusRank('Responded') ? 'Y' : '',
    appointment:  status !== 'Lost' && (statusRank(status) >= statusRank('Appointment') || hasCalendar) ? 'Booked' : '',
    strategySession: status !== 'Lost' && statusRank(status) >= statusRank('Strategy Session') ? 'Y' : '',
    qualified:    status !== 'Lost' && statusRank(status) >= statusRank('Appt Qualified') ? 'Y' : '',
    dealValue:    '',
    urgencyTimeline: '',
    tags:         (c.tags || []).join(', '),
    source:       c.source || '',
    locationId:   c.locationId || '',
    notes:        ''
  };
}

// ─── GHL SHEET TAB + LP + REFERRALS MERGE ────────────────────────────────────
function readGHLLeadsFromSheet() {
  try {
    const ghlLeads = readGHLTabLeads();
    const lpLeads  = readLPLeadsFromAllTabs();
    const refLeads = readReferralsOrganicLeads();

    Logger.log(`Merging: ${ghlLeads.length} GHL + ${lpLeads.length} LP + ${refLeads.length} Referral leads`);

    const deduped = [];
    const seen    = new Set();

    function dedupeKey(lead) {
      const phone = normalisePhone(lead.phone);
      const email = (lead.email || '').toLowerCase().trim();
      const name  = (lead.name  || '').toLowerCase().trim();
      return phone || email || (name ? 'name:'+name : null);
    }

    ghlLeads.forEach(l => {
      const key = dedupeKey(l);
      if (!key || !seen.has(key)) { deduped.push(l); if (key) seen.add(key); }
    });

    lpLeads.forEach(l => {
      const key = dedupeKey(l);
      if (!key || !seen.has(key)) { deduped.push(l); if (key) seen.add(key); }
      else {
        const existing = deduped.find(x => dedupeKey(x) === key);
        if (existing) {
          if (!existing.sourceAdId   && l.sourceAdId)   existing.sourceAdId   = l.sourceAdId;
          if (!existing.sourceAdName && l.sourceAdName) existing.sourceAdName = l.sourceAdName;
          if (!existing.campaignName && l.campaignName) existing.campaignName = l.campaignName;
        }
      }
    });

    refLeads.forEach(l => {
      const key = dedupeKey(l);
      if (!key || !seen.has(key)) { deduped.push(l); if (key) seen.add(key); }
    });

    Logger.log(`Combined leads after dedup: ${deduped.length}`);
    return {
      leads:     deduped,
      total:     deduped.length,
      synced:    new Date().toISOString(),
      source:    'sheet+lp+referrals',
      breakdown: { ghl: ghlLeads.length, lp: lpLeads.length, referrals: refLeads.length }
    };
  } catch (err) {
    Logger.log('readGHLLeadsFromSheet error: ' + err.message);
    return { leads: [], error: err.message, total: 0 };
  }
}

function _formatSheetDate(val) {
  // v8.12: converts GAS Date objects AND Excel/Sheets serial numbers to YYYY-MM-DD
  if (!val && val !== 0) return '';
  if (val instanceof Date) {
    try { return Utilities.formatDate(val, 'Asia/Singapore', 'yyyy-MM-dd'); } catch(e) {}
    return val.toISOString().slice(0, 10);
  }
  if (typeof val === 'number' && val > 1000 && val < 200000) {
    // Excel/Sheets serial: days since Dec 30 1899
    const d = new Date(Math.round((val - 25569) * 86400000));
    try { return Utilities.formatDate(d, 'Asia/Singapore', 'yyyy-MM-dd'); } catch(e) {}
    return d.toISOString().slice(0, 10);
  }
  const s = String(val).trim();
  if (!s) return '';
  if (/^\d{4}-\d{2}-\d{2}$/.test(s)) return s;
  const p = new Date(s);
  if (isNaN(p.getTime())) return s;
  try { return Utilities.formatDate(p, 'Asia/Singapore', 'yyyy-MM-dd'); } catch(e) {}
  return p.toISOString().slice(0, 10);
}

function readGHLTabLeads() {
  try {
    const ss    = SpreadsheetApp.openById(MASTER_SHEET_ID);
    const sheet = ss.getSheetByName('GHL_Leads');
    if (!sheet) return [];
    const data  = sheet.getDataRange().getValues();
    if (data.length < 2) return [];

    const hdrs = data[0].map(h => String(h || '').trim().toLowerCase());
    const _dateIdx = hdrs.indexOf('date'); // raw index for proper date formatting
    return data.slice(1)
      .filter(row => row.some(cell => cell !== '' && cell !== null))
      .map(row => {
        const obj = {};
        hdrs.forEach((h, i) => { if (h) obj[h] = row[i] !== undefined ? String(row[i]) : ''; });
        return {
          ghlId:        obj.ghlid         || obj.id || '',
          name:         obj.name          || '',
          contact:      obj.contact       || obj.email || obj.phone || '',
          phone:        obj.phone         || '',
          email:        obj.email         || '',
          sourceAdId:   obj.sourceadid    || '',
          sourceAdName: obj.sourceadname  || '',
          platform:     obj.platform      || 'Other',
          campaignName: obj.campaignname  || '',
          status:       obj.status        || 'New',
          quality:      obj.quality       || '',   // v8: Real / Junk / Fake
          proptype:     obj.proptype      || '',
          date:         _formatSheetDate(_dateIdx >= 0 ? row[_dateIdx] : (obj.date || '')),
          responded:    obj.responded     || '',
          appointment:  obj.appointment   || '',
          strategySession: obj.strategysession || '',
          qualified:    obj.qualified     || '',
          dealValue:    obj.dealvalue     || '',
          urgencyTimeline: obj.urgencytimeline || 'No Timeline',
          tags:         obj.tags          || '',
          // v8.14: prefer platform field for display; fall back to raw GHL source
          source:       obj.platform === 'Meta' ? 'Meta' : obj.platform === 'Google' ? 'Google' : (obj.source || 'GHL'),
          notes:        obj.notes         || ''
        };
      })
      .filter(l => l.name || l.email || l.phone);
  } catch (err) {
    Logger.log('readGHLTabLeads error: ' + err.message);
    return [];
  }
}

function readLPLeadsFromAllTabs() {
  const allLeads = [];
  try {
    const ss     = SpreadsheetApp.openById(LP_LEADS_SHEET_ID);
    const sheets = ss.getSheets();

    sheets.forEach(sheet => {
      const data = sheet.getDataRange().getValues();
      if (data.length < 2) return;

      let headerRowIdx = -1;
      for (let i = 0; i < Math.min(5, data.length); i++) {
        const rowLower = data[i].map(c => String(c || '').toLowerCase().trim());
        const hasMobile  = rowLower.some(h => h === 'mobile');
        const hasCampaign= rowLower.some(h => h.includes('campaign name'));
        const hasAd      = rowLower.some(h => h === 'ad' || h === 'ad name');
        if (hasMobile && hasCampaign && hasAd) { headerRowIdx = i; break; }
      }
      if (headerRowIdx === -1) return;

      const hdrs    = data[headerRowIdx].map(h => String(h || '').toLowerCase().trim());
      const tabName = sheet.getName();

      // v8.3: within-tab dedup by normalised phone/email
      const tabSeen = new Set();

      data.slice(headerRowIdx + 1)
        .filter(row => row.some(cell => cell !== '' && cell !== null))
        .forEach(row => {
          const obj = {};
          hdrs.forEach((h, i) => { if (h) obj[h] = row[i] !== undefined ? String(row[i]).trim() : ''; });
          const name       = obj.name || '';
          const email      = obj.email || '';
          const phone      = obj.mobile || obj.phone || '';
          if (!name && !email && !phone) return;
          // v8.3: Spam filter — skip obvious junk/test entries
          const nameLower = name.toLowerCase();
          if (/fuck|test lead|spam|fake|xxx|zzz|aaa|111|asdf/.test(nameLower)) return;
          // v8.3: Within-tab dedup
          const normPh = normalisePhone(phone);
          const tabKey = normPh || email.toLowerCase().trim();
          if (tabKey && tabSeen.has(tabKey)) return;
          if (tabKey) tabSeen.add(tabKey);

          const platformRaw = (obj['platform (yt/meta)'] || obj.platform || '').toLowerCase();
          // v8.17: infer platform — if ad/campaign fields populated and not clearly Google → Meta
          const adName     = (obj.ad || obj['ad name'] || '').toLowerCase();
          const campName   = (obj['campaign name'] || '').toLowerCase();
          const isGoogle   = platformRaw.includes('google') || platformRaw.includes('yt') || platformRaw.includes('youtube')
                           || campName.includes('google') || campName.includes('gdn') || campName.includes('youtube');
          const isMeta     = platformRaw.includes('meta') || platformRaw.includes('fb') || platformRaw.includes('facebook');
          const hasAdData  = !!(obj.ad || obj['ad name'] || obj['ad id'] || obj['campaign name']);
          const platform   = isGoogle ? 'Google'
                           : isMeta   ? 'Meta'
                           : hasAdData ? 'Meta'   // has ad attribution → assume Meta
                           : 'Other';

          allLeads.push({
            ghlId:'', name, contact: email || phone, phone, email,
            sourceAdId:   obj['ad id']       || '',
            sourceAdName: obj.ad             || obj['ad name'] || '',
            adsetId:      obj['adset id']    || '',
            adsetName:    obj.adset          || '',
            campaignId:   obj['campaign id'] || '',
            campaignName: obj['campaign name']|| '',
            platform, status: 'New', quality: '',
            proptype:     inferProptypeFromTab(tabName),
            date:         formatDate(obj.date || ''),
            responded:'', appointment:'', strategySession:'', qualified:'',
            dealValue:'', tags:'', source: platform, notes:''
          });
        });
    });
  } catch (err) {
    Logger.log('readLPLeadsFromAllTabs error: ' + err.message);
  }
  return allLeads;
}

function readReferralsOrganicLeads() {
  const leads = [];
  try {
    const ss    = SpreadsheetApp.openById(MASTER_SHEET_ID);
    const sheet = ss.getSheetByName('Referrals_Organic');
    if (!sheet) { Logger.log('Referrals_Organic tab not found'); return leads; }
    const data  = sheet.getDataRange().getValues();
    if (data.length < 2) return leads;
    const hdrs  = data[0].map(h => String(h || '').toLowerCase().trim());
    data.slice(1)
      .filter(row => row.some(cell => cell !== '' && cell !== null))
      .forEach(row => {
        const obj = {};
        hdrs.forEach((h, i) => { if (h) obj[h] = row[i] !== undefined ? String(row[i]).trim() : ''; });
        const name = obj.name || '', phone = obj.phone || obj.mobile || '', email = obj.email || '';
        if (!name && !email && !phone) return;
        leads.push({
          ghlId:'', name, contact: email || phone, phone, email,
          sourceAdId:'', sourceAdName: obj['referred by'] ? 'Ref: ' + obj['referred by'] : '',
          adsetId:'', adsetName:'', campaignId:'', campaignName:'',
          platform: obj.source || 'Referral', status:'New', quality:'',
          proptype: obj['property interest'] || '',
          date: formatDate(obj.date || ''),
          responded:'', appointment:'', strategySession:'', qualified:'',
          dealValue:'', tags: obj.remarks || obj.notes || '',
          source: obj.source || 'Referral', notes:''
        });
      });
    Logger.log(`Referrals_Organic: ${leads.length} leads`);
  } catch (err) {
    Logger.log('readReferralsOrganicLeads error: ' + err.message);
  }
  return leads;
}

// ─── META API HELPER ──────────────────────────────────────────────────────────
function apiGet(token, path, params) {
  const base = `https://graph.facebook.com/${META_API_VER}${path}`;
  const qs   = Object.entries({ ...params, access_token: token })
    .map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`)
    .join('&');
  const res  = UrlFetchApp.fetch(`${base}?${qs}`, { muteHttpExceptions: true });
  const json = JSON.parse(res.getContentText());
  if (json.error) throw new Error(`Meta API error: ${json.error.message} (code ${json.error.code})`);
  return json;
}

// ─── UTILITY ──────────────────────────────────────────────────────────────────
function extractAction(actions, type) {
  if (!actions) return 0;
  const match = actions.find(a => a.action_type === type);
  return parseFloat(match?.value || 0);
}

function extractVideoAction(videoActions) {
  if (!videoActions || !videoActions.length) return 0;
  return parseInt(videoActions[0]?.value || 0);
}

function normaliseStatus(s) {
  if (!s) return 'Active';
  const up = s.toUpperCase();
  if (up === 'ACTIVE' || up === 'ENABLED') return 'Active';
  if (up === 'PAUSED') return 'Paused';
  return 'Paused';
}

function detectFormatFromCreative(cr, adName) {
  const n = (adName || '').toUpperCase();
  if (/-I$|_I$|-IMG$|-IMAGE$|\bIMG\b|\bIMAGE\b/.test(n)) return 'Image';
  if (/-C$|_C$|-CAR$|-CAROUSEL$/.test(n)) return 'Carousel';
  if (/-S$|_S$|-STORY$/.test(n)) return 'Story';
  if (/-V$|_V$|-VID$|-VIDEO$/.test(n)) return 'Video';
  const spec = cr.object_story_spec;
  if (spec) {
    if (spec.template_data?.format === 'CAROUSEL') return 'Carousel';
    if ((spec.link_data?.child_attachments?.length || 0) > 0) return 'Carousel';
    if (cr.image_url) return 'Image';
    if (spec.link_data?.image_hash || spec.link_data?.picture) return 'Image';
    if (spec.video_data) return 'Video';
  }
  if (cr.image_url) return 'Image';
  return 'Video';
}

function extractAudience(targeting) {
  if (!targeting) return '';
  const parts = [];
  if (targeting.custom_audiences?.length) parts.push('Custom Audience');
  if (targeting.lookalike_specs?.length) parts.push('Lookalike');
  if (targeting.flexible_spec?.length) parts.push('Interest');
  if (targeting.geo_locations?.countries?.length) parts.push(targeting.geo_locations.countries.join(','));
  return parts.join(' | ') || 'Broad';
}

function inferProptypeFromTab(tabName) {
  const t = tabName.toLowerCase();
  // v8.17: "new launch" and any "launch" tab (incl. "Legacy Launch" campaign = New Launch property)
  if (t.includes('new launch') || t.includes('lentor')) return 'New Launch';
  if (t.includes('launch')) return 'New Launch'; // "Legacy Launch" campaign still sells New Launch
  if (t.includes('legacy') || t.includes('vela') || t.includes('tengah') || t.includes('family')) return 'Family Legacy';
  return '';
}

function normalisePhone(phone) {
  if (!phone) return '';
  const digits = String(phone).replace(/\D/g, '');
  return digits.length >= 8 ? digits.slice(-8) : digits || '';
}

function formatDate(d) {
  if (!d || d === '') return '';
  if (/^\d{4}-\d{2}-\d{2}/.test(String(d))) return String(d).slice(0, 10);
  const m = String(d).match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})/);
  if (m) return `${m[3]}-${m[2].padStart(2,'0')}-${m[1].padStart(2,'0')}`;
  if (d instanceof Date) return Utilities.formatDate(d, 'Asia/Singapore', 'yyyy-MM-dd');
  return String(d).slice(0, 10);
}

// ─── DASHBOARD HTML ───────────────────────────────────────────────────────────
/**
 * Returns the full REI Dashboard v11 HTML for serving from the Web App URL.
 * Modifications vs REI_Dashboard_v11.html:
 *   - webAppUrl auto-detects current deployment URL
 *   - DOMContentLoaded auto-syncs Meta then loads from sheets
 *   - Web App URL settings input removed (no longer needed)
 */
function getDashboardHtml(webAppUrl) {
  return `<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>REI Media Buyer Dashboard v8.43</title>
<style>
:root{--bg:#F5F2EE;--surface:#FFFFFF;--bg-table:#FAFAF8;--bg-hd:#1F2F3D;--text:#1F2F3D;--muted:#6B7280;--hd-txt:#FFFFFF;--border:#E5E0D8;--champagne:#D8C3A8;--navy:#1F2F3D;--gold:#BFA37A;--gold-lt:#F0E8D8;--kill:#DC2626;--kill-bg:#FEE2E2;--scale:#16A34A;--scale-bg:#DCFCE7;--mon:#D97706;--mon-bg:#FEF3C7;--shadow:0 1px 4px rgba(0,0,0,.08);--radius:10px;--hdr-h:58px;--gbar-h:46px;--tabs-top:104px;--content-top:150px;--lead-panel-h:0px}
[data-theme=dark]{--bg:#111827;--surface:#1F2937;--bg-table:#1A2332;--bg-hd:#0F1923;--text:#F9FAFB;--muted:#9CA3AF;--hd-txt:#F9FAFB;--border:#374151;--gold-lt:#2A2010;--shadow:0 1px 4px rgba(0,0,0,.4)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;font-size:15px;background:var(--bg);color:var(--text);min-height:100vh}

/* Header */
.hdr{background:var(--bg-hd);padding:0 20px;display:flex;align-items:center;min-height:58px;gap:12px;position:sticky;top:0;z-index:200;box-shadow:0 2px 8px rgba(0,0,0,.25)}
.hdr-logo{height:42px;min-width:70px;display:flex;align-items:center}.hdr-logo img{height:40px;width:auto;max-width:126px;object-fit:contain}.hdr-logo-fallback{font-size:18px;font-weight:800;color:var(--champagne)}.ver-badge{background:var(--gold);color:#fff;padding:3px 8px;border-radius:999px;font-size:11px;font-weight:800;letter-spacing:.3px}.qbtn{border:0;border-radius:6px;padding:5px 10px;min-width:48px;color:#fff;font-weight:800;cursor:pointer}.q-a{background:#16A34A}.q-b{background:#D97706}.q-c{background:#DC2626}.q-none{background:#94A3B8}.rev-wrap{display:flex;align-items:center;gap:5px;min-width:145px}.rev-check{width:18px;height:18px;accent-color:#16A34A;cursor:pointer}.rev-input{width:105px;padding:5px 7px;border:1px solid var(--border);border-radius:6px;background:var(--surface);color:var(--text);font-size:12px}
.hdr-sub{font-size:13px;color:rgba(255,255,255,.45);flex:1}
.urg-select{min-width:150px;padding:5px 8px;border:1px solid var(--border);border-radius:7px;background:var(--surface);color:var(--text);font-size:12px;font-weight:650}.urg-no{border-left:4px solid #94A3B8}.urg-year{border-left:4px solid #0EA5E9}.urg-30{border-left:4px solid #DC2626}.urg-short{border-left:4px solid #D97706}
.hdr-r{display:flex;align-items:center;gap:8px}
.sync-dot{width:8px;height:8px;border-radius:50%;background:#6B7280;display:inline-block}
.sync-dot.ok{background:#4ade80}.sync-dot.err{background:#f87171}.sync-dot.syncing{animation:pulse .7s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
.btn{cursor:pointer;border:none;border-radius:7px;padding:7px 14px;font-size:13px;font-weight:500;transition:all .15s;white-space:nowrap}
.btn-ghost{background:rgba(255,255,255,.09);color:#fff;border:1px solid rgba(255,255,255,.18)}.btn-ghost:hover{background:rgba(255,255,255,.18)}
.btn-primary{background:var(--gold);color:#fff}.btn-primary:hover{opacity:.85}
.btn-danger{background:var(--kill);color:#fff}.btn-success{background:var(--scale);color:#fff}
.btn-sm{padding:3px 9px;font-size:12px;border-radius:5px;cursor:pointer;border:1px solid var(--border);background:var(--bg);color:var(--text)}
.btn-sm:hover{background:var(--gold-lt)}.btn-sm-kill:hover{background:var(--kill-bg);border-color:var(--kill);color:var(--kill)}

/* Global filter bar */
.gbar{background:var(--surface);border-bottom:1px solid var(--border);padding:9px 20px;display:flex;align-items:center;gap:18px;flex-wrap:wrap;position:sticky;top:var(--hdr-h);z-index:150}
.gbar-group{display:flex;align-items:center;gap:6px}
.gbar-label{font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.4px;white-space:nowrap}
.pill{padding:4px 12px;border-radius:20px;font-size:12px;font-weight:500;background:var(--bg);border:1px solid var(--border);cursor:pointer;color:var(--muted);transition:all .13s}
.pill:hover{border-color:var(--gold);color:var(--text)}
.pill.active{background:var(--navy);color:#fff;border-color:var(--navy)}
[data-theme=dark] .pill.active{background:var(--gold);border-color:var(--gold)}
.gbar-sync{margin-left:auto;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.sync-label{font-size:12px;color:var(--muted)}

/* Tabs */
.tabs{display:flex;background:var(--surface);border-bottom:2px solid var(--border);padding:0 20px;gap:2px;overflow-x:auto;position:sticky;top:var(--tabs-top);z-index:140;box-shadow:0 2px 7px rgba(0,0,0,.05)}
.tab{padding:12px 16px;cursor:pointer;font-size:13px;font-weight:600;color:var(--muted);border-bottom:2px solid transparent;margin-bottom:-2px;transition:all .15s;white-space:nowrap}
.tab:hover{color:var(--text)}.tab.active{color:var(--navy);border-bottom-color:var(--gold)}
[data-theme=dark] .tab.active{color:var(--champagne)}

/* Pages */
.page{display:none;padding:20px;max-width:1600px;margin:0 auto}.page.active{display:block}

/* KPI Grid */
.kpi-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:14px;margin-bottom:20px}
.kpi{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px;box-shadow:var(--shadow)}
.kpi-lbl{font-size:12px;color:var(--muted);font-weight:500;margin-bottom:4px}
.kpi-val{font-size:26px;font-weight:700}.kpi-sub{font-size:11px;color:var(--muted);margin-top:2px}

/* Section headers */
.sec-hdr{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;gap:10px;flex-wrap:wrap}
.sec-title{font-size:17px;font-weight:700}.sec-acts{display:flex;gap:7px;align-items:center;flex-wrap:wrap}
.search-wrap{position:relative}.search-wrap input{padding:7px 10px 7px 32px;border:1px solid var(--border);border-radius:7px;background:var(--bg);color:var(--text);font-size:13px;width:200px}
.search-wrap::before{content:'🔍';position:absolute;left:8px;top:50%;transform:translateY(-50%);font-size:13px}

/* Standard table */
.tbl-wrap{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);overflow:clip;box-shadow:var(--shadow);margin-bottom:20px}
#page-campaigns .tbl-wrap thead th,#page-adsets .tbl-wrap thead th{position:sticky;top:var(--content-top);z-index:5;background:var(--bg-hd)}
.cr-table thead th{position:sticky;top:0;z-index:5;background:var(--bg-hd);color:var(--hd-txt)}
.tbl-wrap table thead th{position:sticky;top:0;z-index:5;background:var(--bg-hd);color:var(--hd-txt)}
#page-leads .lead-sticky-panel{position:sticky;top:var(--content-top);z-index:125;background:var(--bg);padding:0 0 8px;margin:-2px 0 8px}
#page-leads .tbl-wrap.lead-table-wrap{overflow:auto}
#page-leads .tbl-wrap.lead-table-wrap table{font-size:12px}
#page-leads .tbl-wrap.lead-table-wrap th,#page-leads .tbl-wrap.lead-table-wrap td{padding:4px 6px}
#page-leads .tbl-wrap.lead-table-wrap .col-action{white-space:nowrap;min-width:70px;max-width:85px}
#page-leads .lead-hdr{margin-bottom:8px;align-items:flex-start}
#page-leads .lead-title-row{flex-wrap:wrap;gap:8px}
.filter-row select,.filter-row input{font-size:12px;padding:4px 6px;border-radius:4px;border:1px solid var(--border)}
#page-leads .lead-title-row{display:flex;align-items:center;gap:12px;flex-wrap:wrap;min-width:0}
#page-leads .lead-filter-group{display:flex;align-items:center;gap:5px;flex-wrap:wrap}
#page-leads .lead-filter-label{font-size:11px;color:var(--muted);font-weight:800;text-transform:uppercase;letter-spacing:.3px}
#page-leads .lead-filter-group .pill{padding:3px 9px;font-size:11px}
#page-leads .search-wrap input{width:235px}
#page-leads #leadKpis{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-bottom:10px;padding-bottom:4px}
#page-leads #leadKpis .kpi{padding:4px 6px;min-height:unset;text-align:center}
#page-leads #leadKpis .kpi-lbl{font-size:9px;margin-bottom:2px;line-height:1.2;text-transform:uppercase;letter-spacing:.3px}
#page-leads #leadKpis .kpi-val{font-size:14px!important;line-height:1.1;font-weight:800}
#page-leads #leadKpis .kpi-sub{font-size:9px;line-height:1.2;margin-top:2px}
#page-leads .lead-table-wrap{max-height:calc(100vh - var(--content-top) - var(--lead-panel-h) - 40px);overflow:auto;position:relative}
#page-leads .lead-table-wrap table{min-width:0;width:100%;table-layout:fixed}
#page-leads .lead-table-wrap thead th{position:sticky;top:0;z-index:95;background:var(--bg-hd);color:var(--hd-txt);box-shadow:0 2px 0 var(--border)}
#page-leads .lead-table-wrap td{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#page-leads .lead-table-wrap td:nth-child(6),#page-leads .lead-table-wrap td:nth-child(7),#page-leads .lead-table-wrap td:nth-child(8),#page-leads .lead-table-wrap td:nth-child(9){overflow:visible}
#page-leads th:nth-child(1),#page-leads td:nth-child(1){width:10%}
#page-leads th:nth-child(2),#page-leads td:nth-child(2){width:9%}
#page-leads th:nth-child(3),#page-leads td:nth-child(3){width:15%}
#page-leads th:nth-child(4),#page-leads td:nth-child(4){width:6%}
#page-leads th:nth-child(5),#page-leads td:nth-child(5){width:13%}
#page-leads th:nth-child(6),#page-leads td:nth-child(6){width:19%}
#page-leads th:nth-child(7),#page-leads td:nth-child(7){width:22%;vertical-align:top}
#page-leads th:nth-child(8),#page-leads td:nth-child(8){width:7%}
#page-leads th:nth-child(9),#page-leads td:nth-child(9){width:8%}
#page-leads th:nth-child(10),#page-leads td:nth-child(10){width:5%}
#page-leads th:nth-child(11),#page-leads td:nth-child(11){width:7%;min-width:85px}
#page-leads .pipeline-flow{gap:1px;transform:scale(.82);transform-origin:left center}
#page-leads .row-acts{opacity:1!important}
#page-leads .row-acts .btn-sm{font-size:9px;padding:2px 4px}
#page-leads .pip-btn{padding:4px 7px;font-size:11px}
#page-leads .urg-select{min-width:0;width:100%;font-size:10px;display:block;margin-top:2px}
#page-leads .rev-wrap{min-width:118px}#page-leads .rev-input{width:92px}
@media(max-width:1500px){#page-leads #leadKpis{grid-template-columns:repeat(7,minmax(0,1fr))}#page-leads .lead-table-wrap table{min-width:0}}
table{width:100%;border-collapse:collapse;font-size:13px}
thead th{background:var(--bg-hd);color:var(--hd-txt);padding:10px 12px;text-align:left;font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.5px;white-space:nowrap}
thead th.sortable{cursor:pointer;user-select:none}
thead th.sortable:hover{background:#2a3f52}
tbody tr{border-bottom:1px solid var(--border);transition:background .1s}
tbody tr:hover{background:var(--gold-lt)}
tbody tr:last-child{border-bottom:none}
td{padding:11px 12px;vertical-align:middle}
.td-name{font-weight:600}.td-muted{color:var(--muted);font-size:12px}
.sort-arrow{font-size:10px;margin-left:2px;opacity:.25}.sort-arrow.active{opacity:1;color:var(--gold)}
.row-acts{display:flex;gap:5px;opacity:0;transition:opacity .13s}
tr:hover .row-acts{opacity:1}

/* Creatives wide table — sticky cols */
.cr-wrap{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);overflow:auto;max-height:75vh;box-shadow:var(--shadow);margin-bottom:20px;position:relative}
.cr-table{width:max-content;min-width:100%;border-collapse:collapse;font-size:13px}
.cr-table thead th{background:var(--bg-hd);color:var(--hd-txt);padding:10px 11px;text-align:left;font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.4px;white-space:nowrap}
.cr-table tbody tr{border-bottom:1px solid var(--border)}.cr-table tbody tr:hover td{background:var(--gold-lt)}
.cr-table td{padding:10px 11px;vertical-align:middle;background:var(--surface)}
.cr-table tbody tr:hover td.sticky-l0,.cr-table tbody tr:hover td.sticky-l1,.cr-table tbody tr:hover td.sticky-r0{background:var(--gold-lt)}
.sticky-l0{position:sticky;left:0;z-index:4;background:var(--surface);box-shadow:2px 0 4px rgba(0,0,0,.05)}
.sticky-l1{position:sticky;left:68px;z-index:4;background:var(--surface);min-width:180px;max-width:220px}
.sticky-r0{position:sticky;right:0;z-index:4;background:var(--surface);box-shadow:-3px 0 8px rgba(0,0,0,.12)}
.cr-table thead .sticky-l0,.cr-table thead .sticky-l1{z-index:5}.cr-table thead .sticky-r0{z-index:5}

/* Thumbnail */
.thumb-cell{width:60px;text-align:center}
.thumb{width:56px;height:40px;object-fit:cover;border-radius:5px;cursor:pointer;border:2px solid transparent;transition:border-color .15s}
.thumb:hover{border-color:var(--gold)}
.thumb-placeholder{width:56px;height:40px;border-radius:5px;background:var(--border);display:flex;align-items:center;justify-content:center;font-size:18px;cursor:default}

/* Lightbox */
.lbox{display:none;position:fixed;inset:0;background:rgba(0,0,0,.85);z-index:2000;align-items:center;justify-content:center}
.lbox.open{display:flex}
.lbox-content{max-width:90vw;max-height:92vh;position:relative;overflow-y:auto;overflow-x:hidden;border-radius:8px}
.lbox-content img,.lbox-content video{max-width:100%;max-height:78vh;border-radius:8px}
.lbox-close{position:absolute;top:-36px;right:0;color:#fff;font-size:28px;cursor:pointer;line-height:1}
.lbox-name{position:absolute;bottom:-28px;left:0;right:0;text-align:center;color:rgba(255,255,255,.7);font-size:13px}

/* Signal / Status badges */
.sig{display:inline-block;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.2px}
.sig-Scale{background:var(--scale-bg);color:var(--scale)}
.sig-Monitor{background:var(--mon-bg);color:var(--mon)}
.sig-Kill{background:var(--kill-bg);color:var(--kill)}
.sig-Test{background:#EEF2FF;color:#4338CA}
.sig-Pause{background:#F1F5F9;color:#475569}
.plat-badge{display:inline-block;padding:2px 8px;border-radius:4px;font-size:10px;font-weight:700}
.plat-Meta{background:#E8F0FE;color:#1A56DB}.plat-Google{background:#FEF3C7;color:#92400E}
[data-theme=dark] .plat-Meta{background:#1E3A6E;color:#93C5FD}
.status-Active{color:var(--scale);font-weight:600}.status-Paused{color:var(--muted)}
.lead-badge{display:inline-block;padding:2px 8px;border-radius:20px;font-size:11px;font-weight:600}
.kpi-sel{box-shadow:0 0 0 2px var(--blue,#1D4ED8);background:var(--blue-tint,#EFF6FF)}
.lb-New{background:#EFF6FF;color:#1D4ED8}.lb-Contacted{background:#FFF7ED;color:#C2410C}
.lb-Responded,.lb-Potential,.lb-Qualified{background:#DCFCE7;color:#15803D}
.lb-BookedCall,.lb-Booked{background:#DBEAFE;color:#1D4ED8}.lb-Appointment,.lb-ApptSet{background:#F3E8FF;color:#7E22CE}
.lb-ApptQualified,.lb-ApptVerified{background:#EDE9FE;color:#4C1D95}
.lb-StrategySession{background:#FEF9C3;color:#854D0E}
.lb-Closed{background:#D1FAE5;color:#065F46}.lb-Lost{background:#FEE2E2;color:#991B1B}
/* Funnel stage toggle buttons */
/* v8.19: pipeline flow styles */
.pipeline-flow{display:flex;align-items:center;gap:2px;white-space:nowrap}
.pip-btn{border:none;border-radius:4px;padding:2px 7px;font-size:11px;cursor:pointer;font-weight:600;transition:all .15s}
.pip-done{background:#dcfce7;color:#166534}
.pip-at{background:#2563eb;color:#fff}
.pip-todo{background:#f1f5f9;color:#94a3b8}
.pip-arr{color:#cbd5e1;font-size:11px;padding:0 1px;user-select:none}
.ftgl{display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;border:2px solid var(--border);cursor:pointer;font-size:13px;transition:all .15s;background:var(--surface)}
.ftgl.on{border-color:transparent}
.ftgl-responded.on{background:#DCFCE7;color:#15803D}
.ftgl-appointment.on{background:#F3E8FF;color:#7E22CE}
.ftgl-apptq.on{background:#EDE9FE;color:#4C1D95}
.ftgl-strategy.on{background:#FEF9C3;color:#854D0E}
.src-badge{display:inline-block;padding:1px 7px;border-radius:12px;font-size:10px;font-weight:700}
.src-Meta{background:#E8F0FE;color:#1A56DB}.src-Google{background:#FEF3C7;color:#92400E}
.src-Referral{background:#DCFCE7;color:#15803D}.src-Organic{background:#F0F9FF;color:#0369A1}

/* Action panel */
.act-panel{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:18px;margin-bottom:20px;box-shadow:var(--shadow)}
.act-panel-hdr{font-size:16px;font-weight:700;margin-bottom:14px}
.act-item{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:7px;margin-bottom:8px;border:1px solid var(--border)}
.act-item:last-child{margin-bottom:0}
.act-item.kill-item{background:var(--kill-bg);border-color:#fca5a5}
.act-item.scale-item{background:var(--scale-bg);border-color:#86efac}
.act-item-name{font-weight:600;flex:1}.act-item-reason{font-size:12px;color:var(--muted)}
.overview-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin:0 0 20px}.viz-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px;box-shadow:var(--shadow)}.viz-title{font-weight:800;font-size:14px;margin-bottom:10px}.viz-row{display:grid;grid-template-columns:92px 1fr 92px;gap:8px;align-items:center;margin:9px 0;font-size:12px}.viz-bar{height:10px;border-radius:999px;background:var(--border);overflow:hidden}.viz-fill{height:100%;border-radius:999px;background:var(--gold)}.viz-meta{font-size:11px;color:var(--muted);text-align:right}.playbook{display:grid;gap:10px}.playbook-item{border:1px solid var(--border);border-radius:8px;padding:10px;background:var(--bg)}.playbook-title{font-weight:800;font-size:13px}.playbook-task{font-size:12px;color:var(--muted);margin-top:2px}

/* Pacing bar */
.pbar{height:5px;background:var(--border);border-radius:3px;overflow:hidden;margin-top:3px}
.pbar-fill{height:100%;border-radius:3px}
.pok{background:var(--scale)}.pwarn{background:var(--mon)}.pover{background:var(--kill)}

/* Modal */
.modal-ov{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:999;align-items:center;justify-content:center}
.modal-ov.open{display:flex}
.modal{background:var(--surface);border-radius:12px;padding:24px;width:100%;max-width:540px;max-height:92vh;overflow-y:auto;box-shadow:0 20px 60px rgba(0,0,0,.3)}
.modal-title{font-size:19px;font-weight:700;margin-bottom:18px}
.fg{margin-bottom:14px}.fg label{display:block;font-size:12px;font-weight:600;color:var(--muted);margin-bottom:5px}
.fg input,.fg select,.fg textarea{width:100%;padding:9px 11px;border:1px solid var(--border);border-radius:7px;background:var(--bg);color:var(--text);font-size:14px;font-family:inherit}
.fg textarea{min-height:72px;resize:vertical}
.frow{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.modal-acts{display:flex;justify-content:flex-end;gap:8px;margin-top:18px}

/* Settings */
.scard{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:20px;box-shadow:var(--shadow);margin-bottom:16px}
.scard-title{font-size:15px;font-weight:700;margin-bottom:14px;padding-bottom:8px;border-bottom:1px solid var(--border)}
.srow{display:flex;justify-content:space-between;align-items:center;padding:9px 0;border-bottom:1px solid var(--border);gap:10px}
.srow:last-child{border-bottom:none}
.slabel{font-size:13px;font-weight:500}.ssub{font-size:11px;color:var(--muted);margin-top:1px}
.srow input{padding:5px 9px;border:1px solid var(--border);border-radius:6px;background:var(--bg);color:var(--text);font-size:13px;width:110px;text-align:right}

/* Empty state */
.empty{text-align:center;padding:50px 20px;color:var(--muted)}
.empty-icon{font-size:42px;margin-bottom:10px}

/* Threshold pills in creatives header */
.thr-info{font-size:11px;color:var(--muted);background:var(--bg);border:1px solid var(--border);border-radius:5px;padding:3px 8px}

@media(max-width:640px){.page{padding:12px}.kpi-grid{grid-template-columns:1fr 1fr}.frow{grid-template-columns:1fr}}
</style>
</head>
<body>
<div id="__probe" style="display:none;position:fixed;top:0;left:0;right:0;background:#b91c1c;color:#fff;padding:7px 12px;font:12px monospace;z-index:999999;text-align:center;"></div>

<!-- HEADER -->
<header class="hdr">
  <div class="hdr-logo"><img src="https://drive.google.com/thumbnail?id=1TRY0QBTM_R94M1cOX01NGxF2YUfjcXhL&sz=w240" alt="The REI Method" onerror="this.style.display='none';this.nextElementSibling.style.display='inline'"> <span class="hdr-logo-fallback" style="display:none">THE REI METHOD</span></div>
  <span class="ver-badge">v8.43</span>
  <div class="hdr-sub">Media Buyer Intelligence Dashboard</div>
  <div class="hdr-r">
    <span class="sync-dot" id="syncDot"></span>
    <span class="sync-label" id="syncLabel" style="font-size:12px;color:rgba(255,255,255,.45)">Ready</span>
    <button class="btn btn-ghost" onclick="exportCSV()">↓ CSV</button>
    <button class="btn btn-ghost" id="themeBtn" onclick="toggleTheme()" title="Toggle day/night view">🌙</button>
  </div>
</header>

<!-- GLOBAL FILTER BAR -->
<div class="gbar">
  <div class="gbar-group">
    <span class="gbar-label">Platform</span>
    <button class="pill active" id="pp-all" onclick="setPlatform('all',this)">All</button>
    <button class="pill" id="pp-meta" onclick="setPlatform('Meta',this)">Meta</button>
    <button class="pill" id="pp-google" onclick="setPlatform('Google',this)">Google</button>
    <button class="pill" id="pp-referral" onclick="setPlatform('Referral',this)">Referral</button>
    <button class="pill" id="pp-organic" onclick="setPlatform('Organic',this)">Organic</button>
  </div>
  <div class="gbar-group">
    <span class="gbar-label">Status</span>
    <button class="pill active" id="sp-all" onclick="setStatus('all',this)">All</button>
    <button class="pill" id="sp-active" onclick="setStatus('Active',this)">Active</button>
    <button class="pill" id="sp-paused" onclick="setStatus('Paused',this)">Paused</button>
  </div>
  <div class="gbar-group">
    <span class="gbar-label">Period</span>
    <button class="pill" id="dp-today" onclick="setDate('today',this)">Today</button>
    <button class="pill" id="dp-yesterday" onclick="setDate('yesterday',this)">Yesterday</button>
    <button class="pill" id="dp-7d" onclick="setDate('last_7d',this)">7 Days</button>
    <button class="pill" id="dp-14d" onclick="setDate('last_14d',this)">14 Days</button>
    <button class="pill" id="dp-30d" onclick="setDate('last_30d',this)">30 Days</button>
    <button class="pill active" id="dp-alltime" onclick="setDate('all_time',this)">All Time</button>
    <button class="pill" id="dp-custom" onclick="setDate('custom',this)">Custom</button>
    <span id="custom-range" style="display:none;gap:6px;align-items:center">
      <input type="date" id="customStart" style="padding:3px 8px;border:1px solid var(--border);border-radius:6px;font-size:12px;background:var(--bg);color:var(--text)">
      <span style="color:var(--muted);font-size:12px">to</span>
      <input type="date" id="customEnd" style="padding:3px 8px;border:1px solid var(--border);border-radius:6px;font-size:12px;background:var(--bg);color:var(--text)">
      <button class="btn btn-ghost" style="font-size:12px;padding:4px 10px" onclick="goCustomRange()">Go</button>
    </span>
  </div>
  <div class="gbar-sync">
    <button class="btn btn-ghost" style="font-size:12px;padding:5px 12px" onclick="syncDataFast()">⟳ Sync Now</button>
    <button class="btn btn-ghost" style="font-size:12px;padding:5px 12px;background:#7C3AED;color:#fff;border:none" onclick="syncMetaNow()" title="Force fresh pull from Meta Ads API → Google Sheet">🔄 Sync Meta</button>
  </div>
</div>

<!-- TABS -->
<nav class="tabs">
  <div class="tab active" onclick="showTab('overview',this)">🏆 CEO Overview</div>
  <div class="tab" onclick="showTab('campaigns',this)">🎯 Campaigns</div>
  <div class="tab" onclick="showTab('adsets',this)">📁 Ad Sets</div>
  <div class="tab" onclick="showTab('creatives',this)">🎨 Creatives</div>
  <div class="tab" onclick="showTab('leads',this)">👥 Leads</div>
  <div class="tab" onclick="showTab('log',this)">📋 Kill/Scale Log</div>
  <div class="tab" onclick="showTab('settings',this)">⚙️ Settings</div>
</nav>

<!-- PAGE: CEO SUMMARY — v8.12 redesign: active camps only, period funnel, alert strip -->
<div class="page" id="page-ceo">
  <div class="sec-hdr" style="margin-bottom:12px">
    <div class="sec-title">🏆 CEO Morning Brief</div>
    <div class="sec-acts">
      <span id="ceoSyncTime" style="font-size:12px;color:var(--muted)">—</span>
    </div>
  </div>
  <!-- Top KPI cards -->
  <div class="kpi-grid" id="ceoKpis" style="grid-template-columns:repeat(8,1fr);gap:10px"></div>
  <!-- Alert strip: kill/scale counts, new leads today, active camps -->
  <div id="ceoAlerts" style="display:flex;gap:8px;flex-wrap:wrap;margin:12px 0;padding:10px 16px;background:var(--card);border-radius:8px;border:1px solid var(--border);font-size:13px;align-items:center"></div>
  <!-- Active campaigns decision table -->
  <div class="sec-hdr" style="margin-bottom:8px;margin-top:4px">
    <div class="sec-title" style="font-size:15px">📊 Active Campaigns</div>
  </div>
  <div class="tbl-wrap">
    <table>
      <thead><tr>
        <th>Campaign</th><th>Platform</th><th>Spend</th><th>Leads</th>
        <th>CPL</th><th>Hook %</th><th>Signal</th>
      </tr></thead>
      <tbody id="ceoCampBody"></tbody>
    </table>
  </div>
  <!-- Lead funnel visual -->
  <div class="sec-hdr" style="margin-bottom:8px;margin-top:16px">
    <div class="sec-title" style="font-size:15px">🔽 Lead Funnel (Period)</div>
  </div>
  <div id="ceoFunnel" style="display:flex;align-items:center;flex-wrap:wrap;gap:0;margin-bottom:16px"></div>
  <!-- Campaign breakdown funnel table -->
  <div class="tbl-wrap">
    <table>
      <thead><tr>
        <th>Campaign</th><th>New</th><th>Responded</th><th>Booked Call</th><th>Appointment</th>
        <th>Strategy Session</th><th>Closed</th><th>Revenue</th><th>ROAS</th>
      </tr></thead>
      <tbody id="ceoFunnelBody"></tbody>
    </table>
  </div>
  <!-- Scale / Kill lists -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px">
    <div>
      <div class="sec-hdr" style="margin-bottom:8px"><div class="sec-title" style="font-size:15px">🔥 Scale These</div></div>
      <div id="ceoScaleList"><div class="empty"><p>No scale candidates.</p></div></div>
    </div>
    <div>
      <div class="sec-hdr" style="margin-bottom:8px"><div class="sec-title" style="font-size:15px">🛑 Kill These</div></div>
      <div id="ceoKillList"><div class="empty"><p>No kill candidates.</p></div></div>
    </div>
  </div>
</div>

<!-- PAGE: OVERVIEW -->
<div class="page active" id="page-overview">
  <div class="sec-hdr" style="margin-bottom:12px">
    <div class="sec-title">🏆 CEO Overview</div>
    <div class="sec-acts"><span id="overviewSyncTime" style="font-size:12px;color:var(--muted)">—</span></div>
  </div>
  <div id="overviewAlerts" style="display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px;padding:10px 16px;background:var(--surface);border-radius:8px;border:1px solid var(--border);font-size:13px;align-items:center"></div>
  <div class="act-panel"><div class="act-panel-hdr">⚡ Action Required</div><div id="actionList"><div class="empty"><p>No actions — all clear.</p></div></div></div>
  <div class="kpi-grid" id="kpiGrid"></div>
  <div class="overview-grid" id="overviewViz"></div>
  <div class="sec-hdr"><div class="sec-title">🏆 Top Performers</div></div>
  <div id="topPerformers"></div>
</div>

<!-- PAGE: CAMPAIGNS -->
<div class="page" id="page-campaigns">
  <div class="sec-hdr">
    <div class="sec-title">🎯 Campaigns</div>
    <div class="sec-acts">
      <div class="search-wrap"><input id="campSearch" placeholder="Search…" oninput="renderCampaigns()"></div>
      <button class="btn btn-primary" onclick="openCampaignModal()">+ Add Campaign</button>
    </div>
  </div>
  <div class="tbl-wrap">
    <table>
      <thead><tr>
        <th class="sortable" onclick="sortByCol('campaigns','name')">Campaign <span class="sort-arrow" id="sa-c-name">⇅</span></th>
        <th class="sortable" onclick="sortByCol('campaigns','platform')">Platform <span class="sort-arrow" id="sa-c-plat">⇅</span></th>
        <th class="sortable" onclick="sortByCol('campaigns','objective')">Objective <span class="sort-arrow" id="sa-c-obj">⇅</span></th>
        <th class="sortable" onclick="sortByCol('campaigns','_budget')">Budget <span class="sort-arrow" id="sa-c-bud">⇅</span></th>
        <th class="sortable" onclick="sortByCol('campaigns','_spend')">Spend <span class="sort-arrow" id="sa-c-spd">⇅</span></th>
        <th class="sortable" onclick="sortByCol('campaigns','_leads')">Leads <span class="sort-arrow" id="sa-c-lds">⇅</span></th>
        <th class="sortable" onclick="sortByCol('campaigns','_cpl')">CPL <span class="sort-arrow" id="sa-c-cpl">⇅</span></th>
        <th class="sortable" onclick="sortByCol('campaigns','_responded')">Responded <span class="sort-arrow" id="sa-c-resp">⇅</span></th>
        <th class="sortable" onclick="sortByCol('campaigns','_appts')">Appts <span class="sort-arrow" id="sa-c-ap">⇅</span></th>
        <th class="sortable" onclick="sortByCol('campaigns','_ss')">SS <span class="sort-arrow" id="sa-c-ss">⇅</span></th>
        <th class="sortable" onclick="sortByCol('campaigns','_roasNum')">ROAS <span class="sort-arrow" id="sa-c-roas">⇅</span></th>
        <th class="sortable" onclick="sortByCol('campaigns','status')">Status <span class="sort-arrow" id="sa-c-sta">⇅</span></th>
        <th>Actions</th>
      </tr></thead>
      <tbody id="campaignsBody"></tbody>
    </table>
  </div>
</div>

<!-- PAGE: AD SETS -->
<div class="page" id="page-adsets">
  <div class="sec-hdr">
    <div class="sec-title">📁 Ad Sets</div>
    <div class="sec-acts">
      <div class="search-wrap"><input id="adsetSearch" placeholder="Search…" oninput="renderAdSets()"></div>
      <button class="btn btn-primary" onclick="openAdSetModal()">+ Add Ad Set</button>
    </div>
  </div>
  <div class="tbl-wrap">
    <table>
      <thead><tr>
        <th class="sortable" onclick="sortByCol('adsets','name')">Ad Set <span class="sort-arrow" id="sa-a-name">⇅</span></th>
        <th class="sortable" onclick="sortByCol('adsets','_campName')">Campaign <span class="sort-arrow" id="sa-a-camp">⇅</span></th>
        <th class="sortable" onclick="sortByCol('adsets','platform')">Platform <span class="sort-arrow" id="sa-a-plat">⇅</span></th>
        <th class="sortable" onclick="sortByCol('adsets','audience')">Audience <span class="sort-arrow" id="sa-a-aud">⇅</span></th>
        <th class="sortable" onclick="sortByCol('adsets','_budget')">Budget <span class="sort-arrow" id="sa-a-bud">⇅</span></th>
        <th class="sortable" onclick="sortByCol('adsets','_spend')">Spend <span class="sort-arrow" id="sa-a-spd">⇅</span></th>
        <th class="sortable" onclick="sortByCol('adsets','_leads')">Leads <span class="sort-arrow" id="sa-a-lds">⇅</span></th>
        <th class="sortable" onclick="sortByCol('adsets','_cpl')">CPL <span class="sort-arrow" id="sa-a-cpl">⇅</span></th>
        <th class="sortable" onclick="sortByCol('adsets','_adsCount')">Ads <span class="sort-arrow" id="sa-a-ads">⇅</span></th>
        <th>Actions</th>
      </tr></thead>
      <tbody id="adsetsBody"></tbody>
    </table>
  </div>
</div>

<!-- PAGE: CREATIVES -->
<div class="page" id="page-creatives">
  <div class="sec-hdr">
    <div class="sec-title">🎨 Creatives</div>
    <div class="sec-acts">
      <div class="search-wrap"><input id="crSearch" placeholder="Search…" oninput="renderCreatives()"></div>
      <span class="thr-info" id="thrInfo">Hook Kill: 25% | Scale: 35%</span>
      <button class="btn btn-primary" onclick="openCreativeModal()">+ Add Creative</button>
    </div>
  </div>
  <div class="cr-wrap">
    <table class="cr-table">
      <thead><tr>
        <th class="sticky-l0 thumb-cell">Preview</th>
        <th class="sticky-l1 sortable" onclick="sortByCol('creatives','name')">Ad Name <span class="sort-arrow" id="sa-cr-name">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_asName')">Ad Set <span class="sort-arrow" id="sa-cr-as">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_campName')">Campaign <span class="sort-arrow" id="sa-cr-camp">⇅</span></th>
        <th>Platform</th>
        <th class="sortable" onclick="sortByCol('creatives','format')">Format <span class="sort-arrow" id="sa-cr-fmt">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_hookrate')">Hook% <span class="sort-arrow" id="sa-cr-hook">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_ctr')">CTR% <span class="sort-arrow" id="sa-cr-ctr">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_cpc')">CPC <span class="sort-arrow" id="sa-cr-cpc">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_leads')">Leads/Conv. <span class="sort-arrow" id="sa-cr-lds">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_potential')" title="Leads marked Potential or above">Potential <span class="sort-arrow" id="sa-cr-pot">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_apptSet')" title="Leads with Appt Set or above">Appt Set <span class="sort-arrow" id="sa-cr-ap">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_apptVerified')" title="Appts confirmed / verified">Verified <span class="sort-arrow" id="sa-cr-av">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_spend')">Spend <span class="sort-arrow" id="sa-cr-spd">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_cpl')">CPL <span class="sort-arrow" id="sa-cr-cpl">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_costPotential')" title="Spend ÷ Potential leads">$/Potential <span class="sort-arrow" id="sa-cr-cp">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_costAppt')" title="Spend ÷ Appts Set">$/Appt <span class="sort-arrow" id="sa-cr-ca">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_costVerified')" title="Spend ÷ Verified Appts">$/Verified <span class="sort-arrow" id="sa-cr-cv">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_lqPct')" title="Lead → Potential conversion">L→P% <span class="sort-arrow" id="sa-cr-lq">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_paPct')" title="Potential → Appt conversion">P→A% <span class="sort-arrow" id="sa-cr-qa">⇅</span></th>
        <th class="sortable" onclick="sortByCol('creatives','_signal')">Signal <span class="sort-arrow" id="sa-cr-sig">⇅</span></th>
        <th>Status</th>
        <th class="sticky-r0">Actions</th>
      </tr></thead>
      <tbody id="creativesBody"></tbody>
    </table>
  </div>
</div>

<!-- PAGE: LEADS -->
<div class="page" id="page-leads">
  <div class="lead-sticky-panel">
  <div class="sec-hdr lead-hdr">
    <div class="lead-title-row">
      <div class="sec-title">👥 Leads</div>
      <div class="lead-filter-group">
        <span class="lead-filter-label">Quality</span>
        <button class="pill active" id="ql-all" onclick="setQualityFilter('all',this)">All</button>
        <button class="pill" id="ql-a" onclick="setQualityFilter('a',this)"><span style="color:#16A34A">●</span> A</button>
        <button class="pill" id="ql-b" onclick="setQualityFilter('b',this)"><span style="color:#D97706">●</span> B</button>
        <button class="pill" id="ql-c" onclick="setQualityFilter('c',this)"><span style="color:#DC2626">●</span> C</button>
        <button class="pill" id="ql-untagged" onclick="setQualityFilter('untagged',this)">○ Unset</button>
      </div>
      <div class="lead-filter-group">
        <span class="lead-filter-label">Urgency</span>
        <button class="pill active" id="ug-all" onclick="setUrgencyFilter('all',this)">All</button>
        <button class="pill" id="ug-no" onclick="setUrgencyFilter('No Timeline',this)">No Timeline</button>
        <button class="pill" id="ug-year" onclick="setUrgencyFilter('Exploring This Year',this)">This Year</button>
        <button class="pill" id="ug-30" onclick="setUrgencyFilter('Decision In 30 Days',this)">30 Days</button>
        <button class="pill" id="ug-short" onclick="setUrgencyFilter('Shortlisting Now',this)">Shortlisting</button>
      </div>
    </div>
    <div class="sec-acts">
      <div class="search-wrap"><input id="leadSearch" placeholder="Search…" oninput="renderLeads()"></div>
      <button class="btn" style="background:#6366F1;color:#fff;font-size:13px;padding:7px 14px;border-radius:7px" onclick="syncIntelia()">⟳ Sync Intelia</button>
      <button class="btn btn-primary" onclick="openLeadModal()">+ Add Lead</button>
    </div>
  </div>
  <div class="kpi-grid" id="leadKpis"></div>
  </div>
  <div class="tbl-wrap lead-table-wrap">
    <table>
      <!-- v8.21: quality and closed revenue are editable directly in the table -->
      <thead><tr>
        <th class="sortable" onclick="sortByCol('leads','name')">Name <span class="sort-arrow" id="sa-l-name">⇅</span></th>
        <th class="sortable" onclick="sortByCol('leads','phone')">Mobile <span class="sort-arrow" id="sa-l-ph">⇅</span></th>
        <th class="sortable" onclick="sortByCol('leads','email')">Email <span class="sort-arrow" id="sa-l-em">⇅</span></th>
        <th class="sortable" onclick="sortByCol('leads','platform')">Source <span class="sort-arrow" id="sa-l-src">⇅</span></th>
        <th class="sortable" onclick="sortByCol('leads','campaignName')">Campaign <span class="sort-arrow" id="sa-l-camp">⇅</span></th>
        <th class="sortable" onclick="sortByCol('leads','sourceAdName')">Source Ad Name <span class="sort-arrow" id="sa-l-san">⇅</span></th>
        <th><span onclick="sortByCol('leads','status')" style="cursor:pointer">Stage <span class="sort-arrow" id="sa-l-sta">⇅</span></span>&nbsp;<span onclick="sortByCol('leads','urgencyTimeline')" style="cursor:pointer;font-size:9px;opacity:.65">/ Urgency <span class="sort-arrow" id="sa-l-urg">⇅</span></span></th>
        <th class="sortable" onclick="sortByCol('leads','quality')">Quality <span class="sort-arrow" id="sa-l-qual">⇅</span></th>
        <th>Closed / Revenue</th>
        <th class="sortable" onclick="sortByCol('leads','date')">Received <span class="sort-arrow" id="sa-l-date">⇅</span></th>
        <th>Actions</th>
      </tr></thead>
      <tbody id="leadsBody"></tbody>
    </table>
  </div>
</div>

<!-- PAGE: KILL/SCALE LOG -->
<div class="page" id="page-log">
  <div class="sec-hdr">
    <div class="sec-title">📋 Kill / Scale Log</div>
    <div class="sec-acts"><button class="btn btn-primary" onclick="openLogModal()">+ Add Entry</button></div>
  </div>
  <div class="tbl-wrap">
    <table>
      <thead><tr>
        <th>Date</th><th>Ad Name</th><th>Campaign</th><th>Action</th><th>Spend</th><th>Leads</th><th>CPL</th><th>Hook%</th><th>Reason</th><th>Actions</th>
      </tr></thead>
      <tbody id="logBody"></tbody>
    </table>
  </div>
</div>

<!-- PAGE: SETTINGS -->
<div class="page" id="page-settings">
  <div class="sec-title" style="margin-bottom:16px">⚙️ Settings</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;max-width:900px">
    <div class="scard">
      <div class="scard-title">🔗 Data Connections</div>
      <div class="srow"><div><div class="slabel">Google Sheet ID</div><div class="ssub">Master data sheet</div></div><input id="s_sheetId" placeholder="Paste sheet ID" onchange="saveSetting('sheetId',this.value)"></div>
      <div class="srow"><div><div class="slabel">Intelia (GHL) Sub-Location ID</div><div class="ssub">GHL Settings → General → Location ID · Sub-account API key: Settings → Integrations → API Keys → Private Integrations</div></div><input id="s_ghlLoc" placeholder="e.g. abc123" onchange="saveSetting('ghlLocationId',this.value)"></div>
      <div class="srow"><div><div class="slabel">SGD Rate (vs USD)</div><div class="ssub">Only applies if Meta account is in USD (v8 auto-detects SGD accounts)</div></div><input id="s_sgd" type="number" step="0.01" onchange="saveSetting('sgdRate',parseFloat(this.value))"></div>
    </div>
    <div class="scard">
      <div class="scard-title">📏 Kill / Scale Thresholds</div>
      <div class="srow"><div><div class="slabel">Kill Hook Rate (%)</div><div class="ssub">Below = kill candidate</div></div><input id="s_killHook" type="number" onchange="saveSettingAndRender('killHook',this.value)"></div>
      <div class="srow"><div><div class="slabel">Scale Hook Rate (%)</div><div class="ssub">Above = scale candidate</div></div><input id="s_scaleHook" type="number" onchange="saveSettingAndRender('scaleHook',this.value)"></div>
      <div class="srow"><div><div class="slabel">Kill CPL (SGD)</div><div class="ssub">Above = kill candidate</div></div><input id="s_killCPL" type="number" onchange="saveSettingAndRender('killCPL',this.value)"></div>
      <div class="srow"><div><div class="slabel">Scale CPL (SGD)</div><div class="ssub">Below = scale candidate</div></div><input id="s_scaleCPL" type="number" onchange="saveSettingAndRender('scaleCPL',this.value)"></div>
      <div class="srow"><div><div class="slabel">Min Spend for Signal (SGD)</div><div class="ssub">Spend before kill fires</div></div><input id="s_killSpend" type="number" onchange="saveSettingAndRender('killSpend',this.value)"></div>
      <div class="srow"><div><div class="slabel">Min Leads for Signal</div><div class="ssub">Leads before scale fires</div></div><input id="s_minLeads" type="number" onchange="saveSettingAndRender('minLeads',this.value)"></div>
    </div>
  </div>
  <div style="max-width:900px;margin-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:16px">
    <div class="scard">
      <div class="scard-title">📊 Google Ads Setup</div>
      <div style="font-size:12px;color:var(--muted);line-height:1.6">
        <strong>Status:</strong> Google Ads data flows from the Google Ads Script → Master Sheet tabs → Apps Script sync.<br><br>
        <strong>To enable Google Ads data:</strong><br>
        1. In Google Ads → Tools &amp; Settings → Scripts → + New Script<br>
        2. Paste <strong>REI_GoogleAds_Script_v6.gs</strong> (in this Dashboard Tracking folder)<br>
        3. Confirm <code>MASTER_SHEET_ID</code> is set to your sheet ID<br>
        4. Click Run once, then Schedule → Daily<br>
        5. Next time you click Sync Meta + Google, Google Ads data appears automatically<br><br>
        <span style="color:var(--warn,#f59e0b)">⚠ The Google_Campaigns, Google_AdGroups, Google_Ads tabs must exist in the Master Sheet (created automatically when the script runs).</span>
      </div>
    </div>
    <div class="scard">
      <div class="scard-title">💡 Intelia / GHL Sync</div>
      <div style="font-size:12px;color:var(--muted);line-height:1.6">
        <strong>No API key access?</strong> (Sub-account users)<br>
        Apps Script v8 falls back to the <strong>GHL_Leads</strong> sheet tab automatically.<br><br>
        <strong>Populate GHL_Leads tab — choose one:</strong><br>
        A. Ask Claude to pull contacts via MCP → import the JSON file<br>
        B. GHL → Contacts → Export CSV → paste into GHL_Leads tab in Master Sheet<br>
        C. Get a Private Integration key: GHL Settings → Integrations → API Keys → Private Integrations → Create<br><br>
        v8.22 auto-refreshes GHL while the dashboard is open. For server-side auto-refresh, run <strong>REI Menu → Start Auto-Sync</strong> once in Apps Script.
      </div>
    </div>
    <div class="scard">
      <div class="scard-title">🧭 Urgency Timeline Playbook</div>
      <div class="playbook">
        <div class="playbook-item"><div class="playbook-title">No Timeline</div><div class="playbook-task">Send YouTube nurture.</div></div>
        <div class="playbook-item"><div class="playbook-title">Exploring This Year</div><div class="playbook-task">Invite to webinar or long-form video.</div></div>
        <div class="playbook-item"><div class="playbook-title">Shortlisting Now</div><div class="playbook-task">Offer project rejection framework.</div></div>
        <div class="playbook-item"><div class="playbook-title">Decision In 30 Days</div><div class="playbook-task">Push strategy session immediately.</div></div>
      </div>
    </div>
  </div>
  <div style="max-width:900px;margin-top:14px">
    <div class="scard">
      <div class="scard-title">🗂 Data Management</div>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <button class="btn btn-ghost" onclick="exportJSON()">Export JSON Backup</button>
        <button class="btn btn-ghost" onclick="document.getElementById('importFile').click()">Import Full Backup</button>
        <button class="btn btn-primary" onclick="document.getElementById('importLeadsFile').click()" title="Import the REI_GHL_Leads_Import.json file from Claude">Import GHL Leads File</button>
        <button class="btn btn-danger" onclick="confirmClearAll()">Clear All Data</button>
      </div>
      <div style="font-size:11px;color:var(--muted);margin-top:6px">Import GHL Leads File: load the <em>REI_GHL_Leads_Import.json</em> file generated by Claude — merges leads without overwriting other data.</div>
      <input type="file" id="importFile" accept=".json" style="display:none" onchange="importJSON(event)">
      <input type="file" id="importLeadsFile" accept=".json" style="display:none" onchange="importLeadsJSON(event)">
    </div>
  </div>
</div>

<!-- MODALS -->
<!-- Campaign Modal -->
<div class="modal-ov" id="campModal">
  <div class="modal">
    <div class="modal-title" id="campModalTitle">Add Campaign</div>
    <div class="frow">
      <div class="fg"><label>Campaign Name *</label><input id="cm_name" placeholder="e.g. LL_Lead_Gen_Q1"></div>
      <div class="fg"><label>Platform</label><select id="cm_platform"><option>Meta</option><option>Google</option></select></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Objective</label><input id="cm_obj" placeholder="Lead Generation"></div>
      <div class="fg"><label>Status</label><select id="cm_status"><option>Active</option><option>Paused</option></select></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Daily Budget (SGD)</label><input type="number" id="cm_budget" placeholder="0"></div>
      <div class="fg"><label>Meta Campaign ID</label><input id="cm_metaId" placeholder="act_…"></div>
    </div>
    <div class="modal-acts">
      <button class="btn btn-ghost" onclick="closeModal('campModal')">Cancel</button>
      <button class="btn btn-primary" onclick="saveCampaign()">Save</button>
    </div>
  </div>
</div>

<!-- Ad Set Modal -->
<div class="modal-ov" id="adsetModal">
  <div class="modal">
    <div class="modal-title" id="adsetModalTitle">Add Ad Set</div>
    <div class="frow">
      <div class="fg"><label>Ad Set Name *</label><input id="as_name" placeholder="e.g. LL_Lookalike_1%"></div>
      <div class="fg"><label>Campaign *</label><select id="as_campaign"></select></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Status</label><select id="as_status"><option>Active</option><option>Paused</option></select></div>
      <div class="fg"><label>Audience</label><input id="as_audience" placeholder="e.g. Lookalike 1%"></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Daily Budget (SGD)</label><input type="number" id="as_budget" placeholder="0"></div>
      <div class="fg"><label>Meta Ad Set ID</label><input id="as_metaId"></div>
    </div>
    <div class="modal-acts">
      <button class="btn btn-ghost" onclick="closeModal('adsetModal')">Cancel</button>
      <button class="btn btn-primary" onclick="saveAdSet()">Save</button>
    </div>
  </div>
</div>

<!-- Creative Modal -->
<div class="modal-ov" id="crModal">
  <div class="modal">
    <div class="modal-title" id="crModalTitle">Add Creative</div>
    <div class="frow">
      <div class="fg"><label>Ad Name * (suffix -V/-I/-C for format)</label><input id="cr_name" placeholder="A01-S03-H07-V"></div>
      <div class="fg"><label>Ad Set *</label><select id="cr_adset"></select></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Format (auto-detected from name)</label><select id="cr_format"><option>Video</option><option>Image</option><option>Carousel</option><option>Story</option></select></div>
      <div class="fg"><label>Status</label><select id="cr_status"><option>Active</option><option>Paused</option></select></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Hook Rate (%)</label><input type="number" id="cr_hookrate" placeholder="0"></div>
      <div class="fg"><label>CTR (%)</label><input type="number" id="cr_ctr" placeholder="0"></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Spend (SGD)</label><input type="number" id="cr_spend" placeholder="0"></div>
      <div class="fg"><label>Leads</label><input type="number" id="cr_leads" placeholder="0"></div>
    </div>
    <div class="frow">
      <div class="fg"><label>CPC (SGD)</label><input type="number" id="cr_cpc" placeholder="0"></div>
      <div class="fg"><label>Thumbnail URL</label><input id="cr_thumb" placeholder="https://…"></div>
    </div>
    <div class="fg"><label>Hook / Copy Angle</label><input id="cr_hook" placeholder="e.g. Fear, Curiosity, Social Proof"></div>
    <div class="fg"><label>Notes</label><textarea id="cr_notes"></textarea></div>
    <div class="modal-acts">
      <button class="btn btn-ghost" onclick="closeModal('crModal')">Cancel</button>
      <button class="btn btn-primary" onclick="saveCreative()">Save</button>
    </div>
  </div>
</div>

<!-- Lead Modal -->
<div class="modal-ov" id="leadModal">
  <div class="modal">
    <div class="modal-title" id="leadModalTitle">Add Lead</div>
    <div class="frow">
      <div class="fg"><label>Name *</label><input id="ld_name" placeholder="Full name"></div>
      <div class="fg"><label>Phone / Email</label><input id="ld_contact" placeholder="+65…"></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Source</label><select id="ld_source"><option>Meta</option><option>Google</option><option>Referral</option><option>Organic</option></select></div>
      <div class="fg"><label>Source Ad</label><select id="ld_sourceAd"><option value="">— Not linked —</option></select></div>
      <div class="fg"><label>Status</label><select id="ld_status"><option>New</option><option>Contacted</option><option>Responded</option><option>Booked Call</option><option>Appointment</option><option>Appt Qualified</option><option>Strategy Session</option><option>Closed</option><option>Lost</option></select></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Property Type</label><input id="ld_proptype" placeholder="HDB, Condo, EC…"></div>
      <div class="fg"><label>Budget Range</label><input id="ld_budget" placeholder="SGD 500K–700K"></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Date Received</label><input type="date" id="ld_date"></div>
      <div class="fg"><label>Appointment Date</label><input type="date" id="ld_appt"></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Quality</label><select id="ld_quality"><option value="">— Unset —</option><option value="A">● A (Green — High quality)</option><option value="B">● B (Amber — Medium quality)</option><option value="C">● C (Red — Low quality)</option></select></div>
      <div class="fg"><label>Urgency Timeline</label><select id="ld_urgencyTimeline"><option>No Timeline</option><option>Exploring This Year</option><option>Decision In 30 Days</option><option>Shortlisting Now</option></select></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Deal Value (SGD)</label><input type="number" id="ld_dealValue" placeholder="e.g. 25000" step="1000"></div>
    </div>
    <div class="fg"><label>Notes</label><textarea id="ld_notes"></textarea></div>
    <div class="modal-acts">
      <button class="btn btn-ghost" onclick="closeModal('leadModal')">Cancel</button>
      <button class="btn btn-primary" onclick="saveLead()">Save</button>
    </div>
  </div>
</div>

<!-- Log Modal -->
<div class="modal-ov" id="logModal">
  <div class="modal">
    <div class="modal-title">Add Kill/Scale Log Entry</div>
    <div class="frow">
      <div class="fg"><label>Ad</label><select id="log_ad"></select></div>
      <div class="fg"><label>Action</label><select id="log_action"><option>Kill</option><option>Pause</option><option>Scale</option><option>Monitor</option></select></div>
    </div>
    <div class="frow">
      <div class="fg"><label>Date</label><input type="date" id="log_date"></div>
      <div class="fg"><label>Spend at Decision (SGD)</label><input type="number" id="log_spend"></div>
    </div>
    <div class="fg"><label>Reason / Notes</label><textarea id="log_reason" placeholder="Hook rate too low, CPL above threshold…"></textarea></div>
    <div class="modal-acts">
      <button class="btn btn-ghost" onclick="closeModal('logModal')">Cancel</button>
      <button class="btn btn-primary" onclick="saveLogEntry()">Save</button>
    </div>
  </div>
</div>

<!-- Delete Confirm -->
<div class="modal-ov" id="delModal">
  <div class="modal" style="max-width:360px;text-align:center">
    <div style="font-size:38px;margin-bottom:10px">🗑</div>
    <div class="modal-title" style="justify-content:center">Delete?</div>
    <p style="color:var(--muted);margin-bottom:18px" id="delText">This cannot be undone.</p>
    <div class="modal-acts" style="justify-content:center">
      <button class="btn btn-ghost" onclick="closeModal('delModal')">Cancel</button>
      <button class="btn btn-danger" id="delConfirmBtn">Delete</button>
    </div>
  </div>
</div>

<!-- LIGHTBOX -->
<div class="lbox" id="lightbox" onclick="closeLightbox()">
  <div class="lbox-content" onclick="event.stopPropagation()">
    <span class="lbox-close" onclick="closeLightbox()">×</span>
    <img id="lboxImg" src="" style="display:none">
    <video id="lboxVid" controls style="display:none"></video>
    <div class="lbox-name" id="lboxName"></div>
  </div>
</div>

<script>window.__GAS_URL__='${webAppUrl}';</script>
<script src="${webAppUrl}?action=getscript&v=8.30"></script>
</body>
</html>
`;
}

/* ==============================================
   DASHBOARD JAVASCRIPT — served via action=getscript
   Separating JS from HTML bypasses inline CSP headers
   set by GAS HtmlService.
============================================== */
function getDashboardJs() {
  return `
/* v8.30: keep diagnostics invisible unless a real JavaScript error occurs. */
(function(){
  var p=document.getElementById('__probe');
  if(p){ p.style.display='none'; p.textContent=''; }
})();

/* ══ error capture ══ */
window.__log = function(msg,err){
  if(!err) return;
  var p=document.getElementById('__probe');
  if(!p) return;
  p.style.display='block';
  p.style.background='#b91c1c';
  p.textContent='Dashboard error: '+msg;
};
window.onerror = function(msg,src,line,col,e){
  window.__log('JS-ERROR: '+msg+' ['+line+']',true); return false;
};
window.addEventListener('unhandledrejection',function(e){
  window.__log('REJECT: '+(e.reason&&e.reason.message?e.reason.message:String(e.reason)),true);
});

/* normaliseStatus — defined here for browser context (also exists GAS-side) */
function normaliseStatus(s) {
  if (!s) return 'Active';
  const up = s.toUpperCase();
  if (up === 'ACTIVE' || up === 'ENABLED') return 'Active';
  if (up === 'PAUSED') return 'Paused';
  return 'Paused';
}

/* ═══════════════════════════════════════════
   DATA STORE
═══════════════════════════════════════════ */
const STORE_KEY = 'rei_dash_v6'; // keep v6 key for data compat

const DEFAULT_DB = {
  campaigns:[], adsets:[], creatives:[], leads:[], killScaleLog:[],
  settings:{
    sheetId:'1Wp3zxkQkB7WzlqOaAQENzwJIKjEqzJ42628Q6JCoU0Y',
    webAppUrl:(window.__GAS_URL__||''), sgdRate:1.35,
    killHook:25, scaleHook:35, killCPL:200, scaleCPL:80, killSpend:150, minLeads:3,
    themeMode:'auto', nightStart:19, nightEnd:7, autoSyncMinutes:3
  }
};

let db = JSON.parse(JSON.stringify(DEFAULT_DB));
let editId = {campaign:null,adset:null,creative:null,lead:null,log:null};
let currentPlatform = 'all', currentStatus = 'all', currentDatePreset = 'all_time';

function loadDB(){
  try{
    const s=localStorage.getItem(STORE_KEY);
    if(s){ const p=JSON.parse(s); db=Object.assign({},DEFAULT_DB,p); db.settings=Object.assign({},DEFAULT_DB.settings,p.settings||{}); db.killScaleLog=p.killScaleLog||[]; }
    if(window.__GAS_URL__) db.settings.webAppUrl=window.__GAS_URL__; // v8.43: always use current deployment URL
    // v8.10: one-time purge of any duplicate leads that built up in localStorage
    if(db.leads.length>1){
      function _lkeyLoad(l){
        if(l.ghlId) return 'g:'+l.ghlId;
        const ph=(l.phone||'').replace(/\D/g,'');
        if(ph.length>=8) return 'p:'+ph.slice(-8);
        const em=(l.email||'').toLowerCase().trim();
        if(em) return 'e:'+em;
        return 'n:'+(l.name||'').toLowerCase().trim();
      }
      const seen=new Set();
      db.leads=db.leads.filter(l=>{const k=_lkeyLoad(l);if(seen.has(k))return false;seen.add(k);return true;});
    }
  }catch(e){console.warn(e)}
}
function saveDB(){ try{localStorage.setItem(STORE_KEY,JSON.stringify(db));}catch(e){} }
function saveSetting(k,v){ db.settings[k]=v; saveDB(); }
function saveSettingAndRender(k,v){ db.settings[k]=parseFloat(v)||0; saveDB(); renderCreatives(); renderOverview(); updateThrInfo(); }

/* ═══════════════════════════════════════════
   SORT ENGINE
═══════════════════════════════════════════ */
const sortState = {};
const SORT_META = {
  campaigns:{ spans:['sa-c-name','sa-c-plat','sa-c-obj','sa-c-bud','sa-c-spd','sa-c-lds','sa-c-cpl','sa-c-resp','sa-c-ap','sa-c-ss','sa-c-roas','sa-c-sta'], keys:['name','platform','objective','_budget','_spend','_leads','_cpl','_responded','_appts','_ss','_roasNum','status'] },
  adsets:   { spans:['sa-a-name','sa-a-camp','sa-a-plat','sa-a-aud','sa-a-bud','sa-a-spd','sa-a-lds','sa-a-cpl','sa-a-ads'], keys:['name','_campName','platform','audience','_budget','_spend','_leads','_cpl','_adsCount'] },
  creatives:{ spans:['sa-cr-name','sa-cr-as','sa-cr-camp','sa-cr-fmt','sa-cr-hook','sa-cr-ctr','sa-cr-cpc','sa-cr-lds','sa-cr-pot','sa-cr-ap','sa-cr-av','sa-cr-spd','sa-cr-cpl','sa-cr-cp','sa-cr-ca','sa-cr-cv','sa-cr-lq','sa-cr-qa','sa-cr-sig'],
              keys:['name','_asName','_campName','format','_hookrate','_ctr','_cpc','_leads','_potential','_apptSet','_apptVerified','_spend','_cpl','_costPotential','_costAppt','_costVerified','_lqPct','_paPct','_signal'] },
  leads:    { spans:['sa-l-name','sa-l-ph','sa-l-em','sa-l-src','sa-l-camp','sa-l-san','sa-l-sta','sa-l-urg','sa-l-qual','sa-l-date'], keys:['name','phone','email','platform','campaignName','sourceAdName','status','urgencyTimeline','quality','date'] }
};
const NUM_KEYS = new Set(['_budget','_spend','_leads','_cpl','_adsCount','_hookrate','_ctr','_cpc','_bookings','_qualLeads','_appts','_potential','_apptSet','_apptVerified','_costQual','_costAppt','_costPotential','_costVerified','_lqPct','_qaPct','_paPct','_signal','_responded','_ss','_roasNum']);
const DATE_KEYS = new Set(['date','appt']);
const URGENCY_OPTIONS = ['No Timeline','Exploring This Year','Decision In 30 Days','Shortlisting Now'];
function normaliseUrgency(v){ const s=String(v||'').trim(); return URGENCY_OPTIONS.includes(s)?s:'No Timeline'; }
function urgencyRank(v){ const i=URGENCY_OPTIONS.indexOf(normaliseUrgency(v)); return i<0?0:i; }

function sortByCol(tbl,key){
  if(!sortState[tbl]||sortState[tbl].key!==key) sortState[tbl]={key,dir:'desc'};
  else sortState[tbl].dir=sortState[tbl].dir==='desc'?'asc':'desc';
  if(tbl==='campaigns') renderCampaigns();
  else if(tbl==='adsets') renderAdSets();
  else if(tbl==='creatives') renderCreatives();
  else if(tbl==='leads') renderLeads();
}
function applySort(rows,tbl){
  const st=sortState[tbl]; if(!st) return rows;
  return [...rows].sort((a,b)=>{
    let va=a[st.key],vb=b[st.key];
    if(st.key==='status'&&tbl==='leads'){va=funnelRank(va);vb=funnelRank(vb);}
    else if(st.key==='urgencyTimeline'){va=urgencyRank(va);vb=urgencyRank(vb);}
    else if(st.key==='quality'){const qv={A:3,B:2,C:1};va=qv[String(va||'').toUpperCase()]||0;vb=qv[String(vb||'').toUpperCase()]||0;}
    else if(NUM_KEYS.has(st.key)){va=parseFloat(va)||0;vb=parseFloat(vb)||0;}
    else if(DATE_KEYS.has(st.key)){va=va?new Date(va).getTime():0;vb=vb?new Date(vb).getTime():0;}
    else{va=String(va??'').toLowerCase();vb=String(vb??'').toLowerCase();}
    return va<vb?(st.dir==='asc'?-1:1):va>vb?(st.dir==='asc'?1:-1):0;
  });
}
function updateIcons(tbl){
  const m=SORT_META[tbl]; if(!m) return;
  const st=sortState[tbl];
  m.spans.forEach((id,i)=>{
    const el=document.getElementById(id); if(!el) return;
    if(st&&st.key===m.keys[i]){el.textContent=st.dir==='asc'?'▲':'▼';el.classList.add('active');}
    else{el.textContent='⇅';el.classList.remove('active');}
  });
}

/* ═══════════════════════════════════════════
   GLOBAL FILTERS
═══════════════════════════════════════════ */
function setPlatform(p,btn){
  currentPlatform=p;
  document.querySelectorAll('#pp-all,#pp-meta,#pp-google,#pp-referral,#pp-organic').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  renderAll();
}
function setStatus(s,btn){
  currentStatus=s;
  document.querySelectorAll('#sp-all,#sp-active,#sp-paused').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  renderAll();
}
function goToSettings(msg){
  showToast('⚙️ '+msg,'warn');
  setTimeout(function(){
    var el=document.querySelector('.tab[onclick*="settings"]');
    if(el) showTab('settings',el);
  },900);
}
function setDate(d,btn){
  currentDatePreset=d;
  document.querySelectorAll('#dp-today,#dp-yesterday,#dp-7d,#dp-14d,#dp-30d,#dp-alltime,#dp-custom').forEach(b=>b.classList.remove('active'));
  if(d!=='custom'){ const cr=document.getElementById('custom-range'); if(cr) cr.style.display='none'; }
  btn.classList.add('active');
  if(d==='all_time'){
    if(db.settings.webAppUrl) syncWithPreset(d); else renderAll();
  } else if(d==='custom'){
    const cr=document.getElementById('custom-range'); if(cr) cr.style.display='flex';
    renderAll();
  } else if(db.settings.webAppUrl){ syncWithPreset(d);
  } else { goToSettings('Date filters need a Web App URL — paste it below to enable live sync'); }
}
/* v8.3: Re-sync Meta with selected date preset, then reload from sheets */
async function syncWithPreset(preset){
  const url=db.settings.webAppUrl; if(!url) return;
  const metaPreset=preset==='all_time'?'maximum':preset;
  setSyncStatus('syncing','Syncing '+preset+'…');
  try{
    const r1=await fetch(\`\${url}?action=syncmeta&datePreset=\${metaPreset}\`,{redirect:'follow'});
    if(!r1.ok) throw new Error(\`HTTP \${r1.status}\`);
    const d1=await r1.json(); if(d1.error) throw new Error(d1.error);
    setSyncStatus('syncing','Refreshing GHL leads…');
    try{
      const rg=await fetch(\`\${url}?action=syncghl\`,{redirect:'follow'});
      if(rg.ok){ const dg=await rg.json(); if(dg.error) console.warn('GHL sync before period load:',dg.error); }
    }catch(ge){ console.warn('GHL sync before period load:',ge.message); }
    setSyncStatus('syncing','Loading data…');
    const r2=await fetch(\`\${url}?action=getfromsheets&preset=\${encodeURIComponent(preset)}\`,{redirect:'follow'});
    if(!r2.ok) throw new Error(\`HTTP \${r2.status}\`);
    const d2=await r2.json(); if(d2.error) throw new Error(d2.error);
    mergeApiData(d2); saveDB(); renderAll();
    setSyncStatus('ok','Synced '+new Date().toLocaleTimeString());
    showToast('Data synced for '+preset+' ✓');
  }catch(e){
    setSyncStatus('err','Sync failed');
    showToast('Period sync failed: '+e.message,'error');
  }
}
function filterPlatform(arr){ return currentPlatform==='all'?arr:arr.filter(x=>x.platform===currentPlatform); }
function filterStatus(arr){ return currentStatus==='all'?arr:arr.filter(x=>(x.status||'Active')===currentStatus); }


/* ═══════════════════════════════════════════
   QUALITY FILTER (Leads page)
═══════════════════════════════════════════ */
let currentQuality = 'all';
function setQualityFilter(q, btn) {
  currentQuality = q;
  document.querySelectorAll('[id^="ql-"]').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderLeads();
}
let currentUrgency = 'all';
function setUrgencyFilter(u, btn) {
  currentUrgency = u;
  document.querySelectorAll('[id^="ug-"]').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderLeads();
}
// v8.10: funnel stage quick-filter (click KPI card on Leads tab)
let currentLeadStage = 'all';
function filterLeadsByStage(stage){
  currentLeadStage=(currentLeadStage===stage)?'all':stage; // toggle off on re-click
  renderLeads();
}
// v8.10: date cutoff helper for client-side lead filtering
function getDateCutoff(preset){
  const bounds=periodBounds(preset); return bounds[0]||null;
}
function applyCustomRange(){
  renderAll();
}
function goCustomRange(){
  syncWithPreset('custom');
}
// v8.20: A/B/C colored dot quality system (replaces Real/Junk/Fake)
function qualityBadge(q, leadId) {
  const key=(q||'').toUpperCase();
  const cls=key==='A'?'q-a':key==='B'?'q-b':key==='C'?'q-c':'q-none';
  const label=key||'SET';
  return \`<button class="qbtn \${cls}" onclick="toggleQuality('\${leadId}')" title="Click to cycle A → B → C → unset">\${label}</button>\`;
}
function urgencySelect(value, leadId) {
  const v=normaliseUrgency(value);
  const cls=v==='Decision In 30 Days'?'urg-30':v==='Shortlisting Now'?'urg-short':v==='Exploring This Year'?'urg-year':'urg-no';
  return \`<select class="urg-select \${cls}" onchange="setLeadUrgency('\${leadId}',this.value)" title="Lead urgency timeline">\${URGENCY_OPTIONS.map(o=>\`<option value="\${o}" \${o===v?'selected':''}>\${o}</option>\`).join('')}</select>\`;
}
async function persistLeadRecord(lead,pushGhl=false){
  if(!lead?.ghlId||!db.settings.webAppUrl) return true;
  const base=db.settings.webAppUrl;
  try{
    const q=new URLSearchParams({action:'updatelead',ghlId:lead.ghlId,status:lead.status||'New',quality:lead.quality||'',dealValue:String(lead.dealValue||''),notes:lead.notes||'',urgencyTimeline:normaliseUrgency(lead.urgencyTimeline)});
    const r=await fetch(base+'?'+q.toString(),{redirect:'follow'}); const d=await r.json();
    if(!d.ok) throw new Error(d.error||'Sheet update failed');
    if(pushGhl){
      const g=await fetch(base+'?action=updateghl&ghlId='+encodeURIComponent(lead.ghlId)+'&status='+encodeURIComponent(lead.status)+'&dealValue='+encodeURIComponent(String(lead.dealValue||'')),{redirect:'follow'}); const gd=await g.json();
      if(!gd.ok) throw new Error(gd.error||'GHL stage update failed');
    }
    return true;
  }catch(e){ showToast('Lead save failed: '+e.message,'error'); return false; }
}
async function toggleQuality(leadId) {
  const lead=db.leads.find(l=>(l.id||l.ghlId)===leadId); if(!lead)return;
  const cycle={'':'A','A':'B','B':'C','C':''}; lead.quality=cycle[(lead.quality||'').toUpperCase()]??'A';
  saveDB(); renderLeads(); await persistLeadRecord(lead,false);
}
async function setLeadUrgency(leadId,value){
  const lead=db.leads.find(l=>(l.id||l.ghlId)===leadId); if(!lead)return;
  lead.urgencyTimeline=normaliseUrgency(value);
  saveDB(); renderLeads(); await persistLeadRecord(lead,false);
}
async function setLeadClosed(leadId,checked){
  const lead=db.leads.find(l=>(l.id||l.ghlId)===leadId); if(!lead)return;
  lead.status=checked?'Closed':(lead.status==='Closed'?'Strategy Session':lead.status);
  if(lead.status==='Closed'&&!lead.closedDate) lead.closedDate=new Date().toISOString().slice(0,10);
  saveDB(); renderAll(); await persistLeadRecord(lead,true);
}
async function saveLeadRevenue(leadId,value){
  const lead=db.leads.find(l=>(l.id||l.ghlId)===leadId); if(!lead)return;
  lead.dealValue=Math.max(0,num(value));
  const becameClosed=lead.dealValue>0&&lead.status!=='Closed';
  if(becameClosed){ lead.status='Closed'; if(!lead.closedDate) lead.closedDate=new Date().toISOString().slice(0,10); }
  saveDB(); renderAll(); await persistLeadRecord(lead,becameClosed); showToast('Revenue saved ✓');
}


/* ═══════════════════════════════════════════
   SYNC META NOW (force Meta API pull → sheet)
═══════════════════════════════════════════ */
async function syncMetaNow() {
  const url = db.settings.webAppUrl;
  if (!url) { goToSettings('Sync requires a Web App URL'); return; }
  const metaPreset=currentDatePreset==='all_time'?'maximum':currentDatePreset;
  setSyncStatus('syncing', 'Syncing Meta API…');
  try {
    const r = await fetch(\`\${url}?action=syncmeta&datePreset=\${encodeURIComponent(metaPreset)}\`, { redirect: 'follow' });
    if (!r.ok) throw new Error(\`HTTP \${r.status}\`);
    const data = await r.json();
    if (data.error) throw new Error(data.error);
    const r2=await fetch(\`\${url}?action=getfromsheets&preset=\${encodeURIComponent(currentDatePreset)}\`,{redirect:'follow'});
    if(!r2.ok) throw new Error(\`HTTP \${r2.status}\`);
    const d2=await r2.json();
    if(d2.error) throw new Error(d2.error);
    mergeApiData(d2); saveDB(); renderAll();
    setSyncStatus('ok', 'Meta synced ' + new Date().toLocaleTimeString());
    showToast('Meta API synced for '+currentDatePreset+' ✓');
  } catch (e) {
    setSyncStatus('err', 'Meta sync failed');
    showToast('Meta sync failed: ' + e.message, 'error');
  }
}


/* ═══════════════════════════════════════════
   RENDER: CEO SUMMARY
═══════════════════════════════════════════ */
function renderCEOSummary() {
  const creats=filterPlatform(filterStatus(db.creatives));
  const allCamps=filterPlatform(db.campaigns);
  const activeCamps=allCamps.filter(c=>(c.status||'').toUpperCase()==='ACTIVE');
  let leads=filterLeadsByPeriod(db.leads);
  if(currentPlatform!=='all') leads=leads.filter(l=>l.platform===currentPlatform);
  const metaCamps=allCamps.filter(c=>!c.platform||c.platform==='Meta');
  const googleCamps=allCamps.filter(c=>c.platform==='Google');
  const metaSpend=metaCamps.reduce((s,c)=>s+num(c.spend),0);
  const googleSpend=googleCamps.reduce((s,c)=>s+num(c.spend),0);
  const totalSpend=metaSpend+googleSpend;
  const metaLeads=leads.filter(l=>l.platform==='Meta').length;
  const googleLeads=leads.filter(l=>l.platform==='Google').length;
  const totalLeads=leads.length;
  const responded=leads.filter(l=>funnelRank(l.status)>=funnelRank('Responded')).length;
  const bookedCalls=leads.filter(l=>funnelRank(l.status)>=funnelRank('Booked Call')).length;
  const appts=leads.filter(l=>funnelRank(l.status)>=funnelRank('Appointment')).length;
  const ss=leads.filter(l=>funnelRank(l.status)>=funnelRank('Strategy Session')).length;
  const closedLeads=leads.filter(l=>l.status==='Closed');
  const totalRevenue=closedLeads.reduce((s,l)=>s+num(l.dealValue),0);
  const roas=totalSpend>0&&totalRevenue>0?totalRevenue/totalSpend:0;
  const videoCreats=creats.filter(c=>c.format==='Video'&&num(c.hookrate)>0);
  const avgHook=videoCreats.length?videoCreats.reduce((s,c)=>s+num(c.hookrate),0)/videoCreats.length:0;
  const googleConversions=googleCamps.reduce((s,c)=>s+num(c.conversions),0);
  const periodLabel=db.settings.googlePeriodLabel||currentDatePreset.replaceAll('_',' ');
  document.getElementById('ceoKpis').innerHTML=[
    ['Meta Spend',sgd(metaSpend),periodLabel],
    ['Google Spend',sgd(googleSpend),db.settings.googleWarning||periodLabel],
    ['Total Ad Spend',sgd(totalSpend),'Meta + Google'],
    ['Meta GHL Leads',metaLeads,'Actual opted-in leads'],
    ['Google GHL Leads',googleLeads,'Actual opted-in leads'],
    ['Total GHL Leads',totalLeads,'All sources combined'],
    ['Meta CPL',metaLeads?sgd(metaSpend/metaLeads):'—','Spend ÷ actual Meta leads'],
    ['Google CPL',googleLeads?sgd(googleSpend/googleLeads):'—','Spend ÷ actual Google leads'],
    ['Booked Calls',bookedCalls,bookedCalls?sgd(totalSpend/bookedCalls)+' / booked call':'—'],
    ['Appointments',appts,appts?sgd(totalSpend/appts)+' / appt':'—'],
    ['Strategy Sessions',ss,ss?sgd(totalSpend/ss)+' / SS':'—'],
    ['Cost / Strategy Session',ss?sgd(totalSpend/ss):'—','Spend / Strategy Sessions'],
    ['Closed',closedLeads.length,'Won deals this period'],
    ['Revenue',totalRevenue>0?sgd(totalRevenue):'SGD 0','Sum of closed deal values'],
    ['ROAS',roas?roas.toFixed(2)+'x':'—','Closed revenue ÷ total spend'],
  ].map(([l,v,s])=>\`<div class="kpi"><div class="kpi-lbl">\${l}</div><div class="kpi-val">\${v}</div><div class="kpi-sub">\${s}</div></div>\`).join('');

  // Alert strip
  const killCount = creats.filter(cr => getSignal({ ...cr, _hookrate: cr.hookrate, _cpl: cr.cpl, _spend: cr.spend, _leads: cr.leads }) === 'Kill').length;
  const scaleCount = creats.filter(cr => getSignal({ ...cr, _hookrate: cr.hookrate, _cpl: cr.cpl, _spend: cr.spend, _leads: cr.leads }) === 'Scale').length;
  const newToday=filterLeadsByPeriod(db.leads,'today').length;
  const alertEl = document.getElementById('ceoAlerts');
  if (alertEl) alertEl.innerHTML =
    \`<span style="color:var(--kill,#DC2626);font-weight:600">\u{1F6D1} \${killCount} kill alert\${killCount !== 1 ? 's' : ''}</span>\` +
    \`<span style="color:var(--muted);padding:0 8px">|</span>\` +
    \`<span style="color:var(--scale,#16A34A);font-weight:600">\u{1F525} \${scaleCount} scale candidate\${scaleCount !== 1 ? 's' : ''}</span>\` +
    \`<span style="color:var(--muted);padding:0 8px">|</span>\` +
    \`<span style="color:var(--blue,#1D4ED8);font-weight:600">\u{1F195} \${newToday} new leads today (SGT)</span>\` +
    \`<span style="color:var(--muted);padding:0 8px">|</span>\` +
    \`<span style="color:var(--muted)">Active campaigns: \${activeCamps.length}</span>\`;

  // v8.14: Active campaigns decision table — compute spend/leads/CPL from creats (raw campaigns don't carry _spend)
  const ceoCampEl = document.getElementById('ceoCampBody');
  if (ceoCampEl) {
    // Build per-campaign metrics from creatives
    const campMetrics = {};
    creats.forEach(cr => {
      const key = (cr.campaign || cr.campaignName || '').trim();
      if (!key) return;
      if (!campMetrics[key]) campMetrics[key] = { spend: 0, leads: 0 };
      campMetrics[key].spend += parseFloat(cr.spend) || 0;
      campMetrics[key].leads += parseInt(cr.leads) || 0;
    });
    ceoCampEl.innerHTML = activeCamps.length
      ? activeCamps.sort((a, b) => {
          const sa = (campMetrics[(a.name||'').trim()]||{}).spend || 0;
          const sb2 = (campMetrics[(b.name||'').trim()]||{}).spend || 0;
          return sb2 - sa;
        }).map(c => {
          const nm    = (c.name || '').trim();
          const nmLow = nm.toLowerCase();
          // Match creats by exact campaign name OR partial (first 20 chars) for fuzzy linking
          const sigCreats = creats.filter(cr => {
            const cn = (cr.campaign || cr.campaignName || '').toLowerCase();
            return cn === nmLow || (nmLow.length > 10 && cn.includes(nmLow.slice(0, 18)));
          });
          const cm       = campMetrics[nm] || { spend: 0, leads: 0 };
          const campSpend = cm.spend;
          const campLeads = cm.leads;
          const campCPL  = campLeads > 0 ? campSpend / campLeads : 0;
          const hookVids = sigCreats.filter(x => x.format === 'Video' && parseFloat(x.hookrate) > 0);
          const hookAvg  = hookVids.length ? hookVids.reduce((s, x) => s + (parseFloat(x.hookrate) || 0), 0) / hookVids.length : 0;
          const campKill = sigCreats.filter(cr => getSignal({ ...cr, _hookrate: cr.hookrate, _cpl: cr.cpl, _spend: cr.spend, _leads: cr.leads }) === 'Kill').length;
          const campScale= sigCreats.filter(cr => getSignal({ ...cr, _hookrate: cr.hookrate, _cpl: cr.cpl, _spend: cr.spend, _leads: cr.leads }) === 'Scale').length;
          const verdict  = campKill > 0 ? \`<span class="sig sig-Kill">\${campKill} Kill</span>\` : campScale > 0 ? \`<span class="sig sig-Scale">\${campScale} Scale</span>\` : \`<span class="sig sig-Hold">Hold</span>\`;
          return \`<tr>
            <td><strong>\${nm || '—'}</strong></td>
            <td>\${c.platform || '—'}</td>
            <td>\${campSpend > 0 ? sgd(campSpend) : '—'}</td>
            <td>\${campLeads}</td>
            <td>\${campCPL > 0 ? sgd(campCPL) : '—'}</td>
            <td>\${hookAvg > 0 ? pct(hookAvg) : '—'}</td>
            <td>\${verdict}</td>
          </tr>\`;
        }).join('')
      : '<tr><td colspan="7" style="text-align:center;color:var(--muted);padding:24px">No active campaigns. Sync Meta or check platform filter.</td></tr>';
  }

  // Funnel visual bar
  const funnelEl = document.getElementById('ceoFunnel');
  if (funnelEl) {
    const stages = [
      { label: 'New', count: totalLeads },
      { label: 'Responded', count: responded },
      { label: 'Booked Call', count: bookedCalls },
      { label: 'Appointment', count: appts },
      { label: 'Strat. Session', count: ss },
      { label: 'Closed', count: closedLeads.length },
    ];
    funnelEl.innerHTML = stages.map((st, i) => {
      const conv = i > 0 && stages[i - 1].count > 0 ? Math.round(st.count / stages[i - 1].count * 100) : 100;
      return \`<div style="display:flex;align-items:center;gap:0">\` +
        \`<div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:10px 16px;text-align:center;min-width:88px">\` +
        \`<div style="font-size:22px;font-weight:700;color:var(--blue,#1D4ED8)">\${st.count}</div>\` +
        \`<div style="font-size:11px;color:var(--muted);margin-top:2px">\${st.label}</div>\` +
        (i > 0 ? \`<div style="font-size:10px;color:\${conv < 20 ? 'var(--kill,#DC2626)' : 'var(--muted)'}">\${conv}% conv</div>\` : \`<div style="font-size:10px;color:var(--muted)">Period</div>\`) +
        \`</div>\` +
        (i < stages.length - 1 ? \`<div style="font-size:16px;color:var(--muted);padding:0 4px">→</div>\` : '');
    }).join('') + (totalSpend > 0 && appts > 0 ? \`<div style="margin-left:16px;font-size:12px;color:var(--muted);align-self:center">\$/Appt: \${sgd(totalSpend/appts)}\${ss > 0 ? ' &nbsp;|  \$/SS: ' + sgd(totalSpend/ss) : ''}</div>\` : '');
  }

  // Campaign funnel table (by campaign)
  const funnelBody = document.getElementById('ceoFunnelBody');
  if (funnelBody) {
    const campNames = [...new Set(leads.map(l => l.campaign || l.campaignName || '').filter(Boolean))];
    funnelBody.innerHTML = campNames.length
      ? campNames.map(cname => {
          const cl = leads.filter(l => (l.campaign || l.campaignName || '') === cname);
          const cr2 = cl.filter(l => funnelRank(l.status) >= funnelRank('Responded')).length;
          const cb = cl.filter(l => funnelRank(l.status) >= funnelRank('Booked Call')).length;
          const ca = cl.filter(l => funnelRank(l.status) >= funnelRank('Appointment')).length;
          const cq = cl.filter(l => funnelRank(l.status) >= funnelRank('Appt Qualified')).length;
          const css2 = cl.filter(l => funnelRank(l.status) >= funnelRank('Strategy Session')).length;
          const cc = cl.filter(l => l.status === 'Closed').length;
          const rev = cl.reduce((s, l) => s + (parseFloat(l.dealValue) || 0), 0);
          const spendC = creats.filter(x => (x.campaign || x.campaignName || '').toLowerCase().includes(cname.toLowerCase().slice(0, 15))).reduce((s, x) => s + (parseFloat(x.spend) || 0), 0);
          const roasC = spendC > 0 && rev > 0 ? rev / spendC : 0;
          return \`<tr><td>\${cname}</td><td>\${cl.length}</td><td>\${cr2}</td><td>\${cb}</td><td>\${ca}</td><td>\${css2}</td><td>\${cc}</td><td>\${rev > 0 ? sgd(rev) : '—'}</td><td>\${roasC > 0 ? roasC.toFixed(2) + 'x' : '—'}</td></tr>\`;
        }).join('')
      : '<tr><td colspan="9" style="text-align:center;color:var(--muted);padding:16px">No campaign data on leads yet. Make sure leads have a campaign field.</td></tr>';
  }

  // Scale / Kill lists
  const scale = creats.filter(cr => getSignal({ ...cr, _hookrate: cr.hookrate, _cpl: cr.cpl, _spend: cr.spend, _leads: cr.leads }) === 'Scale').sort((a, b) => (parseFloat(b.hookrate) || 0) - (parseFloat(a.hookrate) || 0));
  document.getElementById('ceoScaleList').innerHTML = scale.length
    ? scale.map(cr => \`<div class="act-item scale-item"><span class="sig sig-Scale">Scale</span><div class="act-item-name">\${cr.name || '—'}</div><div class="act-item-reason">Hook: \${pct(cr.hookrate)} | CPL: \${sgd(cr.cpl)} | Spend: \${sgd(cr.spend)} | Leads: \${cr.leads || 0}</div></div>\`).join('')
    : '<div class="empty" style="padding:14px"><p>No scale candidates yet.</p></div>';

  const kill = creats.filter(cr => getSignal({ ...cr, _hookrate: cr.hookrate, _cpl: cr.cpl, _spend: cr.spend, _leads: cr.leads }) === 'Kill').sort((a, b) => (parseFloat(b.spend) || 0) - (parseFloat(a.spend) || 0));
  document.getElementById('ceoKillList').innerHTML = kill.length
    ? kill.map(cr => \`<div class="act-item kill-item"><span class="sig sig-Kill">Kill</span><div class="act-item-name">\${cr.name || '—'}</div><div class="act-item-reason">Hook: \${pct(cr.hookrate)} | CPL: \${sgd(cr.cpl)} | Spend: \${sgd(cr.spend)} | Leads: \${cr.leads || 0}</div></div>\`).join('')
    : '<div class="empty" style="padding:14px"><p>No kill candidates.</p></div>';

  const syncEl = document.getElementById('ceoSyncTime');
  if (syncEl) syncEl.textContent = 'Last sync: ' + (db.settings.lastSync ? new Date(db.settings.lastSync).toLocaleString('en-SG', { timeZone: 'Asia/Singapore' }) : '—');
}

/* ═══════════════════════════════════════════
   API SYNC
═══════════════════════════════════════════ */
async function syncData(){
  const url=db.settings.webAppUrl;
  if(!url){ goToSettings('Sync requires a Web App URL — paste it below to activate live data'); return; }
  setSyncStatus('syncing','Syncing…');
  try{
    try{
      const rg=await fetch(\`\${url}?action=syncghl\`,{redirect:'follow'});
      if(rg.ok){ const dg=await rg.json(); if(dg.error) console.warn('GHL sync before load:',dg.error); }
    }catch(ge){ console.warn('GHL sync before load:',ge.message); }
    const r=await fetch(\`\${url}?action=getfromsheets&preset=\${encodeURIComponent(currentDatePreset)}\`,{redirect:'follow'});
    if(!r.ok) throw new Error(\`HTTP \${r.status}\`);
    const data=await r.json();
    if(data.error) throw new Error(data.error);
    mergeApiData(data);
    saveDB(); renderAll();
    setSyncStatus('ok','Synced '+new Date().toLocaleTimeString());
    showToast('Data synced ✓');
  }catch(e){
    setSyncStatus('err','Sync failed');
    showToast('Sync failed: '+e.message,'error');
  }
}

async function syncDataFast(){
  const url=db.settings.webAppUrl;
  if(!url){ goToSettings('Sync requires a Web App URL — paste it below to activate live data'); return; }
  setSyncStatus('syncing','Loading sheet data…');
  try{
    const r=await fetch(\`\${url}?action=getfromsheets&preset=\${encodeURIComponent(currentDatePreset)}\`,{redirect:'follow'});
    if(!r.ok) throw new Error(\`HTTP \${r.status}\`);
    const data=await r.json();
    if(data.error) throw new Error(data.error);
    mergeApiData(data); saveDB(); renderAll();
    setSyncStatus('ok','Loaded '+new Date().toLocaleTimeString());
    showToast('Dashboard loaded from sheets ✓');
    refreshIntelBackground('manual sync');
  }catch(e){
    setSyncStatus('err','Load failed');
    showToast('Load failed: '+e.message,'error');
  }
}

async function refreshIntelBackground(reason){
  const url=db.settings.webAppUrl;
  if(!url) return false;
  try{
    setSyncStatus('syncing','Refreshing latest Meta/GHL…');
    const metaPreset=currentDatePreset==='all_time'?'maximum':currentDatePreset;
    try{
      const rm=await fetch(\`\${url}?action=syncmeta&datePreset=\${encodeURIComponent(metaPreset)}\`,{redirect:'follow'});
      if(rm.ok){ const dm=await rm.json(); if(dm.error) console.warn('background Meta sync:',dm.error); }
    }catch(me){ console.warn('background Meta sync:',me.message); }
    try{
      const rg=await fetch(\`\${url}?action=syncghl\`,{redirect:'follow'});
      if(rg.ok){ const dg=await rg.json(); if(dg.error) console.warn('background GHL sync:',dg.error); }
    }catch(ge){ console.warn('background GHL sync:',ge.message); }
    const r2=await fetch(\`\${url}?action=getfromsheets&preset=\${encodeURIComponent(currentDatePreset)}\`,{redirect:'follow'});
    if(!r2.ok) throw new Error(\`HTTP \${r2.status}\`);
    const d2=await r2.json(); if(d2.error) throw new Error(d2.error);
    mergeApiData(d2); saveDB(); renderAll();
    setSyncStatus('ok','Fresh '+new Date().toLocaleTimeString());
    return true;
  }catch(e){
    console.warn('background refresh:',e.message);
    setSyncStatus('err','Background refresh delayed');
    return false;
  }
}

async function syncIntelia(){
  // v8.15: action=syncghl fetches GHL pipeline → writes to GHL_Leads sheet → then reload all
  const url=db.settings.webAppUrl;
  if(!url){ goToSettings('Sync requires a Web App URL — paste it below to activate live data'); return; }
  setSyncStatus('syncing','Syncing GHL pipeline…');
  try{
    const r=await fetch(\`\${url}?action=syncghl\`,{redirect:'follow'});
    if(!r.ok) throw new Error(\`HTTP \${r.status}\`);
    const data=await r.json();
    if(data.error) throw new Error(data.error);
    setSyncStatus('syncing','Loading from sheets…');
    const r2=await fetch(\`\${url}?action=getfromsheets&preset=\${encodeURIComponent(currentDatePreset)}\`,{redirect:'follow'});
    if(!r2.ok) throw new Error(\`HTTP \${r2.status}\`);
    const d2=await r2.json();
    if(d2.error) throw new Error(d2.error);
    mergeApiData(d2); saveDB(); renderAll();
    setSyncStatus('ok','GHL synced');
    showToast(\`GHL sync: \${data.total||0} leads written to sheet ✓\`);
  }catch(e){
    setSyncStatus('err','GHL sync failed');
    const hint=e.message.includes('GHL_API_KEY')?' — Set GHL_API_KEY in Script Properties':'';
    showToast('GHL sync failed: '+e.message+hint,'error');
  }
}

let autoSyncTimer=null, autoSyncInFlight=false, lastGhlAutoSyncAt=0;
async function syncGHLAndReload(opts={}){
  const silent=opts.silent!==false;
  const url=db.settings.webAppUrl;
  if(!url) return false;
  if(autoSyncInFlight) return false;
  autoSyncInFlight=true;
  if(!silent) setSyncStatus('syncing','Syncing GHL pipeline…');
  try{
    const r=await fetch(\`\${url}?action=syncghl\`,{redirect:'follow'});
    if(!r.ok) throw new Error(\`HTTP \${r.status}\`);
    const data=await r.json();
    if(data.error) throw new Error(data.error);
    const r2=await fetch(\`\${url}?action=getfromsheets&preset=\${encodeURIComponent(currentDatePreset)}\`,{redirect:'follow'});
    if(!r2.ok) throw new Error(\`HTTP \${r2.status}\`);
    const d2=await r2.json();
    if(d2.error) throw new Error(d2.error);
    mergeApiData(d2); saveDB(); renderAll();
    lastGhlAutoSyncAt=Date.now();
    setSyncStatus('ok','Auto-synced GHL '+new Date().toLocaleTimeString());
    if(!silent) showToast(\`GHL sync: \${data.total||0} leads updated ✓\`);
    return true;
  }catch(e){
    if(!silent){ setSyncStatus('err','GHL sync failed'); showToast('GHL sync failed: '+e.message,'error'); }
    else { console.warn('auto GHL sync:',e.message); setSyncStatus('err','Auto GHL sync delayed'); }
    return false;
  }finally{
    autoSyncInFlight=false;
  }
}
function startAutoGhlSync(){
  if(autoSyncTimer) clearInterval(autoSyncTimer);
  const mins=Math.max(1,parseInt(db.settings.autoSyncMinutes||3,10));
  autoSyncTimer=setInterval(()=>syncGHLAndReload({silent:true,reason:'interval'}),mins*60*1000);
  window.addEventListener('focus',()=>{ if(Date.now()-lastGhlAutoSyncAt>90000) syncGHLAndReload({silent:true,reason:'focus'}); });
  document.addEventListener('visibilitychange',()=>{ if(!document.hidden&&Date.now()-lastGhlAutoSyncAt>90000) syncGHLAndReload({silent:true,reason:'visible'}); });
}

function mergeApiData(data){
  if(Array.isArray(data.campaigns)){
    const prior={}; db.campaigns.forEach(c=>{if(c.metaId)prior[c.metaId]=c;});
    db.campaigns=db.campaigns.filter(c=>c.platform&&c.platform!=='Meta'&&!c.metaId);
    data.campaigns.forEach(c=>{
      const ex=prior[c.metaId]||{};
      db.campaigns.push({...ex,...c,id:ex.id||uid(),platform:c.platform||'Meta'});
    });
  }
  if(Array.isArray(data.adsets)){
    const prior={}; db.adsets.forEach(a=>{if(a.metaId)prior[a.metaId]=a;});
    db.adsets=db.adsets.filter(a=>a.platform&&a.platform!=='Meta'&&!a.metaId);
    data.adsets.forEach(a=>{
      const camp=db.campaigns.find(c=>c.metaId===a.campaignId||c.name===a.campaignName);
      if(camp) a.campaignId=camp.id;
      const ex=prior[a.metaId]||{};
      db.adsets.push({...ex,...a,id:ex.id||uid(),platform:a.platform||'Meta'});
    });
  }
  if(Array.isArray(data.ads)){
    const prior={}; db.creatives.forEach(cr=>{if(cr.metaId)prior[cr.metaId]=cr;});
    db.creatives=db.creatives.filter(cr=>cr.platform&&cr.platform!=='Meta'&&!cr.metaId);
    data.ads.forEach(ad=>{
      const as=db.adsets.find(a=>a.metaId===ad.adsetId||a.name===ad.adsetName);
      if(as) ad.adsetId=as.id;
      ad.format=detectFormat(ad.name,ad.format);
      const ex=prior[ad.metaId]||{};
      db.creatives.push({...ex,...ad,id:ex.id||uid(),platform:ad.platform||'Meta'});
    });
  }
  if(Array.isArray(data.leads)){
    function _lkey(l){
      if(l.ghlId) return 'g:'+l.ghlId;
      const ph=(l.phone||'').replace(/\D/g,'');
      if(ph.length>=8) return 'p:'+ph.slice(-8);
      const em=(l.email||'').toLowerCase().trim();
      if(em) return 'e:'+em;
      return 'n:'+(l.name||'').toLowerCase().trim();
    }
    const prev={}; db.leads.forEach(x=>{const k=_lkey(x);if(k)prev[k]=x;});
    db.leads=data.leads.map(l=>{
      const ex=prev[_lkey(l)]||{};
      return {...l,id:(ex.id||uid()),date:normaliseDateOnly(l.date),status:(l.status||ex.status||'New'),quality:(l.quality||ex.quality||''),urgencyTimeline:normaliseUrgency(l.urgencyTimeline||l.urgencytimeline||ex.urgencyTimeline||'No Timeline'),notes:(l.notes||ex.notes||''),appt:(l.appt||ex.appt||''),dealValue:(l.dealValue!==''&&l.dealValue!=null?l.dealValue:(ex.dealValue||'')),closedDate:(l.closedDate||ex.closedDate||'')};
    }).sort((a,b)=>String(b.date||'').localeCompare(String(a.date||'')));
  }

  if(Array.isArray(data.googleCampaigns)){
    db.campaigns=db.campaigns.filter(c=>c.platform!=='Google');
    data.googleCampaigns.forEach(raw=>{
      const spend=num(raw.spend), conversions=num(raw.conversions);
      db.campaigns.push({
        id:uid(), platform:'Google', googleId:String(raw.campaignId||raw.googleId||''),
        name:raw.campaign||raw.name||'', objective:raw.campaignType||raw.objective||'',
        status:normaliseStatus(raw.status), budget:num(raw.dailyBudget), spend,
        impressions:Math.round(num(raw.impressions)), clicks:Math.round(num(raw.clicks)),
        leads:0, conversions, cpl:conversions>0?spend/conversions:0, ctr:num(raw.ctr)
      });
    });
  }
  if(Array.isArray(data.googleAdGroups)){
    db.adsets=db.adsets.filter(a=>a.platform!=='Google');
    data.googleAdGroups.forEach(raw=>{
      const spend=num(raw.spend), conversions=num(raw.conversions);
      const a={platform:'Google',googleId:String(raw.adGroupId||raw.googleId||''),name:raw.adGroup||raw.name||'',campaignName:raw.campaign||raw.campaignName||'',googleCampId:String(raw.campaignId||''),status:normaliseStatus(raw.status),spend,leads:0,conversions,cpl:conversions>0?spend/conversions:0,ctr:num(raw.ctr),cpc:num(raw.avgCpc)};
      const camp=db.campaigns.find(c=>c.googleId===a.googleCampId&&a.googleCampId); if(camp) a.campaignId=camp.id;
      const ex=db.adsets.find(x=>x.googleId===a.googleId&&a.googleId); if(ex) Object.assign(ex,a); else db.adsets.push({...a,id:uid()});
    });
  }
  if(Array.isArray(data.googleAds)){
    db.creatives=db.creatives.filter(c=>c.platform!=='Google');
    data.googleAds.forEach(raw=>{
      const conversions=num(raw.conversions), spend=num(raw.spend);
      const rawVid=extractYouTubeIdClient(raw.videoId)||extractYouTubeIdClient(raw.finalUrl)||extractYouTubeIdClient(raw.thumbUrl);
      const ytThumb=rawVid?'https://i.ytimg.com/vi/'+encodeURIComponent(rawVid)+'/hqdefault.jpg':'';
      const safeThumb=extractYouTubeIdClient(raw.thumbUrl)?raw.thumbUrl:ytThumb;
      const ad={platform:'Google',googleId:String(raw.adId||raw.googleId||''),name:raw.ad||raw.adName||raw.name||'',adsetName:raw.adGroup||raw.adsetName||'',googleAgId:String(raw.adGroupId||''),campaignName:raw.campaign||raw.campaignName||'',googleCampId:String(raw.campaignId||''),status:normaliseStatus(raw.status),thumbUrl:safeThumb,imageUrl:raw.imageUrl||'',videoSrc:raw.videoSrc||raw.finalUrl||'',videoId:rawVid,hookrate:num(raw.hookrate),ctr:num(raw.ctr),cpc:num(raw.avgCpc),spend,impressions:Math.round(num(raw.impressions)),clicks:Math.round(num(raw.clicks)),leads:0,conversions,cpl:conversions>0?spend/conversions:0};
      ad.format=detectFormat(ad.name,raw.format||raw.adType||'');
      const as=db.adsets.find(a=>a.googleId===ad.googleAgId&&ad.googleAgId); if(as) ad.adsetId=as.id;
      const camp=db.campaigns.find(c=>c.googleId===ad.googleCampId&&ad.googleCampId); if(camp) ad.campaignId=camp.id;
      const ex=db.creatives.find(x=>x.googleId===ad.googleId&&ad.googleId); if(ex) Object.assign(ex,ad); else db.creatives.push({...ad,id:uid()});
    });
  }
  db.settings.googlePeriodLabel=data.googlePeriodLabel||db.settings.googlePeriodLabel||'';
  db.settings.googleDetailPeriodLabel=data.googleDetailPeriodLabel||'Last 30 days';
  db.settings.googleWarning=data.googleWarning||'';
  db.settings.lastSync=data.syncedAt||data.synced||new Date().toISOString();
  enrichLeadsClient();
}

/* ═══════════════════════════════════════════
   HELPERS
═══════════════════════════════════════════ */
let _uid=Date.now();
function uid(){ return String(++_uid); }
function num(v){
  if(v==null||v==='') return 0;
  const n=Number(String(v).replace(/[$,%\s]/g,'').replace(/,/g,''));
  return Number.isFinite(n)?n:0;
}
function sgd(v){ return 'SGD '+num(v).toLocaleString('en-SG',{maximumFractionDigits:0}); }
function pct(v){ return num(v).toFixed(1)+'%'; }
function normaliseDateOnly(v){
  if(!v) return '';
  const m=String(v).match(/^(\d{4}-\d{2}-\d{2})/); if(m) return m[1];
  const d=new Date(v); if(isNaN(d.getTime())) return '';
  const parts=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Singapore',year:'numeric',month:'2-digit',day:'2-digit'}).formatToParts(d);
  const x={}; parts.forEach(p=>x[p.type]=p.value); return x.year+'-'+x.month+'-'+x.day;
}
function shiftIsoDate(iso,days){ const d=new Date(iso+'T00:00:00Z'); d.setUTCDate(d.getUTCDate()+days); return d.toISOString().slice(0,10); }
function singaporeToday(){ return normaliseDateOnly(new Date()); }
function periodBounds(preset){
  const today=singaporeToday();
  if(preset==='today') return [today,today];
  if(preset==='yesterday'){const y=shiftIsoDate(today,-1);return [y,y];}
  if(preset==='last_7d') return [shiftIsoDate(today,-6),today];
  if(preset==='last_14d') return [shiftIsoDate(today,-13),today];
  if(preset==='last_30d') return [shiftIsoDate(today,-29),today];
  if(preset==='custom') return [document.getElementById('customStart')?.value||'',document.getElementById('customEnd')?.value||''];
  return ['', ''];
}
function filterLeadsByPeriod(list,preset=currentDatePreset){
  const [start,end]=periodBounds(preset);
  if(!start&&!end) return [...list];
  return list.filter(l=>{
    const d=normaliseDateOnly(l.date);
    const cd=normaliseDateOnly(l.closedDate);
    const inByCreate=d&&(!start||d>=start)&&(!end||d<=end);
    const inByClosed=cd&&(!start||cd>=start)&&(!end||cd<=end);
    return inByCreate||inByClosed;
  });
}
function displayLeadDate(v){ const d=normaliseDateOnly(v); if(!d)return '—'; const [y,m,day]=d.split('-'); return new Date(Date.UTC(+y,+m-1,+day)).toLocaleDateString('en-SG',{day:'2-digit',month:'short',year:'numeric',timeZone:'UTC'}); }
function enrichLeadsClient(){
  const ads={}; db.creatives.forEach(a=>{[a.id,a.metaId,a.googleId].filter(Boolean).forEach(id=>ads[String(id)]=a);if(a.name)ads['name:'+String(a.name).toLowerCase().trim()]=a;});
  db.leads.forEach(l=>{let id=String(l.sourceAdId||'').trim();if(!id&&/^\d{8,}$/.test(String(l.sourceAdName||'')))id=String(l.sourceAdName);const nameKey='name:'+String(l.sourceAdName||'').toLowerCase().trim();const a=ads[id]||ads[nameKey];if(a){l.sourceAdId=id||a.metaId||a.googleId||a.id;if(!l.sourceAdName||/^\d{8,}$/.test(String(l.sourceAdName)))l.sourceAdName=a.name||'';if(!l.campaignName)l.campaignName=a.campaignName||getCampName(a.campaignId);l.platform=a.platform||l.platform;}});
}
function getCampName(id){ return db.campaigns.find(c=>c.id===id)?.name||id||'—'; }
function getAsName(id){ return db.adsets.find(a=>a.id===id)?.name||id||'—'; }
function getAsCampId(asId){ return db.adsets.find(a=>a.id===asId)?.campaignId||''; }
function detectFormat(name,apiFormat){
  const n=(name||'').toUpperCase();
  if(/-I$|_I$|-IMG|-IMAGE|\bIMAGE\b|\bIMG\b/.test(n)) return 'Image';
  if(/-C$|_C$|-CAR|-CAROUSEL|\bCAROUSEL\b/.test(n)) return 'Carousel';
  if(/-S$|_S$|-STORY|\bSTORY\b/.test(n)) return 'Story';
  if(/-V$|_V$|-VID|-VIDEO|\bVIDEO\b/.test(n)) return 'Video';
  const af=String(apiFormat||'').toUpperCase();
  if(af.includes('IMAGE')) return 'Image';
  if(af.includes('CAROUSEL')) return 'Carousel';
  if(af.includes('STORY')) return 'Story';
  if(af.includes('VIDEO')) return 'Video';
  return 'Video';
}

function getSignal(cr){
  const s=db.settings;
  const kH=parseFloat(s.killHook)||25, scH=parseFloat(s.scaleHook)||35;
  const kC=parseFloat(s.killCPL)||200, scC=parseFloat(s.scaleCPL)||80;
  const kSp=parseFloat(s.killSpend)||150, mL=parseInt(s.minLeads)||3;
  const hr=parseFloat(cr._hookrate||cr.hookrate)||0;
  const cpl=parseFloat(cr._cpl||cr.cpl)||0;
  const sp=parseFloat(cr._spend||cr.spend)||0;
  const ld=parseInt(cr._leads||cr.leads)||0;
  if(sp<kSp) return 'Test';
  if(hr>=scH&&cpl>0&&cpl<=scC&&ld>=mL) return 'Scale';
  // v8.3: Kill = no leads at all, OR low hook + high CPL once spend threshold met
  if(ld===0&&sp>=kSp) return 'Kill';
  if(hr<kH&&sp>=kSp&&cpl>kC) return 'Kill';
  if(hr>=kH&&cpl>0&&cpl<=kC) return 'Monitor';
  return 'Pause';
}

function fmtBadge(fmt){
  const map={Video:'🎬',Image:'🖼',Carousel:'🎠',Story:'📱'};
  return \`<span style="font-size:12px">\${map[fmt]||'📄'} \${fmt}</span>\`;
}

function platBadge(p){ return \`<span class="plat-badge plat-\${p||'Meta'}">\${p||'Meta'}</span>\`; }

function leadBadge(status){
  const cls={
    'New':'lb-New','Contacted':'lb-Contacted',
    'Responded':'lb-Responded','Potential':'lb-Responded','Qualified':'lb-Responded',
    'Booked Call':'lb-BookedCall','Appointment':'lb-Appointment','Appt Set':'lb-Appointment','Booked':'lb-BookedCall',
    'Appt Qualified':'lb-ApptQualified','Appt Verified':'lb-ApptQualified',
    'Strategy Session':'lb-StrategySession',
    'Closed':'lb-Closed','Lost':'lb-Lost'
  };
  return \`<span class="lead-badge \${cls[status]||'lb-New'}">\${status||'New'}</span>\`;
}
function srcBadge(src){ const s=src||''; return s?\`<span class="src-badge src-\${s}">\${s}</span>\`:'—'; }
// Funnel stage rank: Lead -> Responded -> Booked Call -> Appointment -> Strategy Session -> Closed
const FUNNEL_STAGES=['New','Contacted','Responded','Booked Call','Appointment','Appt Qualified','Strategy Session','Closed','Lost'];
function funnelRank(status){ if(status==='Lost')return -1; const i=FUNNEL_STAGES.indexOf(status); return i>=0?i:0; }
async function toggleFunnelStage(leadId, stage){
  const l=db.leads.find(x=>x.id===leadId||x.ghlId===leadId); if(!l)return;
  const targetRank=FUNNEL_STAGES.indexOf(stage), currentRank=funnelRank(l.status);
  l.status=currentRank===targetRank?FUNNEL_STAGES[Math.max(0,targetRank-1)]:stage;
  saveDB(); renderAll(); await persistLeadRecord(l,true);
}

/* ═══════════════════════════════════════════
   RENDER: OVERVIEW
═══════════════════════════════════════════ */
function renderOverview(){
  const camps=filterPlatform(filterStatus(db.campaigns));
  const creats=filterPlatform(filterStatus(db.creatives));
  let leads=filterLeadsByPeriod(db.leads);
  if(currentPlatform!=='all') leads=leads.filter(l=>l.platform===currentPlatform);
  const metaCamps=camps.filter(c=>!c.platform||c.platform==='Meta');
  const googleCamps=camps.filter(c=>c.platform==='Google');
  const metaSpend=metaCamps.reduce((s,c)=>s+num(c.spend),0);
  const googleSpend=googleCamps.reduce((s,c)=>s+num(c.spend),0);
  const totalSpend=metaSpend+googleSpend;
  const metaLeads=leads.filter(l=>l.platform==='Meta').length;
  const googleLeads=leads.filter(l=>l.platform==='Google').length;
  const totalLeads=leads.length;
  const totalBookedCalls=leads.filter(l=>funnelRank(l.status)>=funnelRank('Booked Call')).length;
  const totalAppts=leads.filter(l=>funnelRank(l.status)>=funnelRank('Appointment')).length;
  const totalSS=leads.filter(l=>funnelRank(l.status)>=funnelRank('Strategy Session')).length;
  const closedLeads=leads.filter(l=>l.status==='Closed');
  const revenue=closedLeads.reduce((s,l)=>s+num(l.dealValue),0);
  const roas=totalSpend&&revenue?revenue/totalSpend:0;
  const videos=creats.filter(c=>c.format==='Video'&&num(c.hookrate)>0);
  const avgHook=videos.length?videos.reduce((s,c)=>s+num(c.hookrate),0)/videos.length:0;
  const googleConversions=googleCamps.reduce((s,c)=>s+num(c.conversions),0);
  const periodLabel=db.settings.googlePeriodLabel||currentDatePreset.replaceAll('_',' ');
  document.getElementById('kpiGrid').innerHTML=[
    ['Total Spend',sgd(totalSpend),'Meta + Google · '+periodLabel],
    ['Meta Spend',sgd(metaSpend),periodLabel],
    ['Google Spend',sgd(googleSpend),db.settings.googleWarning||periodLabel],
    ['Total GHL Leads',totalLeads,'All actual pipeline leads'],
    ['Meta Leads',metaLeads,'Actual GHL leads'],
    ['Google Leads',googleLeads,'Actual GHL leads'],
    ['Meta CPL',metaLeads?sgd(metaSpend/metaLeads):'—','Spend ÷ actual leads'],
    ['Google CPL',googleLeads?sgd(googleSpend/googleLeads):'—','Spend ÷ actual leads'],
    ['Booked Calls',totalBookedCalls,'Booked Call stage or above'],
    ['Appointments',totalAppts,'Appointment stage or above'],
    ['Strategy Sessions',totalSS,'Strategy Session stage or above'],
    ['Cost / Strategy Session',totalSS?sgd(totalSpend/totalSS):'—','Spend / Strategy Sessions'],
    ['Closed',closedLeads.length,'Won deals this period'],
    ['Revenue',revenue>0?sgd(revenue):'SGD 0','Closed deal revenue'],
    ['ROAS',roas?roas.toFixed(2)+'x':'—','Closed revenue ÷ spend'],
    ['Active Campaigns',camps.filter(c=>(c.status||'').toLowerCase()==='active'||!c.status).length,'Running now']
  ].map(([l,v,s])=>\`<div class="kpi"><div class="kpi-lbl">\${l}</div><div class="kpi-val">\${v}</div><div class="kpi-sub">\${s}</div></div>\`).join('');

  const overviewSigRows=creats.map(cr=>{const sig=getSignal({...cr,_hookrate:cr.hookrate,_cpl:cr.cpl,_spend:cr.spend,_leads:cr.leads});return{cr,sig};});
  const killCount=overviewSigRows.filter(x=>x.sig==='Kill').length;
  const scaleCount=overviewSigRows.filter(x=>x.sig==='Scale').length;
  const newToday=filterLeadsByPeriod(db.leads,'today').length;
  const alertEl=document.getElementById('overviewAlerts');
  if(alertEl) alertEl.innerHTML=
    '<span style="color:var(--kill);font-weight:800">🛑 '+killCount+' kill alert'+(killCount!==1?'s':'')+'</span>'+
    '<span style="color:var(--muted);padding:0 6px">|</span>'+
    '<span style="color:var(--scale);font-weight:800">🔥 '+scaleCount+' scale candidate'+(scaleCount!==1?'s':'')+'</span>'+
    '<span style="color:var(--muted);padding:0 6px">|</span>'+
    '<span style="color:var(--navy);font-weight:800">🆕 '+newToday+' new leads today (SGT)</span>'+
    '<span style="color:var(--muted);padding:0 6px">|</span>'+
    '<span style="color:var(--muted)">Active campaigns: '+camps.filter(c=>(c.status||'').toLowerCase()==='active'||!c.status).length+'</span>';

  function vizRows(rows,maxVal){
    return rows.map(function(r){
      const w=Math.max(4,Math.round((r.value/(maxVal||1))*100));
      return '<div class="viz-row"><div><strong>'+r.label+'</strong></div><div class="viz-bar"><div class="viz-fill" style="width:'+w+'%"></div></div><div class="viz-meta">'+r.meta+'</div></div>';
    }).join('');
  }
  const fmtAgg={};
  creats.forEach(function(cr){
    const f=detectFormat(cr.name,cr.format);
    if(!fmtAgg[f]) fmtAgg[f]={label:f,spend:0,leads:0,hookSum:0,hookN:0,value:0,meta:''};
    fmtAgg[f].spend+=num(cr.spend); fmtAgg[f].leads+=num(cr.leads);
    if(num(cr.hookrate)>0){fmtAgg[f].hookSum+=num(cr.hookrate);fmtAgg[f].hookN++;}
  });
  const fmtRows=Object.values(fmtAgg).map(function(r){
    r.value=r.leads||r.spend;
    const cpl=r.leads?sgd(r.spend/r.leads):'—';
    const hook=r.hookN?pct(r.hookSum/r.hookN):'—';
    r.meta=r.leads+' leads · '+cpl+' CPL · '+hook+' hook';
    return r;
  }).sort((a,b)=>b.value-a.value);
  const platRows=['Meta','Google','Referral','Organic'].map(function(p){
    const pLeads=leads.filter(l=>l.platform===p||l.source===p).length;
    const pSpend=p==='Meta'?metaSpend:p==='Google'?googleSpend:0;
    return {label:p,value:pLeads||pSpend,meta:pLeads+' leads'+(pSpend?' · '+sgd(pSpend):'')};
  }).filter(r=>r.value>0);
  const stageRows=['New','Responded','Booked Call','Appointment','Strategy Session','Closed'].map(function(s){
    const count=leads.filter(l=>s==='New'?funnelRank(l.status)>=0:funnelRank(l.status)>=funnelRank(s)).length;
    return {label:s,value:count,meta:count+' leads'};
  });
  const fmtMax=Math.max(1,...fmtRows.map(r=>r.value));
  const platMax=Math.max(1,...platRows.map(r=>r.value));
  const stageMax=Math.max(1,...stageRows.map(r=>r.value));
  const viz=document.getElementById('overviewViz');
  if(viz) viz.innerHTML=
    '<div class="viz-card"><div class="viz-title">Creative Type Performance</div>'+(fmtRows.length?vizRows(fmtRows,fmtMax):'<div class="empty" style="padding:20px">No creative format data yet.</div>')+'</div>'+
    '<div class="viz-card"><div class="viz-title">Platform Mix</div>'+(platRows.length?vizRows(platRows,platMax):'<div class="empty" style="padding:20px">No platform data yet.</div>')+'</div>'+
    '<div class="viz-card"><div class="viz-title">Pipeline Distribution</div>'+vizRows(stageRows,stageMax)+'</div>';
  const syncEl=document.getElementById('overviewSyncTime');
  if(syncEl) syncEl.textContent='Last sync: '+(db.settings.lastSync?new Date(db.settings.lastSync).toLocaleString('en-SG',{timeZone:'Asia/Singapore'}):'—');

  // Action list
  const killScale=creats.map(cr=>{const sig=getSignal({...cr,_hookrate:cr.hookrate,_cpl:cr.cpl,_spend:cr.spend,_leads:cr.leads});return{cr,sig};}).filter(x=>x.sig==='Kill'||x.sig==='Scale');
  const al=document.getElementById('actionList');
  if(!killScale.length){al.innerHTML='<div class="empty" style="padding:14px"><p>No immediate actions needed.</p></div>';return;}
  al.innerHTML=killScale.map(({cr,sig})=>\`
    <div class="act-item \${sig==='Kill'?'kill-item':'scale-item'}">
      <span class="sig sig-\${sig}">\${sig}</span>
      <div class="act-item-name">\${cr.name||'—'}</div>
      <div class="act-item-reason">Hook: \${pct(cr.hookrate)} | CPL: \${sgd(cr.cpl)} | Spend: \${sgd(cr.spend)}</div>
    </div>\`).join('');

  // Top performers
  const top=[...creats].sort((a,b)=>(parseFloat(b.hookrate)||0)-(parseFloat(a.hookrate)||0)).slice(0,5);
  document.getElementById('topPerformers').innerHTML=top.length?\`<div class="tbl-wrap"><table>
    <thead><tr><th>Ad Name</th><th>Format</th><th>Hook%</th><th>CTR%</th><th>Leads</th><th>CPL</th><th>Signal</th></tr></thead>
    <tbody>\${top.map(cr=>{const sig=getSignal({...cr,_hookrate:cr.hookrate,_cpl:cr.cpl,_spend:cr.spend,_leads:cr.leads});return\`<tr>
      <td class="td-name">\${cr.name||'—'}</td><td>\${fmtBadge(cr.format||'Video')}</td>
      <td><b>\${pct(cr.hookrate)}</b></td><td>\${pct(cr.ctr)}</td><td>\${cr.leads||0}</td>
      <td>\${sgd(cr.cpl)}</td><td><span class="sig sig-\${sig}">\${sig}</span></td></tr>\`;}).join('')}
    </tbody></table></div>\`:'<div class="empty"><div class="empty-icon">🎨</div><p>Add creatives to see top performers</p></div>';
}

/* ═══════════════════════════════════════════
   RENDER: CAMPAIGNS
═══════════════════════════════════════════ */
function renderCampaigns(){
  const q=(document.getElementById('campSearch')?.value||'').toLowerCase();
  const periodLeads=filterLeadsByPeriod(db.leads);
  let rows=filterPlatform(filterStatus(db.campaigns)).filter(c=>!q||c.name?.toLowerCase().includes(q));
  rows=rows.map(c=>{
    const cNL=(c.name||'').toLowerCase();
    const campLeads=periodLeads.filter(l=>{
      const lNL=(l.campaignName||'').toLowerCase();
      if(lNL&&(lNL===cNL||lNL.includes(cNL)||cNL.includes(lNL))) return true;
      const cr=db.creatives.find(x=>
        (l.sourceAdId&&(l.sourceAdId===x.id||l.sourceAdId===x.metaId||l.sourceAdId===x.googleId))||
        (l.sourceAdName&&l.sourceAdName===x.name)
      );
      if(!cr) return false;
      if(cr.campaignId&&cr.campaignId===c.id) return true;
      if(cr.googleCampId&&cr.googleCampId===c.googleId) return true;
      const crCamp=(cr.campaignName||getCampName(cr.campaignId)||'').toLowerCase();
      return crCamp&&(crCamp===cNL||crCamp.includes(cNL)||cNL.includes(crCamp));
    });
    const _leads=campLeads.length, _spend=num(c.spend), _budget=num(c.budget), _cpl=_leads?_spend/_leads:0;
    const _responded=campLeads.filter(l=>funnelRank(l.status)>=funnelRank('Responded')).length;
    const _appts=campLeads.filter(l=>funnelRank(l.status)>=funnelRank('Appointment')).length;
    const _ss=campLeads.filter(l=>funnelRank(l.status)>=funnelRank('Strategy Session')).length;
    const _revenue=campLeads.filter(l=>l.status==='Closed').reduce((s,l)=>s+num(l.dealValue),0);
    const _roasNum=_spend&&_revenue?_revenue/_spend:0;
    const _roas=_roasNum?_roasNum.toFixed(2)+'x':'—';
    return{...c,_leads,_spend,_budget,_cpl,_responded,_appts,_ss,_revenue,_roas,_roasNum};
  });
  if(sortState.campaigns) rows=applySort(rows,'campaigns');
  else rows.sort((a,b)=>((b.status||'Active')==='Active')-((a.status||'Active')==='Active')||(b._leads-a._leads)||(b._spend-a._spend)||String(a.name||'').localeCompare(String(b.name||'')));
  updateIcons('campaigns');
  const tbody=document.getElementById('campaignsBody');
  if(!rows.length){tbody.innerHTML=\`<tr><td colspan="13"><div class="empty"><div class="empty-icon">🎯</div><p>No campaign data for this period.</p></div></td></tr>\`;return;}
  tbody.innerHTML=rows.map(c=>{const p=c._budget?Math.min(c._spend/c._budget*100,100):0;const bar=p>90?'pover':p>70?'pwarn':'pok';return\`<tr>
    <td class="td-name">\${c.name||'—'}</td><td>\${platBadge(c.platform)}</td><td class="td-muted">\${c.objective||'—'}</td>
    <td>\${sgd(c._budget)}<div class="pbar"><div class="pbar-fill \${bar}" style="width:\${p}%"></div></div></td>
    <td>\${sgd(c._spend)}</td><td>\${c._leads}</td><td>\${c._leads?sgd(c._cpl):'—'}</td><td>\${c._responded||'—'}</td><td>\${c._appts||'—'}</td><td>\${c._ss||'—'}</td><td>\${c._roas}</td>
    <td><span class="status-\${c.status||'Active'}">\${c.status||'Active'}</span></td><td><div class="row-acts"><button class="btn-sm" onclick="openCampaignModal('\${c.id}')">Edit</button><button class="btn-sm btn-sm-kill" onclick="confirmDelete('campaign','\${c.id}')">Del</button></div></td></tr>\`;}).join('');
}

/* ═══════════════════════════════════════════
   RENDER: AD SETS
═══════════════════════════════════════════ */
function renderAdSets(){
  const q=(document.getElementById('adsetSearch')?.value||'').toLowerCase();
  let rows=filterPlatform(filterStatus(db.adsets)).filter(a=>!q||a.name?.toLowerCase().includes(q));
  rows=rows.map(a=>{
    const _campName=getCampName(a.campaignId);
    const _adsCount=db.creatives.filter(c=>c.adsetId===a.id).length;
    const _spend=parseFloat(a.spend)||0;
    const _leads=parseInt(a.leads)||0;
    const _budget=parseFloat(a.budget)||0;
    const _cpl=_leads>0?_spend/_leads:(parseFloat(a.cpl)||0);
    return{...a,_campName,_adsCount,_spend,_leads,_budget,_cpl};
  });
  if(sortState.adsets) rows=applySort(rows,'adsets');
  else rows.sort((a,b)=>(b._leads-a._leads)||(b._spend-a._spend)||String(a.name||'').localeCompare(String(b.name||'')));
  updateIcons('adsets');
  const tbody=document.getElementById('adsetsBody');
  if(!rows.length){tbody.innerHTML=\`<tr><td colspan="10"><div class="empty"><div class="empty-icon">📁</div><p>No ad sets yet.</p></div></td></tr>\`;return;}
  tbody.innerHTML=rows.map(a=>\`<tr>
    <td class="td-name">\${a.name||'—'}</td>
    <td class="td-muted">\${a._campName}</td>
    <td>\${platBadge(a.platform)}</td>
    <td class="td-muted">\${a.audience||'—'}</td>
    <td>\${sgd(a._budget)}</td><td>\${sgd(a._spend)}</td><td>\${a._leads}</td><td>\${sgd(a._cpl)}</td>
    <td>\${a._adsCount}</td>
    <td><div class="row-acts">
      <button class="btn-sm" onclick="openAdSetModal('\${a.id}')">Edit</button>
      <button class="btn-sm btn-sm-kill" onclick="confirmDelete('adset','\${a.id}')">Del</button>
    </div></td></tr>\`).join('');
}

/* ═══════════════════════════════════════════
   RENDER: CREATIVES
═══════════════════════════════════════════ */
function renderCreatives(){
  const q=(document.getElementById('crSearch')?.value||'').toLowerCase();
  let rows=filterPlatform(filterStatus(db.creatives)).filter(c=>!q||c.name?.toLowerCase().includes(q));
  rows=rows.map(cr=>{
    const _asName=getAsName(cr.adsetId);
    const _campName=getCampName(getAsCampId(cr.adsetId));
    const _hookrate=parseFloat(cr.hookrate)||0;
    const _ctr=parseFloat(cr.ctr)||0;
    const _cpc=parseFloat(cr.cpc)||0;
    const _leads=parseInt(cr.leads)||0;
    const _spend=parseFloat(cr.spend)||0;
    const _cpl=_leads>0?_spend/_leads:(parseFloat(cr.cpl)||0);
    // Full pipeline quality metrics — match leads by ad id or name
    const linkedLeads=db.leads.filter(l=>
      (l.sourceAdId&&(l.sourceAdId===cr.id||l.sourceAdId===cr.metaId||l.sourceAdId===cr.googleId))||
      (l.sourceAdName&&l.sourceAdName===cr.name)
    );
    const _potential=linkedLeads.filter(l=>['Responded','Booked Call','Appointment','Appt Qualified','Strategy Session','Closed','Potential','Qualified','Appt Set','Booked','Appt Verified'].includes(l.status)).length;
    const _apptSet=linkedLeads.filter(l=>['Appointment','Appt Qualified','Strategy Session','Closed','Appt Set','Appt Verified'].includes(l.status)).length;
    const _apptVerified=linkedLeads.filter(l=>['Appt Qualified','Strategy Session','Closed','Appt Verified'].includes(l.status)).length;
    const _closed=linkedLeads.filter(l=>l.status==='Closed').length;
    const _costPotential=_potential>0?_spend/_potential:0;
    const _costAppt=_apptSet>0?_spend/_apptSet:0;
    const _costVerified=_apptVerified>0?_spend/_apptVerified:0;
    const _lqPct=_leads>0?_potential/_leads*100:0;
    const _paPct=_potential>0?_apptSet/_potential*100:0;
    // Legacy aliases for backward compat with sort engine
    const _qualLeads=_potential; const _appts=_apptSet; const _costQual=_costPotential; const _qaPct=_paPct;
    const sigStr=getSignal({_hookrate,_cpl,_spend,_leads});
    const _signal=sigStr==='Scale'?4:sigStr==='Monitor'?3:sigStr==='Test'?2:sigStr==='Pause'?1:0;
    const _sig=sigStr;
    const fmt=detectFormat(cr.name,cr.format);
    return{...cr,_asName,_campName,_hookrate,_ctr,_cpc,_leads,_spend,_cpl,_potential,_apptSet,_apptVerified,_closed,_costPotential,_costAppt,_costVerified,_lqPct,_paPct,_qualLeads,_appts,_costQual,_qaPct,_signal,_sig,format:fmt};
  });
  if(sortState.creatives) rows=applySort(rows,'creatives');
  else rows.sort((a,b)=>(b._lqPct-a._lqPct)||(b._paPct-a._paPct)||(b._signal-a._signal)||(b._leads-a._leads)||(b._hookrate-a._hookrate));
  updateIcons('creatives');
  const tbody=document.getElementById('creativesBody');
  if(!rows.length){tbody.innerHTML=\`<tr><td colspan="21"><div class="empty"><div class="empty-icon">🎨</div><p>No creatives yet. Add one or Sync.</p></div></td></tr>\`;return;}
  tbody.innerHTML=rows.map(cr=>{
    const thumbHtml=cr.thumbUrl
      ?\`<img class="thumb" src="\${cr.thumbUrl}" alt="" onclick="openLightbox('\${cr.thumbUrl}','\${cr.format||'Video'}','\${esc(cr.name)}','\${cr.videoId||''}','\${cr.imageUrl||''}','\${cr.videoSrc||''}','\${cr.adPermalink||''}','\${cr.platform||'Meta'}')">\`
      :cr.videoId
        ?\`<div class="thumb-placeholder" style="cursor:pointer;border:1px dashed var(--gold)" onclick="openLightbox('','\${cr.format||'Video'}','\${esc(cr.name)}','\${cr.videoId||''}','','\${cr.videoSrc||''}','\${cr.adPermalink||''}','\${cr.platform||'Meta'}')" title="Play video">\${cr.format==='Image'?'🖼':cr.format==='Carousel'?'🎠':'🎬'} ▶</div>\`
        :\`<div class="thumb-placeholder">\${cr.format==='Image'?'🖼':cr.format==='Carousel'?'🎠':'🎬'}</div>\`;
    const hookColor=cr._hookrate>=parseFloat(db.settings.scaleHook)?'color:var(--scale);font-weight:700':cr._hookrate<parseFloat(db.settings.killHook)?'color:var(--kill);font-weight:700':'';
    return\`<tr>
      <td class="sticky-l0 thumb-cell">\${thumbHtml}</td>
      <td class="sticky-l1 td-name">\${cr.name||'—'}<br><span class="td-muted">\${cr.hook||''}</span></td>
      <td class="td-muted">\${cr._asName}</td>
      <td class="td-muted">\${cr._campName}</td>
      <td>\${platBadge(cr.platform)}</td>
      <td>\${fmtBadge(cr.format)}</td>
      <td style="\${hookColor}">\${pct(cr._hookrate)}</td>
      <td>\${pct(cr._ctr)}</td>
      <td>\${sgd(cr._cpc)}</td>
      <td><b>\${cr._leads}</b></td>
      <td>\${cr._potential||'—'}</td>
      <td>\${cr._apptSet||'—'}</td>
      <td>\${cr._apptVerified||'—'}</td>
      <td>\${sgd(cr._spend)}</td>
      <td>\${sgd(cr._cpl)}</td>
      <td>\${cr._costPotential>0?sgd(cr._costPotential):'—'}</td>
      <td>\${cr._costAppt>0?sgd(cr._costAppt):'—'}</td>
      <td>\${cr._costVerified>0?sgd(cr._costVerified):'—'}</td>
      <td>\${cr._lqPct>0?pct(cr._lqPct):'—'}</td>
      <td>\${cr._paPct>0?pct(cr._paPct):'—'}</td>
      <td><span class="sig sig-\${cr._sig}">\${cr._sig}</span></td>
      <td><span class="status-\${cr.status||'Active'}">\${cr.status||'Active'}</span></td>
      <td class="sticky-r0"><div class="row-acts" style="opacity:1">
        <button class="btn-sm" onclick="openCreativeModal('\${cr.id}')">Edit</button>
        <button class="btn-sm" onclick="logAction('\${cr.id}')">Log</button>
        <button class="btn-sm btn-sm-kill" onclick="confirmDelete('creative','\${cr.id}')">Del</button>
      </div></td></tr>\`;
  }).join('');
}

/* ─── Src CPL helper ─────────────────────────────────────────────────────────
   Returns the CPL of the creative that sourced this lead.
   Matches by sourceAdId (meta/google ad ID) or sourceAdName (ad name string).
   Used in the Leads table Src CPL column.
*/
function srcCpl(lead){
  if(!lead) return '—';
  const cr=db.creatives.find(c=>
    (lead.sourceAdId&&lead.sourceAdId!==''&&
      (lead.sourceAdId===c.id||lead.sourceAdId===c.metaId||lead.sourceAdId===c.googleId))||
    (lead.sourceAdName&&lead.sourceAdName!==''&&lead.sourceAdName===c.name)
  );
  if(!cr) return '—';
  const spend=parseFloat(cr.spend)||0;
  const leads=parseFloat(cr.leads)||0;
  if(!spend||!leads) return '—';
  return sgd(spend/leads);
}

/* ═══════════════════════════════════════════
   RENDER: LEADS
═══════════════════════════════════════════ */
function renderLeads(){
  const q=(document.getElementById('leadSearch')?.value||'').trim().toLowerCase();
  const qDigits=q.replace(/\D/g,'');
  let rows=filterLeadsByPeriod(db.leads).filter(l=>{
    if(!q)return true;
    if((l.name||'').toLowerCase().includes(q))return true;
    if((l.contact||'').toLowerCase().includes(q))return true;
    if((l.email||'').toLowerCase().includes(q))return true;
    if((l.notes||'').toLowerCase().includes(q))return true;
    if(qDigits.length>=3){
      const pd=(l.phone||'').replace(/\D/g,'');
      const cd=(l.contact||'').replace(/\D/g,'');
      if(pd&&(pd.includes(qDigits)||qDigits.includes(pd)))return true;
      if(cd&&(cd.includes(qDigits)||qDigits.includes(cd)))return true;
    }
    return false;
  });
  if(currentPlatform!=='all') rows=rows.filter(l=>l.platform===currentPlatform);
  if(currentQuality!=='all') rows=currentQuality==='untagged'?rows.filter(l=>!l.quality):rows.filter(l=>(l.quality||'').toUpperCase()===currentQuality.toUpperCase());
  if(currentUrgency!=='all') rows=rows.filter(l=>normaliseUrgency(l.urgencyTimeline)===currentUrgency);
  const total=rows.length,
    responded=rows.filter(l=>funnelRank(l.status)>=funnelRank('Responded')).length,
    bookedCall=rows.filter(l=>funnelRank(l.status)>=funnelRank('Booked Call')).length,
    appointment=rows.filter(l=>funnelRank(l.status)>=funnelRank('Appointment')).length,
    strategy=rows.filter(l=>funnelRank(l.status)>=funnelRank('Strategy Session')).length,
    closed=rows.filter(l=>l.status==='Closed').length;
  const totalRevenueLeads=rows.filter(l=>l.status==='Closed').reduce((s,l)=>s+num(l.dealValue),0);
  const lr=total?responded/total*100:0,
    rb=responded?bookedCall/responded*100:0,
    ba=bookedCall?appointment/bookedCall*100:0,
    ass=appointment?strategy/appointment*100:0,
    sc=strategy?closed/strategy*100:0;
  const urgent30=rows.filter(l=>normaliseUrgency(l.urgencyTimeline)==='Decision In 30 Days').length;
  const shortlisting=rows.filter(l=>normaliseUrgency(l.urgencyTimeline)==='Shortlisting Now').length;
  const cards=[['Leads',total,'all','Period'],['Responded',responded,'Responded','Replied'],['Booked',bookedCall,'Booked Call','Booked'],['Appt',appointment,'Appointment','Appt+'],['SS',strategy,'Strategy Session','SS+'],['Closed',closed,'Closed','Won'],['Revenue',totalRevenueLeads>0?sgd(totalRevenueLeads):'SGD 0',null,'Closed $'],['30d Urgent',urgent30,null,'→SS now'],['Shortlist',shortlisting,null,'Proj FW'],['L→R',pct(lr),null,'Conv%'],['R→B',pct(rb),null,'Conv%'],['B→A',pct(ba),null,'Conv%'],['A→SS',pct(ass),null,'Conv%'],['SS→C',pct(sc),null,'Conv%']];
  document.getElementById('leadKpis').innerHTML=cards.map(([l,v,stg,sub])=>\`<div class="kpi\${stg===currentLeadStage?' kpi-sel':''}" \${stg?\`data-stage="\${stg}" style="cursor:pointer"\`:''}><div class="kpi-lbl">\${l}</div><div class="kpi-val" style="font-size:20px">\${v}</div><div class="kpi-sub">\${sub}</div></div>\`).join('');
  document.querySelectorAll('#leadKpis .kpi[data-stage]').forEach(el=>el.onclick=()=>filterLeadsByStage(el.dataset.stage));
  syncStickyOffsets();
  if(currentLeadStage!=='all'){const rank=funnelRank(currentLeadStage);rows=rows.filter(l=>currentLeadStage==='Closed'?l.status==='Closed':funnelRank(l.status)>=rank);}
  if(sortState.leads) rows=applySort(rows,'leads');
  else rows.sort((a,b)=>String(b.date||'').localeCompare(String(a.date||''))||String(b.name||'').localeCompare(String(a.name||'')));
  updateIcons('leads');
  const tbody=document.getElementById('leadsBody');
  if(!rows.length){tbody.innerHTML=\`<tr><td colspan="11"><div class="empty"><div class="empty-icon">👥</div><p>No leads for this period or filter.</p></div></td></tr>\`;return;}
  tbody.innerHTML=rows.map(l=>{
    const lid=l.id||l.ghlId||'', stages=['New','Responded','Booked Call','Appointment','Strategy Session','Closed'], labels=['New','Resp','Book','Appt','SS','Close'], rank=funnelRank(l.status);
    const pipe=stages.map((s,i)=>{const r=funnelRank(s),cls=rank>r?'pip-done':rank===r?'pip-at':'pip-todo';return\`<button class="pip-btn \${cls}" onclick="toggleFunnelStage('\${lid}','\${s}')" title="\${s}">\${labels[i]}</button>\`;}).join('<span class="pip-arr">›</span>');
    const src=l.sourceAdName||(l.campaignName||'—');
    return\`<tr><td class="td-name">\${l.name||'—'}</td><td class="td-muted" style="font-size:12px">\${l.phone||l.contact||'—'}</td><td class="td-muted" style="font-size:12px">\${l.email||'—'}</td><td>\${platBadge(l.platform||l.source)}</td><td class="td-muted">\${l.campaignName||'—'}</td><td class="td-muted" title="\${esc(src)}">\${src}</td><td style="vertical-align:top"><div class="pipeline-flow" style="margin-bottom:2px">\${pipe}</div><div>\${urgencySelect(l.urgencyTimeline,lid)}</div></td><td style="text-align:center">\${qualityBadge(l.quality,lid)}</td><td><div class="rev-wrap"><input class="rev-check" type="checkbox" \${l.status==='Closed'?'checked':''} onchange="setLeadClosed('\${lid}',this.checked)" title="Mark closed"><input class="rev-input" type="number" min="0" step="1000" value="\${num(l.dealValue)||''}" placeholder="SGD revenue" onchange="saveLeadRevenue('\${lid}',this.value)"></div></td><td class="td-muted">\${displayLeadDate(l.date)}</td><td class="col-action"><button class="btn-sm" onclick="openLeadModal('\${lid}')" style="font-size:10px;padding:2px 5px;margin:0 1px">Edit</button><button class="btn-sm btn-sm-kill" onclick="confirmDelete('lead','\${lid}')" style="font-size:10px;padding:2px 5px;margin:0 1px">Del</button></td></tr>\`;
  }).join('');
}

/* ═══════════════════════════════════════════
   RENDER: KILL/SCALE LOG
═══════════════════════════════════════════ */
function renderLog(){
  const rows=[...db.killScaleLog].sort((a,b)=>b.date>a.date?1:-1);
  const tbody=document.getElementById('logBody');
  if(!rows.length){
    const kH=db.settings.killHook||25,scH=db.settings.scaleHook||35,kC=db.settings.killCPL||200,scC=db.settings.scaleCPL||80,kSp=db.settings.killSpend||150;
    tbody.innerHTML=\`<tr><td colspan="10"><div class="empty" style="max-width:600px;text-align:left;padding:24px">
      <div style="font-size:28px;margin-bottom:8px">📋</div>
      <div style="font-weight:700;font-size:15px;margin-bottom:8px">No decisions logged yet</div>
      <p style="font-size:13px;color:var(--muted);margin-bottom:16px">The Kill/Scale Log is your decision journal — record every time you pause or scale an ad with the data and reason. This creates accountability and reveals patterns over time.</p>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px">
        <div style="background:var(--kill-bg,#FEF2F2);border-left:3px solid var(--kill,#DC2626);padding:12px;border-radius:6px">
          <div style="font-weight:700;color:var(--kill,#DC2626);margin-bottom:6px">🛑 Kill an ad when:</div>
          <div style="font-size:12px;color:var(--text)">• Hook rate &lt; \${kH}% (not stopping the scroll)</div>
          <div style="font-size:12px;color:var(--text)">• CPL &gt; SGD \${kC} (too expensive per lead)</div>
          <div style="font-size:12px;color:var(--text)">• Spend &gt; SGD \${kSp} with fewer than 3 leads</div>
        </div>
        <div style="background:var(--scale-bg,#F0FDF4);border-left:3px solid var(--scale,#16A34A);padding:12px;border-radius:6px">
          <div style="font-weight:700;color:var(--scale,#16A34A);margin-bottom:6px">🚀 Scale an ad when:</div>
          <div style="font-size:12px;color:var(--text)">• Hook rate &gt; \${scH}% (strong scroll-stop)</div>
          <div style="font-size:12px;color:var(--text)">• CPL &lt; SGD \${scC} (efficient lead cost)</div>
          <div style="font-size:12px;color:var(--text)">• Consistent quality leads over 3+ days</div>
        </div>
      </div>
      <p style="font-size:12px;color:var(--muted)">To log a decision: go to <strong>Creatives</strong> tab → find the ad → click <strong>Log</strong>. The system will pre-fill the recommended action and reason based on current metrics.</p>
    </div></td></tr>\`;
    return;
  }
  tbody.innerHTML=rows.map(l=>{
    const cr=db.creatives.find(c=>c.id===l.adId);
    const campName=cr?getCampName(getAsCampId(cr.adsetId)):'—';
    return\`<tr>
      <td class="td-muted">\${l.date||'—'}</td>
      <td class="td-name">\${l.adName||'—'}</td>
      <td class="td-muted">\${campName}</td>
      <td><span class="sig sig-\${l.action}">\${l.action||'—'}</span></td>
      <td>\${sgd(l.spend)}</td>
      <td>\${l.leads||'—'}</td>
      <td>\${l.leads&&l.spend?sgd(l.spend/l.leads):'—'}</td>
      <td>\${l.hookrate?pct(l.hookrate):'—'}</td>
      <td class="td-muted">\${l.reason||'—'}</td>
      <td><div class="row-acts"><button class="btn-sm btn-sm-kill" onclick="confirmDelete('log','\${l.id}')">Del</button></div></td>
    </tr>\`;
  }).join('');
}

function renderAll(){ renderCEOSummary(); renderOverview(); renderCampaigns(); renderAdSets(); renderCreatives(); renderLeads(); renderLog(); }

/* ═══════════════════════════════════════════
   TAB NAVIGATION
═══════════════════════════════════════════ */
function showTab(name,el){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
  document.getElementById('page-'+name).classList.add('active');
  el.classList.add('active');
  if(name==='settings') populateSettings();
  if(name==='ceo') renderCEOSummary();
  if(name==='leads') renderLeads();
  syncStickyOffsets();
}

/* ═══════════════════════════════════════════
   MODALS — CAMPAIGN
═══════════════════════════════════════════ */
function openCampaignModal(id){
  editId.campaign=id||null;
  document.getElementById('campModalTitle').textContent=id?'Edit Campaign':'Add Campaign';
  const c=id?db.campaigns.find(x=>x.id===id):{};
  document.getElementById('cm_name').value=c?.name||'';
  document.getElementById('cm_platform').value=c?.platform||'Meta';
  document.getElementById('cm_obj').value=c?.objective||'';
  document.getElementById('cm_status').value=c?.status||'Active';
  document.getElementById('cm_budget').value=c?.budget||'';
  document.getElementById('cm_metaId').value=c?.metaId||'';
  openModal('campModal');
}
function saveCampaign(){
  const name=document.getElementById('cm_name').value.trim();
  if(!name){alert('Name required');return;}
  const data={name,platform:document.getElementById('cm_platform').value,objective:document.getElementById('cm_obj').value,status:document.getElementById('cm_status').value,budget:parseFloat(document.getElementById('cm_budget').value)||0,metaId:document.getElementById('cm_metaId').value.trim()};
  if(editId.campaign){Object.assign(db.campaigns.find(c=>c.id===editId.campaign),data);}
  else db.campaigns.push({...data,id:uid()});
  saveDB(); renderCampaigns(); renderOverview(); closeModal('campModal');
}

/* ═══════════════════════════════════════════
   MODALS — AD SET
═══════════════════════════════════════════ */
function openAdSetModal(id){
  editId.adset=id||null;
  document.getElementById('adsetModalTitle').textContent=id?'Edit Ad Set':'Add Ad Set';
  const sel=document.getElementById('as_campaign');
  sel.innerHTML=db.campaigns.map(c=>\`<option value="\${c.id}">\${c.name}</option>\`).join('');
  const a=id?db.adsets.find(x=>x.id===id):{};
  document.getElementById('as_name').value=a?.name||'';
  if(a?.campaignId) sel.value=a.campaignId;
  document.getElementById('as_status').value=a?.status||'Active';
  document.getElementById('as_audience').value=a?.audience||'';
  document.getElementById('as_budget').value=a?.budget||'';
  document.getElementById('as_metaId').value=a?.metaId||'';
  openModal('adsetModal');
}
function saveAdSet(){
  const name=document.getElementById('as_name').value.trim();
  if(!name){alert('Name required');return;}
  const data={name,campaignId:document.getElementById('as_campaign').value,status:document.getElementById('as_status').value,audience:document.getElementById('as_audience').value,budget:parseFloat(document.getElementById('as_budget').value)||0,metaId:document.getElementById('as_metaId').value.trim()};
  if(editId.adset){Object.assign(db.adsets.find(a=>a.id===editId.adset),data);}
  else db.adsets.push({...data,id:uid()});
  saveDB(); renderAdSets(); closeModal('adsetModal');
}

/* ═══════════════════════════════════════════
   MODALS — CREATIVE
═══════════════════════════════════════════ */
function openCreativeModal(id){
  editId.creative=id||null;
  document.getElementById('crModalTitle').textContent=id?'Edit Creative':'Add Creative';
  const sel=document.getElementById('cr_adset');
  sel.innerHTML=db.adsets.map(a=>\`<option value="\${a.id}">\${a.name}</option>\`).join('');
  const cr=id?db.creatives.find(x=>x.id===id):{};
  document.getElementById('cr_name').value=cr?.name||'';
  document.getElementById('cr_name').oninput=function(){ document.getElementById('cr_format').value=detectFormat(this.value,''); };
  if(cr?.adsetId) sel.value=cr.adsetId;
  document.getElementById('cr_format').value=detectFormat(cr?.name||'',cr?.format||'');
  document.getElementById('cr_status').value=cr?.status||'Active';
  document.getElementById('cr_hookrate').value=cr?.hookrate||'';
  document.getElementById('cr_ctr').value=cr?.ctr||'';
  document.getElementById('cr_spend').value=cr?.spend||'';
  document.getElementById('cr_leads').value=cr?.leads||'';
  document.getElementById('cr_cpc').value=cr?.cpc||'';
  document.getElementById('cr_thumb').value=cr?.thumbUrl||'';
  document.getElementById('cr_hook').value=cr?.hook||'';
  document.getElementById('cr_notes').value=cr?.notes||'';
  openModal('crModal');
}
function saveCreative(){
  const name=document.getElementById('cr_name').value.trim();
  if(!name){alert('Name required');return;}
  const fmt=detectFormat(name,document.getElementById('cr_format').value);
  const data={name,adsetId:document.getElementById('cr_adset').value,format:fmt,status:document.getElementById('cr_status').value,hookrate:parseFloat(document.getElementById('cr_hookrate').value)||0,ctr:parseFloat(document.getElementById('cr_ctr').value)||0,spend:parseFloat(document.getElementById('cr_spend').value)||0,leads:parseInt(document.getElementById('cr_leads').value)||0,cpc:parseFloat(document.getElementById('cr_cpc').value)||0,thumbUrl:document.getElementById('cr_thumb').value.trim(),hook:document.getElementById('cr_hook').value,notes:document.getElementById('cr_notes').value};
  if(editId.creative){Object.assign(db.creatives.find(c=>c.id===editId.creative),data);}
  else db.creatives.push({...data,id:uid()});
  saveDB(); renderCreatives(); renderOverview(); closeModal('crModal');
}

/* ═══════════════════════════════════════════
   MODALS — LEAD
═══════════════════════════════════════════ */
function openLeadModal(id){
  editId.lead=id||null;
  document.getElementById('leadModalTitle').textContent=id?'Edit Lead':'Add Lead';
  const sel=document.getElementById('ld_sourceAd');
  sel.innerHTML='<option value="">— Not linked —</option>'+db.creatives.map(c=>\`<option value="\${c.id}">\${c.name}</option>\`).join('');
  const l=id?db.leads.find(x=>x.id===id||x.ghlId===id):{};
  document.getElementById('ld_name').value=l?.name||'';
  document.getElementById('ld_contact').value=l?.contact||'';
  document.getElementById('ld_source').value=l?.source||'Meta';
  if(l?.sourceAdId) sel.value=l.sourceAdId;
  document.getElementById('ld_status').value=l?.status||'New';
  document.getElementById('ld_proptype').value=l?.proptype||'';
  document.getElementById('ld_budget').value=l?.budget||'';
  document.getElementById('ld_date').value=l?.date||'';
  document.getElementById('ld_appt').value=l?.appt||'';
  document.getElementById('ld_notes').value=l?.notes||'';
  document.getElementById('ld_quality').value=l?.quality||'';
  document.getElementById('ld_urgencyTimeline').value=normaliseUrgency(l?.urgencyTimeline);
  document.getElementById('ld_dealValue').value=l?.dealValue||'';
  openModal('leadModal');
}
async function saveLead(){
  const name=document.getElementById('ld_name').value.trim(); if(!name){alert('Name required');return;}
  const sel=document.getElementById('ld_sourceAd'), srcId=sel.value, srcCr=db.creatives.find(c=>c.id===srcId);
  const dealValue=Math.max(0,num(document.getElementById('ld_dealValue').value));
  const data={name,contact:document.getElementById('ld_contact').value,source:document.getElementById('ld_source').value,platform:document.getElementById('ld_source').value,sourceAdId:srcId,sourceAdName:srcCr?.name||'',campaignName:srcCr?.campaignName||'',status:dealValue>0?'Closed':document.getElementById('ld_status').value,proptype:document.getElementById('ld_proptype').value,budget:document.getElementById('ld_budget').value,date:normaliseDateOnly(document.getElementById('ld_date').value),appt:document.getElementById('ld_appt').value,notes:document.getElementById('ld_notes').value,quality:document.getElementById('ld_quality').value,urgencyTimeline:normaliseUrgency(document.getElementById('ld_urgencyTimeline').value),dealValue};
  if(data.status==='Closed'&&!editId.lead) data.closedDate=new Date().toISOString().slice(0,10);
  let lead;
  if(editId.lead){lead=db.leads.find(l=>l.id===editId.lead||l.ghlId===editId.lead);Object.assign(lead,data);}else{lead={...data,id:uid()};db.leads.push(lead);}
  saveDB(); renderAll(); closeModal('leadModal'); await persistLeadRecord(lead,true); showToast('Lead saved ✓');
}

/* ═══════════════════════════════════════════
   MODALS — LOG
═══════════════════════════════════════════ */
function _prefillLogReason(cr){
  if(!cr) return;
  const s=db.settings;
  const hook=parseFloat(cr._hookrate||cr.hookrate)||0;
  const cpl=parseFloat(cr._cpl||cr.cpl)||0;
  const spend=parseFloat(cr._spend||cr.spend)||0;
  const leads=parseInt(cr._leads||cr.leads)||0;
  const kH=parseFloat(s.killHook)||25, scH=parseFloat(s.scaleHook)||35;
  const kC=parseFloat(s.killCPL)||200, scC=parseFloat(s.scaleCPL)||80;
  const kSp=parseFloat(s.killSpend)||150, minL=parseInt(s.minLeads)||3;
  const reasons=[];
  let action='Scale';
  if(hook<kH&&hook>0) reasons.push('Hook '+hook.toFixed(1)+'% < Kill threshold '+kH+'%');
  if(cpl>kC&&cpl>0) reasons.push('CPL SGD'+cpl.toFixed(0)+' > Kill threshold SGD'+kC);
  if(spend>=kSp&&leads<minL) reasons.push('Spent SGD'+spend.toFixed(0)+' with only '+leads+' lead(s)');
  if(reasons.length){ action='Kill'; }
  else {
    if(hook>=scH) reasons.push('Hook '+hook.toFixed(1)+'% >= Scale threshold '+scH+'%');
    if(cpl>0&&cpl<scC) reasons.push('CPL SGD'+cpl.toFixed(0)+' < Scale target SGD'+scC);
    if(!reasons.length) reasons.push('Review performance data before deciding');
  }
  const actEl=document.getElementById('log_action');
  if(actEl) actEl.value=action;
  const rEl=document.getElementById('log_reason');
  if(rEl) rEl.value=reasons.join('. ');
}
function openLogModal(crId){
  const sel=document.getElementById('log_ad');
  sel.innerHTML=db.creatives.map(c=>\`<option value="\${c.id}">\${c.name}</option>\`).join('');
  if(crId) sel.value=crId;
  document.getElementById('log_date').value=new Date().toISOString().slice(0,10);
  // v8.12: pre-fill action + reason from ad metrics
  const initCr=crId?db.creatives.find(c=>c.id===crId):(db.creatives[0]||null);
  _prefillLogReason(initCr);
  sel.onchange=function(){ _prefillLogReason(db.creatives.find(c=>c.id===this.value)||null); };
  openModal('logModal');
}
function logAction(crId){ openLogModal(crId); }
function saveLogEntry(){
  const adId=document.getElementById('log_ad').value;
  const cr=db.creatives.find(c=>c.id===adId);
  const entry={id:uid(),adId,adName:cr?.name||'',action:document.getElementById('log_action').value,date:document.getElementById('log_date').value,spend:parseFloat(document.getElementById('log_spend').value)||parseFloat(cr?.spend)||0,leads:parseInt(cr?.leads)||0,hookrate:parseFloat(cr?.hookrate)||0,reason:document.getElementById('log_reason').value};
  db.killScaleLog.push(entry);
  saveDB(); renderLog(); closeModal('logModal');
}

/* ═══════════════════════════════════════════
   LIGHTBOX
═══════════════════════════════════════════ */
/* v8.3: openLightbox — supports Meta CDN video via Facebook embed iframe */
function extractYouTubeIdClient(raw){
  const s=String(raw||'').trim();
  if(/^[A-Za-z0-9_-]{11}$/.test(s)) return s;
  const q=s.match(/[?&]v=([A-Za-z0-9_-]{11})/);
  if(q) return q[1];
  const markers=['youtu.be/','/shorts/','/embed/','/vi/'];
  for(const marker of markers){
    const idx=s.indexOf(marker);
    if(idx>=0){
      const id=s.slice(idx+marker.length).split(/[?&#/]/)[0];
      if(/^[A-Za-z0-9_-]{11}$/.test(id)) return id;
    }
  }
  return '';
}
function openLightbox(thumbUrl,format,name,videoId,imageUrl,videoSrc,adPermalink,platform){
  const hiRes=imageUrl||thumbUrl, img=document.getElementById('lboxImg'), vid=document.getElementById('lboxVid'), box=document.getElementById('lightbox');
  document.getElementById('lboxName').textContent=name||'';
  ['lboxIframe','lboxVidThumb'].forEach(id=>{const x=document.getElementById(id);if(x)x.remove();});
  img.style.display='none'; vid.style.display='none';
  const fmtLower=String(format||'').toLowerCase();
  const yt=extractYouTubeIdClient(videoId)||extractYouTubeIdClient(videoSrc)||extractYouTubeIdClient(thumbUrl)||extractYouTubeIdClient(imageUrl);
  const sourceHref=videoSrc||adPermalink||(yt?'https://www.youtube.com/watch?v='+encodeURIComponent(yt):'');
  const looksYoutube=platform==='Google'||!!yt||/youtu/i.test(String(sourceHref||''));
  if((fmtLower==='video'||looksYoutube)&&looksYoutube){
    const wrap=document.createElement('div'); wrap.id='lboxIframe'; wrap.style.cssText='width:min(860px,88vw);';
    if(yt){
      const watch='https://www.youtube.com/watch?v='+encodeURIComponent(yt);
      const poster=thumbUrl||imageUrl||('https://i.ytimg.com/vi/'+encodeURIComponent(yt)+'/hqdefault.jpg');
      wrap.innerHTML='<div style="position:relative;background:#000;border-radius:10px;overflow:hidden;text-align:center">'+
        (poster?'<img src="'+poster+'" style="width:100%;max-height:62vh;object-fit:contain;opacity:.72">':'<div style="height:360px;background:#111"></div>')+
        '<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px;padding:24px">'+
        '<a href="'+watch+'" target="_blank" rel="noopener" style="background:#ff0000;color:#fff;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:900">▶ Play on YouTube</a>'+
        '<div style="color:#fff;font-size:12px;max-width:520px">YouTube embeds can be blocked by video/privacy settings. This opens the real YouTube page, which is the reliable playback path.</div>'+
        '</div></div>';
      const link=document.createElement('a'); link.href='https://www.youtube.com/watch?v='+encodeURIComponent(yt); link.target='_blank'; link.rel='noopener'; link.textContent='Open on YouTube ↗'; link.style.cssText='display:block;color:#fff;text-align:center;margin-top:9px'; wrap.appendChild(link);
    }else{wrap.innerHTML='<div style="padding:80px 24px;text-align:center;background:#111;color:#fff;border-radius:10px">'+(sourceHref?'<a href="'+sourceHref+'" target="_blank" rel="noopener" style="background:#1877f2;color:#fff;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:900">Open source/ad link</a><div style="font-size:12px;color:#ddd;margin-top:12px">No public YouTube ID is available for this creative.</div>':'No playable video URL is available yet. Refresh Google Ads Script v7 / Meta sync to repopulate video assets.')+'</div>';}
    document.querySelector('.lbox-content').insertBefore(wrap,document.getElementById('lboxName'));
  }else if(String(format).toLowerCase()==='video'){
    const href=adPermalink||videoSrc||(videoId?'https://www.facebook.com/watch/?v='+videoId:'');
    const wrap=document.createElement('div'); wrap.id='lboxVidThumb'; wrap.style.cssText='position:relative;max-width:640px;width:100%;border-radius:8px;overflow:hidden;background:#000;';
    wrap.innerHTML=(hiRes?'<img src="'+hiRes+'" style="width:100%;display:block;max-height:72vh;object-fit:contain;opacity:.82">':'<div style="height:360px;background:#111"></div>')+'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">'+(href?'<a href="'+href+'" target="_blank" rel="noopener" style="background:#1877f2;color:#fff;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:800">▶ Play on Facebook</a>':'<span style="color:#fff">No video URL available</span>')+'</div>';
    document.querySelector('.lbox-content').insertBefore(wrap,document.getElementById('lboxName'));
  }else if(hiRes){img.style.display='';img.src=hiRes;img.style.minWidth='min(640px,85vw)';}
  box.classList.add('open');
}
function closeLightbox(){
  document.getElementById('lightbox').classList.remove('open');
  document.getElementById('lboxVid').src='';
  const prev=document.getElementById('lboxIframe'); if(prev) prev.remove();
  const prev2=document.getElementById('lboxVidThumb'); if(prev2) prev2.remove();
}

/* ═══════════════════════════════════════════
   MODAL HELPERS
═══════════════════════════════════════════ */
function openModal(id){
  const el=document.getElementById(id);
  if(!el) return;
  if(el._escH){ document.removeEventListener('keydown',el._escH); el._escH=null; }
  if(el._outsideH){ el.removeEventListener('click',el._outsideH); el._outsideH=null; }
  el.classList.add('open');
  el._escH=function(e){ if(e.key==='Escape') closeModal(id); };
  el._outsideH=function(e){ if(e.target===el) closeModal(id); };
  document.addEventListener('keydown',el._escH);
  el.addEventListener('click',el._outsideH);
}
function closeModal(id){ const el=document.getElementById(id); if(!el) return; el.classList.remove('open'); if(el._escH){ document.removeEventListener('keydown',el._escH); el._escH=null; } if(el._outsideH){ el.removeEventListener('click',el._outsideH); el._outsideH=null; } }
function confirmDelete(type,id){
  document.getElementById('delText').textContent=\`Delete this \${type}? This cannot be undone.\`;
  document.getElementById('delConfirmBtn').onclick=async ()=>{
    if(type==='campaign') db.campaigns=db.campaigns.filter(x=>x.id!==id);
    else if(type==='adset') db.adsets=db.adsets.filter(x=>x.id!==id);
    else if(type==='creative') db.creatives=db.creatives.filter(x=>x.id!==id);
    else if(type==='lead'){
      const lead=db.leads.find(x=>x.id===id||x.ghlId===id);
      db.leads=db.leads.filter(x=>x.id!==id&&x.ghlId!==id);
      saveDB(); renderAll(); closeModal('delModal');
      if(lead?.ghlId&&db.settings.webAppUrl){
        showToast('Deleting from sheet & GHL…');
        try{
          const r=await fetch(db.settings.webAppUrl+'?action=deletelead&ghlId='+encodeURIComponent(lead.ghlId),{redirect:'follow'});
          const d=await r.json();
          if(d.ok){
            showToast('Deleted'+(d.ghlDeleted?' from sheet & GHL':' from sheet')+'  ✓');
          } else if((d.error||'').toLowerCase().includes('unknown action')){
            showToast('⚠ GAS not re-deployed — Apps Script → Deploy → Manage → New version','error');
          } else {
            showToast('Sync failed: '+(d.error||'error'),'error');
          }
        }catch(ex){showToast('Local deleted; network error — check GAS deployment','error');}
      }
      return;
    }
    else if(type==='log') db.killScaleLog=db.killScaleLog.filter(x=>x.id!==id);
    saveDB(); renderAll(); closeModal('delModal');
  };
  openModal('delModal');
}

/* ═══════════════════════════════════════════
   SETTINGS
═══════════════════════════════════════════ */
function populateSettings(){
  const s=db.settings;
  document.getElementById('s_sheetId').value=s.sheetId||'';
  document.getElementById('s_ghlLoc').value=s.ghlLocationId||'';
  document.getElementById('s_sgd').value=s.sgdRate||1.35;
  document.getElementById('s_killHook').value=s.killHook||25;
  document.getElementById('s_scaleHook').value=s.scaleHook||35;
  document.getElementById('s_killCPL').value=s.killCPL||200;
  document.getElementById('s_scaleCPL').value=s.scaleCPL||80;
  document.getElementById('s_killSpend').value=s.killSpend||150;
  document.getElementById('s_minLeads').value=s.minLeads||3;
}
function updateThrInfo(){
  document.getElementById('thrInfo').textContent=\`Hook Kill: \${db.settings.killHook||25}% | Scale: \${db.settings.scaleHook||35}% | CPL Kill: SGD \${db.settings.killCPL||200}\`;
}
function confirmClearAll(){
  if(confirm('Clear ALL data? This cannot be undone.')){
    db=JSON.parse(JSON.stringify(DEFAULT_DB)); saveDB(); renderAll();
  }
}

/* ═══════════════════════════════════════════
   THEME
═══════════════════════════════════════════ */
let manualThemeUntil=0;
function singaporeHour(){ return Number(new Intl.DateTimeFormat('en-GB',{timeZone:'Asia/Singapore',hour:'2-digit',hourCycle:'h23'}).format(new Date())); }
function applyAutoTheme(force=false){
  if(!force&&Date.now()<manualThemeUntil)return;
  const dark=singaporeHour()>=19||singaporeHour()<7, d=document.documentElement;
  d.setAttribute('data-theme',dark?'dark':'light');
  const b=document.getElementById('themeBtn'); if(b)b.textContent=dark?'☀️':'🌙';
}
function toggleTheme(){
  const d=document.documentElement, dark=d.getAttribute('data-theme')==='dark';
  d.setAttribute('data-theme',dark?'light':'dark'); manualThemeUntil=Date.now()+4*60*60*1000;
  const b=document.getElementById('themeBtn'); if(b)b.textContent=dark?'🌙':'☀️';
}
function syncStickyOffsets(){
  const hdr=document.querySelector('.hdr'), gbar=document.querySelector('.gbar'), tabs=document.querySelector('.tabs'), leadPanel=document.querySelector('#page-leads .lead-sticky-panel');
  const h=hdr?hdr.offsetHeight:58, g=gbar?gbar.offsetHeight:46, t=tabs?tabs.offsetHeight:44, lp=leadPanel?leadPanel.offsetHeight:0;
  document.documentElement.style.setProperty('--hdr-h',h+'px');
  document.documentElement.style.setProperty('--gbar-h',g+'px');
  document.documentElement.style.setProperty('--tabs-top',(h+g)+'px');
  document.documentElement.style.setProperty('--content-top',(h+g+t)+'px');
  document.documentElement.style.setProperty('--lead-panel-h',lp+'px');
}

/* ═══════════════════════════════════════════
   SYNC STATUS
═══════════════════════════════════════════ */
function setSyncStatus(state,label){
  const dot=document.getElementById('syncDot');
  const lbl=document.getElementById('syncLabel');
  dot.className='sync-dot '+state;
  if(lbl) lbl.textContent=label||'';
}

/* ═══════════════════════════════════════════
   EXPORT / IMPORT
═══════════════════════════════════════════ */
function exportJSON(){
  const a=document.createElement('a');
  a.href='data:application/json,'+encodeURIComponent(JSON.stringify(db,null,2));
  a.download='REI_backup_'+new Date().toISOString().slice(0,10)+'.json';
  a.click();
}
function importJSON(e){
  const f=e.target.files[0]; if(!f) return;
  const r=new FileReader();
  r.onload=ev=>{try{const d=JSON.parse(ev.target.result);db=Object.assign({},DEFAULT_DB,d);db.settings=Object.assign({},DEFAULT_DB.settings,d.settings||{});saveDB();renderAll();showToast('Imported ✓');}catch(err){showToast('Import failed','error');}};
  r.readAsText(f);
}

/* Import GHL Leads file — merges leads from { leads:[...], total:N, synced:"" }
   format (produced by Claude MCP bridge). Does NOT overwrite any other data. */
function importLeadsJSON(e){
  const f=e.target.files[0]; if(!f) return;
  const r=new FileReader();
  r.onload=ev=>{
    try{
      const data=JSON.parse(ev.target.result);
      const leadsArr=data.leads||data; // accept array or wrapped object
      if(!Array.isArray(leadsArr)) throw new Error('Expected leads array');
      let added=0,updated=0;
      leadsArr.forEach(l=>{
        const ex=db.leads.find(x=>x.ghlId&&l.ghlId&&x.ghlId===l.ghlId);
        if(ex){
          if(l.status&&l.status!==ex.status){ex.status=l.status;updated++;}
        } else {
          db.leads.push({...l,id:uid(),status:l.status||'New'});
          added++;
        }
      });
      saveDB();renderAll();
      showToast(\`GHL Leads imported: \${added} new, \${updated} updated ✓\`);
    }catch(err){showToast('GHL Leads import failed: '+err.message,'error');}
  };
  r.readAsText(f);
}
function exportCSV(){
  const rows=[['Ad Name','Ad Set','Campaign','Platform','Format','Hook%','CTR%','CPC','Leads','Qual','Appts','Spend','CPL','$/Qual','$/Appt','L→Q%','Q→A%','Signal','Status']];
  db.creatives.forEach(cr=>{
    const _asName=getAsName(cr.adsetId);
    const _campName=getCampName(getAsCampId(cr.adsetId));
    const sp=parseFloat(cr.spend)||0,ld=parseInt(cr.leads)||0;
    const cpl=ld>0?sp/ld:0;
    const linked=db.leads.filter(l=>(l.sourceAdId&&l.sourceAdId===cr.metaId)||(l.sourceAdName&&l.sourceAdName===cr.name));
    const ql=linked.filter(l=>['Qualified','Booked','Closed'].includes(l.status)).length;
    const ap=linked.filter(l=>!!l.appt).length;
    rows.push([cr.name,_asName,_campName,cr.platform||'Meta',cr.format||'Video',cr.hookrate||0,cr.ctr||0,cr.cpc||0,ld,ql,ap,sp.toFixed(2),cpl.toFixed(2),ql>0?(sp/ql).toFixed(2):'',ap>0?(sp/ap).toFixed(2):'',ld>0?((ql/ld)*100).toFixed(1):'',ql>0?((ap/ql)*100).toFixed(1):'',getSignal({_hookrate:cr.hookrate,_cpl:cpl,_spend:sp,_leads:ld}),cr.status||'Active']);
  });
  const csv=rows.map(r=>r.map(v=>\`"\${String(v).replace(/"/g,'""')}"\`).join(',')).join('\\n');
  const a=document.createElement('a');
  a.href='data:text/csv,'+encodeURIComponent(csv);
  a.download='REI_creatives_'+new Date().toISOString().slice(0,10)+'.csv';
  a.click();
}

/* ═══════════════════════════════════════════
   TOAST
═══════════════════════════════════════════ */
function showToast(msg,type='ok'){
  const t=document.createElement('div');
  t.style.cssText=\`position:fixed;bottom:24px;right:24px;background:\${type==='ok'?'#16A34A':type==='warn'?'#D97706':'#DC2626'};color:#fff;padding:10px 18px;border-radius:8px;font-size:13px;z-index:9999;box-shadow:0 4px 14px rgba(0,0,0,.25);animation:fadein .2s\`;
  t.textContent=msg;
  document.body.appendChild(t);
  setTimeout(()=>t.remove(),3000);
}

/* ═══════════════════════════════════════════
   ESCAPE HELPER
═══════════════════════════════════════════ */
function esc(s){ return String(s||'').replace(/'/g,"\\\\'").replace(/"/g,'&quot;'); }

/* ═══════════════════════════════════════════
   INIT
═══════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', async ()=>{
  applyAutoTheme(true); setInterval(()=>applyAutoTheme(false),600000);
  syncStickyOffsets(); window.addEventListener('resize',syncStickyOffsets);
  window.__log('DOM ready');
  try{ loadDB();           window.__log('loadDB ok'); }           catch(e){ window.__log('loadDB: '+e.message,true); }
  try{ renderAll(); syncStickyOffsets(); window.__log('renderAll ok'); }        catch(e){ window.__log('renderAll: '+e.message,true); }
  try{ updateThrInfo();    window.__log('updateThrInfo ok'); }    catch(e){ window.__log('updateThrInfo: '+e.message,true); }
  try{ populateSettings(); window.__log('popSettings ok'); }      catch(e){ window.__log('popSettings: '+e.message,true); }
  const url = db.settings.webAppUrl;
  window.__log('url: '+(url||'[NONE]'), !url);
  if(url){
    await syncDataFast();
    try{ startAutoGhlSync(); window.__log('auto GHL sync armed'); }catch(e){ console.warn(e); }
    return;
    setSyncStatus('syncing','Syncing Meta data…');
    try{
      window.__log('fetch syncmeta...');
      const r1=await fetch(\`\${url}?action=syncmeta\`,{redirect:'follow'});
      window.__log('syncmeta HTTP '+r1.status, !r1.ok);
      if(!r1.ok) throw new Error(\`HTTP \${r1.status}\`);
      const d1=await r1.json();
      if(d1.error) throw new Error(d1.error);
      window.__log('syncmeta ok');
    }catch(e){
      window.__log('syncmeta fail: '+e.message,true);
      showToast('Meta sync: '+e.message,'warn');
    }
    // v8.16: auto-sync GHL pipeline on every page load
    try{
      window.__log('fetch syncghl...');
      setSyncStatus('syncing','Syncing GHL pipeline…');
      const rg=await fetch(\`\${url}?action=syncghl\`,{redirect:'follow'});
      window.__log('syncghl HTTP '+rg.status, !rg.ok);
      if(!rg.ok) throw new Error(\`HTTP \${rg.status}\`);
      const dg=await rg.json();
      if(dg.error) throw new Error(dg.error);
      window.__log('syncghl ok: '+(dg.total||0)+' leads');
      setSyncStatus('syncing','Loading data from sheets…');
    }catch(e){
      window.__log('syncghl fail: '+e.message,true);
      showToast('GHL sync: '+e.message,'warn');
    }
    try{
      window.__log('fetch getfromsheets...');
      const r2=await fetch(\`\${url}?action=getfromsheets&preset=\${encodeURIComponent(currentDatePreset)}\`,{redirect:'follow'});
      window.__log('getfromsheets HTTP '+r2.status, !r2.ok);
      if(!r2.ok) throw new Error(\`HTTP \${r2.status}\`);
      const d2=await r2.json();
      window.__log('parsed: c='+(d2.campaigns||[]).length+' l='+(d2.leads||[]).length);
      if(d2.error) throw new Error(d2.error);
      try{ mergeApiData(d2); window.__log('merge ok'); }catch(e){ window.__log('merge: '+e.message,true); throw e; }
      saveDB();
      try{ renderAll(); window.__log('render ok'); }catch(e){ window.__log('render: '+e.message,true); throw e; }
      setSyncStatus('ok','Synced '+new Date().toLocaleTimeString());
      showToast('Dashboard synced ✓');
    }catch(e){
      window.__log('getfromsheets fail: '+e.message,true);
      setSyncStatus('err','Load failed');
      showToast('Load from sheets failed: '+e.message,'error');
    }
    try{ startAutoGhlSync(); window.__log('auto GHL sync armed'); }catch(e){ console.warn(e); }
  } else {
    window.__log('no url - skipped',true);
  }
});
`;
}

