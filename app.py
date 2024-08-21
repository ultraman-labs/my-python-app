import os
import signal
from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)

# This function will trigger the app to terminate after 10 seconds
def force_failure():
    time.sleep(10)
    os.kill(os.getpid(), signal.SIGKILL)

# Start the failure thread
threading.Thread(target=force_failure).start()

@app.route('/', methods=['GET'])
def home():
    return jsonify({"msg": "BC4M"})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
