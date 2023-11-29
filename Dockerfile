# Use an official Python 3.11 image as the base image
FROM python:3.11

# Install Rust and Cargo
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain=1.74.0

# Set environment variables
ENV PATH="/root/.cargo/bin:${PATH}"
ENV LD_LIBRARY_PATH="/root/.cargo/bin:${LD_LIBRARY_PATH}"

# Set the working directory inside the container
WORKDIR /app/

# Copy the requirements.txt file to the working directory
COPY ./requirements.txt /app/requirements.txt

# Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app/

# Define the default command to run when the container starts

CMD ["python", app, ]