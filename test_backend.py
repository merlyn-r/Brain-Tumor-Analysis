import requests

try:
    print("Testing backend API...")
    response = requests.get('http://localhost:5000/api/health', timeout=5)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    print("✅ Backend is running and responding!")
except Exception as e:
    print(f"❌ Error: {e}")
    print("Backend may not be running properly.")