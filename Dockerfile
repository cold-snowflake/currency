FROM python:3.11.5

COPY requirements.txt requirements.txt


WORKDIR /project/code

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONPATH /project/code/app

CMD gunicorn --workers 4 --threads 4 settings.wsgi --timeout 30 --max-requests 10000 --log-level info --bind 0.0.0.0:8000