FROM python:3.12-slim
WORKDIR /app
COPY requirements_long.txt .
# COPY . .
RUN pip install -r requirements_long.txt
COPY . .
CMD ["python", "app.py"]
# ARG TOKEN=super-secret-123
# RUN echo $TOKEN > /tmp/t && rm /tmp/t
