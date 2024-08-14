FROM python:3.10.14-slim-bullseye
SHELL [ "sh", "-eu", "-c" ]

RUN { \
    apt-get update -y ; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      git ; \
    rm -fr /var/cache/apt/* ; \
    rm -fr /var/lib/apt/lists/* ; \
  }

COPY . /root/tts-service-api-python
WORKDIR /root/tts-service-api-python

ENV VIRTUAL_ENV=/root/tts-service-api-python/.venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
RUN { \
    python -m venv "${VIRTUAL_ENV}" ; \
    pip install --upgrade pip ; \
    pip install --editable . ; \
  }
