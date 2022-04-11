# Assignment 1: Shorty URL

As part of the first assignment of the Web Services & Cloud Based Systems course we developed a RESTful service to shorten URLs.  

Implementation details, answer to question 3 and the group members contribution can be found in the ```report.pdf``` document in this repository.


## How to Run

1. Clone this repository
```commandline
    git clone https://github.com/Web-Services-and-Cloud-Based-Systems-G9/assignment-1
```

2. Install dependencies (pip3 can be replaced with pip)
```commandline
    pip3 install -r requirements.txt
```

3. Run file ShortyURL.py
```commandline
    python3 ShortyURL.py
```

4. The service will be in the 8080 port (http://127.0.0.1:8080). An user interface to use the service can be found on the ```/home``` path

Tested on Python 3.8.9. Developed on Flask 2.1.1.


## Deployment

Our web service is deployed on a cloud provider (Heroku) and it is accesible through the following URL: https://shortyurl-ws.herokuapp.com/. A web client with an user interface can be found in: https://shortyurl-ws.herokuapp.com/home