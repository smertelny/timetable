FROM python:3.6
ENV PYTHONUNBUFFERED=1
WORKDIR /app
ADD /dev.txt /app
RUN pip install -r dev.txt
