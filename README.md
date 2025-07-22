# Prais4 reporting manual

Documentation source code for <https://prais4-reporting-manual.readthedocs.io>

PDF version is available [here](https://buildmedia.readthedocs.org/media/pdf/prais4-reporting-manual/latest/prais4-reporting-manual.pdf)

## Local python environment

    python3.12 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt

## Build HTML version (English only)

    READTHEDOCS=True sphinx-build -b html -d _build/.doctrees/en -D language=en . _build/html/en/latest

## Build translations (HTML version)

    ./make_translations.sh

## Run local HTTP server

    python -m http.server -d _build/html/
    # Then open http://localhost:8000/en/latest/

## Build PDFs

    ./make_pdfs.sh              # English only
    ./make_pdfs.sh all          # all languages (en es fr ar ru zh_CN)
    ./make_pdfs.sh ar ru zh_CN  # specific languages

## Clean all output

    make clean

## Prerequisites for PDF build

    latexmk
    chktex
    texlive-xetex
    fonts-freefont-otf
    texlive-fonts-extra
    texlive-lang-arabic
    texlive-lang-chinese
    texlive-lang-cjk

