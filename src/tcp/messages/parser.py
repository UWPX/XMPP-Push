import json
from tcp.messages.SetChannelUriMessage import SetChannelUriMessage
from tcp.messages.SetPushAccountsMessage import SetPushAccountsMessage
from tcp.messages.RequestTestPushMessage import RequestTestPushMessage
from typing import Any
from traceback import print_exc
from sys import stdout

def parseJson(jsonObj: Any):
    action: str = jsonObj["action"]

    if action == SetChannelUriMessage.ACTION:
        return SetChannelUriMessage(jsonObj)
    elif action == SetPushAccountsMessage.ACTION:
        return SetPushAccountsMessage(jsonObj)
    elif action == RequestTestPushMessage.ACTION:
        return RequestTestPushMessage(jsonObj)

    print("Unknown message received: {}".format(jsonObj))
    return None

def parseJsonSave(jsonObj: Any):
    try:
        return parseJson(jsonObj)
    except Exception as e:
        print("Failed to parse message: '{}' - {}".format(jsonObj, e))
        print_exc(file=stdout)
        return None

def parse(msg: str):
    jsonObj: Any = None
    try:
        jsonObj = json.loads(msg)
    except ValueError as e:
        print("Failed to parse received message '{}' as JSON: {}".format(msg, e))
        return None
    return parseJsonSave(jsonObj)