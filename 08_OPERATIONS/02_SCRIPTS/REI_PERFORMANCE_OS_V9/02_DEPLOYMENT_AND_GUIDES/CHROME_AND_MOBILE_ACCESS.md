# Chrome and Mobile Access — Why v9 avoids the multi-account failure

The current dashboard uses a Google-authenticated Apps Script deployment and then makes browser-side requests back to its own `/exec` URL. When Chrome has several Google accounts open, Google can apply the default account when it cannot determine which account a service should use. That can cause the app to open under an account without the necessary access.

v9 changes the access model:

- The web app executes as the deploying user.
- The deployment is accessible to anyone with the link.
- The dashboard shows its own access-key screen.
- Data calls use `google.script.run`, not repeated `fetch()` calls to the public deployment URL.
- The access key is sent through the encrypted Apps Script client/server channel and is checked against Script Properties.
- No Meta or GHL token is returned to the browser.
- Lead phone numbers and emails are excluded from the browser payload.

## Chrome test

1. Open the new `/exec` URL in Incognito.
2. Confirm there is no Google sign-in or account chooser.
3. Enter the dashboard access key.
4. Close and reopen the tab.
5. Test with several Google accounts signed in to normal Chrome.

## Mobile setup

1. Open the `/exec` URL in Chrome mobile.
2. Enter the access key.
3. Menu → **Add to Home screen**.
4. Launch from the home-screen icon.
5. Use the bottom navigation: Overview, Ads, Funnel, Leads, Forecast, Health.

## Security decision

This design trades Google-account gating for a server-side app access key. Use a strong key, do not share the URL and key publicly, and rotate the key immediately if it is exposed. For stricter enterprise authentication, the next step is Cloud Run with Identity-Aware Proxy—not another Apps Script account-selection workaround.
