# 3apps
## Setup
### Clone Repository
`git clone https://github.com/KDworakowski/3apps`
### Run the app in Docker
`docker-compose up --build`
## Sending Requests
Producer requests: `http://localhost:80/docs`

GetSize requests: `http://localhost:90/docs`
## Producer
Producer allows you to send JSON add request to RabbitMQ
## GetSize
GetSize allows you to get the amount of objects stored in MongoDB
