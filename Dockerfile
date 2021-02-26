 FROM python:3
 WORKDIR /combination
 COPY . /combination
 RUN pip3 install --upgrade pip -r requirements.txt
 EXPOSE 6005
 CMD ["gunicorn", "-b", "0.0.0.0:6005", "app:app", "--worker-class", "aiohttp.GunicornWebWorker"]