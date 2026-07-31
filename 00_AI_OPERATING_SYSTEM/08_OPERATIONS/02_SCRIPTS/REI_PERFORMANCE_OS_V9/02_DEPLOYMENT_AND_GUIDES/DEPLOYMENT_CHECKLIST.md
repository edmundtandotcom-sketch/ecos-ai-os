# REI Performance OS v9.0 — Deployment Checklist

## A. Create the Apps Script project

1. Open `REI_Performance_OS_MASTER_SHEET_v9.0`.
2. Go to **Extensions → Apps Script**.
3. Rename the project to `REI Performance OS v9.0`.
4. Delete the default `Code.gs` contents.
5. **Recommended fast path:** paste `REI_AppsScript_v9.0_ALL_IN_ONE.gs` into `Code.gs`, then create `Dashboard.html`, `Styles.html` and `Client.html`. Do not paste the numbered `.gs` files as well.
6. **Modular alternative:** instead of the all-in-one file, create the numbered `.gs` files `00_Config.gs` through `07_Setup.gs`, plus the three HTML files.
7. Open **Project Settings → Show appsscript.json manifest file** and replace it with the supplied manifest.

## B. Run setup

1. Select `setupV9` in the function dropdown.
2. Click **Run** and approve permissions.
3. Return to the Sheet and refresh it.
4. Use the new **REI Performance OS v9** menu to store:
   - Dashboard access key
   - Meta access token
   - GHL private integration key
5. In Apps Script **Project Settings → Script Properties**, verify or add:
   - `SHEET_ID` = `167C_gZsN5RtImBFArt5hXcUqMAHlfJFqX52f0rN_pWk`
   - `META_AD_ACCOUNT_ID` = your `act_...` account
   - `META_API_VERSION` = the version currently working in your Meta app
   - `GHL_LOCATION_ID`
   - `GHL_PIPELINE_ID`
   - `GOOGLE_ADS_CUSTOMER_ID`
6. Run **REI Performance OS v9 → Run full sync now**.
7. Resolve any missing-credential or API errors shown in `Error_Log`.
8. Run **REI Performance OS v9 → Install safe sync triggers** only after the manual sync passes.

## C. Deploy so Chrome and mobile do not choose a Google account

1. Click **Deploy → New deployment**.
2. Select **Web app**.
3. Description: `REI Performance OS v9.0 production`.
4. **Execute as:** `Me` / `User deploying`.
5. **Who has access:** `Anyone` — not `Anyone with Google account`.
6. Click **Deploy** and copy the `/exec` URL.
7. Open the URL in a Chrome Incognito window. It should show the REI access-key screen, not a Google account chooser.
8. Open the same URL on Chrome mobile and choose **Add to Home screen**.

The access key is checked server-side against Script Properties. Do not put it in the URL.

## D. Install Google Ads v9 script

1. Google Ads → **Tools → Bulk actions → Scripts**.
2. Create a new script and paste `REI_GoogleAds_Script_v9.0.gs`.
3. Preview and authorise.
4. Run once.
5. Schedule daily at 6:00 AM Singapore time.

## E. Validate

1. Run `runFullSyncFromEditor` once.
2. Run `runHealthCheckFromEditor`.
3. Confirm `Health_Check` reports required credentials and tabs as OK.
4. Confirm `Daily_Performance_Fact` contains both Meta and Google rows.
5. Confirm `Daily_Funnel_Fact` contains aggregate GHL rows without phone/email fields.
6. Open desktop Chrome, Android Chrome and iPhone Chrome/Safari.
7. Check Overview, Ads, Funnel, Leads, Forecast and Health.

## F. Cutover and rollback

Keep the current v8.43 `/exec` URL active until v9 passes three consecutive days of checks. If v9 fails, continue using v8.43 and inspect `Error_Log`; the archived source and original master sheet remain untouched.
