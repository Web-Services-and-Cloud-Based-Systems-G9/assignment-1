# Assignment 2: Shorty URL

As part of the second assignment of the Web Services & Cloud Based Systems course we developed a RESTful service to shorten URLs alongside an authentication service which works using a JWT schema.  
This repository contains the logic of the shortener-service and UI.

Implementation details, answer to questions and the group members contribution can be found in the ```report.pdf``` document in this repository.


## How to Run

0. Make sure you are running the [login-service](https://github.com/Web-Services-and-Cloud-Based-Systems-G9/login-service) in port `8081`.

1. Clone this repository or download the source code
```commandline
    git clone https://github.com/Web-Services-and-Cloud-Based-Systems-G9/assignment-1
```

2. Install dependencies (`pip3` can be replaced with `pip`, depending on your computer configurations)
```commandline
    pip3 install -r requirements.txt
```

3. Run file ShortyURL.py (`python3` can be replaced with `python`, depending on your computer configurations)
```commandline
    python3 ShortyURL.py
```

4. The service will be in the 8080 port (http://127.0.0.1:8080). An user interface to use the web service can be found on the ```/login``` path

Tested on Python 3.8.9. Developed on Flask 2.1.1. A production ready environment is available using `waitress`

## Monitoring

Run the service using the following command to enable monitoring with New Relic: (`python3` can be replaced with `python`, depending on your computer configurations)

```commandline
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python3 ShortyURL.py
```