FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.settings



WORKDIR /code

COPY ./src/indicaa-api/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 5432
