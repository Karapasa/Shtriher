 FROM python:3
 WORKDIR /shtrih
 COPY . /shtrih
 RUN pip3 install --upgrade pip -r requirements.txt
 EXPOSE 6005
 CMD ["gunicorn", "-b", "0.0.0.0:6005", "app.main:create_app", "--worker-class", "aiohttp.GunicornWebWorker"]
