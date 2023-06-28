# Set base image (host OS)
FROM python:3.10-alpine

# By default, listen on port 5000
EXPOSE 5001/tcp

# Set the working directory in the container
WORKDIR /api

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN apk add gcc libc-dev libffi-dev python3-dev
RUN pip install pip==23.1.2
RUN pip install --no-binary :all: cffi
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "python", "./application.py" ]