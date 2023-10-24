# Use a base image with Python and any necessary dependencies
FROM python:3.8

# Set the working directory inside the container
WORKDIR /docker/

# Copy your script and data files into the container
COPY src/ ./../src
COPY data/ ./../data
COPY model/ ./../model
COPY requirements.txt ./

# Install any Python dependencies your script requires
RUN pip install -r requirements.txt

# Define an entry point for the script
WORKDIR ./../src/naive_RF
CMD ["python3", "RF_testing_pipeline.py", "--test_path", "./../../data/raw/dataset2.json"]