/** REI Performance OS v9.0 — ALL-IN-ONE SERVER SOURCE
 * Generated from modular source files. Use either this file OR the numbered .gs files, not both.
 */

// ==================== 00_Config.gs ====================
/**
 * REI Performance OS v9.0 — Configuration and shared helpers.
 * Mobile-first, account-neutral Apps Script web app.
 */
const APP = Object.freeze({
  VERSION: '9.15.0',
  NAME: 'REI Performance OS',
  TZ: 'Asia/Singapore',
  MASTER_SHEET_ID: '167C_gZsN5RtImBFArt5hXcUqMAHlfJFqX52f0rN_pWk',
  CACHE_SECONDS: 120,
  MAX_RECENT_LEADS: 100,
  DEFAULT_META_DAYS: 90,
  DEFAULT_GHL_PAGE_LIMIT: 100,
  TABS: Object.freeze({
    PERFORMANCE: 'Daily_Performance_Fact',
    FUNNEL: 'Daily_Funnel_Fact',
    ASSUMPTIONS: 'Forecast_Assumptions',
    SCENARIOS: 'Forecast_Scenarios',
    FORECAST: 'Forecast_Output',
    ACTUAL: 'Forecast_vs_Actual',
    STAGES: 'Stage_Map',
    SYNC_LOG: 'Sync_Log',
    ERROR_LOG: 'Error_Log',
    AUDIT_LOG: 'Audit_Log',
    HEALTH: 'Health_Check',
    CONFIG: 'Config_v9',
    GHL: 'GHL_Leads',
    META_CAMPAIGNS: 'Meta_Campaigns',
    META_ADSETS: 'Meta_AdSets',
    META_ADS: 'Meta_Ads',
    GOOGLE_DAILY: 'Google_Campaigns_Daily',
    INVESTMENTS: 'Investments'
  })
});

/**
 * Internal stage ladder. Order defines rank, so a lead at 'Booked Call' counts as
 * having passed 'Responded'.
 *
 * NOTE — 'Appt Qualified' does NOT exist in the live GHL 1-To-1 Pipeline
 * (New Lead > Responded > Booked Call > Appointment > Strategy Session > Close >
 * Nurture > Unqualified). Nothing reaches it except records that are already Closed,
 * which is why the dashboard reported Qualified and Closed as the same number. It is
 * retained here only so Daily_Funnel_Fact and the forecaster keep a stable schema, and
 * is deliberately NOT shown as a headline metric. If a real qualification stage is ever
 * added in GHL, map it in normaliseStage_ and surface it again.
 */
const CANONICAL_STAGES = Object.freeze([
  'New', 'Contacted', 'Responded', 'Booked Call', 'Appointment',
  'Nurture', 'Strategy Session', 'Appt Qualified', 'Closed', 'Lost'
]);

const TAB_HEADERS = Object.freeze({
  Daily_Performance_Fact: [
    'date','platform','accountId','campaignId','campaignName','adSetId','adSetName',
    'adId','adName','objective','status','spend','impressions','reach','clicks',
    'linkClicks','leads','conversions','conversionValue','ctr','cpc','cpl',
    'sourceUpdatedAt','syncRunId'
  ],
  Daily_Funnel_Fact: [
    'date','platform','campaignId','campaignName','newLeads','contacted','responded',
    'bookedCalls','appointments','strategySessions','qualified','closedWon','closedLost',
    'revenue','sourceUpdatedAt','syncRunId','attributionConfidence','notes'
  ],
  Sync_Log: [
    'timestamp','syncRunId','service','status','startedAt','completedAt','durationSeconds',
    'recordsRead','recordsWritten','dateFrom','dateTo','message','triggerType','version'
  ],
  Error_Log: [
    'timestamp','syncRunId','service','function','severity','message','httpCode','responseSnippet',
    'stack','context','triggerType','version'
  ],
  Audit_Log: [
    'timestamp','actor','action','entityType','entityId','oldValue','newValue','source',
    'requestId','result','version'
  ],
  /* Non-advertising money: masterminds, mentorship, coaching. Hand-entered in the sheet
     rather than through the dashboard, because the web app is deployed to ANYONE_ANONYMOUS
     and must never be able to write financial records. `date` is optional — an annual
     mastermind fee has no meaningful single date, so `year` alone is enough. */
  Investments: [
    'year','date','category','vendor','description','amount','notes'
  ]
});

function getMasterSheetId_() {
  return PropertiesService.getScriptProperties().getProperty('SHEET_ID') || APP.MASTER_SHEET_ID;
}

function getMasterSpreadsheet_() {
  return SpreadsheetApp.openById(getMasterSheetId_());
}

function getSheet_(name, createIfMissing) {
  const ss = getMasterSpreadsheet_();
  let sheet = ss.getSheetByName(name);
  if (!sheet && createIfMissing) sheet = ss.insertSheet(name);
  return sheet;
}

function prop_(name, fallback) {
  const value = PropertiesService.getScriptProperties().getProperty(name);
  return value === null || value === '' ? fallback : value;
}

function nowIso_() { return new Date().toISOString(); }

/**
 * Normalise a date cell to yyyy-MM-dd for use in upsert keys.
 *
 * Sheets silently converts an ISO date STRING into a real Date VALUE on write, so the
 * same row reads back as a Date object. Building an upsert key with safeText_ therefore
 * produced "2026-07-21" for incoming rows but "Mon Jul 21 2026 00:00:00 GMT+0800..."
 * for stored ones — the keys never matched, so every re-sync APPENDED duplicates rather
 * than replacing. That is what inflated total spend (dashboard read $107k against
 * $79k in Meta's own export) and multiplied lead counts on repeated backfill runs.
 */
function dayKey_(value) {
  if (value instanceof Date) return Utilities.formatDate(value, APP.TZ, 'yyyy-MM-dd');
  return safeText_(value).slice(0, 10);
}

/**
 * Context-safe alert. SpreadsheetApp.getUi() only exists when the script is run
 * from the spreadsheet UI — calling it from the script editor or a time-based
 * trigger throws "Cannot call SpreadsheetApp.getUi() from this context" and kills
 * the run. Setup and the *FromEditor helpers are meant to be runnable from the
 * editor, so their messages fall back to the execution log instead of dying.
 * Note: promptProperty_ still uses getUi() directly — it needs a real input
 * dialog, so credential entry must be done from the sheet menu.
 */
function uiAlert_(message) {
  try { SpreadsheetApp.getUi().alert(message); }
  catch (e) { console.log(message); }
}

function sgtDate_(date) {
  return Utilities.formatDate(date || new Date(), APP.TZ, 'yyyy-MM-dd');
}

function addDaysIso_(isoDate, delta) {
  const parts = String(isoDate).split('-').map(Number);
  const d = new Date(Date.UTC(parts[0], parts[1] - 1, parts[2], 12));
  d.setUTCDate(d.getUTCDate() + delta);
  return Utilities.formatDate(d, 'UTC', 'yyyy-MM-dd');
}

function asNumber_(value) {
  const n = Number(String(value === null || value === undefined ? '' : value).replace(/,/g, ''));
  return isFinite(n) ? n : 0;
}

function safeText_(value) { return value === null || value === undefined ? '' : String(value); }

function normaliseName_(value) {
  return safeText_(value).toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
}

function statusRank_(status) {
  const idx = CANONICAL_STAGES.indexOf(normaliseStage_(status));
  return idx < 0 ? 0 : idx;
}

function normaliseStage_(value) {
  const key = safeText_(value).toLowerCase().replace(/[_-]+/g, ' ').replace(/\s+/g, ' ').trim();
  const aliases = {
    'new lead':'New','new':'New','signup':'New',
    'attempting contact':'Contacted','contacted':'Contacted',
    /* Nurture is a POST-appointment holding bucket: the lead attended, did not move
       forward, and is kept for future follow-up. Mapping it to 'Contacted' ranked it
       below Booked Call and quietly erased an attended appointment from the funnel.
       It sits after Appointment and before Strategy Session, which is where it belongs. */
    'nurture':'Nurture','nurturing':'Nurture','follow up':'Nurture','followup':'Nurture',
    'responded':'Responded','reply':'Responded','replied':'Responded',
    'booked call':'Booked Call','booked calls':'Booked Call','book call':'Booked Call',
    'call booked':'Booked Call','booking':'Booked Call','booked':'Booked Call',
    'booked appointment':'Booked Call','appointment booked':'Booked Call',
    'diagnosis call booked':'Booked Call',
    'appointment':'Appointment','showed':'Appointment','show':'Appointment',
    'strategy session booked':'Strategy Session','strategy session':'Strategy Session',
    'implementation opportunity':'Appt Qualified','attended':'Appt Qualified',
    'appt qualified':'Appt Qualified','qualified':'Appt Qualified',
    'close':'Closed','closed':'Closed','won':'Closed','closed won':'Closed',
    'unqualified':'Lost','lost':'Lost','closed lost':'Lost'
  };
  return aliases[key] || (CANONICAL_STAGES.indexOf(value) >= 0 ? value : 'New');
}

function makeRunId_(prefix) {
  return (prefix || 'run') + '-' + Utilities.formatDate(new Date(), APP.TZ, 'yyyyMMdd-HHmmss') + '-' + Utilities.getUuid().slice(0, 8);
}

function constantTimeEqual_(a, b) {
  a = safeText_(a); b = safeText_(b);
  let mismatch = a.length ^ b.length;
  const len = Math.max(a.length, b.length);
  for (let i = 0; i < len; i++) mismatch |= (a.charCodeAt(i % Math.max(1, a.length)) || 0) ^ (b.charCodeAt(i % Math.max(1, b.length)) || 0);
  return mismatch === 0;
}

function assertAccess_(accessKey) {
  // v9.0.1: direct-link mode. The web app has no dashboard access-key gate.
  return true;
}

function withScriptLock_(label, waitMs, fn) {
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(waitMs || 5000)) throw new Error((label || 'Operation') + ' is already running. Try again after the current sync finishes.');
  try { return fn(); } finally { lock.releaseLock(); }
}

/**
 * Chunked cache. CacheService caps a single value at ~100KB; the dashboard payload is
 * larger, so it is split across numbered keys with a companion count key. A partial or
 * expired chunk returns null so the caller rebuilds rather than parsing half a payload.
 */
function cachePut_(key, json, seconds) {
  const CHUNK = 80000, MAX_PARTS = 12;
  const parts = Math.ceil(json.length / CHUNK);
  if (parts > MAX_PARTS) return false;                 // implausibly large — skip caching
  const map = {};
  for (let i = 0; i < parts; i++) map[key + '::' + i] = json.substr(i * CHUNK, CHUNK);
  map[key + '::n'] = String(parts);
  CacheService.getScriptCache().putAll(map, seconds);
  return true;
}

function cacheGet_(key) {
  const cache = CacheService.getScriptCache();
  const n = cache.get(key + '::n');
  if (!n) return null;
  const parts = Number(n);
  if (!parts || parts < 1) return null;
  const keys = [];
  for (let i = 0; i < parts; i++) keys.push(key + '::' + i);
  const got = cache.getAll(keys);
  let out = '';
  for (let i = 0; i < parts; i++) {
    const piece = got[key + '::' + i];
    if (piece === undefined || piece === null) return null;   // a chunk expired — rebuild
    out += piece;
  }
  return out;
}

function clearDashboardCache_() {
  // Keys are now chunked ("<key>::0", "<key>::n"), and the real key also carries the
  // custom-date suffix. Dropping the "::n" count key alone is enough to invalidate an
  // entry, since cacheGet_ returns null without it — the orphaned chunks then expire
  // on their own TTL.
  const cache = CacheService.getScriptCache();
  const keys = [];
  ['today','7d','30d','90d','all'].forEach(k => {
    const base = 'dashboard:' + k + '::';
    keys.push(base + 'n');
    for (let i = 0; i < 12; i++) keys.push(base + i);
  });
  try { cache.removeAll(keys); } catch (e) { /* cache clearing is never fatal */ }
}

function sheetRowsAsObjects_(sheetName) {
  const sheet = getSheet_(sheetName, false);
  if (!sheet || sheet.getLastRow() < 2) return [];
  const values = sheet.getDataRange().getValues();
  const headers = values.shift().map(h => safeText_(h).trim());
  return values.filter(r => r.some(v => v !== '' && v !== null)).map(r => {
    const out = {};
    headers.forEach((h, i) => out[h] = r[i]);
    return out;
  });
}

function overwriteObjects_(sheetName, headers, objects) {
  const sheet = getSheet_(sheetName, true);
  sheet.clearContents();
  const rows = [headers].concat((objects || []).map(o => headers.map(h => o[h] === undefined ? '' : o[h])));
  sheet.getRange(1, 1, rows.length, headers.length).setValues(rows);
  sheet.setFrozenRows(1);
}

function upsertObjects_(sheetName, headers, objects, keyFn) {
  if (!objects || !objects.length) return 0;
  const sheet = getSheet_(sheetName, true);
  const existing = sheet.getLastRow() > 1 ? sheetRowsAsObjects_(sheetName) : [];
  const map = {};
  existing.forEach(o => map[keyFn(o)] = o);
  objects.forEach(o => map[keyFn(o)] = Object.assign({}, map[keyFn(o)] || {}, o));
  const merged = Object.keys(map).filter(Boolean).map(k => map[k]);
  merged.sort((a,b) => safeText_(a.date).localeCompare(safeText_(b.date)) || safeText_(a.platform).localeCompare(safeText_(b.platform)));
  overwriteObjects_(sheetName, headers, merged);
  return objects.length;
}

// ==================== 01_EntryPoints.gs ====================
/** Web app entry points. No public query-string write endpoints. */
function doGet() {
  const template = HtmlService.createTemplateFromFile('Dashboard');
  template.appName = APP.NAME;
  template.appVersion = APP.VERSION;
  return template.evaluate()
    .setTitle(APP.NAME + ' v' + APP.VERSION)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1, viewport-fit=cover')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.DEFAULT);
}

function include_(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}

function login(accessKey) {
  assertAccess_(accessKey);
  return { ok: true, appName: APP.NAME, version: APP.VERSION, serverTime: nowIso_() };
}

function getDashboardData(request) {
  request = request || {};
  assertAccess_(request.accessKey);
  const rangeKey = request.rangeKey || '30d';
  const cacheKey = 'dashboard:' + rangeKey + ':' + safeText_(request.customStart) + ':' + safeText_(request.customEnd);
  // Cache is an optimisation, never a requirement — a cache failure must never fail the
  // request. Values are chunked because CacheService rejects anything over ~100KB, and
  // the v9.1+ payload (per-ad rows, ad sets, pipeline) is well past that. Without
  // chunking every range switch rebuilt from ~2,800 sheet rows, which is why loading
  // each period felt slow.
  let cached = null;
  try { cached = cacheGet_(cacheKey); } catch (e) { cached = null; }
  if (cached && !request.force) {
    try { return JSON.parse(cached); } catch (e) { /* corrupt entry — rebuild below */ }
  }
  const payload = buildDashboardPayload_(rangeKey, request.customStart, request.customEnd);
  try { cachePut_(cacheKey, JSON.stringify(payload), APP.CACHE_SECONDS); } catch (e) { /* serve uncached */ }
  return payload;
}

function runManualSync(request) {
  request = request || {};
  assertAccess_(request.accessKey);
  return withScriptLock_('Manual sync', 1000, function() {
    const runId = makeRunId_('manual');
    const result = syncAllV9_(runId, 'manual');
    clearDashboardCache_();
    return result;
  });
}

function saveForecastScenario(request) {
  request = request || {};
  assertAccess_(request.accessKey);
  const values = request.values || {};
  const scenario = calculateOneForecast_(values);
  const sheet = getSheet_(APP.TABS.SCENARIOS, true);
  const headers = ['savedAt','scenarioName','forecastDays','budget','cpl','responseRate','bookingRate','showRate','qualificationRate','closeRate','averageCommission','collectionRate','variableCostPerClose','leads','responded','bookedCalls','shows','qualified','closings','collectedRevenue','netContribution'];
  if (sheet.getLastRow() === 0) sheet.appendRow(headers);
  sheet.appendRow(headers.map(h => h === 'savedAt' ? nowIso_() : h === 'scenarioName' ? (request.name || 'Custom') : (scenario[h] === undefined ? (values[h] === undefined ? '' : values[h]) : scenario[h])));
  appendAuditLog_('dashboard-user', 'SAVE_FORECAST', 'forecast', request.name || 'Custom', '', JSON.stringify(values), 'webapp', '', 'success');
  return scenario;
}

