FROM python:3.12
WORKDIR /app

#Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Copies everything in the current directory so we copy everything in WORKDIR
COPY . . 

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]