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
