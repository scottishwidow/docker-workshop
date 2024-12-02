FROM python:3.12.3-alpine

RUN apk --no-cache add curl

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]


# CMD ["flask", "--app=app", "run", "--host=0.0.0.0", "--port=5000"]
