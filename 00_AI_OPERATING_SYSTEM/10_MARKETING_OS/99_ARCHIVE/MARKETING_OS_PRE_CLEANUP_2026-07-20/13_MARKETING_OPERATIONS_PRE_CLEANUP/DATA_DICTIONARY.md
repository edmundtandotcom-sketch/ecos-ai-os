# DATA DICTIONARY
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (proposed field definitions — reconcile against registries as other builders complete them)
Evidence level: N/A — schema definition, not a factual claim
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF.md §8 (registry descriptions across 05_FRAMEWORK_LIBRARY, 07_CREATIVE_LIBRARY, 08_CAMPAIGNS, 09_EXPERIMENTS, 11_WINNERS_AND_LEARNINGS, 14_CHANGE_LOG); 12_TEMPLATES field lists; reconciled against the 6 live registry CSVs' actual header rows
Next review: on next registry schema change (flag via CHANGE_PROPOSAL.md if fields drift)
Reconciled against live CSVs 2026-07-11

Field lists below are transcribed directly from each registry's live header row (not proposed) as of 2026-07-11. Column order matches the CSV. If a future edit to a registry's header row is not mirrored here, file a `CHANGE_PROPOSAL.md`.

## FRAMEWORK_REGISTRY.csv (05_FRAMEWORK_LIBRARY)
FrameworkID · Name · Family · Purpose · BestUse · AwarenessStage · Channels · Inputs · EvidenceTier · Status · SourcePath · CampaignsUsing · LastReview

## CAMPAIGN_REGISTRY.csv (08_CAMPAIGNS)
CampaignID · Name · Engine · CampaignDoor · Status · Objective · Platform · Audience · Offer · StartDate · EndDate · Spend · Leads · Responded · CPL · CostPerResponded · Appointments · CPA · EvidenceTier · SourcePath · Decision · Lessons · ConflictFlags

## CREATIVE_REGISTRY.csv (07_CREATIVE_LIBRARY)
CreativeID · CampaignID · AngleID · Format · Title · Hook · MainMessage · VisualDevice · CTA · Destination · Platform · Orientations · Status · EvidenceTier · SourcePath · Learning

## EXPERIMENT_REGISTRY.csv (09_EXPERIMENTS)
ExperimentID · CampaignID · Variable · Hypothesis · Control · Variant · KPI · MinData · DecisionRule · Status · Result · Learning · SourcePath

## LEARNING_REGISTRY.csv (11_WINNERS_AND_LEARNINGS)
LearningID · Date · Context · Learning · EvidenceTier · SourcePath · Status · AppliesTo

## CHANGE_LOG.csv (14_CHANGE_LOG)
ChangeID · Date · ProposedBy · Type · CurrentRule · ProposedRule · Reason · Evidence · Confidence · Scope · FilesAffected · CampaignsAffected · Risk · ApprovalStatus · ReviewDate · Rollback

## Funnel metrics (used in FUNNEL_BRIEF.md, 10_PERFORMANCE)
FunnelID (FUN-) · Stage · Visitors · Started · Completed · DropOffPct · CTAClicks · QualifiedLeads · CPL · TimeToFirstResponse · Source

## Sales-quality metrics (used in PERFORMANCE_REVIEW.md, 10_PERFORMANCE — aggregates only, PII rule applies)
LeadSource · LeadGrade (A/B/C) · QualifiedY/N · ConsultBooked · ConsultShowed · Proposal · Closed · Revenue/GCI (if available) · CAC · TimeToClose

## Shared fields (every registry)
EvidenceTier (1–5 or N/A, see 00_COMMAND_CENTER evidence-tier definitions) · SourcePath (file this row's data came from) · Status · LastUpdated

## PII rule
Never populate LeadSource/registry rows with names, phone numbers, emails, or NRIC-adjacent identifiers. Aggregates only, cited to the archived source (e.g. `lead_summary_*.json`).
