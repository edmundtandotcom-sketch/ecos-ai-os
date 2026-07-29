# 02_DASHBOARD_AD_TRACKING_SYSTEM

Version: v2.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: none (copied as-is; current master at time of migration)
Sources: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\01_CLIENT_EDITION\06_OPERATIONS_AND_TRACKING\02_DASHBOARD_AD_TRACKING_SYSTEM_v2.0.md`

Folder: 01_CRM_AND_TRACKING (AI OS) — legacy folder: 06_OPERATIONS_AND_TRACKING
Purpose: Define how ad performance, creative intelligence, dashboards and automation scripts should be stored and interpreted.

## 1. Core Principle

One dashboard system, not one dashboard per campaign.

Campaigns are filters. Creative assets are rows. Business decisions come from comparing spend, leads, quality, bookings and consult outcomes across campaigns.

## 2. Active Dashboard Folder

Active dashboard assets live in:

`06_OPERATIONS_AND_TRACKING / 01_DASHBOARD_TRACKING_SYSTEM`

This folder should keep only:

- active master performance sheet;
- active Apps Script file;
- active Google Ads script if currently used;
- active dashboard documentation if needed.

Old script versions and coding dumps should be archived.

## 3. Minimum Dashboard Fields

The performance dashboard should support these fields:

- date;
- platform;
- campaign name;
- ad set / audience;
- ad / creative name;
- campaign pack;
- creative format;
- awareness stage;
- buyer profile;
- hook / angle;
- spend;
- impressions;
- clicks;
- CTR;
- leads;
- CPL;
- replies;
- booking link clicks;
- booked appointments;
- completed consults;
- lead quality grade;
- notes / decision.

## 4. Decision Output

Every performance review should produce one of these actions:

- keep monitoring;
- kill;
- scale;
- duplicate / iterate;
- retest with new angle;
- move learning to Knowledge Vault;
- update campaign pack.

## 5. Script Version Rule

Only the latest script version should stay visible in the active dashboard folder.

Old versions belong in Archive unless they are needed for rollback.

Active visible scripts should be named clearly:

- `REI_AppsScript_ACTIVE.gs`
- `REI_GoogleAds_Script_ACTIVE.gs`

If you keep version numbers, the highest verified version is the active version and older versions should be archived.

## 6. Dashboard Safety Rule

Do not make budget decisions from CPL alone.

Minimum decision logic should consider:

- lead quality;
- booking rate;
- consult completion;
- advisory fit;
- cost per qualified booked consult;
- whether the creative attracts the right problem.
