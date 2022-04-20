FROM python:3.9.12-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.settings



WORKDIR /code

COPY ./src/indicaa-api/requirements.txt .
RUN pip install -r requirements.txt

RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends firefox

COPY . .

EXPOSE 8000
EXPOSE 5432
