Smart Attendance System based on Face Recognition Using Machine Learning.

This project is a Face Recognition & Attendance System that captures images from a webcam, recognizes faces using the K-Nearest Neighbors (KNN) algorithm, and marks attendance in a CSV file. The system uses OpenCV for face detection, scikit-learn for face recognition, and Python's datetime module to keep track of attendance timings.
Requirements:
-> Python 3.8 or higher
-> OpenCV
-> Scikit-Learn
-> Numpy
-> Pywin32

![image](https://github.com/user-attachments/assets/6daca6a0-654a-49b4-8f97-c60113bcff9f)


test.py:
This is the main script that implements the face detection and attendance marking functionality. It captures real-time video from the webcam, detects faces using the Haar Cascade classifier, and recognizes them using a pre-trained KNN model. Once a face is recognized, it marks the attendance with the name and timestamp and stores the data in a CSV file.

haarcascade_frontalface_default.xml:
This is a pre-trained Haar Cascade model provided by OpenCV. It is used for detecting faces in the video frames by finding patterns that match facial features such as eyes, nose, and mouth.

names.pkl:
This file contains serialized data with the names or labels of individuals corresponding to the face data. It is generated during the training phase when face data is collected and is used to map recognized faces to their respective names.

faces_data.pkl:
This file holds the serialized face data in a matrix format. Each row in the matrix represents a face, which is used to train the KNN classifier for face recognition. This file is crucial for the recognition process to correctly identify individuals.

background.png:
This image file is used as the background template for displaying the video feed and attendance status in the application. It provides a user interface for the system, showing the video feed and guiding the user to take attendance.

Attendance/ (Folder):
This folder is used to store all the attendance files generated by the system. Each attendance file is named as Attendance_<date>.csv and contains records with the names of recognized individuals and the time they were marked present.
