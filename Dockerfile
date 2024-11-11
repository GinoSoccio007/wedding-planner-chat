FROM python:3.9-slim

WORKDIR /app

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

# Add healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Add explicit start command
CMD streamlit run app.py --server.port=8501 --server.address=0.0.0.0
