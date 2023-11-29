FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m venv env && \
    . env/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD [ "python", "./your_script.py" ]