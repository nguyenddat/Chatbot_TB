FROM python:3.12.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \ 
curl 
RUN apt-get install -y gcc g++ python3-dev musl-dev  libffi-dev netcat-traditional
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 zbar-tools libzbar-dev -y


# Set the working directory
RUN mkdir -p backend
WORKDIR /backend

# Copy the requirements file into the container at /backend
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

RUN python main.py