# Use a base image with Python and any necessary dependencies
FROM python:3.8

# Set the working directory inside the container
WORKDIR /

# Copy your script and data files into the container
COPY ../src/ src/
COPY ../data/ data/
COPY ../model/ model/
COPY ../requirements.txt requirements.txt

# Install any Python dependencies your script requires
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Vim for editing scripts on-the-fly
RUN apt-get update
RUN apt install -y vim

# Define an entry point for the script
WORKDIR /src/RF

ENTRYPOINT /bin/bash
