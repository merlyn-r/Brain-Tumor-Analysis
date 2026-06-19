🧠 Brain Tumor MRI Prediction using Deep Learning

📌 Project Overview
Brain Tumor MRI Prediction is an AI-based medical image classification system that detects and classifies brain tumors from MRI scans. The project uses deep learning and transfer learning techniques to assist in faster and more accurate tumor identification.

The model is built using a pretrained ResNet50 architecture and trained on MRI image datasets to classify different brain tumor categories. A Flask-based web application interface allows users to upload MRI images and receive real-time predictions.



✨ Features
- MRI image classification using deep learning
- Transfer Learning with ResNet50
- Automated image preprocessing
- Real-time tumor prediction
- User-friendly web interface
- High accuracy image classification



🛠️ Tech Stack

AI Tools
- Google Colab
- Kaggle
- Jupyter Notebook

Machine Learning / Deep Learning
- TensorFlow
- Keras
- ResNet50 (Transfer Learning)

Computer Vision
- OpenCV
- Image Processing Techniques

Backend
- Python
- Flask

Libraries
- NumPy
- Pandas
- Matplotlib


🧠 Model Architecture

MRI Image  
↓  
Image Preprocessing  
↓  
ResNet50 Pretrained Model  
↓  
Feature Extraction  
↓  
Fully Connected Layers  
↓  
Classification Output  



📂 Dataset
Dataset used:
- Brain Tumor MRI Dataset from Kaggle

Classes:
- Glioma Tumor
- Meningioma Tumor
- Pituitary Tumor
- No Tumor



⚙️ Workflow

1. Data collection from Kaggle
2. Image preprocessing and resizing
3. Data augmentation
4. Transfer learning using ResNet50
5. Model training and validation
6. Performance evaluation
7. Flask web application integration
8. MRI image upload and prediction



Installation and Usage-

Install Dependencies:
pip install -r requirements.txt

Run the application:
python app.py

Open Browser:
http://localhost:5000/

📊 Results:
Successfully classified MRI scans into multiple tumor categories
Improved performance using transfer learning
Reduced training time with pretrained ResNet50 model

🔮 Future Enhancements:
Deploy application on cloud platforms
Add explainable AI visualization
Improve model accuracy with larger datasets
Integrate Grad-CAM for tumor region visualization



👩‍💻 Author

Merlyn R
CSE - Artificial Intelligence & Machine Learning
SRM Institute of Science and Technology

⭐ If you find this project useful, consider giving it a star!
