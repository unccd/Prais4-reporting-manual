#! /bin/bash
sphinx-build -b gettext -d _build/.doctrees . locales/source
sphinx-intl update -p locales/source -l es -l fr -l ar -l ru -l zh
sphinx-build -b html -d _build/doctrees -D language=es . _build/html