function getHealthData(request) {
  request = request || {};
  assertAccess_(request.accessKey);
  return buildHealthReport_(false);
}

// ==================== 02_DataService.gs ====================
/** Dashboard aggregation and fact-table maintenance. */
function resolveRange_(rangeKey, customStart, customEnd) {
  const today = sgtDate_(new Date());
  if (customStart && customEnd) return { start: customStart, end: customEnd, label: customStart + ' to ' + customEnd };
  if (rangeKey === 'today') return { start: today, end: today, label: 'Today' };
  if (rangeKey === '7d') return { start: addDaysIso_(today, -6), end: today, label: 'Last 7 days' };
  if (rangeKey === '90d') return { start: addDaysIso_(today, -89), end: today, label: 'Last 90 days' };
  if (rangeKey === 'all') return { start: '2000-01-01', end: today, label: 'All time' };
  return { start: addDaysIso_(today, -29), end: today, label: 'Last 30 days' };
}

function inDateRange_(dateValue, range) {
  const d = dateValue instanceof Date ? Utilities.formatDate(dateValue, APP.TZ, 'yyyy-MM-dd') : safeText_(dateValue).slice(0,10);
  return d && d >= range.start && d <= range.end;
}

function buildDashboardPayload_(rangeKey, customStart, customEnd) {
  const range = resolveRange_(rangeKey, customStart, customEnd);
  let perf = sheetRowsAsObjects_(APP.TABS.PERFORMANCE).filter(r => inDateRange_(r.date, range));
  if (!perf.length) {
    backfillGoogleDailyFact_();
    perf = sheetRowsAsObjects_(APP.TABS.PERFORMANCE).filter(r => inDateRange_(r.date, range));
  }
  const funnel = sheetRowsAsObjects_(APP.TABS.FUNNEL).filter(r => inDateRange_(r.date, range));
  const leads = readRecentLeadSummaries_(range, APP.MAX_RECENT_LEADS);
  const campaigns = aggregateCampaigns_(perf, funnel);
  const platforms = aggregatePlatforms_(perf, funnel);
  const overview = aggregateOverview_(perf, funnel);
  const forecast = getForecastData_();
  const health = buildHealthReport_(true);
  const funnelTotals = aggregateFunnel_(funnel);

  // v9.1 additions are individually fault-isolated. If one throws on unexpected data
  // it must not take the whole payload down with it — that returns an error to the
  // client and renders a blank dashboard, which is indistinguishable from "broken".
  // Failures degrade to empty and are surfaced as warnings instead.
  const warnings = [];
  const safely = function (label, fn, fallback) {
    try { return fn(); }
    catch (e) { warnings.push(label + ': ' + (e && e.message || e)); return fallback; }
  };
  const ads = safely('ads', function () { return aggregateAds_(perf); }, []);
  const adSets = safely('adSets', function () { return aggregateAdSets_(perf); }, []);
  const pipeline = safely('pipeline', function () { return buildPipelineByStage_(leads); }, []);
  const census = safely('census', function () { return buildStageCensus_(range); }, null);
  const stages = safely('stages', function () { return buildStageConversions_(funnelTotals, census); }, null);
  const investments = safely('investments', function () { return readInvestments_(range); }, { total: 0, byYear: [], count: 0 });
  /* Ad spend and mentorship stay separate in the maths so CPL/CPA keep meaning ads only,
     while all-in ROAS answers "what did the whole investment return". */
  overview.investment = investments.total;
  overview.totalInvested = asNumber_(overview.spend) + investments.total;
  overview.roasAllIn = overview.totalInvested ? asNumber_(overview.revenue) / overview.totalInvested : 0;
  overview.cplAllIn = overview.leads ? overview.totalInvested / overview.leads : 0;
  // v9.2 segmentation
  const segments = safely('segments', function () { return buildPlatformBreakdown_(perf, funnel); }, { combined: null, platforms: [] });
  const monthly = safely('monthly', function () { return buildMonthlyComparison_(12); }, []);
  const months = safely('months', function () { return availableMonths_(); }, []);
  const formats = safely('formats', function () { return buildFormatBreakdown_(ads); }, []);
  const decisionTrend = safely('trend', function () { return buildDecisionTrend_(perf, funnel); }, []);
  if (warnings.length) {
    try { appendErrorLog_(makeRunId_('dash'), 'Dashboard', 'buildDashboardPayload_', 'WARN', warnings.join(' | '), '', '', '', {}, 'webapp'); } catch (ignored) {}
  }
  return {
    ok: true,
    app: { name: APP.NAME, version: APP.VERSION },
    range: range,
    generatedAt: nowIso_(),
    overview: overview,
    platforms: platforms,
    campaigns: campaigns.slice(0, 100),
    ads: ads.slice(0, 200),
    adSets: adSets.slice(0, 100),
    leads: leads,
    funnel: funnelTotals,
    stages: stages,
    pipeline: pipeline,
    census: census,
    investments: investments,
    warnings: warnings,
    segments: segments,
    monthly: monthly,
    months: months,
    formats: formats,
    decisionTrend: decisionTrend,
    actions: {
      kill: ads.filter(a => a.signal === 'KILL').length,
      scale: ads.filter(a => a.signal === 'SCALE').length,
      test: ads.filter(a => a.signal === 'TEST').length,
      newAds: ads.filter(a => a.isNew).length,
      byRule: {
        CPA: ads.filter(a => (a.firedRules || []).indexOf('CPA') >= 0).length,
        CTR: ads.filter(a => (a.firedRules || []).indexOf('CTR') >= 0).length,
        FREQ: ads.filter(a => (a.firedRules || []).indexOf('FREQ') >= 0).length,
        FATIGUE: ads.filter(a => (a.firedRules || []).indexOf('FATIGUE') >= 0).length
      },
      staleLeads: pipeline.reduce((n, g) => n + asNumber_(g.staleCount), 0)
    },
    thresholds: signalThresholds_(),
    trend: buildDailyTrend_(perf, funnel),
    forecast: forecast,
    health: health
  };
}

function aggregateOverview_(perf, funnel) {
  const spend = perf.reduce((s,r) => s + asNumber_(r.spend), 0);
  const impressions = perf.reduce((s,r) => s + asNumber_(r.impressions), 0);
  const clicks = perf.reduce((s,r) => s + asNumber_(r.clicks), 0);
  const adLeads = perf.reduce((s,r) => s + asNumber_(r.leads), 0);
  const newLeads = funnel.reduce((s,r) => s + asNumber_(r.newLeads), 0);
  const responded = funnel.reduce((s,r) => s + asNumber_(r.responded), 0);
  const booked = funnel.reduce((s,r) => s + asNumber_(r.bookedCalls), 0);
  const appointments = funnel.reduce((s,r) => s + asNumber_(r.appointments), 0);
  const strategySessions = funnel.reduce((s,r) => s + asNumber_(r.strategySessions), 0);
  const qualified = funnel.reduce((s,r) => s + asNumber_(r.qualified), 0);
  const closed = funnel.reduce((s,r) => s + asNumber_(r.closedWon), 0);
  const revenue = funnel.reduce((s,r) => s + asNumber_(r.revenue), 0);
  const leads = newLeads || adLeads;
  return {
    spend, impressions, clicks, leads, adLeads, responded, bookedCalls: booked,
    appointments, strategySessions, qualified, closed, revenue,
    cpl: leads ? spend / leads : 0,
    costPerResponded: responded ? spend / responded : 0,
    costPerBooked: booked ? spend / booked : 0,
    costPerAppointment: appointments ? spend / appointments : 0,
    costPerStrategySession: strategySessions ? spend / strategySessions : 0,
    costPerQualified: qualified ? spend / qualified : 0,
    costPerClose: closed ? spend / closed : 0,
    roas: spend ? revenue / spend : 0,
    ctr: impressions ? clicks / impressions * 100 : 0,
    responseRate: leads ? responded / leads : 0,
    bookingRate: responded ? booked / responded : 0,
    showRate: booked ? appointments / booked : 0,
    qualificationRate: appointments ? qualified / appointments : 0,
    closeRate: qualified ? closed / qualified : 0
  };
}

function aggregateCampaigns_(perf, funnel) {
  const map = {};
  function keyFor(r) { return safeText_(r.platform) + '|' + (safeText_(r.campaignId) || normaliseName_(r.campaignName)); }
  perf.forEach(r => {
    const k = keyFor(r); if (!map[k]) map[k] = { platform:r.platform, campaignId:r.campaignId, campaignName:r.campaignName, spend:0, impressions:0, clicks:0, leads:0 };
    const x = map[k]; x.spend += asNumber_(r.spend); x.impressions += asNumber_(r.impressions); x.clicks += asNumber_(r.clicks); x.leads += asNumber_(r.leads);
  });
  funnel.forEach(r => {
    const k = keyFor(r); if (!map[k]) map[k] = { platform:r.platform, campaignId:r.campaignId, campaignName:r.campaignName, spend:0, impressions:0, clicks:0, leads:0 };
    const x = map[k]; x.newLeads = (x.newLeads||0)+asNumber_(r.newLeads); x.responded=(x.responded||0)+asNumber_(r.responded); x.bookedCalls=(x.bookedCalls||0)+asNumber_(r.bookedCalls); x.appointments=(x.appointments||0)+asNumber_(r.appointments); x.qualified=(x.qualified||0)+asNumber_(r.qualified); x.closed=(x.closed||0)+asNumber_(r.closedWon); x.revenue=(x.revenue||0)+asNumber_(r.revenue);
  });
  return Object.keys(map).map(k => {
    const x=map[k]; const leads=x.newLeads||x.leads||0;
    x.cpl=leads?x.spend/leads:0; x.cpa=x.appointments?x.spend/x.appointments:0; x.costPerQualified=x.qualified?x.spend/x.qualified:0; x.roas=x.spend&&x.revenue?x.revenue/x.spend:0; x.ctr=x.impressions?x.clicks/x.impressions*100:0;
    return x;
  }).sort((a,b)=>b.spend-a.spend);
}

function aggregatePlatforms_(perf, funnel) {
  const platforms = ['Meta','Google','Organic','Other'];
  return platforms.map(p => {
    const pp=perf.filter(r=>safeText_(r.platform)===p); const ff=funnel.filter(r=>safeText_(r.platform)===p);
    return Object.assign({platform:p},aggregateOverview_(pp,ff));
  }).filter(x=>x.spend||x.leads||x.closed);
}

function aggregateFunnel_(rows) {
  return rows.reduce((o,r)=>{
    o.newLeads+=asNumber_(r.newLeads); o.contacted+=asNumber_(r.contacted); o.responded+=asNumber_(r.responded); o.bookedCalls+=asNumber_(r.bookedCalls); o.appointments+=asNumber_(r.appointments); o.strategySessions+=asNumber_(r.strategySessions); o.qualified+=asNumber_(r.qualified); o.closedWon+=asNumber_(r.closedWon); o.closedLost+=asNumber_(r.closedLost); o.revenue+=asNumber_(r.revenue); return o;
  },{newLeads:0,contacted:0,responded:0,bookedCalls:0,appointments:0,strategySessions:0,qualified:0,closedWon:0,closedLost:0,revenue:0});
}

function buildDailyTrend_(perf, funnel) {
  const map={};
  perf.forEach(r=>{const d=safeText_(r.date).slice(0,10); if(!map[d])map[d]={date:d,spend:0,leads:0,bookedCalls:0,appointments:0,closed:0,revenue:0}; map[d].spend+=asNumber_(r.spend); map[d].leads+=asNumber_(r.leads);});
  funnel.forEach(r=>{const d=safeText_(r.date).slice(0,10); if(!map[d])map[d]={date:d,spend:0,leads:0,bookedCalls:0,appointments:0,closed:0,revenue:0}; map[d].leads=Math.max(map[d].leads,asNumber_(r.newLeads)); map[d].bookedCalls+=asNumber_(r.bookedCalls); map[d].appointments+=asNumber_(r.appointments); map[d].closed+=asNumber_(r.closedWon); map[d].revenue+=asNumber_(r.revenue);});
  return Object.keys(map).sort().map(k=>map[k]);
}

/**
 * Head-count of where every lead is standing right now, by pipeline stage.
 *
 * This is what GHL's board shows, so the cards and the board can be read side by side.
 * It is deliberately NOT the funnel total: the funnel counts everyone who ever reached
 * a stage, so a lead now sitting in Appointment still counts as a booked call there.
 * Both are true and both are needed — the census answers "who is where", the funnel
 * answers "where are we leaking". Showing only one of them was the whole confusion.
 *
 * Range-filtered on lead creation date, so a narrower range reads as "of the leads that
 * came in during this period, where are they now". At "All" it matches the board exactly.
 */
function buildStageCensus_(range) {
  const rows = sheetRowsAsObjects_(APP.TABS.GHL).filter(function (r) { return inDateRange_(r.date, range); });
  const blank = function () {
    const o = {};
    CANONICAL_STAGES.forEach(function (stage) { o[stage] = 0; });
    o.total = 0;
    /* Split by whether the lead is still workable. The funnel used to report every
       non-advancing lead as "lost", which read as a catastrophic leak when nearly all of
       them are simply sitting in the stage waiting to be worked: 120 people at Booked
       Call were reported lost, while only ~10 leads in the whole pipeline are truly dead. */
    o.live = {}; o.dead = {};
    CANONICAL_STAGES.forEach(function (stage) { o.live[stage] = 0; o.dead[stage] = 0; });
    return o;
  };
  // Split by platform as well as combined, so the dashboard can be filtered to one
  // channel without a second server round trip.
  const census = { all: blank(), Meta: blank(), Google: blank(), Other: blank() };
  rows.forEach(function (r) {
    const stage = normaliseStage_(r.stage || r.status);
    const platform = platformOf_(r.platform);
    const outcome = safeText_(r.outcome).toLowerCase();
    const bucket = (outcome === 'lost' || outcome === 'abandoned') ? 'dead' : 'live';
    census.all[stage] = (census.all[stage] || 0) + 1;
    census.all.total++;
    census.all[bucket][stage] = (census.all[bucket][stage] || 0) + 1;
    census[platform][stage] = (census[platform][stage] || 0) + 1;
    census[platform].total++;
    census[platform][bucket][stage] = (census[platform][bucket][stage] || 0) + 1;
  });
  return census;
}

/** Create the Investments tab with its headers so there is somewhere to type. */
function ensureInvestmentsTab_() {
  const sheet = getSheet_(APP.TABS.INVESTMENTS, true);
  if (safeText_(sheet.getRange(1, 1).getValue()).trim()) return sheet;
  sheet.getRange(1, 1, 1, TAB_HEADERS.Investments.length).setValues([TAB_HEADERS.Investments]);
  sheet.setFrozenRows(1);
  return sheet;
}

/**
 * Mentorship and mastermind investment for the selected period.
 *
 * Kept out of `spend` on purpose: ad spend buys leads and its CPL/CPA must stay clean,
 * whereas mentorship is an overhead that changes what the business truly returned. The
 * dashboard therefore reports both — ROAS on ads alone, and all-in ROAS including this.
 *
 * Rows carrying a real date are range-filtered like anything else. Rows with only a year
 * count whenever the selected range touches that year, since an annual fee cannot be
 * attributed to one day without inventing a number.
 */
function readInvestments_(range) {
  ensureInvestmentsTab_();
  const rows = sheetRowsAsObjects_(APP.TABS.INVESTMENTS);
  const startYear = Number(safeText_(range.start).slice(0, 4));
  const endYear = Number(safeText_(range.end).slice(0, 4));

  const kept = rows.filter(function (r) {
    if (!asNumber_(r.amount)) return false;
    const date = dayKey_(r.date);
    if (date) return inDateRange_(date, range);
    const y = Number(safeText_(r.year).slice(0, 4));
    return y && y >= startYear && y <= endYear;
  });

  const byYear = {};
  kept.forEach(function (r) {
    const y = safeText_(r.year).slice(0, 4) || dayKey_(r.date).slice(0, 4) || 'Unassigned';
    if (!byYear[y]) byYear[y] = { year: y, amount: 0, items: [] };
    byYear[y].amount += asNumber_(r.amount);
    byYear[y].items.push({
      category: safeText_(r.category) || 'Mentorship',
      vendor: safeText_(r.vendor),
      description: safeText_(r.description),
      amount: asNumber_(r.amount)
    });
  });

  return {
    total: kept.reduce(function (sum, r) { return sum + asNumber_(r.amount); }, 0),
    byYear: Object.keys(byYear).sort().map(function (y) { return byYear[y]; }),
    count: kept.length
  };
}

