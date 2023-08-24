FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install plotly_express dash

# Expose port 8050 for Dash application
EXPOSE 8050

# Command to run the Python script
CMD ["python", "./src/main.py"]
