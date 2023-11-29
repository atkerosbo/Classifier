FROM python:3.11

# Install Rust and Cargo
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt

CMD ["python", app, ]