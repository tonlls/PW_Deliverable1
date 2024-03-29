FROM python:3.8.10
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
RUN python manage.py collectstatic
EXPOSE 8081