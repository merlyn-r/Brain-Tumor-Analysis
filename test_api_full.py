import requests
import os

# Test with a sample image
image_path = r'C:\Users\Lenovo\Desktop\SEAI\brain_dataset\Testing\glioma\Te-gl_1.jpg'

if os.path.exists(image_path):
    print('Found test image, testing API...')
    with open(image_path, 'rb') as f:
        files = {'image': f}
        try:
            response = requests.post('http://localhost:5000/api/predict', files=files, timeout=30)
            print(f'Status: {response.status_code}')
            if response.status_code == 200:
                data = response.json()
                print('✅ API working! Prediction:', data.get('prediction', 'N/A'))
                print('Confidence:', data.get('confidence', 'N/A'))
                print('Has explanation:', 'explanation' in data)
                if 'explanation' in data:
                    print('Explanation length:', len(data['explanation']))
            else:
                print('❌ API error:', response.text)
        except Exception as e:
            print(f'❌ Request failed: {e}')
else:
    print('❌ Test image not found at:', image_path)