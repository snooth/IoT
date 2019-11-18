#!/usr/bin/python3

## SnoothDogg 2019 - Satoshi Nakamoto
# Verion 1.5
# Option 1 - subscribes to mosquitto broker and sends each json message to az iot hub
# Option 2 - reads last line of iot_messages file and send json message to az iot hub

import random
import time
import paho.mqtt.client as mqtt
import subprocess
import sys
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=TelstraIoT.azure-devices.net;DeviceId=SDN-GW-10;SharedAccessKey=x2h9GUun0Drr8VqlDvTPtD3lbJAZ4HrpQUUxhbTvT9U="

# Create an client instance of AZ
def iothub_client_init():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

# Subscribes to mosquitto broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("snooth_iot")

# Grabs json message and prints to screen
def on_message(client, userdata, msg):
    print(msg.payload.decode())

# Try sending message back to AZ IOT HUB
def send_message_to_az_hub():

    try:
        client = iothub_client_init()
        clientM = mqtt.Client()

        while True:

            # reads in last json message message in file and stores in event
            event = subprocess.check_output(['tail', '-1', "/root/iot_messages"])
            clientM.connect("172.24.1.1",1883,60)

            clientM.on_connect = on_connect
            clientM.on_message = on_message

            client.send_message(event)

            # debug showing what is parsed in console
            print( "Sending message: {}".format(event) )
            #client.loop_forever()
            # loop ever 1 sec
            time.sleep(1)


    except KeyboardInterrupt:
        print ( "Data feed stopped" )

if __name__ == '__main__':
    print ( "Press Ctrl-C to exit" )
    send_message_to_az_hub()