function readRecentLeadSummaries_(range, maxRows) {
  const rows = sheetRowsAsObjects_(APP.TABS.GHL).filter(r => inDateRange_(r.date, range));
  rows.sort((a,b)=>safeText_(b.date).localeCompare(safeText_(a.date)));
  return rows.slice(0,maxRows).map(r=>({
    id:safeText_(r.ghlId), name:safeText_(r.name), platform:safeText_(r.platform)||'Other',
    campaignName:safeText_(r.campaignName), sourceAdName:safeText_(r.sourceAdName),
    status:normaliseStage_(r.status), quality:safeText_(r.quality), proptype:safeText_(r.proptype),
    date:r.date instanceof Date?Utilities.formatDate(r.date,APP.TZ,'yyyy-MM-dd'):safeText_(r.date).slice(0,10),
    urgencyTimeline:safeText_(r.urgencyTimeline), dealValue:asNumber_(r.dealValue)
  }));
}

function rebuildDailyFunnelFact_(runId) {
  const rows = sheetRowsAsObjects_(APP.TABS.GHL);
  const map={};
  rows.forEach(r=>{
    const date=r.date instanceof Date?Utilities.formatDate(r.date,APP.TZ,'yyyy-MM-dd'):safeText_(r.date).slice(0,10); if(!date)return;
    const platform=safeText_(r.platform)||'Other'; const campaign=safeText_(r.campaignName)||'(Unattributed)'; const key=date+'|'+platform+'|'+normaliseName_(campaign);
    if(!map[key])map[key]={date,platform,campaignId:'',campaignName:campaign,newLeads:0,contacted:0,responded:0,bookedCalls:0,appointments:0,strategySessions:0,qualified:0,closedWon:0,closedLost:0,revenue:0,sourceUpdatedAt:nowIso_(),syncRunId:runId||'',attributionConfidence:campaign==='(Unattributed)'?'Low':'Medium',notes:''};
    const x=map[key]; x.newLeads++;
    /* How far a lead got is read from its STAGE, so a lead marked Lost still counts at
       every stage it genuinely passed through. Rows written before v9.9 have no stage
       column and fall back to status, which behaves exactly as before until the next
       sync fills it in. 'Lost' remains excluded from progression because GHL's
       Unqualified stage normalises to it and carries no position. */
    const stage=normaliseStage_(r.stage||r.status);
    const outcome=safeText_(r.outcome).toLowerCase();
    const live=stage!=='Lost';
    if(live&&statusRank_(stage)>=statusRank_('Contacted'))x.contacted++;
    if(live&&statusRank_(stage)>=statusRank_('Responded'))x.responded++;
    if(live&&statusRank_(stage)>=statusRank_('Booked Call'))x.bookedCalls++;
    if(live&&statusRank_(stage)>=statusRank_('Appointment'))x.appointments++;
    if(live&&statusRank_(stage)>=statusRank_('Strategy Session'))x.strategySessions++;
    if(live&&statusRank_(stage)>=statusRank_('Appt Qualified'))x.qualified++;
    if(outcome==='won'||stage==='Closed'){x.closedWon++;x.revenue+=asNumber_(r.dealValue);}
    if(outcome==='lost'||stage==='Lost')x.closedLost++;
  });
  overwriteObjects_(APP.TABS.FUNNEL,TAB_HEADERS.Daily_Funnel_Fact,Object.keys(map).map(k=>map[k]));
  return Object.keys(map).length;
}

function backfillGoogleDailyFact_() {
  const rows=sheetRowsAsObjects_(APP.TABS.GOOGLE_DAILY); if(!rows.length)return 0;
  const runId=makeRunId_('google-backfill');
  const facts=rows.map(r=>({date:r.date instanceof Date?Utilities.formatDate(r.date,APP.TZ,'yyyy-MM-dd'):safeText_(r.date).slice(0,10),platform:'Google',accountId:prop_('GOOGLE_ADS_CUSTOMER_ID',''),campaignId:safeText_(r.campaignId),campaignName:safeText_(r.campaign),adSetId:'',adSetName:'',adId:'',adName:'',objective:safeText_(r.campaignType),status:safeText_(r.status),spend:asNumber_(r.spend),impressions:asNumber_(r.impressions),reach:0,clicks:asNumber_(r.clicks),linkClicks:asNumber_(r.clicks),leads:asNumber_(r.conversions),conversions:asNumber_(r.conversions),conversionValue:asNumber_(r.conversionValue),ctr:asNumber_(r.ctr),cpc:asNumber_(r.avgCpc),cpl:asNumber_(r.conversions)?asNumber_(r.spend)/asNumber_(r.conversions):0,sourceUpdatedAt:safeText_(r.updatedAt)||nowIso_(),syncRunId:runId}));
  return upsertObjects_(APP.TABS.PERFORMANCE,TAB_HEADERS.Daily_Performance_Fact,facts,r=>[dayKey_(r.date),safeText_(r.platform),safeText_(r.campaignId),safeText_(r.adSetId),safeText_(r.adId)].join('|'));
}

// ==================== 03_MetaSync.gs ====================
/** Meta daily-insights synchronisation with full pagination. */
function syncMetaDaily_(runId, days) {
  const started = new Date();
  const token = prop_('META_ACCESS_TOKEN','');
  const accountId = prop_('META_AD_ACCOUNT_ID','act_1467621970951606');
  const apiVersion = prop_('META_API_VERSION','v19.0');
  if(!token) throw new Error('META_ACCESS_TOKEN is missing.');
  // Explicit window wins, so the history backfill can walk arbitrary past periods.
  // Routine syncs stay on the short rolling window to finish inside the 6-minute limit.
  const end = arguments[3] ? String(arguments[3]) : sgtDate_(new Date());
  const start = arguments[2] ? String(arguments[2])
              : addDaysIso_(end, -Math.max(1, Number(days || APP.DEFAULT_META_DAYS) - 1));
  const fields=['date_start','date_stop','account_id','campaign_id','campaign_name','adset_id','adset_name','ad_id','ad_name','objective','spend','impressions','reach','clicks','inline_link_clicks','actions','action_values','ctr','cpc'].join(',');
  const params={level:'ad',time_increment:1,time_range:JSON.stringify({since:start,until:end}),fields:fields,limit:500};
  const url='https://graph.facebook.com/'+apiVersion+'/'+accountId+'/insights';
  const rows=metaFetchAll_(url,params,token,runId);
  const now=nowIso_();
  const facts=rows.map(r=>{
    const spend=asNumber_(r.spend), leads=extractMetaLeads_(r.actions);
    return {date:safeText_(r.date_start),platform:'Meta',accountId:safeText_(r.account_id)||accountId,campaignId:safeText_(r.campaign_id),campaignName:safeText_(r.campaign_name),adSetId:safeText_(r.adset_id),adSetName:safeText_(r.adset_name),adId:safeText_(r.ad_id),adName:safeText_(r.ad_name),objective:safeText_(r.objective),status:'',spend:spend,impressions:asNumber_(r.impressions),reach:asNumber_(r.reach),clicks:asNumber_(r.clicks),linkClicks:asNumber_(r.inline_link_clicks),leads:leads,conversions:leads,conversionValue:extractMetaAction_(r.action_values,['purchase','omni_purchase']),ctr:asNumber_(r.ctr),cpc:asNumber_(r.cpc),cpl:leads?spend/leads:0,sourceUpdatedAt:now,syncRunId:runId};
  });
  const written=upsertObjects_(APP.TABS.PERFORMANCE,TAB_HEADERS.Daily_Performance_Fact,facts,r=>[dayKey_(r.date),safeText_(r.platform),safeText_(r.campaignId),safeText_(r.adSetId),safeText_(r.adId)].join('|'));
  rebuildMetaSnapshotTabs_(facts,start,end);
  appendSyncLog_(runId,'Meta','SUCCESS',started,new Date(),rows.length,written,start,end,'Daily ad insights synced','scheduled');
  return {service:'Meta',recordsRead:rows.length,recordsWritten:written,dateFrom:start,dateTo:end};
}

function metaFetchAll_(url, params, token, runId) {
  let next=buildUrl_(url,Object.assign({},params,{access_token:token})); const all=[]; let page=0;
  while(next && page<100){
    const res=fetchWithRetry_(next,{method:'get',muteHttpExceptions:true},'Meta',runId);
    const code=res.getResponseCode(), text=res.getContentText(); let body;
    try{body=JSON.parse(text);}catch(e){throw new Error('Meta returned non-JSON HTTP '+code+': '+text.slice(0,300));}
    if(code<200||code>=300||body.error)throw new Error('Meta API HTTP '+code+': '+safeText_(body.error&&body.error.message||text).slice(0,500));
    if(Array.isArray(body.data))all.push.apply(all,body.data);
    next=body.paging&&body.paging.next?body.paging.next:''; page++; if(next)Utilities.sleep(120);
  }
  if(page>=100)throw new Error('Meta pagination safety limit reached.');
  return all;
}

/**
 * Sum the named Meta action types. Correct for genuinely distinct events (e.g. adding
 * separate purchase types), WRONG for leads — see extractMetaLeads_.
 */
function extractMetaAction_(actions, names) {
  const wanted={}; names.forEach(n=>wanted[n]=true); let total=0;
  (actions||[]).forEach(a=>{if(wanted[a.action_type])total+=asNumber_(a.value);});
  return total;
}

/**
 * Lead count for one row. Takes the LARGEST single action type, never the sum.
 *
 * Meta reports one lead under several action_type labels simultaneously — a lead-form
 * submission commonly appears as both 'lead' and 'onsite_conversion.lead_grouped', and
 * a pixel lead as both 'lead' and 'offsite_conversion.fb_pixel_lead'. Summing them
 * multiplies the count: this account read 1,342 leads against 395 in Meta's own export
 * (~3.4x), which in turn understated CPL as ~$80 when the true figure is ~$201 — an
 * error that makes a channel look cheaper than it is.
 *
 * The largest single type is the closest match to Meta Ads Manager's own "Leads"
 * column, because the overlapping labels are views of the same underlying event
 * rather than separate events.
 */
function extractMetaLeads_(actions) {
  const names=['lead','onsite_conversion.lead_grouped','offsite_conversion.fb_pixel_lead','onsite_web_lead'];
  const wanted={}; names.forEach(n=>wanted[n]=true);
  let best=0;
  (actions||[]).forEach(a=>{ if(wanted[a.action_type]) best=Math.max(best,asNumber_(a.value)); });
  return best;
}

function buildUrl_(base, params) {
  return base+'?'+Object.keys(params).map(k=>encodeURIComponent(k)+'='+encodeURIComponent(params[k])).join('&');
}

/**
 * Live status and creative metadata for ads, ad sets and campaigns.
 *
 * The Insights endpoint returns performance only — it has no notion of whether an ad is
 * currently running. Status therefore has to come from the entity endpoints, and until
 * this existed every ad in Meta_Ads carried status:'' — which made the dashboard's
 * "Live only" filter hide the entire list.
 *
 * effective_status is used rather than status, because an ad whose own status is ACTIVE
 * is still not running if its ad set or campaign is paused. effective_status accounts
 * for the whole chain, which is what "is this actually live" means.
 *
 * Failures here are non-fatal: performance data is the point, and a missing status
 * should degrade the filter, not break the sync.
 */
function fetchMetaEntityMeta_(runId) {
  const token = prop_('META_ACCESS_TOKEN', '');
  const accountId = prop_('META_AD_ACCOUNT_ID', 'act_1467621970951606');
  const apiVersion = prop_('META_API_VERSION', 'v19.0');
  const out = { ads: {}, adsets: {}, campaigns: {} };
  if (!token) return out;

  const base = 'https://graph.facebook.com/' + apiVersion + '/' + accountId;
  try {
    metaFetchAll_(base + '/ads',
      { fields: 'id,name,effective_status,creative{id,thumbnail_url,image_url,video_id,object_type},preview_shareable_link', limit: 200 },
      token, runId).forEach(function (a) {
        const c = a.creative || {};
        const objectType = safeText_(c.object_type).toUpperCase();
        out.ads[safeText_(a.id)] = {
          status: safeText_(a.effective_status),
          thumbUrl: safeText_(c.thumbnail_url) || safeText_(c.image_url),
          imageUrl: safeText_(c.image_url),
          videoId: safeText_(c.video_id),
          format: c.video_id ? 'Video' : (objectType.indexOf('VIDEO') >= 0 ? 'Video' : (c.image_url || c.thumbnail_url) ? 'Image' : ''),
          adPermalink: safeText_(a.preview_shareable_link)
        };
      });
  } catch (e) {
    appendErrorLog_(runId, 'Meta', 'fetchMetaEntityMeta_', 'WARN', 'Ad metadata unavailable: ' + e.message, '', '', e.stack, {}, 'sync');
  }
  try {
    metaFetchAll_(base + '/adsets', { fields: 'id,name,effective_status,daily_budget,lifetime_budget', limit: 200 }, token, runId)
      .forEach(function (a) {
        out.adsets[safeText_(a.id)] = {
          status: safeText_(a.effective_status),
          budget: asNumber_(a.daily_budget || a.lifetime_budget) / 100   // Meta returns minor units
        };
      });
  } catch (e) { /* non-fatal */ }
  try {
    metaFetchAll_(base + '/campaigns', { fields: 'id,name,effective_status,objective', limit: 200 }, token, runId)
      .forEach(function (c) { out.campaigns[safeText_(c.id)] = { status: safeText_(c.effective_status) }; });
  } catch (e) { /* non-fatal */ }
  return out;
}

function rebuildMetaSnapshotTabs_(facts,start,end){
  const campaigns={},adsets={},ads={};
  facts.forEach(r=>{
    const ck=r.campaignId||normaliseName_(r.campaignName); if(!campaigns[ck])campaigns[ck]={metaId:r.campaignId,name:r.campaignName,platform:'Meta',objective:r.objective,status:'',budget:0,spend:0,leads:0,cpl:0,impressions:0,clicks:0,ctr:0,reach:0,updatedAt:r.sourceUpdatedAt};
    const c=campaigns[ck]; c.spend+=r.spend;c.leads+=r.leads;c.impressions+=r.impressions;c.clicks+=r.clicks;c.reach+=r.reach;
    const ak=r.adSetId||ck+'|'+normaliseName_(r.adSetName); if(!adsets[ak])adsets[ak]={metaId:r.adSetId,name:r.adSetName,campaignId:r.campaignId,campaignName:r.campaignName,platform:'Meta',status:'',budget:0,spend:0,leads:0,cpl:0,audience:'',updatedAt:r.sourceUpdatedAt};
    adsets[ak].spend+=r.spend;adsets[ak].leads+=r.leads;
    const dk=r.adId||ak+'|'+normaliseName_(r.adName); if(!ads[dk])ads[dk]={metaId:r.adId,name:r.adName,adsetId:r.adSetId,adsetName:r.adSetName,campaignId:r.campaignId,campaignName:r.campaignName,platform:'Meta',status:'',format:'',thumbUrl:'',videoId:'',imageUrl:'',videoSrc:'',hookrate:0,ctr:0,cpc:0,cpm:0,spend:0,impressions:0,clicks:0,leads:0,cpl:0,p25:0,p50:0,p75:0,p95:0,adPermalink:'',updatedAt:r.sourceUpdatedAt};
    const d=ads[dk];d.spend+=r.spend;d.impressions+=r.impressions;d.clicks+=r.clicks;d.leads+=r.leads;
  });
  // Status and creative come from the entity endpoints, not from insights.
  const em = fetchMetaEntityMeta_(makeRunId_('meta-meta'));
  const campArr=Object.keys(campaigns).map(k=>{const x=campaigns[k];x.cpl=x.leads?x.spend/x.leads:0;x.ctr=x.impressions?x.clicks/x.impressions*100:0;
    const e=em.campaigns[safeText_(x.metaId)]; if(e)x.status=e.status;
    return x;});
  const adsetArr=Object.keys(adsets).map(k=>{const x=adsets[k];x.cpl=x.leads?x.spend/x.leads:0;
    const e=em.adsets[safeText_(x.metaId)]; if(e){x.status=e.status;x.budget=e.budget;}
    return x;});
  const adArr=Object.keys(ads).map(k=>{const x=ads[k];x.cpl=x.leads?x.spend/x.leads:0;x.ctr=x.impressions?x.clicks/x.impressions*100:0;x.cpc=x.clicks?x.spend/x.clicks:0;x.cpm=x.impressions?x.spend/x.impressions*1000:0;
    const e=em.ads[safeText_(x.metaId)];
    if(e){x.status=e.status;x.thumbUrl=e.thumbUrl;x.imageUrl=e.imageUrl;x.videoId=e.videoId;x.format=e.format;x.adPermalink=e.adPermalink;}
    return x;});
  overwriteObjects_(APP.TABS.META_CAMPAIGNS,['metaId','name','platform','objective','status','budget','spend','leads','cpl','impressions','clicks','ctr','reach','updatedAt'],campArr);
  overwriteObjects_(APP.TABS.META_ADSETS,['metaId','name','campaignId','campaignName','platform','status','budget','spend','leads','cpl','audience','updatedAt'],adsetArr);
  overwriteObjects_(APP.TABS.META_ADS,['metaId','name','adsetId','adsetName','campaignId','campaignName','platform','status','format','thumbUrl','videoId','imageUrl','videoSrc','hookrate','ctr','cpc','cpm','spend','impressions','clicks','leads','cpl','p25','p50','p75','p95','adPermalink','updatedAt'],adArr);
}

