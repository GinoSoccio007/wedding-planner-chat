FROM python:3.9-slim

# Install curl for health check
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

# Add a startup script
COPY <<EOF /start.sh
#!/bin/bash
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
EOF

RUN chmod +x /start.sh

# Modified healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD curl --fail http://localhost:8501/_stcore/health || exit 1

CMD ["/start.sh"]
