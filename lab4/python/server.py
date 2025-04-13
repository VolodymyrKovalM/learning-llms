from flask import Flask, request, jsonify
from flask_cors import CORS
from llama import generate_output

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

@app.route('/generate-answer', methods=['POST'])
def generate_answer():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400
        
        prompt = data.get("prompt", "Unknown")
        max_tokens = data.get("maxTokens", 2000)
        temperature = data.get("temperature", 0.75)
        top_p = data.get("topP", 1)
        
        generatedOutput = generate_output(prompt=prompt, max_tokens=max_tokens, temperature=temperature, top_p=top_p);

        return jsonify({"generatedOutput": generatedOutput }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)
