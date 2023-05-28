FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install plotly_express dash

# Den "lyssnar" på den här porten
EXPOSE 8050

CMD ["python", "./src/main.py"]