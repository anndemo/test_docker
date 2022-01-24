FROM python

WORKDIR /app

COPY . .

VOLUME ["/app/data"]

CMD ["python", "index.py"]