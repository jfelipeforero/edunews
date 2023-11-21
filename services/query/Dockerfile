FROM python:3.10

WORKDIR /app

COPY /app/requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

CMD ["alembic", "upgrade", "head"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4000"]
