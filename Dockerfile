FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN pip install gunicorn
ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY . /code/
WORKDIR /code/lylesightings

# EXPOSE 8000
CMD ["../run.sh"]