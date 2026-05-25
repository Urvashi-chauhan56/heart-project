FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --default-timeout=100 -r requirements.txt
CMD ["python", "heart_project.py"]