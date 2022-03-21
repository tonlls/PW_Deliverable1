FROM python:3.8.10
ENV DJANGO_SECRET_KEY abcde0s&&$uyc)hf_3rv@!a95nasd22e-dxt^9k^7!f+$jxkk+$k-
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
RUN python manage.py collectstatic
EXPOSE 8081