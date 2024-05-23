FROM python:3.9
RUN apt-get -y update
RUN apt-get -y install libgdal-dev gdal-bin
RUN pip install geopandas

RUN mkdir src

WORKDIR src

COPY script.py .

COPY data /data

CMD ["python", "./script.py"]


