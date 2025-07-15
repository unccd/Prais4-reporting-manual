#! /bin/bash
LANGUAGES=("en" "es" "fr" "ar" "ru" "zh_CN")
# LANGUAGES=("en")
mkdir -p _build/pdf
for LANGUAGE in "${LANGUAGES[@]}"; do
    SPHINX_DOCTREES="_build/.doctrees/$LANGUAGE"
    python -m sphinx -b latex -D language=$LANGUAGE -d "$SPHINX_DOCTREES" . _build/latex
    (cd _build/latex && \
     latexmk -r latexmkrc -pdf -f -dvi- -ps- -jobname="PRAIS4 Reporting manual $LANGUAGE" -interaction=nonstopmode -outdir=../pdf \
    )
done