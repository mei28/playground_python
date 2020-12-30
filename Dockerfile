FROM jupyter/base-notebook:python-3.8.6

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

COPY requirements.txt .

RUN pip install -U pip  && \ 
    pip install -r requirements.txt

