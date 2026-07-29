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
  return {
    ok: true,
    app: { name: APP.NAME, version: APP.VERSION },
    range: range,
    generatedAt: nowIso_(),
    overview: overview,
    platforms: platforms,
    campaigns: campaigns.slice(0, 100),
    leads: leads,
    funnel: aggregateFunnel_(funnel),
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
