#! /bin/bash
sphinx-build -b gettext -d _build/.doctrees/gettext . locales/source
sphinx-intl update -p locales/source -l es -l fr -l ar -l ru -l zh_CN
