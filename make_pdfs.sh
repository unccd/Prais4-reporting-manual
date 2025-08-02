#! /bin/bash
ALL_LANGUAGES=("en" "es" "fr" "ar" "ru" "zh_CN")
DEFAULT_LANGUAGES=("en")

# Check if arguments are provided
if [ "$#" -eq 0 ]; then
    # No arguments, use default languages
    LANGUAGES=("${DEFAULT_LANGUAGES[@]}")
elif [ "$1" == "all" ]; then
    LANGUAGES=("${ALL_LANGUAGES[@]}")
else
    # Use provided language codes from arguments
    LANGUAGES=("$@")
fi

mkdir -p _build/pdf
for LANGUAGE in "${LANGUAGES[@]}"; do
    SPHINX_DOCTREES="_build/.doctrees/$LANGUAGE"
    python -m sphinx -T -b latex -D language=$LANGUAGE -d "$SPHINX_DOCTREES" . _build/latex
    (cd _build/latex && \
      latexmk -r latexmkrc -pdf -f -dvi- -ps- \
      -jobname="prais4-reporting-manual-$LANGUAGE" \
      -interaction=nonstopmode -outdir=../pdf \
      "prais4-reporting-manual-$LANGUAGE.tex"
    )
done
