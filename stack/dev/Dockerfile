FROM python:alpine
WORKDIR /webapp
EXPOSE 8000
RUN apk add --no-cache libxslt-dev
RUN apk add --no-cache --virtual build-deps gcc python3-dev zlib-dev build-base linux-headers libffi-dev libxml2-dev
RUN LIBRARY_PATH=/lib:/usr/lib
COPY src/requirements.txt .
RUN pip3 install -r requirements.txt
RUN rm requirements.txt
RUN apk del build-deps
ENV PYTHONPATH=/webapp
CMD [ "/webapp/bootstrap.sh" ]