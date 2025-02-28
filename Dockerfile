FROM python

COPY . .
WORKDIR /app

RUN pip install -r requirements

ENTRYPOINT ["python3","main.py"]