#! /bin/bash
sphinx-build -b gettext -d _build/.doctrees/gettext . locales/source
sphinx-intl update -p locales/source -l es -l fr -l ar -l ru -l zh_CN
READTHEDOCS=True sphinx-build -b html -d _build/.doctrees/en -D language=en . _build/html/en/latest
READTHEDOCS=True sphinx-build -b html -d _build/.doctrees/es -D language=es . _build/html/es/latest
READTHEDOCS=True sphinx-build -b html -d _build/.doctrees/fr -D language=fr . _build/html/fr/latest
READTHEDOCS=True sphinx-build -b html -d _build/.doctrees/ar -D language=ar . _build/html/ar/latest
READTHEDOCS=True sphinx-build -b html -d _build/.doctrees/ru -D language=ru . _build/html/ru/latest
READTHEDOCS=True sphinx-build -b html -d _build/.doctrees/zh_CN -D language=zh_CN . _build/html/zh-cn/latest


# python -m http.server -d _build/html/