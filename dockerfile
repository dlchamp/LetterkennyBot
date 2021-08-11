FROM python:3.10.0rc1-buster

#Create application directory
RUN mkdir /app
WORKDIR /app

#Install dependcies
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copy source code
COPY . /app/

#Run application

CMD ["python","-u", "main.py"]


