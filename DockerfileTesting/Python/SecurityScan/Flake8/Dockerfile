FROM python:3.9

# Install Bandit scanner
RUN pip install flake8

# Set working directory (optional, but improves clarity)
WORKDIR /app

# Copy user script volume (adjust mount point if needed)
COPY dirty.py .

# Run Bandit scanner and redirect output to file
RUN flake8 dirty.py | tee dirty.txt