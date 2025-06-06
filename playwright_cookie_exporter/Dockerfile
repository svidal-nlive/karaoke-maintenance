FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy

USER root
RUN apt-get update && apt-get install -y supervisor python3-pyvirtualdisplay \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Set up for playwright
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN playwright install chromium

COPY export_cookies.py ./
COPY supervisor.conf /etc/supervisor/conf.d/supervisord.conf

# Entrypoint: runs supervisord (VNC+cron runner)
CMD ["/usr/bin/supervisord"]