// ==================== 04_GHLSync.gs ====================
/** GoHighLevel contacts + opportunity pipeline synchronisation. */
function syncGHL_(runId) {
  const started=new Date(); const apiKey=prop_('GHL_API_KEY',''); const locationId=prop_('GHL_LOCATION_ID','cyeYxFVQE1l73kO6S6Lx'); const pipelineId=prop_('GHL_PIPELINE_ID','BdutTA7xHUrNoPpWc5Nu');
  if(!apiKey)throw new Error('GHL_API_KEY is missing.');
  const headers={'Authorization':'Bearer '+apiKey,'Version':prop_('GHL_API_VERSION','2021-07-28'),'Content-Type':'application/json'};
  const contacts=fetchAllGHLContacts_(locationId,headers,runId); const opportunityData=fetchAllGHLOpportunities_(locationId,pipelineId,headers,runId); const stageNames=fetchGHLStageNames_(locationId,pipelineId,headers,runId);
  const byContact=indexOpportunitiesByContact_(opportunityData,stageNames);
  const existing=sheetRowsAsObjects_(APP.TABS.GHL), preserved={}; existing.forEach(r=>preserved[safeText_(r.ghlId)]={quality:r.quality,dealValue:r.dealValue,urgencyTimeline:r.urgencyTimeline,notes:r.notes});
  const leads=contacts.filter(c=>c.id&&byContact[c.id]).map(c=>mapGHLContact_(c,byContact[c.id],preserved[c.id]||{}));
  overwriteObjects_(APP.TABS.GHL,GHL_LEAD_HEADERS,leads);
  const funnelRows=rebuildDailyFunnelFact_(runId);
  appendSyncLog_(runId,'GHL','SUCCESS',started,new Date(),contacts.length,leads.length,'','',leads.length+' pipeline leads; '+funnelRows+' daily funnel rows','scheduled');
  return {service:'GHL',contactsRead:contacts.length,opportunitiesRead:opportunityData.length,leadsWritten:leads.length,funnelRows:funnelRows};
}

function fetchAllGHLContacts_(locationId,headers,runId){
  let url='https://services.leadconnectorhq.com/contacts/?locationId='+encodeURIComponent(locationId)+'&limit='+APP.DEFAULT_GHL_PAGE_LIMIT;const all=[];let page=0;
  while(url&&page<100){const body=ghlGetJson_(url,headers,'GHL contacts',runId);const rows=body.contacts||[];all.push.apply(all,rows);if(!rows.length)break;const meta=body.meta||{};if(meta.nextPageUrl)url=meta.nextPageUrl;else if(meta.startAfter&&meta.startAfterId)url='https://services.leadconnectorhq.com/contacts/?locationId='+encodeURIComponent(locationId)+'&limit='+APP.DEFAULT_GHL_PAGE_LIMIT+'&startAfter='+encodeURIComponent(meta.startAfter)+'&startAfterId='+encodeURIComponent(meta.startAfterId);else url='';page++;if(url)Utilities.sleep(100);}
  if(page>=100)throw new Error('GHL contact pagination safety limit reached.');return all;
}

function fetchAllGHLOpportunities_(locationId,pipelineId,headers,runId){
  const all=[];let page=1;
  while(page<=100){const url='https://services.leadconnectorhq.com/opportunities/search?location_id='+encodeURIComponent(locationId)+'&pipeline_id='+encodeURIComponent(pipelineId)+'&limit=100&page='+page;const body=ghlGetJson_(url,headers,'GHL opportunities',runId);const rows=body.opportunities||[];all.push.apply(all,rows);if(!rows.length)break;const meta=body.meta||{};if(meta.nextPage===false||rows.length<100)break;page++;Utilities.sleep(100);}
  if(page>100)throw new Error('GHL opportunity pagination safety limit reached.');return all;
}

function fetchGHLStageNames_(locationId,pipelineId,headers,runId){
  const map={};try{const body=ghlGetJson_('https://services.leadconnectorhq.com/opportunities/pipelines?locationId='+encodeURIComponent(locationId),headers,'GHL pipelines',runId);(body.pipelines||[]).filter(p=>!pipelineId||p.id===pipelineId).forEach(p=>(p.stages||[]).forEach(s=>map[s.id]=s.name));}catch(e){appendErrorLog_(runId,'GHL','fetchGHLStageNames_','WARN',e.message,'','','',{} ,'scheduled');}return map;
}

function ghlGetJson_(url,headers,label,runId){const res=fetchWithRetry_(url,{method:'get',headers:headers,muteHttpExceptions:true},label,runId);const code=res.getResponseCode(),text=res.getContentText();let body;try{body=JSON.parse(text);}catch(e){throw new Error(label+' returned non-JSON HTTP '+code+': '+text.slice(0,300));}if(code<200||code>=300)throw new Error(label+' HTTP '+code+': '+safeText_(body.message||text).slice(0,500));return body;}

/**
 * Which channel actually paid for this lead.
 *
 * Order matters, and it used to be wrong. A loose match on the string "google" anywhere
 * in utmSource / adSource / medium was tested BEFORE the Meta ad id, so a lead carrying
 * a Meta ad id but a source like "google-contacts ads manual add" was credited to
 * Google. Roughly 30 Meta-paid leads sat under Google as a result, which is why Google
 * reported an 83.5% lead-to-booked rate and 35 booked calls against zero revenue.
 *
 * The hard signals now outrank the text:
 *   gclid    — only Google issues one, so it settles the question outright.
 *   utmAdId  — Meta lead ads populate this; Google Ads does not.
 * Only when neither is present does the source text get a say, and the Meta words are
 * checked first so "facebook" cannot lose to an incidental "google" elsewhere in the
 * same string.
 */
function classifyLeadPlatform_(attr, contact) {
  attr = attr || {};
  if (safeText_(attr.gclid)) return 'Google';
  if (safeText_(attr.utmAdId)) return 'Meta';
  const text = safeText_(attr.utmSource || attr.adSource || attr.medium ||
                         (contact && contact.source)).toLowerCase();
  if (text.indexOf('facebook') >= 0 || text.indexOf('instagram') >= 0 || text.indexOf('meta') >= 0) return 'Meta';
  if (text.indexOf('google') >= 0 || text.indexOf('youtube') >= 0) return 'Google';
  return 'Other';
}

function mapGHLContact_(c,stage,preserved){
  const attrs=c.attributions||[];const attr=attrs.find(a=>a.utmAdId)||attrs[0]||{};const status=normaliseStage_(stage.status);const tags=Array.isArray(c.tags)?c.tags:[];const tagText=tags.join(' ').toLowerCase();let proptype='';if(tagText.indexOf('newlaunch')>=0||tagText.indexOf('new launch')>=0)proptype='New Launch';else if(tagText.indexOf('familylegacy')>=0||tagText.indexOf('family legacy')>=0)proptype='Family Legacy';else proptype=safeText_(c.source);
  const date=c.dateAdded?Utilities.formatDate(new Date(c.dateAdded),APP.TZ,'yyyy-MM-dd'):(stage.createdAt?Utilities.formatDate(new Date(stage.createdAt),APP.TZ,'yyyy-MM-dd'):'');
  return {ghlId:safeText_(c.id),name:safeText_(c.contactName||[c.firstName,c.lastName].filter(Boolean).join(' ')),contact:safeText_(c.email||c.phone),phone:safeText_(c.phone),email:safeText_(c.email),sourceAdId:safeText_(attr.utmAdId),sourceAdName:safeText_(attr.utmContent||attr.utmCampaign),platform:classifyLeadPlatform_(attr,c),campaignName:safeText_(attr.utmCampaign),status:status,quality:safeText_(preserved.quality),proptype:proptype,date:date,responded:status!=='Lost'&&statusRank_(status)>=statusRank_('Responded')?'Y':'',appointment:status!=='Lost'&&statusRank_(status)>=statusRank_('Appointment')?'Booked':'',strategySession:status!=='Lost'&&statusRank_(status)>=statusRank_('Strategy Session')?'Y':'',qualified:status!=='Lost'&&statusRank_(status)>=statusRank_('Appt Qualified')?'Y':'',dealValue:asNumber_(preserved.dealValue)||asNumber_(stage.monetaryValue),urgencyTimeline:safeText_(preserved.urgencyTimeline),tags:tags.join(', '),source:safeText_(c.source),notes:safeText_(preserved.notes),stage:normaliseStage_(stage.stage||stage.status),outcome:safeText_(stage.outcome)||'open'};
}

/** Column order of GHL_Leads. Shared so the full sync and the quick refresh can never
 *  drift into writing different shapes into the same tab. */
const GHL_LEAD_HEADERS = Object.freeze(['ghlId','name','contact','phone','email','sourceAdId',
  'sourceAdName','platform','campaignName','status','quality','proptype','date','responded',
  'appointment','strategySession','qualified','dealValue','urgencyTimeline','tags','source','notes',
  'stage','outcome']);

/**
 * Reduce raw opportunities to one canonical stage per contact.
 *
 * A contact can hold more than one opportunity; the furthest-advanced one is what the
 * funnel should count, hence the statusRank_ comparison. GHL's own won/lost status
 * overrides the stage name, because an opportunity marked Won while still sitting in
 * "Appointment" is closed business, not an appointment.
 */
function indexOpportunitiesByContact_(opportunities, stageNames) {
  const byContact = {};
  (opportunities || []).forEach(function (o) {
    const cid = safeText_(o.contact && o.contact.id || o.contactId);
    if (!cid) return;
    const stageId = safeText_(o.pipelineStageId || o.pipeline_stage_id || o.stageId || (o.stage && o.stage.id));
    const rawName = safeText_(o.stage && o.stage.name || (stageNames || {})[stageId]);
    const raw = safeText_(o.status).toLowerCase();
    const status = raw === 'won' ? 'Closed' : raw === 'lost' ? 'Lost' : normaliseStage_(rawName);
    const entry = {
      status: status,
      /* Pipeline position, recorded separately from the outcome. GHL overwrites the
         stage with won/lost in `status` above, which erased how far a lost lead had
         actually got: 5 leads lost at Appointment stage were dropping out of both the
         booked-call and appointment counts, understating appointments by ~10% and
         making the dashboard disagree with the GHL board. */
      stage: normaliseStage_(rawName),
      outcome: raw || 'open',
      createdAt: safeText_(o.createdAt), stageId: stageId,
      opportunityId: safeText_(o.id), monetaryValue: asNumber_(o.monetaryValue || o.value)
    };
    if (!byContact[cid] || statusRank_(entry.status) > statusRank_(byContact[cid].status)) byContact[cid] = entry;
  });
  return byContact;
}

/**
 * Re-stamp an existing lead row from its current pipeline stage.
 *
 * Only the stage and the flags derived from it are touched. quality, urgencyTimeline
 * and notes are hand-maintained in the sheet and must survive a refresh, and the
 * contact's name/phone/attribution cannot change without a full contact pull anyway.
 */
function applyStageToLead_(row, stage) {
  const status = normaliseStage_(stage.status);
  const live = function (floor) { return status !== 'Lost' && statusRank_(status) >= statusRank_(floor); };
  const out = {};
  GHL_LEAD_HEADERS.forEach(function (h) { out[h] = row[h]; });
  out.ghlId = safeText_(row.ghlId);
  out.date = dayKey_(row.date);              // Sheets hands dates back as Date objects
  out.status = status;
  out.responded = live('Responded') ? 'Y' : '';
  out.appointment = live('Appointment') ? 'Booked' : '';
  out.strategySession = live('Strategy Session') ? 'Y' : '';
  out.qualified = live('Appt Qualified') ? 'Y' : '';
  out.dealValue = asNumber_(row.dealValue) || asNumber_(stage.monetaryValue);
  out.stage = normaliseStage_(stage.stage || stage.status);
  out.outcome = safeText_(stage.outcome) || 'open';
  return out;
}

/**
 * Quick GHL refresh — pipeline stages only.
 *
 * The full sync re-reads every contact in the account (~9,100 records, 45-60s). That is
 * far too slow to sit inside a page load, and almost all of it is wasted: names and
 * phone numbers do not change between one dashboard visit and the next. Stage moves do.
 * There are only ~400 opportunities, so pulling those alone gives the dashboard the
 * thing that actually changed, in a couple of seconds.
 *
 * Contacts appearing for the first time are fetched individually and capped, so a
 * sudden burst of new leads cannot turn a page load into a full sync. Anything past
 * the cap lands in the nightly reconciliation instead.
 */
function refreshGHLStages_(runId) {
  const started = new Date();
  const apiKey = prop_('GHL_API_KEY', '');
  if (!apiKey) throw new Error('GHL_API_KEY is missing.');
  const locationId = prop_('GHL_LOCATION_ID', 'cyeYxFVQE1l73kO6S6Lx');
  const pipelineId = prop_('GHL_PIPELINE_ID', 'BdutTA7xHUrNoPpWc5Nu');
  const headers = {
    'Authorization': 'Bearer ' + apiKey,
    'Version': prop_('GHL_API_VERSION', '2021-07-28'),
    'Content-Type': 'application/json'
  };

  const opportunities = fetchAllGHLOpportunities_(locationId, pipelineId, headers, runId);
  // A partial or empty read would otherwise wipe the tab, since rows without a matching
  // opportunity are dropped. Refuse to write rather than destroy the pipeline view.
  if (!opportunities.length) throw new Error('GHL returned no opportunities — refusing to overwrite the pipeline.');

  const stageNames = fetchGHLStageNames_(locationId, pipelineId, headers, runId);
  const byContact = indexOpportunitiesByContact_(opportunities, stageNames);

  const existing = sheetRowsAsObjects_(APP.TABS.GHL);
  const rowFor = {};
  existing.forEach(function (r) { rowFor[safeText_(r.ghlId)] = r; });

  const out = [];
  let moved = 0;
  Object.keys(byContact).forEach(function (cid) {
    const row = rowFor[cid];
    if (!row) return;
    const before = normaliseStage_(row.status);
    const updated = applyStageToLead_(row, byContact[cid]);
    if (updated.status !== before) moved++;
    out.push(updated);
  });

  const missing = Object.keys(byContact).filter(function (cid) { return !rowFor[cid]; });
  const cap = asNumber_(prop_('FRESHEN_MAX_NEW_CONTACTS', 40));
  let added = 0;
  missing.slice(0, cap).forEach(function (cid) {
    try {
      const body = ghlGetJson_('https://services.leadconnectorhq.com/contacts/' + encodeURIComponent(cid),
        headers, 'GHL contact', runId);
      const contact = body.contact || body;
      if (contact && contact.id) { out.push(mapGHLContact_(contact, byContact[cid], {})); added++; }
    } catch (e) { /* one unreadable contact must not sink the whole refresh */ }
  });

  overwriteObjects_(APP.TABS.GHL, GHL_LEAD_HEADERS, out);
  const funnelRows = rebuildDailyFunnelFact_(runId);
  const deferred = Math.max(0, missing.length - cap);
  const note = out.length + ' pipeline leads; ' + moved + ' stage changes; ' + added + ' new' +
    (deferred ? '; ' + deferred + ' deferred to the nightly sync' : '');
  appendSyncLog_(runId, 'GHL-Quick', 'SUCCESS', started, new Date(), opportunities.length, out.length, '', '', note, 'freshen');
  return { service: 'GHL-Quick', opportunitiesRead: opportunities.length, leadsWritten: out.length,
           stageChanges: moved, newLeads: added, deferred: deferred, funnelRows: funnelRows };
}

