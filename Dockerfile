FROM python:3.12-slim-bookworm
WORKDIR /manual

RUN apt-get -q update \
 && apt-get install -qq \
    build-essential \
    latexmk \
    chktex \
    texlive-xetex \
    texlive-luatex \
    fonts-freefont-otf \
    texlive-fonts-extra \
    texlive-lang-arabic \
    texlive-lang-chinese \
    texlive-lang-cjk \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]
