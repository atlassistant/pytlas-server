FROM python:3.6
COPY requirements.txt /src/
WORKDIR /src
RUN pip install -r requirements.txt
COPY . /src/
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0", "pytlas_server.wsgi"]
