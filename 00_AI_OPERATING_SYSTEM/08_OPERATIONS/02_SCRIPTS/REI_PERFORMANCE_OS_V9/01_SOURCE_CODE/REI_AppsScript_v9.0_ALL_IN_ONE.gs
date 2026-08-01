/** REI Performance OS v9.0 — ALL-IN-ONE SERVER SOURCE
 * Generated from modular source files. Use either this file OR the numbered .gs files, not both.
 */

// ==================== 00_Config.gs ====================
/**
 * REI Performance OS v9.0 — Configuration and shared helpers.
 * Mobile-first, account-neutral Apps Script web app.
 */
const APP = Object.freeze({
  VERSION: '9.2.0',
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
    GOOGLE_DAILY: 'Google_Campaigns_Daily'
  })
});

const CANONICAL_STAGES = Object.freeze([
  'New', 'Contacted', 'Responded', 'Booked Call', 'Appointment',
  'Strategy Session', 'Appt Qualified', 'Closed', 'Lost'
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
    'attempting contact':'Contacted','contacted':'Contacted','nurture':'Contacted',
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

function clearDashboardCache_() {
  const cache = CacheService.getScriptCache();
  ['today','7d','30d','90d','all'].forEach(k => cache.remove('dashboard:' + k));
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
  // Cache is an optimisation, never a requirement. CacheService rejects values over
  // ~100KB with "Argument too large: value", and the v9.1 payload (per-ad rows, ad
  // sets, pipeline) exceeds that. Previously the failing put() threw AFTER the data
  // was built, so the whole call failed and the dashboard kept showing the last
  // payload it managed to receive — which looked exactly like "ranges do nothing".
  let cached = null;
  try { cached = CacheService.getScriptCache().get(cacheKey); } catch (e) { cached = null; }
  if (cached && !request.force) {
    try { return JSON.parse(cached); } catch (e) { /* corrupt entry — rebuild below */ }
  }
  const payload = buildDashboardPayload_(rangeKey, request.customStart, request.customEnd);
  try {
    const json = JSON.stringify(payload);
    if (json.length < 90000) CacheService.getScriptCache().put(cacheKey, json, APP.CACHE_SECONDS);
  } catch (e) {
    // Too large or cache unavailable — serve uncached rather than fail the request.
  }
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
  const stages = safely('stages', function () { return buildStageConversions_(funnelTotals); }, null);
  const pipeline = safely('pipeline', function () { return buildPipelineByStage_(leads); }, []);
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
  const qualified = funnel.reduce((s,r) => s + asNumber_(r.qualified), 0);
  const closed = funnel.reduce((s,r) => s + asNumber_(r.closedWon), 0);
  const revenue = funnel.reduce((s,r) => s + asNumber_(r.revenue), 0);
  const leads = newLeads || adLeads;
  return {
    spend, impressions, clicks, leads, adLeads, responded, bookedCalls: booked,
    appointments, qualified, closed, revenue,
    cpl: leads ? spend / leads : 0,
    costPerResponded: responded ? spend / responded : 0,
    costPerBooked: booked ? spend / booked : 0,
    costPerAppointment: appointments ? spend / appointments : 0,
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
    const x=map[key], stage=normaliseStage_(r.status); x.newLeads++;
    if(statusRank_(stage)>=statusRank_('Contacted')&&stage!=='Lost')x.contacted++;
    if(statusRank_(stage)>=statusRank_('Responded')&&stage!=='Lost')x.responded++;
    if(statusRank_(stage)>=statusRank_('Booked Call')&&stage!=='Lost')x.bookedCalls++;
    if(statusRank_(stage)>=statusRank_('Appointment')&&stage!=='Lost')x.appointments++;
    if(statusRank_(stage)>=statusRank_('Strategy Session')&&stage!=='Lost')x.strategySessions++;
    if(statusRank_(stage)>=statusRank_('Appt Qualified')&&stage!=='Lost')x.qualified++;
    if(stage==='Closed'){x.closedWon++;x.revenue+=asNumber_(r.dealValue);} if(stage==='Lost')x.closedLost++;
  });
  overwriteObjects_(APP.TABS.FUNNEL,TAB_HEADERS.Daily_Funnel_Fact,Object.keys(map).map(k=>map[k]));
  return Object.keys(map).length;
}

function backfillGoogleDailyFact_() {
  const rows=sheetRowsAsObjects_(APP.TABS.GOOGLE_DAILY); if(!rows.length)return 0;
  const runId=makeRunId_('google-backfill');
  const facts=rows.map(r=>({date:r.date instanceof Date?Utilities.formatDate(r.date,APP.TZ,'yyyy-MM-dd'):safeText_(r.date).slice(0,10),platform:'Google',accountId:prop_('GOOGLE_ADS_CUSTOMER_ID',''),campaignId:safeText_(r.campaignId),campaignName:safeText_(r.campaign),adSetId:'',adSetName:'',adId:'',adName:'',objective:safeText_(r.campaignType),status:safeText_(r.status),spend:asNumber_(r.spend),impressions:asNumber_(r.impressions),reach:0,clicks:asNumber_(r.clicks),linkClicks:asNumber_(r.clicks),leads:asNumber_(r.conversions),conversions:asNumber_(r.conversions),conversionValue:asNumber_(r.conversionValue),ctr:asNumber_(r.ctr),cpc:asNumber_(r.avgCpc),cpl:asNumber_(r.conversions)?asNumber_(r.spend)/asNumber_(r.conversions):0,sourceUpdatedAt:safeText_(r.updatedAt)||nowIso_(),syncRunId:runId}));
  return upsertObjects_(APP.TABS.PERFORMANCE,TAB_HEADERS.Daily_Performance_Fact,facts,r=>[safeText_(r.date),safeText_(r.platform),safeText_(r.campaignId),safeText_(r.adSetId),safeText_(r.adId)].join('|'));
}

// ==================== 03_MetaSync.gs ====================
/** Meta daily-insights synchronisation with full pagination. */
function syncMetaDaily_(runId, days) {
  const started = new Date();
  const token = prop_('META_ACCESS_TOKEN','');
  const accountId = prop_('META_AD_ACCOUNT_ID','act_1467621970951606');
  const apiVersion = prop_('META_API_VERSION','v19.0');
  if(!token) throw new Error('META_ACCESS_TOKEN is missing.');
  const end=sgtDate_(new Date()); const start=addDaysIso_(end,-Math.max(1,Number(days||APP.DEFAULT_META_DAYS)-1));
  const fields=['date_start','date_stop','account_id','campaign_id','campaign_name','adset_id','adset_name','ad_id','ad_name','objective','spend','impressions','reach','clicks','inline_link_clicks','actions','action_values','ctr','cpc'].join(',');
  const params={level:'ad',time_increment:1,time_range:JSON.stringify({since:start,until:end}),fields:fields,limit:500};
  const url='https://graph.facebook.com/'+apiVersion+'/'+accountId+'/insights';
  const rows=metaFetchAll_(url,params,token,runId);
  const now=nowIso_();
  const facts=rows.map(r=>{
    const spend=asNumber_(r.spend), leads=extractMetaAction_(r.actions,['lead','onsite_conversion.lead_grouped','offsite_conversion.fb_pixel_lead','onsite_web_lead']);
    return {date:safeText_(r.date_start),platform:'Meta',accountId:safeText_(r.account_id)||accountId,campaignId:safeText_(r.campaign_id),campaignName:safeText_(r.campaign_name),adSetId:safeText_(r.adset_id),adSetName:safeText_(r.adset_name),adId:safeText_(r.ad_id),adName:safeText_(r.ad_name),objective:safeText_(r.objective),status:'',spend:spend,impressions:asNumber_(r.impressions),reach:asNumber_(r.reach),clicks:asNumber_(r.clicks),linkClicks:asNumber_(r.inline_link_clicks),leads:leads,conversions:leads,conversionValue:extractMetaAction_(r.action_values,['purchase','omni_purchase']),ctr:asNumber_(r.ctr),cpc:asNumber_(r.cpc),cpl:leads?spend/leads:0,sourceUpdatedAt:now,syncRunId:runId};
  });
  const written=upsertObjects_(APP.TABS.PERFORMANCE,TAB_HEADERS.Daily_Performance_Fact,facts,r=>[safeText_(r.date),safeText_(r.platform),safeText_(r.campaignId),safeText_(r.adSetId),safeText_(r.adId)].join('|'));
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

function extractMetaAction_(actions, names) {
  const wanted={}; names.forEach(n=>wanted[n]=true); let total=0;
  (actions||[]).forEach(a=>{if(wanted[a.action_type])total+=asNumber_(a.value);});
  return total;
}

function buildUrl_(base, params) {
  return base+'?'+Object.keys(params).map(k=>encodeURIComponent(k)+'='+encodeURIComponent(params[k])).join('&');
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
  const campArr=Object.keys(campaigns).map(k=>{const x=campaigns[k];x.cpl=x.leads?x.spend/x.leads:0;x.ctr=x.impressions?x.clicks/x.impressions*100:0;return x;});
  const adsetArr=Object.keys(adsets).map(k=>{const x=adsets[k];x.cpl=x.leads?x.spend/x.leads:0;return x;});
  const adArr=Object.keys(ads).map(k=>{const x=ads[k];x.cpl=x.leads?x.spend/x.leads:0;x.ctr=x.impressions?x.clicks/x.impressions*100:0;x.cpc=x.clicks?x.spend/x.clicks:0;x.cpm=x.impressions?x.spend/x.impressions*1000:0;return x;});
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
  const byContact={};
  opportunityData.forEach(o=>{const cid=safeText_(o.contact&&o.contact.id||o.contactId);if(!cid)return;const stageId=safeText_(o.pipelineStageId||o.pipeline_stage_id||o.stageId||(o.stage&&o.stage.id));const rawName=safeText_(o.stage&&o.stage.name||stageNames[stageId]);const status=safeText_(o.status).toLowerCase()==='won'?'Closed':safeText_(o.status).toLowerCase()==='lost'?'Lost':normaliseStage_(rawName);const entry={status:status,createdAt:safeText_(o.createdAt),stageId:stageId,opportunityId:safeText_(o.id),monetaryValue:asNumber_(o.monetaryValue||o.value)};if(!byContact[cid]||statusRank_(entry.status)>statusRank_(byContact[cid].status))byContact[cid]=entry;});
  const existing=sheetRowsAsObjects_(APP.TABS.GHL), preserved={}; existing.forEach(r=>preserved[safeText_(r.ghlId)]={quality:r.quality,dealValue:r.dealValue,urgencyTimeline:r.urgencyTimeline,notes:r.notes});
  const leads=contacts.filter(c=>c.id&&byContact[c.id]).map(c=>mapGHLContact_(c,byContact[c.id],preserved[c.id]||{}));
  const headersOut=['ghlId','name','contact','phone','email','sourceAdId','sourceAdName','platform','campaignName','status','quality','proptype','date','responded','appointment','strategySession','qualified','dealValue','urgencyTimeline','tags','source','notes'];
  overwriteObjects_(APP.TABS.GHL,headersOut,leads);
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

function mapGHLContact_(c,stage,preserved){
  const attrs=c.attributions||[];const attr=attrs.find(a=>a.utmAdId)||attrs[0]||{};const platformRaw=safeText_(attr.utmSource||attr.adSource||attr.medium||c.source).toLowerCase();const status=normaliseStage_(stage.status);const tags=Array.isArray(c.tags)?c.tags:[];const tagText=tags.join(' ').toLowerCase();let proptype='';if(tagText.indexOf('newlaunch')>=0||tagText.indexOf('new launch')>=0)proptype='New Launch';else if(tagText.indexOf('familylegacy')>=0||tagText.indexOf('family legacy')>=0)proptype='Family Legacy';else proptype=safeText_(c.source);
  const date=c.dateAdded?Utilities.formatDate(new Date(c.dateAdded),APP.TZ,'yyyy-MM-dd'):(stage.createdAt?Utilities.formatDate(new Date(stage.createdAt),APP.TZ,'yyyy-MM-dd'):'');
  return {ghlId:safeText_(c.id),name:safeText_(c.contactName||[c.firstName,c.lastName].filter(Boolean).join(' ')),contact:safeText_(c.email||c.phone),phone:safeText_(c.phone),email:safeText_(c.email),sourceAdId:safeText_(attr.utmAdId),sourceAdName:safeText_(attr.utmContent||attr.utmCampaign),platform:platformRaw.indexOf('google')>=0||platformRaw.indexOf('youtube')>=0?'Google':platformRaw.indexOf('facebook')>=0||platformRaw.indexOf('meta')>=0||attr.utmAdId?'Meta':'Other',campaignName:safeText_(attr.utmCampaign),status:status,quality:safeText_(preserved.quality),proptype:proptype,date:date,responded:status!=='Lost'&&statusRank_(status)>=statusRank_('Responded')?'Y':'',appointment:status!=='Lost'&&statusRank_(status)>=statusRank_('Appointment')?'Booked':'',strategySession:status!=='Lost'&&statusRank_(status)>=statusRank_('Strategy Session')?'Y':'',qualified:status!=='Lost'&&statusRank_(status)>=statusRank_('Appt Qualified')?'Y':'',dealValue:asNumber_(preserved.dealValue)||asNumber_(stage.monetaryValue),urgencyTimeline:safeText_(preserved.urgencyTimeline),tags:tags.join(', '),source:safeText_(c.source),notes:safeText_(preserved.notes)};
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

/** Tunable decision thresholds — Script Properties, so they change without code edits. */
function signalThresholds_() {
  return {
    targetCpl:     asNumber_(prop_('TARGET_CPL', 80)),
    minSpend:      asNumber_(prop_('SIGNAL_MIN_SPEND', 100)),
    minLeads:      asNumber_(prop_('SIGNAL_MIN_LEADS', 3)),
    killCplMult:   asNumber_(prop_('SIGNAL_KILL_CPL_MULT', 2)),
    scaleCplMult:  asNumber_(prop_('SIGNAL_SCALE_CPL_MULT', 0.7)),
    killHookRate:  asNumber_(prop_('SIGNAL_KILL_HOOKRATE', 15)),
    scaleHookRate: asNumber_(prop_('SIGNAL_SCALE_HOOKRATE', 30))
  };
}

/**
 * Kill / Scale / Monitor / Test verdict for one ad.
 * TEST is returned whenever there is not enough spend or volume to judge — a low CPL
 * on 1 lead is noise, not a winner. Every verdict carries a plain-English reason so
 * the number is never presented without its justification.
 */
function adSignal_(row, t) {
  const spend = asNumber_(row.spend), leads = asNumber_(row.leads);
  const cpl = leads > 0 ? spend / leads : 0;
  const hook = asNumber_(row.hookrate);
  const money = function (n) { return '$' + Math.round(n); };

  if (leads === 0 && spend >= t.minSpend * 2)
    return { signal: 'KILL', reason: money(spend) + ' spent, zero leads' };
  if (spend < t.minSpend && leads < t.minLeads)
    return { signal: 'TEST', reason: 'Too early — needs ' + money(t.minSpend) + ' spend or ' + t.minLeads + ' leads' };
  if (leads >= t.minLeads && cpl >= t.targetCpl * t.killCplMult)
    return { signal: 'KILL', reason: 'CPL ' + money(cpl) + ' vs ' + money(t.targetCpl) + ' target' };
  if (hook > 0 && hook < t.killHookRate && spend >= t.minSpend)
    return { signal: 'KILL', reason: 'Hook rate ' + hook.toFixed(1) + '% — people scroll past' };
  if (leads >= t.minLeads && cpl > 0 && cpl <= t.targetCpl * t.scaleCplMult)
    return { signal: 'SCALE', reason: 'CPL ' + money(cpl) + ' vs ' + money(t.targetCpl) + ' target' };
  if (hook >= t.scaleHookRate && leads >= t.minLeads)
    return { signal: 'SCALE', reason: 'Hook rate ' + hook.toFixed(1) + '% and converting' };
  return { signal: 'MONITOR', reason: 'CPL ' + money(cpl) + ' — near target, keep watching' };
}

/** Per-ad economics for the selected range, joined to current creative metadata. */
function aggregateAds_(perf) {
  const t = signalThresholds_(), meta = {};
  sheetRowsAsObjects_(APP.TABS.META_ADS).forEach(a => { if (safeText_(a.metaId)) meta[safeText_(a.metaId)] = a; });

  const map = {};
  perf.forEach(r => {
    const id = safeText_(r.adId); if (!id) return;
    if (!map[id]) map[id] = {
      adId: id, adName: safeText_(r.adName), adSetId: safeText_(r.adSetId), adSetName: safeText_(r.adSetName),
      campaignId: safeText_(r.campaignId), campaignName: safeText_(r.campaignName), platform: safeText_(r.platform),
      spend: 0, impressions: 0, clicks: 0, leads: 0
    };
    const x = map[id];
    x.spend += asNumber_(r.spend); x.impressions += asNumber_(r.impressions);
    x.clicks += asNumber_(r.clicks); x.leads += asNumber_(r.leads);
  });

  return Object.keys(map).map(id => {
    const x = map[id], m = meta[id] || {};
    x.hookrate = asNumber_(m.hookrate);
    x.status = safeText_(m.status);
    x.format = safeText_(m.format);
    x.thumbUrl = safeText_(m.thumbUrl) || safeText_(m.imageUrl);
    x.videoSrc = safeText_(m.videoSrc);
    x.adPermalink = safeText_(m.adPermalink);
    x.cpl = x.leads > 0 ? x.spend / x.leads : 0;
    x.ctr = x.impressions > 0 ? (x.clicks / x.impressions) * 100 : 0;
    x.cpc = x.clicks > 0 ? x.spend / x.clicks : 0;
    x.cpm = x.impressions > 0 ? (x.spend / x.impressions) * 1000 : 0;
    const s = adSignal_(x, t);
    x.signal = s.signal; x.signalReason = s.reason;
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
      spend: 0, impressions: 0, clicks: 0, leads: 0, adIds: {}
    };
    const x = map[id];
    x.spend += asNumber_(r.spend); x.impressions += asNumber_(r.impressions);
    x.clicks += asNumber_(r.clicks); x.leads += asNumber_(r.leads);
    if (safeText_(r.adId)) x.adIds[safeText_(r.adId)] = 1;
  });

  return Object.keys(map).map(id => {
    const x = map[id], m = meta[id] || {};
    x.adCount = Object.keys(x.adIds).length; delete x.adIds;
    x.budget = asNumber_(m.budget); x.audience = safeText_(m.audience); x.status = safeText_(m.status);
    x.cpl = x.leads > 0 ? x.spend / x.leads : 0;
    x.ctr = x.impressions > 0 ? (x.clicks / x.impressions) * 100 : 0;
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
function buildStageConversions_(f) {
  const minVolume = asNumber_(prop_('LEAK_MIN_VOLUME', 5));
  const pct = function (num, den) { return den > 0 ? (num / den) * 100 : 0; };

  const steps = [
    { key: 'lead_responded',      label: 'New Lead → Responded',           from: 'New Leads',        fromCount: f.newLeads,         to: f.responded },
    { key: 'responded_booked',    label: 'Responded → Booked Call',        from: 'Responded',        fromCount: f.responded,        to: f.bookedCalls },
    { key: 'booked_appointment',  label: 'Booked Call → Appointment',      from: 'Booked Calls',     fromCount: f.bookedCalls,      to: f.appointments },
    { key: 'appointment_session', label: 'Appointment → Strategy Session', from: 'Appointments',     fromCount: f.appointments,     to: f.strategySessions },
    { key: 'session_closed',      label: 'Strategy Session → Closed',      from: 'Strategy Sessions', fromCount: f.strategySessions, to: f.closedWon }
  ].map(s => {
    s.rate = pct(s.to, s.fromCount);
    s.dropped = Math.max(0, s.fromCount - s.to);
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
    leak: leak ? { key: leak.key, label: leak.label, rate: leak.rate, dropped: leak.dropped } : null,
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

  const list = ['Meta', 'Google', 'Other'].map(k => finaliseSegment_(seg[k])).filter(s => s.spend > 0 || s.leads > 0);
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
function onOpen(){SpreadsheetApp.getUi().createMenu('REI Performance OS v9').addItem('Run v9 setup','setupV9').addItem('Store Meta token','storeMetaAccessToken').addItem('Store GHL key','storeGHLApiKey').addSeparator().addItem('Install safe sync triggers','installV9Triggers').addItem('Remove v9 sync triggers','removeV9Triggers').addItem('Run full sync now','runFullSyncFromEditor').addItem('Run health check','runHealthCheckFromEditor').addToUi();}

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

function installV9Triggers(){removeV9Triggers(false);ScriptApp.newTrigger('scheduledMetaSyncV9').timeBased().everyMinutes(30).create();ScriptApp.newTrigger('scheduledGHLSyncV9').timeBased().everyMinutes(15).create();ScriptApp.newTrigger('scheduledHealthCheckV9').timeBased().everyHours(6).create();}
function removeV9Triggers(showAlert){ScriptApp.getProjectTriggers().forEach(t=>{if(['scheduledMetaSyncV9','scheduledGHLSyncV9','scheduledHealthCheckV9'].indexOf(t.getHandlerFunction())>=0)ScriptApp.deleteTrigger(t);});if(showAlert!==false)uiAlert_('v9 triggers removed.');}
function scheduledMetaSyncV9(){withScriptLock_('Meta scheduled sync',1000,function(){const runId=makeRunId_('meta');try{syncMetaDaily_(runId,APP.DEFAULT_META_DAYS);backfillGoogleDailyFact_();clearDashboardCache_();}catch(e){appendErrorLog_(runId,'Meta','scheduledMetaSyncV9','ERROR',e.message,'','',e.stack,{},'scheduled');throw e;}});}
function scheduledGHLSyncV9(){withScriptLock_('GHL scheduled sync',1000,function(){const runId=makeRunId_('ghl');try{syncGHL_(runId);clearDashboardCache_();}catch(e){appendErrorLog_(runId,'GHL','scheduledGHLSyncV9','ERROR',e.message,'','',e.stack,{},'scheduled');throw e;}});}
function scheduledHealthCheckV9(){buildHealthReport_(false);}
function syncAllV9_(runId,triggerType){const result={ok:true,runId:runId,startedAt:nowIso_(),services:[]};try{result.services.push(syncMetaDaily_(runId,APP.DEFAULT_META_DAYS));}catch(e){result.ok=false;result.services.push({service:'Meta',error:e.message});appendErrorLog_(runId,'Meta','syncAllV9_','ERROR',e.message,'','',e.stack,{},triggerType);}try{result.services.push(syncGHL_(runId));}catch(e){result.ok=false;result.services.push({service:'GHL',error:e.message});appendErrorLog_(runId,'GHL','syncAllV9_','ERROR',e.message,'','',e.stack,{},triggerType);}try{result.services.push({service:'Google',recordsWritten:backfillGoogleDailyFact_()});}catch(e){result.ok=false;result.services.push({service:'Google',error:e.message});appendErrorLog_(runId,'Google','syncAllV9_','ERROR',e.message,'','',e.stack,{},triggerType);}getForecastData_();buildHealthReport_(false);result.completedAt=nowIso_();return result;}

function storeMetaAccessToken(){promptProperty_('META_ACCESS_TOKEN','Store Meta access token','Paste the Meta long-lived/system-user access token.');}
function storeGHLApiKey(){promptProperty_('GHL_API_KEY','Store GHL private integration key','Paste the GHL Private Integration key.');}
function promptProperty_(property,title,prompt){const ui=SpreadsheetApp.getUi(),res=ui.prompt(title,prompt,ui.ButtonSet.OK_CANCEL);if(res.getSelectedButton()!==ui.Button.OK)return;const value=res.getResponseText().trim();if(!value){ui.alert('Nothing saved.');return;}PropertiesService.getScriptProperties().setProperty(property,value);ui.alert(property+' saved in Script Properties.');}
function runFullSyncFromEditor(){const result=withScriptLock_('Editor sync',1000,()=>syncAllV9_(makeRunId_('editor'),'editor'));uiAlert_(JSON.stringify(result,null,2));}
function runHealthCheckFromEditor(){const report=buildHealthReport_(false);uiAlert_(report.overall+'\n\n'+report.checks.map(c=>c.status+' — '+c.name+': '+c.detail).join('\n'));}

