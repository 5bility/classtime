FROM python:3.8

COPY . /app

RUN pip install --upgrade pip
RUN pip3 install flask
RUN pip3 install Flask-Migrate
RUN pip3 install SQLAlchemy==1.3.23
RUN pip3 install requests
RUN pip3 install mysqlclient

WORKDIR /app

ENV FLASK_APP=build/app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5003"]