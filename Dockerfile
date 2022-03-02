FROM python:3.8
LABEL maintainer="jorgeav527@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

COPY ./scripts /scripts

EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip wheel setuptools && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

RUN mkdir /app
WORKDIR /app
COPY ./app /app

ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]