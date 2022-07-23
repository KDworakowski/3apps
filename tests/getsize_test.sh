#!/bin/bash
while true
do
curl -X 'GET' \
  'http://localhost:90/GetStats' \
  -H 'accept: application/json'
done
