FROM python:3.12.7

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN playwright install --with-deps

COPY .env .env
COPY main.py main.py   
COPY app app            

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
