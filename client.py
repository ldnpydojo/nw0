import networkzero
import time
import json


def get_key(key):
    return networkzero.send_message_to(server, json.dumps({
        "cmd": "GET",
        "key": key
    }))


def set_key(key, value):
    return networkzero.send_message_to(server, json.dumps({
        "cmd": "SET",
        "key": key,
        "data": value
    }))


server = networkzero.discover("foo")

print(set_key("foo", "bar"))
print(get_key("foo"))
