FROM continuumio/miniconda3:4.8.2
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY environment.yml ./
RUN conda env update -f environment.yml -n base
COPY . /app
CMD ["python", "./script.py"]


