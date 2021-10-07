#! /bin/bash
sphinx-build -b gettext . _build/gettext
sphinx-intl update -p _build/gettext -l es -l fr -l ar -l ru -l zh
