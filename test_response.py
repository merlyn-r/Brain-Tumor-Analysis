#!/usr/bin/env python3
import requests

url = 'http://localhost:5000/api/predict'
with open(r'c:\Users\Lenovo\Desktop\SEAI\brain_dataset\Testing\glioma\Te-gl_1.jpg', 'rb') as f:
    files = {'image': f}
    response = requests.post(url, files=files)

print('Status:', response.status_code)
if response.status_code == 200:
    data = response.json()
    print('Response keys:', list(data.keys()))
    print('AI Generated:', data.get('ai_generated'))
    print('Has explanation:', bool(data.get('explanation')))
    print('Explanation preview:', data.get('explanation')[:100] if data.get('explanation') else 'None')
else:
    print('Error response:', response.text)