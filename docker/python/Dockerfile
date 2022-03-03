FROM python:3.8.3

ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /usr/shopping

COPY ./app /usr/shopping/app
# COPY ./seeds /usr/doc-classifier/seeds
# COPY .env /usr/doc-classifier

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN apt-get update && pip install -r /usr/shopping/app/requirements.txt

# COPY ./docker/python/entrypoint.sh /usr/local/bin/
# RUN chmod 755 /usr/local/bin/entrypoint.sh
# RUN ln -s /usr/local/bin/entrypoint.sh /entrypoint.sh # backwards compat
# convert entrypoint CRLF back to LF (as this file may be altered by git on Windows hosts)
# RUN sed -i -e 's/\r$//' /usr/local/bin/entrypoint.sh
RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y
# set entrypoint
CMD ["flask", "run"]
