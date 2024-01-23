FROM python:3.10.11
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

EXPOSE 8000


RUN python manage.py makemigrations 

RUN python manage.py migrate 
RUN python manage.py collectstatic --noinput 

CMD python manage.py runserver 0.0.0.0:8000