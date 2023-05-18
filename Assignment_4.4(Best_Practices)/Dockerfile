FROM python:3.8-slim-buster

WORKDIR /home/app/

COPY ./ /home/app/

ENV PYTHONPATH=${PYTHONPATH}:/home/app/


VOLUME /app/todo_data

# SET (1 for Development and 0 for Production)
ENV DEBUG = 1 
COPY requirements.txt .

# Requirements installation should be moved from runtime to build time.
RUN pip install -r requirements.txt

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000"]

