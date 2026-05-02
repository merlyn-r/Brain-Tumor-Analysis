#!/usr/bin/env python3
"""
Test script for the prediction API
"""

import requests
import os

# Test the API
url = "http://localhost:5000/api/predict"
image_path = r"c:\Users\Lenovo\Desktop\SEAI\brain_dataset\Testing\glioma\Te-gl_1.jpg"

if os.path.exists(image_path):
    with open(image_path, 'rb') as f:
        files = {'image': f}
        response = requests.post(url, files=files)

    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print("Prediction:", result.get('prediction'))
        print("Confidence:", result.get('confidence'))
        print("AI Generated:", result.get('ai_generated'))
        print("Explanation preview:", result.get('explanation')[:200] + "..." if result.get('explanation') else "No explanation")
    else:
        print("Error:", response.text)
else:
    print(f"Image not found: {image_path}")