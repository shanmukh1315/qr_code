# Use official Python base image
FROM python:3.12-slim-bullseye

# Set working directory
WORKDIR /app

# Copy dependency file and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Add non-root user and folders
RUN useradd -m myuser && mkdir logs qr_codes && chown myuser:myuser logs qr_codes

# Copy application code
COPY --chown=myuser:myuser . .

# Switch to non-root user
USER myuser

# Default run command
ENTRYPOINT ["python", "main.py"]
CMD ["--url", "http://github.com/kaw393939"]
