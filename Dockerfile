FROM jupyter/base-notebook:python-3.8.6

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

COPY requirements.txt .

RUN pip install -U pip  && \ 
    pip install -r requirements.txt 

RUN cd && \
    wget https://linux.kite.com/dls/linux/current && \
    chmod 777 current && \
    sed -i 's/"--no-launch"//g' current > /dev/null && \
    ./current --install ./kite-installer

RUN jupyter labextension install "@kiteco/jupyterlab-kite"
