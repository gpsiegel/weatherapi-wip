FROM python:3.8-alpine

#Create environment variables
ARG AWS_KEY
ARG AWS_SECRET
ARG API_KEY

ENV AWS_KEY=$AWS_KEY
ENV AWS_SECRET=$AWS_SECRET
ENV API_KEY=$API_KEY

# Set the working directory in the container
WORKDIR /app/

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . /app/

# Specify the command to run on container start
CMD [ "python3", "scan.py" ]