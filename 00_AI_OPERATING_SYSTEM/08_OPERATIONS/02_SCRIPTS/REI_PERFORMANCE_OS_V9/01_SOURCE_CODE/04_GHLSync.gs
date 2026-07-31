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
