#!/bin/bash
while true
do
curl -X 'POST' \
  'http://localhost:80/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "taskid": "task1234",
  "description": "Example description",
  "params": {
    "test1": "1234",
    "test2": "5678"
  }
}'
done
