FROM python:3.11

WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt

CMD ["python", app, ]