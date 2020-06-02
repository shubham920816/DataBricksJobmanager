FROM alpine:3.7
FROM python:3.6
MAINTAINER shubhammishra920816@gmail.com
USER root
COPY . /mnt/
WORKDIR /mnt/
RUN pip install -r requirements.txt
RUN pip install --index-url https://build:sngw4qsmpoqgicbaujzb3aa7p2la4w4cbrhsgidrynde25mg4szq@pkgs.dev.azure.com/shubhammishra920816/Artifact/_packaging/Personalpippackages-dev/pypi/simple/
EXPOSE 80
CMD ["python","-m","flask","run","--host=0.0.0.0"]
CMD ["python","app/app.py"]
