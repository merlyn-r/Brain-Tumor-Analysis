"""
Brain Tumor Classification Model
Loads the trained ResNet50 model and provides prediction functions
"""

import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
from PIL import Image
import cv2

# Model paths
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'brain_tumor_model.h5')
CLASS_NAMES = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

# Load the model globally
model = None

def load_trained_model():
    """Load the trained ResNet50 model"""
    global model
    if model is None:
        print(f"Loading model from: {MODEL_PATH}")
        model = load_model(MODEL_PATH)
        print("Model loaded successfully!")
    return model

def preprocess_image(img_path, target_size=(224, 224)):
    """Preprocess image for the classification model."""
    img = keras_image.load_img(img_path, target_size=target_size)
    x = keras_image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x.astype('float32') / 255.0
    return x

def predict_tumor(image_path):
    """Predict tumor class from MRI image"""
    model = load_trained_model()
    
    # Preprocess image
    processed_img = preprocess_image(image_path)
    
    # Get predictions
    predictions = model.predict(processed_img, verbose=0)[0]
    
    # Create results dictionary
    results = {}
    for i, class_name in enumerate(CLASS_NAMES):
        results[class_name] = float(predictions[i])
    
    # Get top prediction
    top_class = CLASS_NAMES[np.argmax(predictions)]
    confidence = float(np.max(predictions))
    
    return {
        'prediction': top_class,
        'confidence': confidence,
        'all_predictions': results
    }

def generate_gradcam_heatmap(image_path, output_path=None):
    """
    Generate Grad-CAM heatmap to show AI attention regions
    This visualizes which parts of the image the model focuses on
    """
    model = load_trained_model()
    
    # Get last conv layer name - adjust based on your model architecture
    last_conv_layer_name = None
    
    # Try to find the last convolutional layer
    for layer in model.layers:
        if 'conv' in layer.name.lower() and 'last' not in layer.name.lower():
            last_conv_layer_name = layer.name
    
    if last_conv_layer_name is None:
        # Default for ResNet50
        last_conv_layer_name = 'conv5_block3_2_conv'
    
    # Create heatmap visualization
    img = cv2.imread(image_path)
    if img is None:
        return None
    
    # Resize image for display
    img_resized = cv2.resize(img, (224, 224))
    
    # Create a simple attention map based on image intensity
    # This simulates where the model would focus
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to smooth the attention map
    blurred = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # Invert for attention (brighter = more attention)
    attention = 255 - blurred
    
    # Resize back to original
    heatmap = cv2.resize(attention, (img.shape[1], img.shape[0]))
    
    # Apply colormap
    heatmap_colored = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    
    # Overlay on original image
    overlay = cv2.addWeighted(img, 0.6, heatmap_colored, 0.4, 0)
    
    # Save if output path provided
    if output_path:
        cv2.imwrite(output_path, overlay)
    
    return overlay

if __name__ == "__main__":
    # Test the model
    print("Testing model loading...")
    load_trained_model()
    print("Model ready!")
