from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        data = request.json # Assuming the client sends JSON data
        if 'first' in data and 'second' in data
            x = data['first']
            y = data['second']
            result = x + y
            return jsonify({"result": result})
        else:
            return jsonify({"error": "Invalid input data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        data = request.json  # Assuming the client sends JSON data
        if 'first' in data and 'second' in data:
            x = data['first']
            y = data['second']
            result = x - y
            return jsonify({"result": result})
        else:
            return jsonify({"error": "Invalid input data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