/**
 * Pull the latest from Meta and GHL on demand — this is what the dashboard calls on
 * every page load, so that opening the URL always shows current data.
 *
 * Deliberately narrow. Meta gets a short rolling window because older days are settled
 * and re-reading them costs minutes and trips the Graph API rate limiter (seen as
 * "There have been too many calls" on 2026-08-05); GHL gets stages only, for the
 * reasons in refreshGHLStages_. The nightly full sync is what reconciles everything.
 *
 * Failures are collected, not thrown: if GHL's token is dead the Meta numbers should
 * still refresh, and the dashboard should say what broke rather than show nothing.
 */
function freshenDashboard(request) {
  request = request || {};
  assertAccess_(request.accessKey);

  const props = PropertiesService.getScriptProperties();
  const now = new Date();
  const lastIso = prop_('LAST_FRESHEN_AT', '');
  // Repeated refreshes of the browser tab must not each trigger an API round trip;
  // both platforms rate-limit, and Meta has already thrown 400s for call volume.
  const minGap = asNumber_(prop_('FRESHEN_MIN_GAP_SECONDS', 120));
  if (!request.force && lastIso) {
    const age = (now.getTime() - new Date(lastIso).getTime()) / 1000;
    if (age >= 0 && age < minGap) {
      return { ran: false, reason: 'recent', secondsAgo: Math.round(age), lastFreshenAt: lastIso };
    }
  }

  const runId = makeRunId_('freshen');
  const result = { ran: true, errors: [], meta: null, ghl: null };

  try {
    result.meta = syncMetaDaily_(runId, asNumber_(prop_('FRESHEN_META_DAYS', 3)));
  } catch (e) {
    result.errors.push('Meta: ' + e.message);
    appendErrorLog_(runId, 'Meta', 'freshenDashboard', 'ERROR', e.message, '', '', e.stack, {}, 'freshen');
  }
  try {
    result.ghl = refreshGHLStages_(runId);
  } catch (e) {
    result.errors.push('GHL: ' + e.message);
    appendErrorLog_(runId, 'GHL', 'freshenDashboard', 'ERROR', e.message, '', '', e.stack, {}, 'freshen');
  }

  props.setProperty('LAST_FRESHEN_AT', now.toISOString());
  clearDashboardCache_();
  result.lastFreshenAt = now.toISOString();
  result.ok = !result.errors.length;
  return result;
}

// ==================== 05_Forecast.gs ====================
/** Scenario forecasting. */
function defaultForecastAssumptions_(){return [
  {metric:'forecastDays',label:'Forecast days',conservative:90,base:90,aggressive:90,unit:'days'},
  {metric:'budget',label:'Advertising budget',conservative:15000,base:25000,aggressive:40000,unit:'SGD'},
  {metric:'cpl',label:'Cost per lead',conservative:90,base:65,aggressive:50,unit:'SGD'},
  {metric:'responseRate',label:'Lead to responded',conservative:0.30,base:0.42,aggressive:0.52,unit:'rate'},
  {metric:'bookingRate',label:'Responded to booked call',conservative:0.20,base:0.28,aggressive:0.36,unit:'rate'},
  {metric:'showRate',label:'Booked call to appointment',conservative:0.60,base:0.72,aggressive:0.82,unit:'rate'},
  {metric:'qualificationRate',label:'Appointment to qualified',conservative:0.45,base:0.55,aggressive:0.65,unit:'rate'},
  {metric:'closeRate',label:'Qualified to close',conservative:0.12,base:0.20,aggressive:0.28,unit:'rate'},
  {metric:'averageCommission',label:'Average net commission per close',conservative:15000,base:18000,aggressive:22000,unit:'SGD'},
  {metric:'collectionRate',label:'Revenue collection rate',conservative:0.85,base:0.90,aggressive:0.95,unit:'rate'},
  {metric:'variableCostPerClose',label:'Variable cost per close',conservative:2000,base:1500,aggressive:1000,unit:'SGD'}
];}

function getForecastData_(){
  let rows=sheetRowsAsObjects_(APP.TABS.ASSUMPTIONS);if(!rows.length){seedForecastAssumptions_();rows=sheetRowsAsObjects_(APP.TABS.ASSUMPTIONS);}
  const scenarios=['Conservative','Base','Aggressive'].map(name=>{const key=name.toLowerCase();const values={};rows.forEach(r=>values[r.metric]=asNumber_(r[key]));values.scenarioName=name;return calculateOneForecast_(values);});
  writeForecastOutput_(scenarios);return {assumptions:rows,scenarios:scenarios,historical:calculateHistoricalRates_()};
}

function calculateOneForecast_(v){
  const budget=asNumber_(v.budget),cpl=Math.max(0.01,asNumber_(v.cpl)),leads=budget/cpl,responded=leads*asNumber_(v.responseRate),booked=responded*asNumber_(v.bookingRate),shows=booked*asNumber_(v.showRate),qualified=shows*asNumber_(v.qualificationRate),closings=qualified*asNumber_(v.closeRate),gross=closings*asNumber_(v.averageCommission),collected=gross*asNumber_(v.collectionRate),net=collected-budget-closings*asNumber_(v.variableCostPerClose);
  return Object.assign({},v,{scenarioName:v.scenarioName||'Custom',forecastDays:asNumber_(v.forecastDays)||90,budget:budget,cpl:cpl,leads:leads,responded:responded,bookedCalls:booked,shows:shows,qualified:qualified,closings:closings,grossRevenue:gross,collectedRevenue:collected,costPerClose:closings?budget/closings:0,roas:budget?collected/budget:0,netContribution:net});
}

function seedForecastAssumptions_(){
  const headers=['metric','label','conservative','base','aggressive','unit','source','lastUpdated','notes'];const now=nowIso_();const rows=defaultForecastAssumptions_().map(r=>Object.assign({},r,{source:'Initial management assumptions — replace with weighted historical rates after sufficient data',lastUpdated:now,notes:''}));overwriteObjects_(APP.TABS.ASSUMPTIONS,headers,rows);
}

function writeForecastOutput_(scenarios){
  const headers=['scenarioName','forecastDays','budget','cpl','leads','responseRate','responded','bookingRate','bookedCalls','showRate','shows','qualificationRate','qualified','closeRate','closings','averageCommission','grossRevenue','collectionRate','collectedRevenue','netContribution'];overwriteObjects_(APP.TABS.FORECAST,headers,scenarios);
}

function calculateHistoricalRates_(){
  const today=sgtDate_(new Date());const windows=[{name:'last30',start:addDaysIso_(today,-29),end:today,weight:.5},{name:'prior30',start:addDaysIso_(today,-59),end:addDaysIso_(today,-30),weight:.3},{name:'days61to90',start:addDaysIso_(today,-89),end:addDaysIso_(today,-60),weight:.2}];let weighted={cpl:0,responseRate:0,bookingRate:0,showRate:0,qualificationRate:0,closeRate:0},weightUsed=0;
  windows.forEach(w=>{const perf=sheetRowsAsObjects_(APP.TABS.PERFORMANCE).filter(r=>inDateRange_(r,w));const funnel=sheetRowsAsObjects_(APP.TABS.FUNNEL).filter(r=>inDateRange_(r,w));const o=aggregateOverview_(perf,funnel);if(o.leads>0){Object.keys(weighted).forEach(k=>weighted[k]+=asNumber_(o[k])*w.weight);weightUsed+=w.weight;}});if(weightUsed>0)Object.keys(weighted).forEach(k=>weighted[k]/=weightUsed);return weighted;
}

// ==================== 06_LogsHealth.gs ====================
/** Logging, retries and health monitoring. */
function appendSyncLog_(runId,service,status,started,completed,read,written,dateFrom,dateTo,message,triggerType){
  appendLogRow_(APP.TABS.SYNC_LOG,TAB_HEADERS.Sync_Log,[nowIso_(),runId,service,status,started?started.toISOString():'',completed?completed.toISOString():'',started&&completed?(completed-started)/1000:'',read||0,written||0,dateFrom||'',dateTo||'',message||'',triggerType||'',APP.VERSION]);
}
function appendErrorLog_(runId,service,fn,severity,message,httpCode,responseSnippet,stack,context,triggerType){appendLogRow_(APP.TABS.ERROR_LOG,TAB_HEADERS.Error_Log,[nowIso_(),runId||'',service||'',fn||'',severity||'ERROR',message||'',httpCode||'',responseSnippet||'',stack||'',JSON.stringify(context||{}),triggerType||'',APP.VERSION]);}
function appendAuditLog_(actor,action,entityType,entityId,oldValue,newValue,source,requestId,result){appendLogRow_(APP.TABS.AUDIT_LOG,TAB_HEADERS.Audit_Log,[nowIso_(),actor||'',action||'',entityType||'',entityId||'',oldValue||'',newValue||'',source||'',requestId||'',result||'',APP.VERSION]);}
function appendLogRow_(sheetName,headers,row){const sheet=getSheet_(sheetName,true);if(sheet.getLastRow()===0)sheet.appendRow(headers);sheet.appendRow(row);}

function fetchWithRetry_(url,options,service,runId){
  let lastErr;for(let attempt=1;attempt<=4;attempt++){try{const res=UrlFetchApp.fetch(url,options||{});const code=res.getResponseCode();if(code===429||code>=500){lastErr=new Error(service+' HTTP '+code);Utilities.sleep(Math.min(8000,Math.pow(2,attempt)*500));continue;}return res;}catch(e){lastErr=e;Utilities.sleep(Math.min(8000,Math.pow(2,attempt)*500));}}
  appendErrorLog_(runId,service,'fetchWithRetry_','ERROR',lastErr&&lastErr.message,'','',lastErr&&lastErr.stack,{url:url.slice(0,250)},'sync');throw lastErr;
}

function buildHealthReport_(light){
  const checks=[];const props=['META_ACCESS_TOKEN','META_AD_ACCOUNT_ID','GHL_API_KEY','GHL_LOCATION_ID','GHL_PIPELINE_ID'];props.forEach(p=>checks.push({name:p,status:prop_(p,'')?'OK':'MISSING',detail:prop_(p,'')?'Configured':'Run setup and set this Script Property'}));
  Object.keys(APP.TABS).forEach(k=>{const name=APP.TABS[k];const sh=getSheet_(name,false);checks.push({name:'Sheet: '+name,status:sh?'OK':'MISSING',detail:sh?Math.max(0,sh.getLastRow()-1)+' data rows':'Run setupV9()'});});
  const syncRows=sheetRowsAsObjects_(APP.TABS.SYNC_LOG);const last={};syncRows.forEach(r=>{const s=safeText_(r.service);if(!last[s]||safeText_(r.timestamp)>safeText_(last[s].timestamp))last[s]=r;});
  Object.keys(last).forEach(s=>checks.push({name:'Last '+s+' sync',status:safeText_(last[s].status)==='SUCCESS'?'OK':'ERROR',detail:safeText_(last[s].timestamp)+' — '+safeText_(last[s].message)}));

  // Errors logged AFTER the last successful sync. Without this, a token that expired
  // an hour ago still reads green because the last SUCCESS row never changes.
  // This is what let an expired Meta token (16-Jul) sit unnoticed for two weeks.
  try{
    const errs=sheetRowsAsObjects_(APP.TABS.ERROR_LOG);
    const recent={};
    errs.forEach(r=>{
      const svc=safeText_(r.service); if(!svc) return;
      const ts=safeText_(r.timestamp);
      const lastOk=last[svc]&&safeText_(last[svc].status)==='SUCCESS'?safeText_(last[svc].timestamp):'';
      if(ts>lastOk&&(!recent[svc]||ts>safeText_(recent[svc].timestamp)))recent[svc]=r;
    });
    Object.keys(recent).forEach(svc=>checks.push({
      name:svc+' — errors since last success',
      status:'ERROR',
      detail:safeText_(recent[svc].timestamp)+' — '+safeText_(recent[svc].message).slice(0,240)
    }));
  }catch(e){checks.push({name:'Error-log review',status:'WARN',detail:'Could not read Error_Log: '+(e&&e.message||e)});}

  // Token lifetime, so an expiring credential is visible before it breaks the syncs.
  try{
    const days = metaTokenDaysRemaining_();
    if (days === null) {
      checks.push({name:'Meta token expiry',status:'WARN',detail:'Unknown — set META_APP_ID and META_APP_SECRET to enable auto-refresh and expiry tracking'});
    } else if (days === Infinity) {
      checks.push({name:'Meta token expiry',status:'OK',detail:'Never expires (system user token)'});
    } else {
      checks.push({name:'Meta token expiry',status:days>14?'OK':days>3?'WARN':'ERROR',detail:days+' day(s) remaining. Auto-refresh runs weekly; last refresh '+(prop_('META_TOKEN_REFRESHED_AT','')||'never')});
    }
  }catch(e){checks.push({name:'Meta token expiry',status:'WARN',detail:'Could not check: '+(e&&e.message||e)});}

  // Staleness of the actual data, not of the sync attempt. A sync can report SUCCESS
  // while writing nothing new, so measure the newest fact row instead.
  try{
    const perfRows=sheetRowsAsObjects_(APP.TABS.PERFORMANCE);
    let newest='';
    perfRows.forEach(r=>{const d=r.date instanceof Date?Utilities.formatDate(r.date,APP.TZ,'yyyy-MM-dd'):safeText_(r.date).slice(0,10);if(d>newest)newest=d;});
    const today=sgtDate_(new Date());
    const ageDays=newest?Math.round((new Date(today+'T00:00:00Z')-new Date(newest+'T00:00:00Z'))/86400000):null;
    checks.push({
      name:'Performance data freshness',
      status:newest?(ageDays<=2?'OK':ageDays<=7?'WARN':'ERROR'):'ERROR',
      detail:newest?('Newest row '+newest+' ('+ageDays+' day'+(ageDays===1?'':'s')+' old)'):'No dated rows found'
    });
  }catch(e){checks.push({name:'Performance data freshness',status:'WARN',detail:'Could not evaluate: '+(e&&e.message||e)});}
  const report={generatedAt:nowIso_(),overall:checks.some(c=>c.status==='ERROR')?'ERROR':checks.some(c=>c.status==='MISSING')?'SETUP REQUIRED':'HEALTHY',checks:checks};
  if(!light)writeHealthSheet_(report);return report;
}
function writeHealthSheet_(report){const headers=['check','status','detail','checkedAt'];overwriteObjects_(APP.TABS.HEALTH,headers,report.checks.map(c=>({check:c.name,status:c.status,detail:c.detail,checkedAt:report.generatedAt})));}

// ==================== 08_Insights.gs (added v9.1, 2026-07-31) ====================
/**
 * Decision layer. Three audiences, one dataset:
 *   Media buyer — per-ad and per-ad-set economics with a Kill/Scale verdict
 *   CEO         — stage-by-stage conversion with the biggest leak named
 *   Agents      — who to follow up next, grouped by GHL pipeline stage
 *
 * Everything here is READ-ONLY. Nothing writes to Meta, GHL, or the ad account.
 *
 * Range-filtered performance comes from Daily_Performance_Fact (daily grain, carries
 * adId/adSetId). Creative metadata (thumbnail, hook rate, permalink) comes from the
 * Meta_Ads snapshot, which is current-state only — so metadata reflects "now" while
 * the money reflects the selected range. That is intentional and matches how Meta
 * itself reports.
 */

