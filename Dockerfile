FROM python:3.10.8-slim AS blog-tool-base

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /blog-tool
COPY . /blog-tool
RUN chmod -R ug+rwx /blog-tool

FROM blog-tool-base as blog-tool-system

RUN apt -yqq update && apt -yqq upgrade && apt -yqq install ssh build-essential gcc sudo && apt -yqq autoremove

FROM blog-tool-system as blog-tool-poetry

RUN python -m pip install pip --upgrade
RUN /blog-tool/scripts/setup-tooling-poetry.sh
RUN /bin/bash -c ". ~/.profile && cd /blog-tool && poetry install && pip install -e ."
WORKDIR /blog-tool

# ENTRYPOINT [ "/bin/bash", "-c", "blog-tool" ]
ENTRYPOINT [ "blog-tool" ]
