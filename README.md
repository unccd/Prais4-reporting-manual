# Prais4 reporting manual

Documentation source code for <https://prais4-reporting-manual.readthedocs.io>

PDF version is available [here](https://buildmedia.readthedocs.org/media/pdf/prais4-reporting-manual/latest/prais4-reporting-manual.pdf)

## Local build

    python3.7 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt
    # sphinx-build -b html . _build/html
    # python -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
    # python -m sphinx -b latex -D language=en -d _build/doctrees . _build/latex
    # cd _build/latex
    # latexmk -r latexmkrc -pdf -f -dvi- -ps- -jobname=prais4-reporting-manual -interaction=nonstopmode

## Prerequisites for PDF build

    latexmk
    texlive-xetex
    fonts-freefont-otf
    texlive-fonts-extra