/**
 * Kill/scale rules, as specified by Edmund 2026-08-02. All tunable via Script
 * Properties so the thresholds move without a code change.
 *
 * TARGET_CPA is the anchor. Edmund's working band is 150-250; the default sits at the
 * midpoint. Everything else keys off it.
 */
function signalThresholds_() {
  return {
    targetCpa:        asNumber_(prop_('TARGET_CPA', prop_('TARGET_CPL', 200))),
    cpaKillMult:      asNumber_(prop_('KILL_CPA_MULT', 2)),        // CPA >= 2x target
    killSpendMult:    asNumber_(prop_('KILL_SPEND_MULT', 2)),      // ...and >= 2x target spent
    ctrFloor:         asNumber_(prop_('KILL_CTR_FLOOR', 0.5)),     // % link CTR
    ctrMinImpr:       asNumber_(prop_('KILL_CTR_MIN_IMPRESSIONS', 1000)),
    freqCeiling:      asNumber_(prop_('KILL_FREQUENCY', 3.5)),
    ctrDeclinePct:    asNumber_(prop_('KILL_CTR_DECLINE_PCT', 30)),
    trendDays:        asNumber_(prop_('TREND_WINDOW_DAYS', 14)),
    scaleCpaMult:     asNumber_(prop_('SCALE_CPA_MULT', 0.7)),     // CPA <= 70% of target
    minLeads:         asNumber_(prop_('SIGNAL_MIN_LEADS', 3))
  };
}

/**
 * Evaluate one ad against the kill rules. Returns every rule that fired, not just the
 * first, because "expensive AND saturated AND declining" is a different conversation
 * from any one of those alone.
 *
 * Rules (Edmund's, verbatim intent):
 *   1. CPA >= 2x target AND spend >= 2x target   — proven expensive, enough spend to trust
 *   2. CTR < 0.5% once impressions >= 1,000      — creative is not earning the click
 *   3. Frequency >= 3.5 AND CPA rising           — audience saturated and getting worse
 *   4. CTR down >= 30% across two windows        — creative fatigue
 *
 * A rule needing trend data is skipped rather than guessed at when history is too thin.
 */
function evaluateAdRules_(x, t) {
  const fired = [];
  const cpa = x.leads > 0 ? x.spend / x.leads : 0;
  const money = function (n) { return '$' + Math.round(n); };

  if (x.leads > 0 && cpa >= t.targetCpa * t.cpaKillMult && x.spend >= t.targetCpa * t.killSpendMult) {
    fired.push({ rule: 'CPA', text: 'CPA ' + money(cpa) + ' is ' + (cpa / t.targetCpa).toFixed(1) + 'x target on ' + money(x.spend) + ' spent' });
  }
  if (x.leads === 0 && x.spend >= t.targetCpa * t.killSpendMult) {
    fired.push({ rule: 'CPA', text: money(x.spend) + ' spent, zero leads' });
  }
  if (x.impressions >= t.ctrMinImpr && x.ctr > 0 && x.ctr < t.ctrFloor) {
    fired.push({ rule: 'CTR', text: 'CTR ' + x.ctr.toFixed(2) + '% below ' + t.ctrFloor + '% on ' + Math.round(x.impressions).toLocaleString() + ' impressions' });
  }
  if (x.frequency >= t.freqCeiling && x.cpaChangePct !== null && x.cpaChangePct > 0) {
    fired.push({ rule: 'FREQ', text: 'Frequency ' + x.frequency.toFixed(1) + ' and CPA up ' + Math.round(x.cpaChangePct) + '% — audience saturated' });
  }
  if (x.ctrChangePct !== null && x.ctrChangePct <= -t.ctrDeclinePct) {
    fired.push({ rule: 'FATIGUE', text: 'CTR down ' + Math.abs(Math.round(x.ctrChangePct)) + '% vs previous ' + t.trendDays + ' days' });
  }
  return { fired: fired, cpa: cpa };
}

/**
 * Verdict for one ad. KILL when any rule fires; SCALE only on proven cheap volume;
 * TEST while there is not yet enough spend or volume to judge — a good CPA on one lead
 * is noise, and calling it a winner is how budget gets wasted.
 */
function adSignal_(x, t) {
  const ev = evaluateAdRules_(x, t);
  x.firedRules = ev.fired.map(f => f.rule);

  if (ev.fired.length) {
    return { signal: 'KILL', reason: ev.fired.map(f => f.text).join(' · '), rules: ev.fired };
  }
  const enoughToJudge = x.spend >= t.targetCpa || x.leads >= t.minLeads;
  if (!enoughToJudge) {
    return { signal: 'TEST', reason: 'Too early — under ' + Math.round(t.targetCpa) + ' spent and fewer than ' + t.minLeads + ' leads', rules: [] };
  }
  if (x.leads >= t.minLeads && ev.cpa > 0 && ev.cpa <= t.targetCpa * t.scaleCpaMult) {
    return { signal: 'SCALE', reason: 'CPA $' + Math.round(ev.cpa) + ' vs $' + Math.round(t.targetCpa) + ' target' + (x.ctrChangePct > 0 ? ', CTR still rising' : ''), rules: [] };
  }
  return { signal: 'MONITOR', reason: ev.cpa > 0 ? ('CPA $' + Math.round(ev.cpa) + ' — inside tolerance, watching') : 'Spending, no leads yet', rules: [] };
}

/**
 * Per-ad economics for the selected range, joined to current creative metadata, plus
 * the trend signals the kill rules need.
 *
 * Trend windows are anchored on TODAY, not on the selected range — "is this ad fatiguing
 * right now" is a question about the present, and would be meaningless if it drifted
 * with whatever period happens to be on screen.
 *
 * Frequency note: computed as impressions / summed daily reach. Daily reach counts a
 * person again on each day they are reached, so the sum OVERSTATES unique reach and this
 * figure therefore UNDERSTATES true period frequency. That error is deliberate in this
 * direction — it makes the saturation rule fire late rather than early, so no ad is
 * killed on an overstated number.
 */
function aggregateAds_(perf) {
  const t = signalThresholds_(), meta = {};
  sheetRowsAsObjects_(APP.TABS.META_ADS).forEach(a => { if (safeText_(a.metaId)) meta[safeText_(a.metaId)] = a; });

  const today = sgtDate_(new Date());
  const recentFrom = addDaysIso_(today, -(t.trendDays - 1));
  const priorFrom = addDaysIso_(today, -(t.trendDays * 2 - 1));
  const priorTo = addDaysIso_(recentFrom, -1);

  // Trend windows read from the full fact table, independent of the on-screen range.
  const allRows = sheetRowsAsObjects_(APP.TABS.PERFORMANCE);
  const win = {};
  allRows.forEach(r => {
    const id = safeText_(r.adId); if (!id) return;
    const d = dayKey_(r.date); if (!d) return;
    const bucket = (d >= recentFrom && d <= today) ? 'recent' : (d >= priorFrom && d <= priorTo) ? 'prior' : null;
    if (!win[id]) win[id] = { recent: { impr: 0, clicks: 0, spend: 0, leads: 0 }, prior: { impr: 0, clicks: 0, spend: 0, leads: 0 }, first: d };
    if (d < win[id].first) win[id].first = d;
    if (!bucket) return;
    const b = win[id][bucket];
    b.impr += asNumber_(r.impressions); b.clicks += asNumber_(r.clicks);
    b.spend += asNumber_(r.spend); b.leads += asNumber_(r.leads);
  });

  const map = {};
  perf.forEach(r => {
    const id = safeText_(r.adId); if (!id) return;
    if (!map[id]) map[id] = {
      adId: id, adName: safeText_(r.adName), adSetId: safeText_(r.adSetId), adSetName: safeText_(r.adSetName),
      campaignId: safeText_(r.campaignId), campaignName: safeText_(r.campaignName), platform: safeText_(r.platform),
      spend: 0, impressions: 0, reach: 0, clicks: 0, leads: 0
    };
    const x = map[id];
    x.spend += asNumber_(r.spend); x.impressions += asNumber_(r.impressions);
    x.reach += asNumber_(r.reach); x.clicks += asNumber_(r.clicks); x.leads += asNumber_(r.leads);
  });

  const pctChange = function (now, was) { return was > 0 ? ((now - was) / was) * 100 : null; };

  return Object.keys(map).map(id => {
    const x = map[id], m = meta[id] || {}, w = win[id];
    x.hookrate = asNumber_(m.hookrate);
    x.status = safeText_(m.status);
    x.format = safeText_(m.format);
    x.thumbUrl = safeText_(m.thumbUrl) || safeText_(m.imageUrl);
    x.videoSrc = safeText_(m.videoSrc);
    x.adPermalink = safeText_(m.adPermalink);
    x.cpl = x.leads > 0 ? x.spend / x.leads : 0;
    x.cpa = x.cpl;
    x.ctr = x.impressions > 0 ? (x.clicks / x.impressions) * 100 : 0;
    x.cpc = x.clicks > 0 ? x.spend / x.clicks : 0;
    x.cpm = x.impressions > 0 ? (x.spend / x.impressions) * 1000 : 0;
    x.frequency = x.reach > 0 ? x.impressions / x.reach : 0;

    // Trend comparisons. Null where a window has no data — the rules skip nulls rather
    // than treating "no history" as "no change".
    if (w) {
      const rc = w.recent.impr > 0 ? (w.recent.clicks / w.recent.impr) * 100 : null;
      const pc = w.prior.impr > 0 ? (w.prior.clicks / w.prior.impr) * 100 : null;
      x.recentCtr = rc; x.priorCtr = pc;
      x.ctrChangePct = (rc !== null && pc !== null) ? pctChange(rc, pc) : null;

      const rcpa = w.recent.leads > 0 ? w.recent.spend / w.recent.leads : null;
      const pcpa = w.prior.leads > 0 ? w.prior.spend / w.prior.leads : null;
      x.recentCpa = rcpa; x.priorCpa = pcpa;
      x.cpaChangePct = (rcpa !== null && pcpa !== null) ? pctChange(rcpa, pcpa) : null;

      x.firstSeen = w.first;
      x.isNew = w.first >= recentFrom;      // launched inside the trend window
    } else {
      x.ctrChangePct = null; x.cpaChangePct = null; x.isNew = false;
    }

    const s = adSignal_(x, t);
    x.signal = s.signal; x.signalReason = s.reason; x.rules = s.rules || [];
    return x;
  }).sort((a, b) => b.spend - a.spend);
}

/** Per-ad-set economics — which audience/targeting is working. */
function aggregateAdSets_(perf) {
  const t = signalThresholds_(), meta = {};
  sheetRowsAsObjects_(APP.TABS.META_ADSETS).forEach(a => { if (safeText_(a.metaId)) meta[safeText_(a.metaId)] = a; });

  const map = {};
  perf.forEach(r => {
    const id = safeText_(r.adSetId); if (!id) return;
    if (!map[id]) map[id] = {
      adSetId: id, adSetName: safeText_(r.adSetName), campaignId: safeText_(r.campaignId),
      campaignName: safeText_(r.campaignName), platform: safeText_(r.platform),
      spend: 0, impressions: 0, reach: 0, clicks: 0, leads: 0, adIds: {}
    };
    const x = map[id];
    x.spend += asNumber_(r.spend); x.impressions += asNumber_(r.impressions);
    x.reach += asNumber_(r.reach);
    x.clicks += asNumber_(r.clicks); x.leads += asNumber_(r.leads);
    if (safeText_(r.adId)) x.adIds[safeText_(r.adId)] = 1;
  });

  return Object.keys(map).map(id => {
    const x = map[id], m = meta[id] || {};
    x.adCount = Object.keys(x.adIds).length; delete x.adIds;
    x.budget = asNumber_(m.budget); x.audience = safeText_(m.audience); x.status = safeText_(m.status);
    x.cpl = x.leads > 0 ? x.spend / x.leads : 0;
    x.cpa = x.cpl;
    x.ctr = x.impressions > 0 ? (x.clicks / x.impressions) * 100 : 0;
    x.frequency = x.reach > 0 ? x.impressions / x.reach : 0;
    // Ad sets are judged on the volume rules only; fatigue and saturation are creative-
    // level questions, so their trend inputs stay null rather than being faked at 0.
    x.ctrChangePct = null; x.cpaChangePct = null;
    const s = adSignal_(x, t);
    x.signal = s.signal; x.signalReason = s.reason;
    return x;
  }).sort((a, b) => b.spend - a.spend);
}

/**
 * Stage-by-stage conversion following the live GHL 1-To-1 Pipeline, and the leak.
 * Steps mirror the pipeline exactly: New Lead > Responded > Booked Call >
 * Appointment > Strategy Session > Close.
 *
 * The "leak" is the weakest step by conversion rate, ignoring steps whose entry
 * volume is too small to read (a 0% step with 1 lead in it is noise, not a leak).
 */
/**
 * Stage-to-stage conversion, splitting the gap into people still being worked and
 * people genuinely gone.
 *
 * fromCount - to is NOT a loss. Someone who reached Booked Call and has not yet reached
 * Appointment is usually sitting in Booked Call right now, live and workable. Reporting
 * that as "lost" turned a 120-person follow-up list into what looked like a 120-person
 * haemorrhage. stayStages names the stages a lead occupies while stalled at a step, so
 * waiting + dropped reconciles exactly to the gap.
 */
function buildStageConversions_(f, census) {
  const minVolume = asNumber_(prop_('LEAK_MIN_VOLUME', 5));
  const pct = function (num, den) { return den > 0 ? (num / den) * 100 : 0; };

  const c = (census && census.all) ? census.all : (census || {});
  const live = c.live || {}, dead = c.dead || {};
  const sum = function (map, keys) {
    return keys.reduce(function (n, k) { return n + asNumber_(map[k]); }, 0);
  };

  /* GHL's Unqualified stage normalises to 'Lost' and carries no pipeline position, so a
     lead parked there loses its history and can only be accounted for at entry. */
  const steps = [
    { key: 'lead_responded',      label: 'New Lead → Responded',           from: 'New Leads',        fromCount: f.newLeads,         to: f.responded,        stayStages: ['New', 'Contacted', 'Lost'] },
    { key: 'responded_booked',    label: 'Responded → Booked Call',        from: 'Responded',        fromCount: f.responded,        to: f.bookedCalls,      stayStages: ['Responded'] },
    { key: 'booked_appointment',  label: 'Booked Call → Appointment',      from: 'Booked Calls',     fromCount: f.bookedCalls,      to: f.appointments,     stayStages: ['Booked Call'] },
    { key: 'appointment_session', label: 'Appointment → Strategy Session', from: 'Appointments',     fromCount: f.appointments,     to: f.strategySessions, stayStages: ['Appointment', 'Nurture'] },
    { key: 'session_closed',      label: 'Strategy Session → Closed',      from: 'Strategy Sessions', fromCount: f.strategySessions, to: f.closedWon,        stayStages: ['Strategy Session'] }
  ].map(s => {
    s.rate = pct(s.to, s.fromCount);
    s.gap = Math.max(0, s.fromCount - s.to);
    s.waiting = sum(live, s.stayStages);
    s.dropped = sum(dead, s.stayStages);
    /* Never report more than the gap allows, and never silently lose a person: any
       remainder the census cannot explain stays visible as still-waiting. */
    if (s.waiting + s.dropped !== s.gap) s.waiting = Math.max(0, s.gap - s.dropped);
    s.readable = s.fromCount >= minVolume;
    return s;
  });

  const readable = steps.filter(s => s.readable);
  let leak = null;
  if (readable.length) {
    leak = readable.reduce((worst, s) => (s.rate < worst.rate ? s : worst), readable[0]);
  }

  return {
    steps: steps,
    leak: leak ? { key: leak.key, label: leak.label, rate: leak.rate, dropped: leak.dropped, waiting: leak.waiting, gap: leak.gap } : null,
    leakNote: leak ? null : 'Not enough volume yet to identify a leak (needs ' + minVolume + '+ entering a stage).',
    overall: { rate: pct(f.closedWon, f.newLeads), from: f.newLeads, to: f.closedWon },
    minVolume: minVolume
  };
}

