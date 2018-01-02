FROM python:3.6
LABEL maintainer="Tom Dyson"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

RUN pip install pipenv
RUN pipenv install --system
RUN pip install gunicorn

COPY . /code/
WORKDIR /code/

EXPOSE 8000
CMD python manage.py migrate
CMD exec gunicorn wagtail_docker_test.wsgi:application --bind 0.0.0.0:8000 --workers 3