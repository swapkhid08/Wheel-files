import json
from configparser import ConfigParser
from queue import Empty, Queue
from threading import Thread
import socket
import time
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
try:
    sock.connect((self.host, int(self.port)))
except socket.error as e:
    print("Socket Commuincator: Socket Error %s", e)

   
request = {
    "request-time":datetime.now().strftime("!%Y-%m-%d %H:%M:%S UTC"),
    "auth-request":{
        "credentials":[self.username,self.password ]
    },
    "data-request":{
        "data-types":["line-crossing", "v-loop"]
    }
}
request = json.dumps(request)
try:
    sock.send(str.encode(request))
    print('VDT: Data sent to %s', request)
    data = json.loads(sock.recv(1024).decode())
    print('VDT: Data recv is %s', data)
    if data["auth-response"] == "SUCCESS":
         while True:
            try:
                data = the_socket.recv(2048)
                #self.__logger.debug("data is %s",data)
                if data:
                    data = data.decode("utf-8")
                    break
                else:
                    time.sleep(0.1)
            except socket.timeout:
                continue

            if data:
                # join all parts to make final string
                string = data.strip()
                print(string)
