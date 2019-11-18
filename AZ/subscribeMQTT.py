#!/usr/bin/env python3

## SnoothDogg 2019 -
# Mosquitto MQTT Broker
# Subscribes to a Mosquitto broker and prints json messages to console 
# Uses Paho.Mqtt.client implementation

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("snooth_iot")

def on_message(client, userdata, msg):
  print(msg.payload.decode())
  #return (msg.payload.decode())
  #client.disconnect()

client = mqtt.Client()
client.connect("172.24.1.1",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
