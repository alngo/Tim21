FROM python:3.7

RUN apt-get update \
    && apt-get -y install curl build-essential libssl-dev \
    && apt-get clean \
    && pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

# TA-Lib
RUN cd /tmp; \
	wget http://sourceforge.net/projects/ta-lib/files/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz; \
	tar -xzf ta-lib-0.4.0-src.tar.gz; \
	cd ta-lib; \
	./configure ; make; make install; \
	cd ..; \
	rm ta-lib-0.4.0-src.tar.gz; \
	rm -rf ta-lib
RUN pip install TA-Lib

ENTRYPOINT []
