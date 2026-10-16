FROM python:3.11-slim-bookworm
WORKDIR /app
COPY app/ ./app/
COPY config/ ./config/
RUN python -m py_compile app/main.py
EXPOSE 8000
CMD ["python", "app/main.py"]