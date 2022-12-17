####################################################################################################
## Builder image
####################################################################################################
FROM python:3.11-slim-bullseye AS builder

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
  && apt install -y --no-install-recommends \
  build-essential \
  ca-certificates \
  curl

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN python -m pip install --upgrade pip setuptools
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /Kumiko_IPC

COPY /pyproject.toml /Kumiko_IPC/
COPY /poetry.lock /Kumiko_IPC/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes \
  && pip wheel --wheel-dir=/Kumiko_IPC/wheels -r requirements.txt

####################################################################################################
## Final image
####################################################################################################
FROM python:3.11-slim-bullseye
RUN apt update \
  && apt install -y --no-install-recommends \
  tini \
  ca-certificates \
  bash \
  netcat

WORKDIR /Kumiko_IPC
COPY /dramatiq_ipc/ /Kumiko_IPC/dramatiq_ipc/
COPY /Docker/start.sh /Kumiko_IPC/start.sh
COPY /Docker/wait-for /Kumiko_IPC/wait-for

COPY --from=builder /Kumiko_IPC/wheels /Kumiko_IPC/wheels
COPY --from=builder /Kumiko_IPC/requirements.txt /Kumiko_IPC/requirements.txt

RUN pip install --upgrade pip setuptools

RUN adduser --disabled-password --gecos "" kumiko_ipc \
  && chown -R kumiko_ipc:kumiko_ipc /Kumiko_IPC \
  && chmod +x /Kumiko_IPC/start.sh \
  && chmod +x /Kumiko_IPC/wait-for

USER kumiko_ipc

ENV PATH="${PATH}:/home/kumiko_ipc/.local/bin"

RUN pip install --user --no-index --find-links=/Kumiko_IPC/wheels -r requirements.txt

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["/Kumiko_IPC/start.sh"]

STOPSIGNAL SIGTERM

LABEL org.opencontainers.image.title="Kumiko_IPC"
LABEL org.opencontainers.image.description="Kumiko's High Performance IPC Workers"
LABEL org.opencontainers.image.licenses="GPL-3.0"
LABEL org.opencontainers.image.source="https://github.com/No767/Kumiko_IPC"
