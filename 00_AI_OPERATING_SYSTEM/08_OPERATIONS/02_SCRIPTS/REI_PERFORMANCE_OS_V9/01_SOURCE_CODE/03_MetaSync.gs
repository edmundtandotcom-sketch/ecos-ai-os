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
