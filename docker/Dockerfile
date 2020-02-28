FROM python:3.7-alpine
COPY requirements.txt

RUN pip install -r requirements.txt

COPY src/ /app

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

WORKDIR /bot
