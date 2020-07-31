FROM python:3.8.5-alpine3.12

COPY python/ /python/

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip && pip install -r /requirements.txt

ENTRYPOINT ["python", "/python/api.py"]