FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
# ENV PYTHONUNBUFFERED=0
# ENV FLASK_DEBUG=1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--reload", "run:app"]
