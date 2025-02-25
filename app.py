from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return "Server is running"

@app.route("/status")
def status():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
