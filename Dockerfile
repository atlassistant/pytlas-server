FROM python:3.6-slim
COPY requirements.txt /src/
WORKDIR /src

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove gcc libc-dev

RUN snips-nlu download-all-languages

COPY . /src/

RUN python manage.py collectstatic --noinput

EXPOSE 8000
ENTRYPOINT ["daphne", "-b", "0.0.0.0", "pytlas_server.asgi:application"]
