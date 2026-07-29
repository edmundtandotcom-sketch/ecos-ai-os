/**
 * REI Performance OS v9.0 — Configuration and shared helpers.
 * Mobile-first, account-neutral Apps Script web app.
 */
const APP = Object.freeze({
  VERSION: '9.0.0',
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
  const expected = prop_('DASHBOARD_ACCESS_KEY', '');
  if (!expected) throw new Error('DASHBOARD_ACCESS_KEY is not configured. Run setDashboardAccessKey() in Apps Script.');
  if (!constantTimeEqual_(accessKey, expected)) throw new Error('Access denied.');
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
