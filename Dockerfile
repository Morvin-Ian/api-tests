FROM python:3.8  
 
WORKDIR /django  
ENV PYTHONUNBUFFERED 1  
COPY . /django  
RUN pip install -r requirements.txt  

