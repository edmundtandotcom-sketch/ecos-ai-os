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
  const cached = CacheService.getScriptCache().get(cacheKey);
  if (cached && !request.force) return JSON.parse(cached);
  const payload = buildDashboardPayload_(rangeKey, request.customStart, request.customEnd);
  CacheService.getScriptCache().put(cacheKey, JSON.stringify(payload), APP.CACHE_SECONDS);
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
