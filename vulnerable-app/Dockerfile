# Intentionally pinned to an old base image + old pinned dependencies so that
# both `qscanner code` (SCA on requirements.txt) and `qscanner image` (on the
# built image) flag the same vulnerable Python packages, plus vulnerable OS
# packages inherited from the old base image.
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py config.yaml ./

EXPOSE 5000
CMD ["python", "app.py"]
