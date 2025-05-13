# Visual regression tests for UNCCD PRAIS4 manual

This test suite uses [Backstopjs](https://github.com/garris/BackstopJS).
It can generate screenshots of pages configured in `backstop.config.js` and compare the locally generated pages with published versions.

## Running on development environment

```bash
# Install
cd backstopjs
npm install
# Create reference screenshots from production
npm run reference
# Compare test environment with saved reference
npm run test
# Check HTML report generated in `backstop_data/html_report` or run remote http server and open http://localhost:3000/backstop_data/html_report/
npx backstop remote
npx backstop openReport
```

## Other notes

- Some DOM elements are removed (language switcher, etc.), see `removeSelectors` property in `backstop.config.js`
