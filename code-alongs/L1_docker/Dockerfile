FROM python:3.11

# Host (main) container(.)
ADD main.py .

RUN pip install plotly_express dash

# Den "lyssnar" på den här porten
EXPOSE 8050

CMD ["python", "./main.py"]