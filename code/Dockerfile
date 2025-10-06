FROM ubuntu:focal
MAINTAINER Thomas Krijnen <thomas@aecgeeks.org>

# --- Configurable branches/paths ---
ENV REPO_BRANCH=translations

# translations
ENV TRANSLATIONS_REPO_DIR=/app/translations
ENV TRANSLATIONS_BRANCH=translations
ENV TRANSLATIONS_SRC_DIR=${TRANSLATIONS_REPO_DIR}/translations
ENV TRANSLATIONS_BUILD_DIR=/data/translations-build
ENV PO_HASH_PATH=${TRANSLATIONS_BUILD_DIR}/po_hash_map.json

#1week interval

# system dependencies
RUN mkdir -p /usr/share/man/man1
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -y curl openjdk-11-jdk-headless python3 python3-distutils procps lsof supervisor graphviz unzip git texlive texlive-pictures texlive-latex-extra imagemagick-6.q16 wget redis-server

# remove policy to disable PDF conversion
RUN rm /etc/ImageMagick-6/policy.xml

# Python dependencies
RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/pip/3.8/get-pip.py | python3
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r /code/requirements.txt

# Solr
WORKDIR /
RUN curl --location --silent --show-error --retry 5 'https://archive.apache.org/dist/lucene/solr/8.6.3/solr-8.6.3.tgz' -o - | tar zxf -
RUN chmod +x /solr-8.6.3/bin/*

# ifcopenshell
WORKDIR /code
RUN curl --silent --show-error --retry 5 -o /tmp/ifcopenshell_python.zip https://s3.amazonaws.com/ifcopenshell-builds/ifcopenshell-python-`python3 -c 'import sys;print("".join(map(str, sys.version_info[0:2])))'`-v0.7.0-476ab50-linux64.zip
RUN mkdir -p `python3 -c 'import site; print(site.getusersitepackages())'`
RUN unzip -d `python3 -c 'import site; print(site.getusersitepackages())'` /tmp/ifcopenshell_python.zip

# Sample models
ADD https://api.github.com/repos/buildingSMART/IFC4.3.x-sample-models/git/refs/heads/main /tmp/sample-models-version.json
RUN git clone --depth 1 https://github.com/buildingSMART/IFC4.3.x-sample-models /examples

# Main repo
ADD https://api.github.com/repos/buildingSMART/IFC4.3.x-development/git/refs/heads/$REPO_BRANCH /tmp/repo-initial-version.json
RUN git clone --depth 1 https://github.com/buildingSMART/IFC4.3.x-development /ifc43 --branch $REPO_BRANCH
ENV REPO_DIR=/ifc43

# Translations repo (branch: translations) → cloned into $TRANSLATIONS_REPO_DIR
ADD https://api.github.com/repos/buildingSMART/IFC4.3.x-output/git/refs/heads/$TRANSLATIONS_BRANCH /tmp/translations-branch-version.json
RUN git clone --depth 1 https://github.com/buildingSMART/IFC4.3.x-output $TRANSLATIONS_REPO_DIR --branch $TRANSLATIONS_BRANCH

ADD version.json *.py tikz-uml.sty IFC4_conf.xml mvdXML_V1.1_add1.xsd /code/
ADD express_diff/* /code/express_diff/
ADD templates/* /code/templates/

WORKDIR /code

RUN mkdir svgs psd /var/redis-data $TRANSLATIONS_BUILD_DIR

COPY supervisord.conf /etc/supervisord.conf

ENTRYPOINT supervisord -n
