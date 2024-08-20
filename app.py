from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Variable to control health check failure
failure_mode = False

@app.route('/', methods=['GET'])
def home():
    return jsonify({"msg": "BC4M"})

@app.route('/health', methods=['GET'])
def health_check():
    if failure_mode:
        os._exit(1)  # Forcefully exit the process with an error status
    else:
        return jsonify({"status": "healthy"})

@app.route('/toggle-failure', methods=['GET'])
def toggle_failure():
    global failure_mode
    failure_mode = not failure_mode
    return f"Failure mode is now {'on' if failure_mode else 'off'}", 200

@app.route('/', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



