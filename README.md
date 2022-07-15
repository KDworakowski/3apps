# 3apps
## Setup
### Clone Repository
`git clone https://github.com/KDworakowski/3apps`
### Run Listener
`cd listener && ./listener.py`
### Run Producer
`cd producer && uvicorn api:app --host 0.0.0.0 --port 80`
### Run GetSize
`cd getSize && uvicorn api:app --host 0.0.0.0 --port 90`
## Sending Requests
Producer requests: `http://localhost:80/docs`
GetSize requests: `http://localhost:90/docs`
## Producer
Producer allows you to send JSON add request to RabbitMQ
## GetSize
GetSize allows you to get the amount of objects stored in MongoDB
