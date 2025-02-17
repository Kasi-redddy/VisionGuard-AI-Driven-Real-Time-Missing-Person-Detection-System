# VisionGuard-AI-Driven-Real-Time-Missing-Person-Detection-System
An AI-based real-time missing person detection system using facial recognition. It highlights identified persons with a red circle and others with a green circle, ensuring quick and efficient recognition. No database is required, making it lightweight and easy to deploy. 
Real-Time Missing Person Detection using AI

Description
This project is an AI-based real-time missing person detection system using facial recognition. It compares real-time camera feed with stored images of missing persons. If a match is found, the system highlights the person with a red circle, otherwise, a green circle is used. The project is designed for fast and efficient recognition without requiring a database, making it lightweight and easy to deploy.

Features
✅ Real-time facial recognition using OpenCV and Deep Learning
✅ Highlights detected persons (Red for missing, Green for normal)
✅ No database required, making it simple and lightweight
✅ User-friendly interface for seamless interaction
✅ Deployable on any system with a webcam

Technologies Used
Python 🐍
OpenCV (Computer Vision)
Deep Learning (Face Recognition)
Flask (For Web Interface)
HTML, CSS (For Frontend)

Installation Steps
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/missing-person-detection.git
cd missing-person-detection
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Application
bash
Copy
Edit
python app.py
4. Open in Browser
Go to http://127.0.0.1:5000/ to access the system.


How It Works
1️⃣ Upload or store images of missing persons in the designated folder.
2️⃣ The camera feed will compare every face detected with the stored images.
3️⃣ If a match is found, a red circle will be drawn around the face.
4️⃣ If no match is found, a green circle will be drawn around the face.
5️⃣ The system can run continuously to identify missing persons in real-time.


Deployment Strategies
🔹 Local Deployment: Run directly on your computer with Python and OpenCV.
🔹 Cloud Deployment: Use platforms like Google Colab, AWS, or Azure to deploy online.
🔹 Web Hosting: Host with Flask & Gunicorn for a web-based interface.
🔹 Edge Devices: Deploy on Raspberry Pi for portable and offline detection.

Contributing
Pull requests are welcome! If you’d like to contribute, follow these steps:

Fork this repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Added new feature").
Push to the branch (git push origin feature-branch).



