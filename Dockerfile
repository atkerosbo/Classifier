FROM python:3.10.13-bookworm

WORKDIR /app

COPY requirements.txt .

RUN python -m venv env && \
    . env/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD [ "python", "./classifier.py" ]