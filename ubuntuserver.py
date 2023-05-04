from flask import Flask, jsonify, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Start a separate process to run stress_cpu.py
        subprocess.Popen(["python", "stress_cpu.py"])
        return jsonify({'message': 'Stressing CPU'})

    elif request.method == 'GET':
        # Get private IP address of the EC2 instance
        ip_address = socket.gethostbyname(socket.gethostname())
        return jsonify({'ip_address': ip_address})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
