#define the docker file
#specify a base image
FROM python:3.8

#add the main file into our container
ADD main.py .

#install the dependences
RUN pip install git+https://github.com/Ifyokoh/End-to-End-Machine-Learning.git

#specify the entry command when we start our container
CMD ["python", "./main.py"]