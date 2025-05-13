// see https://www.metaltoad.com/blog/backstopjs-part-deux-javascript-config-and-makefile

const baseUrlTest = 'http://localhost:8000/_build/html/'
const baseUrlReference = 'https://prais4-reporting-manual.unccd.int/zh-cn/latest/'

var scenarios = [];
var paths = [
    'index.html',
    'introduction.html',
    'SO1.html',
    'SO2.html',
    'SO3.html',
    'SO4.html',
    'SO5.html',
    'voluntary_targets_and_others.html',
    'implementationFramework.html',
    'annex_I.html',
    'annex_II.html',
];

for (var k = 0; k < paths.length; k++) {
    scenarios.push (
      {
        "label": paths[k],
        "referenceUrl": baseUrlReference+paths[k],
        "url": baseUrlTest+paths[k]
      }
    );
}

module.exports = {
    "id": "prais4-reporting-manual",
    "viewports": [
      {
        "label": "desktop",
        "width": 2560,
        "height": 1440
      }
    ],
    "onBeforeScript": "playwright/onBefore.js",
    "onReadyScript": "playwright/onReady.js",
    "scenarios": scenarios,
    "scenarioDefaults": {
        "readyEvent": "",
        "readySelector": "",
        "delay": 1000,
        "hideSelectors": [],
        "removeSelectors": [".wy-breadcrumbs", ".switch-menus", "readthedocs-flyout"],
        "hoverSelector": "",
        //"clickSelectors": [".eu-cookie-compliance-agree-button"],
        //"postInteractionWait": 1000,
        "selectors": [],
        "selectorExpansion": true,
        "expect": 0,
        "misMatchThreshold" : 0.5,
        "requireSameDimensions": true
    },
    "paths": {
      "bitmaps_reference": "backstop_data/bitmaps_reference",
      "bitmaps_test": "backstop_data/bitmaps_test",
      "engine_scripts": "engine_scripts",
      "html_report": "backstop_data/html_report",
      "ci_report": "backstop_data/ci_report"
    },
    "report": ["browser"],
    "engine": "playwright",
    "engineOptions": {
      "args": ["--no-sandbox"]
    },
    "asyncCaptureLimit": 5,
    "asyncCompareLimit": 50,
    "debug": true,
    "debugWindow": false
}