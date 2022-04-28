import socket
from datetime import datetime
import json

socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_conn.settimeout(10)
try:
    socket_conn.connect(("", 1024))
    is_connected = True
except socket.error as e:
    print("VDT RLVD: Socket Error %s", e)

request = {
    "request-time":datetime.now().strftime("!%Y-%m-%d %H:%M:%S UTC"),
    "auth-request":{
        "credentials":[username,password ]
    }
}
request = json.dumps(request) + "\n"
try:
    socket_conn.send(str.encode(request))
    print('VDT RLVD: Data sent to %s', request)
    data = json.loads(socket_conn.recv(1024).decode())
    print('VDT RLVD: Data recv is %s', data)
    if data["auth-response"] == "SUCCESS":
        is_connected = True
    else:
        is_connected = False
except Exception as ex:
    print('VDT RLVD: %s',ex)

if is_connected:
    request = {}
    request = {'Command': 'GET LAMPS STATUS', 'LampStatus': '1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0'}

    request = json.dumps(request) + "\n"
    try:
        print('VDT RLVD: Data sent to %s', request)
        socket_conn.send(str.encode(request))
    except Exception as ex:
        print.error('VDT RLVD: %s',ex)