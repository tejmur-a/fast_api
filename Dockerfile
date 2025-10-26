FROM python:3.12-slim

COPY . .

RUN pip install -r requerements.txt

CMD ["uvicorn", "main:app", "--hosts", "0.0.0.0", "--port", "80"]