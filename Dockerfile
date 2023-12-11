FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENV MONGODB_URI=mongodb+srv://<>:<>@cluster0.qjzs4nm.mongodb.net/?retryWrites=true&w=majority
ENV DATABASE_NAME=efgh

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]