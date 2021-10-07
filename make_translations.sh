#! /bin/bash
sphinx-build -b gettext . _build/gettext
sphinx-intl update -p _build/gettext -l es_ES -l fr_FR -l ar_DZ -l ru_RU -l zh_CN
