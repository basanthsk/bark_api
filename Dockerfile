FROM python:3.8

WORKDIR /barkapp

# Copy the requirements file separately to leverage Docker's caching
COPY ./requirements.txt /barkapp

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the repository code into the container
COPY . /barkapp

# Set the entrypoint command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
