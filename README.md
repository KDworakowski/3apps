![Optional_Text](../master/docs/docs.drawio.png)
# Setup
### Clone Repository
`git clone https://github.com/KDworakowski/3apps`
### Setup ENV variables in docker-compose.yaml
```
- RABBITMQ_HOST=rabbitmq_host
- RABBITMQ_ROUTING=rabbitmq_routing
- RABBITMQ_USER=rabbitmq_user
- RABBITMQ_PASSWORD=rabbitmq_password
- MONGODB_URL=mongodb://mongodb_host:27017/
- RABBITMQ_URL=amqp://rabbitmq_user:rabbitmq_password@rabbitmq_host/
```
### Run the app in Docker
`docker-compose up --build`

**BEFORE RUNNING THE APP MAKE SURE YOU HAVE RABBITMQ AND MONGODB INSTALLED AND TURNED ON**
# Sending Requests
(producer)Post add requests: `http://localhost:80/add`

(getSize)Get size requests: `http://localhost:90/size`
## Producer
Producer allows you to send JSON Post request to RabbitMQ.
## Listener
Listener listens on RabbitMQ queue, after it receive the data it will add the timestamp to the data and insert the data to MongoDB.
## GetSize
GetSize allows you to send Get request to receive the amount of objects stored in MongoDB.
# RabbitMQ Installation
You can install it using any package manager like apt or brew on macOS.

You also need to enable RabbitMQ Management Console, you can do it running `sudo rabbitmq-plugins enable rabbitmq_management` command.

Using homebrew you might need to add RabbitMQ and CLI scripts to the path.
You can do that adding below config to your shell config file
```
export HOMEBREW_RABBITMQ=/opt/homebrew/Cellar/rabbitmq/(version)/sbin/
export PATH=$PATH:$HOMEBREW_RABBITMQ
```
**IMPORTANT: Location of the homebrew may be different on your device, you can also try /usr/local/Cellar/rabbitmq/(version)/sbin/**

Then simply run `rabbitmq-server` or `homebrew services start rabbitmq`, default username and passwords are guest
# MongoDB Community Edition Installation
You can install it using any package manager like apt or brew on macOS.
[Here is the installation tutorial for some distros including Ubuntu](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

On macOS with homebrew simply run these commands
```
brew tap mongodb/brew
brew update
brew install mongodb-community@5.0
```

Then you can run it using `mongod` or `homebrew services start mongodb-community`.