/**
 * Agent view — the live pipeline grouped by stage, with the oldest-untouched first.
 * Terminal stages (Closed/Lost) are excluded: this answers "who do I call next",
 * not "what happened". No PII beyond what readRecentLeadSummaries_ already exposes.
 */
function buildPipelineByStage_(leads) {
  const today = sgtDate_(new Date());
  const daysBetween = function (iso) {
    if (!iso) return 0;
    const a = new Date(iso + 'T00:00:00Z'), b = new Date(today + 'T00:00:00Z');
    return Math.max(0, Math.round((b - a) / 86400000));
  };
  const active = CANONICAL_STAGES.filter(s => s !== 'Closed' && s !== 'Lost');
  const buckets = {};
  active.forEach(s => buckets[s] = []);

  (leads || []).forEach(l => {
    const stage = normaliseStage_(l.status);
    if (!buckets[stage]) return;                     // Closed/Lost drop out here
    const age = daysBetween(l.date);
    buckets[stage].push({
      id: l.id, name: l.name, stage: stage, platform: l.platform,
      campaignName: l.campaignName, sourceAdName: l.sourceAdName,
      quality: l.quality, date: l.date, daysInStage: age,
      stale: age >= asNumber_(prop_('STALE_DAYS', 7))
    });
  });

  return active.map(stage => {
    const rows = buckets[stage].sort((a, b) => b.daysInStage - a.daysInStage);
    return {
      stage: stage, count: rows.length,
      staleCount: rows.filter(r => r.stale).length,
      leads: rows.slice(0, 25)
    };
  }).filter(g => g.count > 0);
}

// ==================== 11_TokenRefresh.gs (added v9.3, 2026-08-01) ====================
/**
 * Keeps the Meta access token alive indefinitely.
 *
 * A long-lived Meta token lasts 60 days and does NOT renew itself. It can, however, be
 * exchanged for a fresh 60-day token at any point before it expires. Running that
 * exchange weekly means the clock resets long before it ever runs down, so the token
 * effectively never expires and nobody has to repeat the Graph Explorer dance.
 *
 * What this CANNOT survive, by design: a Facebook password change, the app being
 * removed, or Meta invalidating the session for security. Those require a new token by
 * hand — no automation can work around them. The health check surfaces days-remaining
 * so that case is visible early rather than discovered by empty data.
 *
 * Requires META_APP_ID and META_APP_SECRET in Script Properties. Secrets are read from
 * there and never written into source or logs.
 */
function refreshMetaToken() {
  const appId = prop_('META_APP_ID', '');
  const appSecret = prop_('META_APP_SECRET', '');
  const current = prop_('META_ACCESS_TOKEN', '');
  if (!appId || !appSecret) throw new Error('META_APP_ID and META_APP_SECRET must be set in Script Properties before the token can auto-refresh.');
  if (!current) throw new Error('META_ACCESS_TOKEN is missing — store a long-lived token first.');

  const url = 'https://graph.facebook.com/' + prop_('META_API_VERSION', 'v19.0') + '/oauth/access_token'
    + '?grant_type=fb_exchange_token'
    + '&client_id=' + encodeURIComponent(appId)
    + '&client_secret=' + encodeURIComponent(appSecret)
    + '&fb_exchange_token=' + encodeURIComponent(current);

  const res = UrlFetchApp.fetch(url, { method: 'get', muteHttpExceptions: true });
  const code = res.getResponseCode();
  let body;
  try { body = JSON.parse(res.getContentText()); }
  catch (e) { throw new Error('Token refresh returned non-JSON (HTTP ' + code + ').'); }

  if (code < 200 || code >= 300 || !body.access_token) {
    // Never echo the token or secret into the log — only Meta's own message.
    const why = (body && body.error && body.error.message) || ('HTTP ' + code);
    throw new Error('Token refresh failed: ' + why);
  }

  PropertiesService.getScriptProperties().setProperties({
    META_ACCESS_TOKEN: body.access_token,
    META_TOKEN_REFRESHED_AT: nowIso_()
  }, false);

  appendSyncLog_(makeRunId_('token'), 'Meta', 'SUCCESS', new Date(), new Date(), 0, 0, '', '',
    'Access token refreshed — 60-day window reset', 'scheduled');
  return { ok: true, refreshedAt: nowIso_() };
}

/** Scheduled wrapper — logs failures rather than throwing into the trigger runner. */
function scheduledMetaTokenRefresh() {
  try { refreshMetaToken(); }
  catch (e) {
    appendErrorLog_(makeRunId_('token'), 'Meta', 'scheduledMetaTokenRefresh', 'ERROR', e.message, '', '', e.stack, {}, 'scheduled');
  }
}

/** Days until the current token expires, via Meta's own debug endpoint. */
function metaTokenDaysRemaining_() {
  const appId = prop_('META_APP_ID', ''), appSecret = prop_('META_APP_SECRET', '');
  const token = prop_('META_ACCESS_TOKEN', '');
  if (!appId || !appSecret || !token) return null;
  const url = 'https://graph.facebook.com/' + prop_('META_API_VERSION', 'v19.0') + '/debug_token'
    + '?input_token=' + encodeURIComponent(token)
    + '&access_token=' + encodeURIComponent(appId + '|' + appSecret);
  const res = UrlFetchApp.fetch(url, { method: 'get', muteHttpExceptions: true });
  if (res.getResponseCode() !== 200) return null;
  let body; try { body = JSON.parse(res.getContentText()); } catch (e) { return null; }
  const exp = body && body.data && body.data.expires_at;
  if (exp === 0) return Infinity;                    // never-expiring (system user) token
  if (!exp) return null;
  return Math.round((exp * 1000 - new Date().getTime()) / 86400000);
}

/** Dashboard entry point so the refresh can be triggered without the script editor. */
function runTokenRefresh(request) {
  request = request || {};
  assertAccess_(request.accessKey);
  try {
    refreshMetaToken();
    const days = metaTokenDaysRemaining_();
    return { ok: true, message: 'Token refreshed. ' + (days === Infinity ? 'This token does not expire.' : days === null ? 'Expiry unknown.' : 'Valid for about ' + days + ' more days.') };
  } catch (e) {
    return { ok: false, message: e.message };
  }
}

// ==================== 10_Backfill.gs (added v9.2, 2026-07-31) ====================
/**
 * Historical Meta backfill.
 *
 * Routine syncs deliberately pull only a short rolling window (DEFAULT_META_DAYS) so
 * they finish well inside Apps Script's 6-minute execution limit. That is correct for
 * a 30-minute trigger, but it means the sheet never contains anything older than that
 * window — so "All time" was only ever showing the last 90 days of Meta spend.
 *
 * This walks backwards in month-sized chunks, writing each chunk as it goes and saving
 * a resume pointer. It stops before the execution limit rather than dying mid-write.
 * Re-run it until it reports DONE. Safe to re-run — rows upsert on their natural key.
 *
 * Run from the editor: backfillMetaHistory
 */
/**
 * Dashboard entry point for the backfill, so it can be run from the web app instead of
 * hunting for a function name in the Apps Script editor's ~100-entry dropdown.
 * Returns the same status string; the client re-runs until it sees DONE.
 */
function runMetaBackfill(request) {
  request = request || {};
  assertAccess_(request.accessKey);
  const message = backfillMetaHistory(true);
  return { ok: true, done: String(message).indexOf('DONE') === 0, message: message };
}

function backfillMetaHistory(silent) {
  const CHUNK_DAYS = 30;
  // 3 minutes: short enough that a browser call returns comfortably, long enough to
  // move several chunks per click. The hard platform limit is ~6.
  const SAFE_MS = 3 * 60 * 1000;
  // 2025-09-01: the account's first campaign started 2025-09-06, confirmed against
  // Edmund's own Meta export (1 Jul 2023 – 1 Aug 2026 pull, 123 campaigns, SGD 79,295).
  // Reaching further back only burns chunks on empty months.
  const EARLIEST = prop_('META_BACKFILL_EARLIEST', '2025-09-01');
  const started = new Date();
  const props = PropertiesService.getScriptProperties();

  let cursor = prop_('META_BACKFILL_CURSOR', '');
  if (!cursor) cursor = sgtDate_(new Date());   // first run starts today, walks back

  const runId = makeRunId_('backfill');
  let chunks = 0, rowsWritten = 0;

  while (cursor > EARLIEST) {
    if (new Date() - started > SAFE_MS) {
      props.setProperty('META_BACKFILL_CURSOR', cursor);
      const msg = 'Paused safely at ' + cursor + ' after ' + chunks + ' chunk(s), ' +
                  rowsWritten + ' rows. Run backfillMetaHistory again to continue.';
      if(!silent) uiAlert_(msg);
      return msg;
    }
    const end = cursor;
    const start = addDaysIso_(end, -(CHUNK_DAYS - 1));
    const from = start < EARLIEST ? EARLIEST : start;
    try {
      const res = syncMetaDaily_(runId, null, from, end);
      rowsWritten += asNumber_(res && res.recordsWritten);
      chunks++;
    } catch (e) {
      props.setProperty('META_BACKFILL_CURSOR', cursor);
      appendErrorLog_(runId, 'Meta', 'backfillMetaHistory', 'ERROR', e.message, '', '', e.stack, { from: from, end: end }, 'backfill');
      const msg = 'Stopped at ' + from + ' to ' + end + ': ' + e.message +
                  '\n\nProgress saved — fix the cause and run again to resume.';
      if(!silent) uiAlert_(msg);
      return msg;
    }
    cursor = addDaysIso_(from, -1);
  }

  props.deleteProperty('META_BACKFILL_CURSOR');

  // Each chunk overwrites the Meta_Ads / Meta_AdSets snapshot tabs, and this walks
  // backwards — so without this the snapshot would be left showing the OLDEST period's
  // creatives. One final current-window sync restores them. (The 30-minute trigger
  // would also heal this on its own, but not before someone looked at a wrong screen.)
  try { syncMetaDaily_(runId, APP.DEFAULT_META_DAYS); }
  catch (e) { appendErrorLog_(runId, 'Meta', 'backfillMetaHistory', 'WARN', 'History written, but the closing snapshot refresh failed: ' + e.message, '', '', e.stack, {}, 'backfill'); }

  clearDashboardCache_();
  const msg = 'DONE — Meta history backfilled to ' + EARLIEST + '. ' + chunks +
              ' chunk(s), ' + rowsWritten + ' rows written. Reload the dashboard.';
  if(!silent) uiAlert_(msg);
  return msg;
}

/**
 * Wipe every Meta row from Daily_Performance_Fact and reset the backfill cursor, so the
 * next backfill rebuilds Meta history from clean ground.
 *
 * Needed once, because rows written before the dayKey_ fix were duplicated (mismatched
 * upsert keys) and carried inflated lead counts from the old summing extraction.
 * Correcting the code does not correct rows already on the sheet.
 *
 * Only Meta rows are removed. Google rows come from a different source and are left
 * untouched. Nothing here is irreversible: every removed row is re-fetchable from the
 * Meta API, which is the whole point of a fact table.
 */
function rebuildMetaDataFromScratch() {
  const rows = sheetRowsAsObjects_(APP.TABS.PERFORMANCE);
  const kept = rows.filter(r => platformOf_(r.platform) !== 'Meta');
  const removed = rows.length - kept.length;

  // Re-normalise dates on the way out so the surviving rows key consistently too.
  kept.forEach(r => { r.date = dayKey_(r.date); });
  overwriteObjects_(APP.TABS.PERFORMANCE, TAB_HEADERS.Daily_Performance_Fact, kept);

  PropertiesService.getScriptProperties().deleteProperty('META_BACKFILL_CURSOR');
  clearDashboardCache_();

  const msg = 'Removed ' + removed + ' Meta row(s); ' + kept.length + ' non-Meta row(s) kept. ' +
              'Backfill cursor reset. Now click "Backfill Meta history" repeatedly until it says DONE.';
  uiAlert_(msg);
  return msg;
}

/** Dashboard entry point for the rebuild. */
function runMetaRebuild(request) {
  request = request || {};
  assertAccess_(request.accessKey);
  return { ok: true, message: rebuildMetaDataFromScratch() };
}

/** Clear the resume pointer to force the next backfill to start from today again. */
function resetMetaBackfill() {
  PropertiesService.getScriptProperties().deleteProperty('META_BACKFILL_CURSOR');
  uiAlert_('Backfill cursor cleared. The next backfillMetaHistory run starts from today.');
}

// ==================== 09_Segments.gs (added v9.2, 2026-07-31) ====================
/**
 * Platform separation, month-over-month, and creative-format analysis.
 *
 * Why platform separation is not optional: Meta and Google behave nothing alike in
 * this account (Meta ~$96 CPL with attributed revenue; Google ~$515 CPL with none).
 * A blended number hides that completely and would have you optimising an average
 * that describes neither channel.
 *
 * Read-only. Nothing here writes to Meta, Google or GHL.
 */

/** Canonical platform buckets. Anything unrecognised lands in Other rather than being
 *  silently folded into a real channel. */
function platformOf_(value) {
  const p = safeText_(value).toLowerCase();
  if (p.indexOf('meta') >= 0 || p.indexOf('facebook') >= 0 || p.indexOf('instagram') >= 0) return 'Meta';
  if (p.indexOf('google') >= 0 || p.indexOf('youtube') >= 0) return 'Google';
  return 'Other';
}

function emptySegment_(name) {
  return { platform: name, spend: 0, impressions: 0, clicks: 0, leads: 0,
           newLeads: 0, responded: 0, bookedCalls: 0, appointments: 0,
           strategySessions: 0, qualified: 0, closedWon: 0, revenue: 0 };
}

function finaliseSegment_(x) {
  x.cpl = x.leads > 0 ? x.spend / x.leads : 0;
  x.ctr = x.impressions > 0 ? (x.clicks / x.impressions) * 100 : 0;
  x.cpc = x.clicks > 0 ? x.spend / x.clicks : 0;
  x.costPerBooked = x.bookedCalls > 0 ? x.spend / x.bookedCalls : 0;
  x.costPerAppointment = x.appointments > 0 ? x.spend / x.appointments : 0;
  x.costPerStrategySession = x.strategySessions > 0 ? x.spend / x.strategySessions : 0;
  x.leadToAppointment = x.leads > 0 ? (x.appointments / x.leads) * 100 : 0;
  x.showRate = x.bookedCalls > 0 ? x.appointments / x.bookedCalls : 0;
  x.responseRate = (x.newLeads || x.leads) > 0 ? x.responded / (x.newLeads || x.leads) : 0;
  x.costPerClose = x.closedWon > 0 ? x.spend / x.closedWon : 0;
  x.roas = x.spend > 0 ? x.revenue / x.spend : 0;
  x.leadToBooked = x.leads > 0 ? (x.bookedCalls / x.leads) * 100 : 0;
  x.leadToClose = x.leads > 0 ? (x.closedWon / x.leads) * 100 : 0;
  return x;
}

/** Meta / Google / Other side by side, plus the combined total. */
function buildPlatformBreakdown_(perf, funnel) {
  const seg = { Meta: emptySegment_('Meta'), Google: emptySegment_('Google'), Other: emptySegment_('Other') };
  const all = emptySegment_('All channels');

  perf.forEach(r => {
    const s = seg[platformOf_(r.platform)];
    ['spend', 'impressions', 'clicks', 'leads'].forEach(k => {
      const v = asNumber_(r[k]); s[k] += v; all[k] += v;
    });
  });
  funnel.forEach(r => {
    const s = seg[platformOf_(r.platform)];
    [['newLeads','newLeads'],['responded','responded'],['bookedCalls','bookedCalls'],
     ['appointments','appointments'],['strategySessions','strategySessions'],
     ['qualified','qualified'],['closedWon','closedWon'],['revenue','revenue']].forEach(p => {
      const v = asNumber_(r[p[1]]); s[p[0]] += v; all[p[0]] += v;
    });
  });

  /* Previously this dropped any segment with no ad spend and no ad leads — which hid
     the "Other" bucket while still counting it in the combined total, so the platform
     cards never summed to the headline (182 CRM leads combined vs 103 + 72 shown).
     A segment holding CRM leads is shown even when it carries no ad spend. */
  const list = ['Meta', 'Google', 'Other']
    .map(k => finaliseSegment_(seg[k]))
    .filter(s => s.spend > 0 || s.leads > 0 || s.newLeads > 0);
  return { combined: finaliseSegment_(all), platforms: list };
}

