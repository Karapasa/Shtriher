 FROM python:3
 WORKDIR /shtrih
 COPY . /shtrih
 RUN pip3 install --upgrade pip -r requirements.txt
 EXPOSE 6005
