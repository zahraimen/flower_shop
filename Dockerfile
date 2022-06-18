FROM python:3.9-slim

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY . /app
WORKDIR /app

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "--workers=2", "config.wsgi", "-b", "0.0.0.0:80"]