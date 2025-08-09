FROM python:3.6
#MAINTAINER xie186@purdue.edu

#COPY ./omblog/ /app

COPY ./requirement.txt  /app/

WORKDIR /app/

RUN pip install -r ./requirement.txt

#CMD ["sleep", "infinity"]
#CMD ["python","manage.py","runserver","0.0.0.0:8123"]
#
COPY ./docker/python/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
