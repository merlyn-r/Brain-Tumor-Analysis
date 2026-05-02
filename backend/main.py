"""
Brain Tumor MRI Classification API
Flask backend server for prediction endpoints
"""

import os
import io
import base64
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from PIL import Image
import cv2
import model as tumor_model
import llm as ai_llm

app = Flask(__name__, static_folder='../frontend')
CORS(app)

# Ensure uploads directory exists
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """Serve the main dashboard page"""
    return send_from_directory('../frontend', 'index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    return send_from_directory('../frontend', filename)

@app.route('/api/predict', methods=['POST'])
def predict():
    """Handle image prediction request"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        
        # Save uploaded file
        filename = f"upload_{np.random.randint(10000)}.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # Get prediction
        result = tumor_model.predict_tumor(filepath)
        
        # Generate AI explanation (load LLM if needed)
        explanation = None
        ai_generated = False
        try:
            if not ai_llm.get_llm_status()['loaded']:
                ai_llm.load_llm_model()
            
            if ai_llm.get_llm_status()['loaded']:
                explanation = ai_llm.generate_diagnosis_explanation(
                    result['prediction'],
                    result['confidence'],
                    result['all_predictions']
                )
                ai_generated = True
            else:
                explanation = f"The AI analysis indicates a {result['prediction'].lower()} with {result['confidence']*100:.1f}% confidence. This is a preliminary assessment using deep learning technology."
        except Exception as e:
            print(f"Warning: Could not generate AI explanation: {e}")
            explanation = f"The analysis indicates a {result['prediction'].lower()} with {result['confidence']*100:.1f}% confidence. AI explanation unavailable."
        
        # Generate heatmap
        heatmap_path = os.path.join(UPLOAD_FOLDER, f"heatmap_{filename}")
        tumor_model.generate_gradcam_heatmap(filepath, heatmap_path)
        
        # Read heatmap as base64
        heatmap_b64 = None
        if os.path.exists(heatmap_path):
            with open(heatmap_path, 'rb') as f:
                heatmap_b64 = base64.b64encode(f.read()).decode('utf-8')
        
        # Clean up files
        if os.path.exists(filepath):
            os.remove(filepath)
        if os.path.exists(heatmap_path):
            os.remove(heatmap_path)
        
        response_data = {
            'success': True,
            'prediction': result['prediction'],
            'confidence': result['confidence'],
            'all_predictions': result['all_predictions'],
            'explanation': explanation,
            'ai_generated': ai_generated,
            'heatmap': heatmap_b64
        }
        
        print(f"API Response: prediction={result['prediction']}, confidence={result['confidence']:.3f}, ai_generated={ai_generated}, explanation_length={len(explanation) if explanation else 0}")
        
        return jsonify(response_data)
    
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/classes', methods=['GET'])
def get_classes():
    """Get available tumor classes"""
    return jsonify({
        'classes': tumor_model.CLASS_NAMES,
        'model': 'ResNet50 (Transfer Learning)',
        'dataset': 'Brain Tumor MRI Dataset'
    })

@app.route('/api/explain', methods=['POST'])
def explain_diagnosis():
    """Generate AI explanation for a diagnosis"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        prediction = data.get('prediction')
        confidence = data.get('confidence')
        all_predictions = data.get('all_predictions')

        if not all([prediction, confidence is not None, all_predictions]):
            return jsonify({'error': 'Missing required fields: prediction, confidence, all_predictions'}), 400

        # Load LLM if not already loaded
        if not ai_llm.get_llm_status()['loaded']:
            llm_loaded = ai_llm.load_llm_model()
            if not llm_loaded:
                return jsonify({
                    'success': True,
                    'explanation': f"The AI analysis indicates a {prediction.lower()} with {confidence*100:.1f}% confidence. This is a preliminary assessment using deep learning technology.",
                    'ai_generated': False,
                    'note': 'AI language model is not available'
                })

        explanation = ai_llm.generate_diagnosis_explanation(prediction, confidence, all_predictions)

        return jsonify({
            'success': True,
            'explanation': explanation,
            'ai_generated': True
        })

    except Exception as e:
        print(f"Error generating explanation: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/educate/<tumor_type>', methods=['GET'])
def get_tumor_education(tumor_type):
    """Get educational information about a tumor type"""
    try:
        if tumor_type not in tumor_model.CLASS_NAMES:
            return jsonify({'error': f'Unknown tumor type: {tumor_type}'}), 400

        # Load LLM if not already loaded
        if not ai_llm.get_llm_status()['loaded']:
            llm_loaded = ai_llm.load_llm_model()
            if not llm_loaded:
                return jsonify({
                    'success': True,
                    'tumor_type': tumor_type,
                    'information': f"{tumor_type} is a type of brain tumor that can be detected through MRI imaging. This classification is based on medical imaging analysis.",
                    'ai_generated': False,
                    'note': 'AI language model is not available'
                })

        info = ai_llm.get_tumor_info(tumor_type)

        return jsonify({
            'success': True,
            'tumor_type': tumor_type,
            'information': info,
            'ai_generated': True
        })

    except Exception as e:
        print(f"Error getting educational info: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/llm-status', methods=['GET'])
def get_llm_status():
    """Get the status of the LLM model"""
    status = ai_llm.get_llm_status()
    return jsonify(status)

if __name__ == '__main__':
    print("=" * 50)
    print("🧠 Brain Tumor MRI Diagnostic Dashboard")
    print("=" * 50)
    print("Loading trained model...")
    tumor_model.load_trained_model()
    print("\n✅ Model loaded successfully!")

    print("\n🚀 Starting server at http://localhost:5000")
    print("AI language model will be loaded on first use")
    print("=" * 50)
    app.run(debug=True, port=5000)
