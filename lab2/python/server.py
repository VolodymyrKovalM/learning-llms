from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime
from nlpconnect import predict_step
from salesforce import generateCaption

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

models = {
    'nlpconnect': predict_step,
    'salesforce': generateCaption
}

def generateCaption(model_name):
    models = {
        'nlpconnect': predict_step,
        'salesforce': generateCaption
    }

    return models[model_name]

@app.route('/upload', methods=['POST'])
def upload_image():
    print(request.files)
    if 'model' not in request.form:
        return jsonify({'error': 'There is not model name in request payload'}), 400

    if 'image' not in request.files:
        return jsonify({'error': 'There is not image in request payload'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name_with_timestamp = f"{timestamp}_{file.filename}"

    file_path = os.path.join(UPLOAD_FOLDER, file_name_with_timestamp)
    file.save(file_path)

    model_name = request.form.get('model', 'nlpconnect')

    generatedCaption = models[model_name](file_path)
    
    return jsonify({
        'message': 'Image uploaded successfully',
        'filePath': file_path,
        'generatedCaption': generatedCaption
    }), 200

if __name__ == '__main__':
    app.run(port=8000, debug=True)
