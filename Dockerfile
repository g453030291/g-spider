FROM python:3.11-slim-buster

WORKDIR /app

COPY . /app

#RUN ls -l requirements.txt

RUN pip3 install -r requirements.txt --default-timeout=100

#COPY .github/workflows .

CMD ["scrapy", "runspider", "bilibilispider.py"]

#CMD [ "docker", "build" , "--tag", "g-python-docker", "."]