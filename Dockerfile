# Pull base image
FROM python:3.7
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY 'e!0#xt5#gx-l$vw@xm8=!rotmy(ucuv0_yhc^asx_zxqu@a#g_'
# Set work directory
WORKDIR /code
# Install dependencies
COPY Pipfile Pipfile.lock /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /code/