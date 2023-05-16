FROM python:3.8-slim-buster

WORKDIR /home/app/
COPY ./ /home/app/
# RUN agt-get update && apt-get -yy install wget && apt-get clean

ENV PYTHONPATH=${PYTHONPATH}:/home/app/

# volume Configuration
VOLUME /app/todo_data

# Change the DEBUG variable to 0 to run it in production mode and 1 to run in debug mode.
ENV DEBUG=1 
COPY requirements.txt .

# Requirements.txt is running.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000"]


