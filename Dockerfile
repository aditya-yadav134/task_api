FROM python:3.10-alpine

RUN mkdir -p taskapi

COPY . /taskapi

RUN pip install -r ./taskapi/requirements.txt 

RUN python ./taskapi/manage.py migrate

CMD ["python", "./taskapi/manage.py","runserver", "0.0.0.0:8000"]