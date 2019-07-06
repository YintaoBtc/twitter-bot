FROM python:3.7-alpine

COPY bots/config.py /bots/
COPY bots/fav_new.py /bots/
COPY bots/one_time.py /bots/
COPY bots/bender_phrases.txt /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "one_time.py"]
CMD ["python3", "fav_new.py"]
