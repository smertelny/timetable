FROM python:3.6
ENV PYTHONUNBUFFERED=1
WORKDIR /app
ADD . /app
RUN pip install -r dev.txt
EXPOSE 80 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
