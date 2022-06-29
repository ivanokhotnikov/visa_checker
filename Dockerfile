FROM python:3.8.10-slim
EXPOSE 8501
COPY requirements.txt app/requirements.txt
RUN apt-get update && pip install -r app/requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "visa_checker.py", "--server.port=8501", "--server.address=0.0.0.0"]