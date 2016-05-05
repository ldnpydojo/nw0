import json
import traceback

import networkzero

address = networkzero.advertise("foo")

STORE = {}


def my_func(input_data):
    try:
        command = json.loads(input_data)
        if command["cmd"] == "SET":
            STORE[command["key"]] = command["data"]
            response = {"status": "ok"}
        elif command["cmd"] == "GET":
            response = {
                "status": "ok",
                "info": STORE[command["key"]]
            }
        else:
            raise NotImplementedError(command)
    except:
        response = {
            "status": "error",
            "info": traceback.format_exc()
        }
    return json.dumps(response)


while True:
    input_data = networkzero.wait_for_message_from(address)
    print(input_data)
    networkzero.send_reply_to(address, my_func(input_data))