/**
 * Month-by-month performance, newest first, with change vs the previous month.
 * Ignores the selected range deliberately — month-over-month only means something
 * across the full history, not inside a 7-day window.
 */
function buildMonthlyComparison_(maxMonths) {
  const perf = sheetRowsAsObjects_(APP.TABS.PERFORMANCE);
  const funnel = sheetRowsAsObjects_(APP.TABS.FUNNEL);
  const months = {};
  const monthOf = function (v) {
    const d = v instanceof Date ? Utilities.formatDate(v, APP.TZ, 'yyyy-MM-dd') : safeText_(v).slice(0, 10);
    return d.length >= 7 ? d.slice(0, 7) : '';
  };

  perf.forEach(r => {
    const m = monthOf(r.date); if (!m) return;
    if (!months[m]) months[m] = emptySegment_(m);
    ['spend', 'impressions', 'clicks', 'leads'].forEach(k => months[m][k] += asNumber_(r[k]));
  });
  funnel.forEach(r => {
    const m = monthOf(r.date); if (!m) return;
    if (!months[m]) months[m] = emptySegment_(m);
    months[m].newLeads += asNumber_(r.newLeads);
    months[m].bookedCalls += asNumber_(r.bookedCalls);
    months[m].appointments += asNumber_(r.appointments);
    months[m].closedWon += asNumber_(r.closedWon);
    months[m].revenue += asNumber_(r.revenue);
  });

  const keys = Object.keys(months).sort().reverse().slice(0, maxMonths || 12);
  const rows = keys.map(k => { const x = finaliseSegment_(months[k]); x.month = k; return x; });

  // Attach deltas against the following (older) entry.
  rows.forEach((r, i) => {
    const prev = rows[i + 1];
    const pctChange = function (now, was) { return was > 0 ? ((now - was) / was) * 100 : null; };
    r.change = prev ? {
      spend: pctChange(r.spend, prev.spend),
      leads: pctChange(r.leads, prev.leads),
      cpl: pctChange(r.cpl, prev.cpl),
      revenue: pctChange(r.revenue, prev.revenue),
      roas: pctChange(r.roas, prev.roas)
    } : null;
  });
  return rows;
}

/** Months present in the data, newest first — powers the month picker. */
function availableMonths_() {
  const seen = {};
  sheetRowsAsObjects_(APP.TABS.PERFORMANCE).forEach(r => {
    const d = r.date instanceof Date ? Utilities.formatDate(r.date, APP.TZ, 'yyyy-MM-dd') : safeText_(r.date).slice(0, 10);
    if (d.length >= 7) seen[d.slice(0, 7)] = 1;
  });
  return Object.keys(seen).sort().reverse();
}

/**
 * Image vs video performance. Format comes from the Meta_Ads snapshot; spend and
 * leads come from the range-filtered daily facts, joined on adId.
 * Ads whose format is unknown are reported separately rather than guessed at.
 */
function buildFormatBreakdown_(ads) {
  const buckets = {};
  (ads || []).forEach(a => {
    const raw = safeText_(a.format).toLowerCase();
    const key = raw.indexOf('video') >= 0 ? 'Video'
              : (raw.indexOf('image') >= 0 || raw.indexOf('photo') >= 0) ? 'Image'
              : a.videoSrc ? 'Video' : (a.thumbUrl ? 'Image' : 'Unknown');
    if (!buckets[key]) buckets[key] = { format: key, ads: 0, spend: 0, leads: 0, impressions: 0, clicks: 0, hookSum: 0, hookCount: 0 };
    const b = buckets[key];
    b.ads++; b.spend += asNumber_(a.spend); b.leads += asNumber_(a.leads);
    b.impressions += asNumber_(a.impressions); b.clicks += asNumber_(a.clicks);
    if (asNumber_(a.hookrate) > 0) { b.hookSum += asNumber_(a.hookrate); b.hookCount++; }
  });
  return Object.keys(buckets).map(k => {
    const b = buckets[k];
    b.cpl = b.leads > 0 ? b.spend / b.leads : 0;
    b.ctr = b.impressions > 0 ? (b.clicks / b.impressions) * 100 : 0;
    b.avgHookRate = b.hookCount > 0 ? b.hookSum / b.hookCount : 0;
    delete b.hookSum; delete b.hookCount;
    return b;
  }).sort((a, b) => b.spend - a.spend);
}

/**
 * Daily series carrying the metrics a media buyer actually decides on — spend and
 * leads split by platform, plus CPL. A single blended spend bar (the old "daily
 * pulse") shows activity but supports no decision.
 */
function buildDecisionTrend_(perf, funnel) {
  const days = {};
  const dayOf = function (v) { return v instanceof Date ? Utilities.formatDate(v, APP.TZ, 'yyyy-MM-dd') : safeText_(v).slice(0, 10); };

  perf.forEach(r => {
    const d = dayOf(r.date); if (!d) return;
    if (!days[d]) days[d] = { date: d, spend: 0, leads: 0, metaSpend: 0, googleSpend: 0, metaLeads: 0, googleLeads: 0, bookedCalls: 0 };
    const p = platformOf_(r.platform), spend = asNumber_(r.spend), leads = asNumber_(r.leads);
    days[d].spend += spend; days[d].leads += leads;
    if (p === 'Meta') { days[d].metaSpend += spend; days[d].metaLeads += leads; }
    else if (p === 'Google') { days[d].googleSpend += spend; days[d].googleLeads += leads; }
  });
  funnel.forEach(r => {
    const d = dayOf(r.date); if (!d || !days[d]) return;
    days[d].bookedCalls += asNumber_(r.bookedCalls);
  });

  return Object.keys(days).sort().map(k => {
    const x = days[k];
    x.cpl = x.leads > 0 ? x.spend / x.leads : 0;
    x.metaCpl = x.metaLeads > 0 ? x.metaSpend / x.metaLeads : 0;
    x.googleCpl = x.googleLeads > 0 ? x.googleSpend / x.googleLeads : 0;
    return x;
  });
}

// ==================== 07_Setup.gs ====================
/** One-time setup, triggers and menu. */
function onOpen(){SpreadsheetApp.getUi().createMenu('REI Performance OS v9').addItem('Run v9 setup','setupV9').addItem('Store Meta token','storeMetaAccessToken').addItem('Store GHL key','storeGHLApiKey').addSeparator().addItem('Install safe sync triggers','installV9Triggers').addItem('Remove v9 sync triggers','removeV9Triggers').addItem('Run full sync now','runFullSyncFromEditor').addSeparator().addItem('Backfill Meta history','backfillMetaHistory').addItem('Refresh Meta token now','refreshMetaToken').addItem('Run health check','runHealthCheckFromEditor').addToUi();}

/**
 * One-time config setter — run once from the editor, then never again.
 *
 * These four are non-secret IDENTIFIERS (which sheet, which ad account, which GHL
 * location/pipeline), not credentials. They live in Script Properties, which the web
 * app deliberately cannot edit: the dashboard is deployed with ANYONE_ANONYMOUS access,
 * so exposing config writes there would let anyone with the URL repoint the system.
 *
 * Secrets are NOT set here and never should be. META_ACCESS_TOKEN, GHL_API_KEY and
 * DASHBOARD_ACCESS_KEY are entered by a human via the sheet menu (promptProperty_),
 * so they are never written into source code or version control.
 *
 * Values verified 2026-07-31 against the live GHL API and the v9 master sheet.
 * Existing values are overwritten — safe to re-run if an ID ever changes.
 */
function setV9ConfigProperties(){
  const props={
    SHEET_ID:'167C_gZsN5RtImBFArt5hXcUqMAHlfJFqX52f0rN_pWk',
    META_AD_ACCOUNT_ID:'act_1467621970951606',   // 1CallClose x The REI Method Team
    META_API_VERSION:'v19.0',                    // bump only after testing (Config_v9 note)
    GHL_LOCATION_ID:'cyeYxFVQE1l73kO6S6Lx',
    GHL_PIPELINE_ID:'BdutTA7xHUrNoPpWc5Nu'       // 1-To-1 Pipeline
  };
  PropertiesService.getScriptProperties().setProperties(props,false);
  const missing=['META_ACCESS_TOKEN','GHL_API_KEY','DASHBOARD_ACCESS_KEY']
    .filter(k=>!prop_(k,''));
  uiAlert_('v9 config identifiers set:\n- '+Object.keys(props).join('\n- ')+
    (missing.length?'\n\nStill needed (enter via the sheet menu, never in code):\n- '+missing.join('\n- ')
                   :'\n\nAll credentials already configured. Next: Run full sync now.'));
}

function setupV9(){
  const ss=getMasterSpreadsheet_();Object.keys(TAB_HEADERS).forEach(name=>{let sh=ss.getSheetByName(name);if(!sh)sh=ss.insertSheet(name);if(sh.getLastRow()===0)sh.appendRow(TAB_HEADERS[name]);sh.setFrozenRows(1);});
  seedStageMap_();seedForecastAssumptions_();seedConfigV9_();backfillGoogleDailyFact_();rebuildDailyFunnelFact_(makeRunId_('setup'));buildHealthReport_(false);uiAlert_('REI Performance OS v9 setup complete. Next: set the API credentials, run a manual sync, then install the safe triggers and deploy as Web App.');
}

function seedStageMap_(){const headers=['canonicalStage','rank','countsAsResponded','countsAsBooked','countsAsAppointment','countsAsQualified','countsAsClosed','knownAliases'];const aliases={New:'new lead, new, signup',Contacted:'attempting contact, contacted, nurture',Responded:'responded, replied', 'Booked Call':'booked call, booking, booked appointment, diagnosis call booked',Appointment:'appointment, show, showed','Strategy Session':'strategy session, strategy session booked','Appt Qualified':'implementation opportunity, attended, qualified','Closed':'close, closed, won','Lost':'unqualified, lost'};const rows=CANONICAL_STAGES.map((s,i)=>({canonicalStage:s,rank:i,countsAsResponded:i>=2&&s!=='Lost'?'Y':'',countsAsBooked:i>=3&&s!=='Lost'?'Y':'',countsAsAppointment:i>=4&&s!=='Lost'?'Y':'',countsAsQualified:i>=6&&s!=='Lost'?'Y':'',countsAsClosed:s==='Closed'?'Y':'',knownAliases:aliases[s]||''}));overwriteObjects_(APP.TABS.STAGES,headers,rows);}
function seedConfigV9_(){const headers=['setting','value','required','description'];const rows=[['Sheet ID',getMasterSheetId_(),'Yes','v9 master spreadsheet'],['Meta API version',prop_('META_API_VERSION','v19.0'),'Yes','Keep configurable; change only after testing'],['Meta history days',APP.DEFAULT_META_DAYS,'No','Daily ad insights lookback'],['GHL sync interval','15 minutes','No','Server trigger only; no browser polling'],['Meta sync interval','30 minutes','No','Server trigger only'],['Web app execute as','User deploying','Yes','Avoids per-viewer Google OAuth'],['Web app access','Anyone','Yes','Direct-link access; no dashboard login gate'],['Mobile mode','Responsive bottom navigation','Yes','Designed for Chrome Android/iOS']].map(r=>({setting:r[0],value:r[1],required:r[2],description:r[3]}));overwriteObjects_(APP.TABS.CONFIG,headers,rows);}

/**
 * Trigger set.
 *
 * The 30-minute Meta poll and 15-minute GHL poll were replaced by one nightly
 * reconciliation: freshenDashboard now pulls on every page load, so polling around the
 * clock only burned API quota against a dashboard nobody was looking at — and the GHL
 * poll in particular was writing a 401 into Error_Log every 15 minutes.
 *
 * The nightly run is the one that reads every contact and picks up deletions, so it
 * stays. 05:00 SGT is after Meta has settled the previous day's spend.
 */
function installV9Triggers(){
  removeV9Triggers(false);
  ScriptApp.newTrigger('scheduledDailySyncV9').timeBased().atHour(5).everyDays(1).inTimezone(APP.TZ).create();
  ScriptApp.newTrigger('scheduledMetaTokenRefresh').timeBased().everyWeeks(1).onWeekDay(ScriptApp.WeekDay.MONDAY).atHour(4).create();
  ScriptApp.newTrigger('scheduledHealthCheckV9').timeBased().everyHours(6).create();
  uiAlert_('v9 triggers installed: nightly full sync 05:00 SGT, weekly Meta token refresh, 6-hourly health check.');
}

/** Nightly reconciliation — the full pull, including contacts and deleted records. */
function scheduledDailySyncV9(){withScriptLock_('Daily sync',1000,function(){const runId=makeRunId_('daily');try{syncAllV9_(runId,'scheduled');clearDashboardCache_();}catch(e){appendErrorLog_(runId,'All','scheduledDailySyncV9','ERROR',e.message,'','',e.stack,{},'scheduled');throw e;}});}
function removeV9Triggers(showAlert){ScriptApp.getProjectTriggers().forEach(t=>{if(['scheduledMetaSyncV9','scheduledGHLSyncV9','scheduledHealthCheckV9','scheduledMetaTokenRefresh','scheduledDailySyncV9'].indexOf(t.getHandlerFunction())>=0)ScriptApp.deleteTrigger(t);});if(showAlert!==false)uiAlert_('v9 triggers removed.');}
function scheduledMetaSyncV9(){withScriptLock_('Meta scheduled sync',1000,function(){const runId=makeRunId_('meta');try{syncMetaDaily_(runId,APP.DEFAULT_META_DAYS);backfillGoogleDailyFact_();clearDashboardCache_();}catch(e){appendErrorLog_(runId,'Meta','scheduledMetaSyncV9','ERROR',e.message,'','',e.stack,{},'scheduled');throw e;}});}
function scheduledGHLSyncV9(){withScriptLock_('GHL scheduled sync',1000,function(){const runId=makeRunId_('ghl');try{syncGHL_(runId);clearDashboardCache_();}catch(e){appendErrorLog_(runId,'GHL','scheduledGHLSyncV9','ERROR',e.message,'','',e.stack,{},'scheduled');throw e;}});}
function scheduledHealthCheckV9(){buildHealthReport_(false);}
function syncAllV9_(runId,triggerType){const result={ok:true,runId:runId,startedAt:nowIso_(),services:[]};try{result.services.push(syncMetaDaily_(runId,APP.DEFAULT_META_DAYS));}catch(e){result.ok=false;result.services.push({service:'Meta',error:e.message});appendErrorLog_(runId,'Meta','syncAllV9_','ERROR',e.message,'','',e.stack,{},triggerType);}try{result.services.push(syncGHL_(runId));}catch(e){result.ok=false;result.services.push({service:'GHL',error:e.message});appendErrorLog_(runId,'GHL','syncAllV9_','ERROR',e.message,'','',e.stack,{},triggerType);}try{result.services.push({service:'Google',recordsWritten:backfillGoogleDailyFact_()});}catch(e){result.ok=false;result.services.push({service:'Google',error:e.message});appendErrorLog_(runId,'Google','syncAllV9_','ERROR',e.message,'','',e.stack,{},triggerType);}getForecastData_();buildHealthReport_(false);result.completedAt=nowIso_();return result;}

function storeMetaAccessToken(){promptProperty_('META_ACCESS_TOKEN','Store Meta access token','Paste the Meta long-lived/system-user access token.');}
function storeGHLApiKey(){promptProperty_('GHL_API_KEY','Store GHL private integration key','Paste the GHL Private Integration key.');}
function promptProperty_(property,title,prompt){const ui=SpreadsheetApp.getUi(),res=ui.prompt(title,prompt,ui.ButtonSet.OK_CANCEL);if(res.getSelectedButton()!==ui.Button.OK)return;const value=res.getResponseText().trim();if(!value){ui.alert('Nothing saved.');return;}PropertiesService.getScriptProperties().setProperty(property,value);ui.alert(property+' saved in Script Properties.');}
function runFullSyncFromEditor(){const result=withScriptLock_('Editor sync',1000,()=>syncAllV9_(makeRunId_('editor'),'editor'));uiAlert_(JSON.stringify(result,null,2));}
function runHealthCheckFromEditor(){const report=buildHealthReport_(false);uiAlert_(report.overall+'\n\n'+report.checks.map(c=>c.status+' — '+c.name+': '+c.detail).join('\n'));}

