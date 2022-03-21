FROM python
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install --upgrade pip
RUN apk add libffi-dev
RUN pip install -r requirements.txt
ADD . /app/
RUN python manage.py collectstatic