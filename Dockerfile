FROM python:3.9-slim

WORKDIR /app

# Install wget for healthcheck (lighter than curl)
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

# Environment variables
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_BASE_URL_PATH=""

# Modified healthcheck using wget
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8501/_stcore/health || exit 1

# Start command with explicit wait
CMD streamlit run app.py \
    --server.port=8501 \
    --server.address=0.0.0.0 \
    --server.baseUrlPath="" \
    --browser.serverAddress=0.0.0.0 \
    --server.enableCORS=true
