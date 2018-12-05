FROM python:3.6-slim
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn", "gunicorn pytlas_server.wsgi"]