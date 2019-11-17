#!/bin/bash

## SnoothDogg
# Make sure mosquitto and mosquitto-clients are installed on gateway
## USAGE
# ./postMQTT.sh <client> <topic> <message>

## e.g. ./postMQTT.sh blah blah hello_world

CLIENT=$1
TOPIC=$2
MESSAGE=$3

HOST="172.24.1.1"
DATE=$(date '+%Y-%m-%d')
TIME=$(date '+%H:%M:%S')

JSON_MSG='{ "hostname": "'$CLIENT'", "topic": "'$TOPIC'", "date": "'$DATE'", "time": "'$TIME'", "iot_msg": "'$MESSAGE'" }'

## post message to topic
mosquitto_pub -h $HOST -t $TOPIC -m "$JSON_MSG"
