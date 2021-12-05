FROM ubuntu
MAINTAINER Deepak Verma "deepakv243601@gmail.com"
RUN apt update && apt install python3 -y && apt install pip -y 
COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt
RUN useradd cloud && chown -R cloud /opt
USER cloud
ENTRYPOINT ["python3"]
CMD ["app.py"]
