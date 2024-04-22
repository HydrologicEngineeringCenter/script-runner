FROM python:3.9
 
# Install Bandit scanner
RUN pip install bandit
 
# Set working directory (optional, but improves clarity)
WORKDIR /app
 
# Copy user script volume (adjust mount point if needed)
COPY ./dirty.py /app/dirty.py
 
#RUN chmod 644 dirty.py
 
# Run Bandit scanner and redirect output to file
RUN bandit /app/dirty.py | tee dirty.txt