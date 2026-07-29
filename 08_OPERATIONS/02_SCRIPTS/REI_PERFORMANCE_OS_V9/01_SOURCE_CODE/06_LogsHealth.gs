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
  const checks=[];const props=['DASHBOARD_ACCESS_KEY','META_ACCESS_TOKEN','META_AD_ACCOUNT_ID','GHL_API_KEY','GHL_LOCATION_ID','GHL_PIPELINE_ID'];props.forEach(p=>checks.push({name:p,status:prop_(p,'')?'OK':'MISSING',detail:prop_(p,'')?'Configured':'Run setup and set this Script Property'}));
  Object.keys(APP.TABS).forEach(k=>{const name=APP.TABS[k];const sh=getSheet_(name,false);checks.push({name:'Sheet: '+name,status:sh?'OK':'MISSING',detail:sh?Math.max(0,sh.getLastRow()-1)+' data rows':'Run setupV9()'});});
  const syncRows=sheetRowsAsObjects_(APP.TABS.SYNC_LOG);const last={};syncRows.forEach(r=>{const s=safeText_(r.service);if(!last[s]||safeText_(r.timestamp)>safeText_(last[s].timestamp))last[s]=r;});
  Object.keys(last).forEach(s=>checks.push({name:'Last '+s+' sync',status:safeText_(last[s].status)==='SUCCESS'?'OK':'ERROR',detail:safeText_(last[s].timestamp)+' — '+safeText_(last[s].message)}));
  const report={generatedAt:nowIso_(),overall:checks.some(c=>c.status==='ERROR')?'ERROR':checks.some(c=>c.status==='MISSING')?'SETUP REQUIRED':'HEALTHY',checks:checks};
  if(!light)writeHealthSheet_(report);return report;
}
function writeHealthSheet_(report){const headers=['check','status','detail','checkedAt'];overwriteObjects_(APP.TABS.HEALTH,headers,report.checks.map(c=>({check:c.name,status:c.status,detail:c.detail,checkedAt:report.generatedAt})));}
