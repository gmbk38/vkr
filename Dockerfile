FROM python:3

COPY . .

WORKDIR /

# EXPOSE 8000

RUN pip install flask
RUN pip install flasgger

CMD [ "python", "./main_flask.py" ]