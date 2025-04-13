from flask import Flask, request, jsonify
from flask_cors import CORS
from deep_seek import generateAnswer

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

@app.route('/generate-answer', methods=['POST'])
def upload_image():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        prompt = data.get("prompt", "Unknown")

        generatedOutput = generateAnswer(prompt)

        return jsonify({"message": generatedOutput }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)
