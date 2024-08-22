FROM python:3.8.5-slim-buster
RUN apt update -y && apt install awscli -y
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# Define the entry point for the container
ENTRYPOINT ["python", "main.py"]
# Serve the model
CMD ["serve"]

#CMD ["python3", "main.py"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
