FROM python:3.11-slim-buster

WORKDIR /app

RUN pip3 install -r requirements.txt

#COPY .github/workflows .

CMD ["scrapy", "runspider", "bilibilispider.py"]

#CMD [ "docker", "build" , "--tag", "g-python-docker", "."]