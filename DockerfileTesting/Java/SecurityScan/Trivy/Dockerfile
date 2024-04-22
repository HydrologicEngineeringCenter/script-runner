FROM ubuntu:latest

RUN apt-get update && apt-get install -y trivy

WORKDIR /app

# User submits Java file (replace with actual submission mechanism)
COPY dockerTest.java .

# Scan the file with Trivy (adjust format as needed)
RUN trivy fs --format json dockerTest.java | tee trivy_report.json

# (Optional) Further processing or build failure based on Trivy report
