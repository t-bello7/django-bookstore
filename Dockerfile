# Pull base image
FROM python:3.7
# Set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/home/appuser/.local/bin:${PATH}"


# Set work directory
WORKDIR /code 
RUN useradd -ms /bin/bash appuser 
RUN    chown -R appuser:appuser /code
RUN    chmod 755 /code
USER appuser

# Install dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends gcc
COPY Pipfile Pipfile.lock /code/ 


RUN pip install --upgrade pip \ 
    pip install pipenv && pipenv install --system
RUN pip uninstall pipenv -y

# COPY ./requirements.txt /code/requirements.txt
# RUN pipenv install -r requirements.txt

# Copy project
COPY . /code/
