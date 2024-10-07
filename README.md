Smart Attendance System based on Face Recognition Using Machine Learning.

This project is a Face Recognition & Attendance System that captures images from a webcam, recognizes faces using the K-Nearest Neighbors (KNN) algorithm, and marks attendance in a CSV file. The system uses OpenCV for face detection, scikit-learn for face recognition, and Python's datetime module to keep track of attendance timings.
Requirements:
-> Python 3.8 or higher
-> OpenCV
-> Scikit-Learn
-> Numpy
-> Pywin32


Folder Structure:
The project folder should be structured as follows:

Attendance-System

-> haarcascade_frontalface_default.xml         # Pre-trained Haar Cascade model for face detection
-> test.py                                     # Main script for face detection and attendance
-> names.pkl                                   # Serialized file containing the names/labels of recognized individuals
-> faces_data.pkl                               # Serialized file containing the face data
-> Attendance/                                  # Folder where attendance files will be saved
-> background.png                               # UI background image for the attendance system
-> README.md                                    # Project documentation
