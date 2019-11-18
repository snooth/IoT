#!/bin/sh

## SnoothDogg 2019 -
# Monitors message ingress to Azure IOT HUB
# You have configure environment connection string in the consumeAndPostToAZ.py

AZHUB="<HUB_NAME>"
DEVICE="<DEVICE_NAME>"

az iot hub monitor-events --hub-name $AZHUB --device-id $DEVICE
