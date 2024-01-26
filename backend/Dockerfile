# 
FROM python:3.12.1-slim-bullseye

# 
WORKDIR /backendCode

# 
COPY ./requirements.txt /backendCode/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /backendCode/requirements.txt

# 
COPY ./backendCode /backendCode/backend

# Expose the port on which the application will run
EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "backend.server.app:app", "--host", "0.0.0.0", "--port", "8080"]