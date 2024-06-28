FROM python:3.9-slim

# Install dependencies
RUN apt-get update \
  && apt-get -y install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ara libtesseract-dev libleptonica-dev

RUN apt-get install -y ffmpeg libsm6 libxext6

# Set up the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uvicorn python-multipart

# Expose the default port
EXPOSE 8000

ARG PORT
# Run the application
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "${PORT}"]

