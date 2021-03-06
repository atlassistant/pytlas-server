FROM python:3.7-slim
COPY requirements.txt /src/
WORKDIR /src

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove gcc libc-dev

COPY . /src/

RUN python manage.py collectstatic --noinput
RUN chmod +x /src/entrypoint.sh /src/postinstall.sh

EXPOSE 8000
ENTRYPOINT ["/src/entrypoint.sh"]
CMD ["daphne", "-b", "0.0.0.0", "pytlas_server.asgi:application"]
