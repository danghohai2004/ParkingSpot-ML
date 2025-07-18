# 🅿️ ParkingSpot-ML
ParkingSpot-ML is a project that uses Machine Learning and Computer Vision to detect and classify parking spaces in videos. The goal is to support more efficient parking management by determining the status of each parking space: vacant or occupied.

## 🚀 Project Overview
- Model used: SVC (Support Vector Machine)
- Input: Video from surveillance cameras.
- Output: Location of parking spaces and their status (empty/occupied).

## 🎯 Goals
- Real-time parking status detection and classification.
- Provides information on the number of vacant and occupied parking spaces.
- Supports integration with existing monitoring systems.

---

## 🧠 Dataset
**The dataset used in this project is sourced from** [ParkingLotDetectorAndCounter]([https://drive.google.com/drive/folders/1CjEFWihRqTLNUnYRwHXxGAVwSXF2k8QC).  
**Please refer to their terms of use for dataset licensing and usage.**

---

## ⏱️ Video Demo

![Example Prediction](demo/video_pre.gif)

---

## 📂 File Structure
- [Data](./data)
- [Detection Parking ID](./detection_parking_ID/parking_slots_ID.py) 
- [Processing](./processing/drop_cars_images.py) 
- [Model Training](./train.py)  
- [model.pkl](./model.pkl)  
- [main.py](./main.py)  
- [Demo](./demo)  
  - [video_pre.gif](./demo/video_pre.gif)
- [requirements.txt](./requirements.txt)
- [README.md](./README.md)

---

## 🔧 Installation & Setup
### Clone the Repository
    git clone https://github.com/danghohai2004/ParkingSpot-ML.git
    cd ParkingSpot-ML
### Install Dependencies (Python 3.9.12)
    pip install -r requirements.txt
### Run Real-Time Detection
    python main.py

---

## 📜 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

---

## 📬 Contact

- 📧 **Email** — [contact me](mailto:dhhaics2004@gmail.com?subject=Question%20about%20the%20Face%20Mask%20Detection%20Project)
- 🌐 **GitHub** — [@danghohai2004](https://github.com/danghohai2004)

---

# Thank you for your interest in this project!