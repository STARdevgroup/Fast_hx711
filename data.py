import os
import time
import ujson

def get_log():
    with open("get_log.json","r") as f:
        data = f.read()
        f.close()
    data = ujson.loads(data)
    log = data["log"]
    data["log"] = data["log"] + 1
    with open("get_log.json","w") as f:
        f.write(ujson.dumps(data))
        f.close()
    return log

def log_usb(data,path='log.csv'):
    with open(path, 'a') as f:
        f.write(f"{time.ticks_ms()},{data}\n")
    f.close()