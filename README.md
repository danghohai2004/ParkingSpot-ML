# ParkingSpot-ML

**ParkingSpot-ML** is a project that uses **Machine Learning** and **Computer Vision** to detect and classify parking spaces in video streams.  
The goal is to support more efficient parking management by determining the status of each parking space: **vacant** or **occupied**.

---

## Project Overview

- **Model used**: SVC (Support Vector Classifier)
- **Input**: Video footage from surveillance cameras
- **Output**: Location of parking spaces and their status (empty/occupied)

---

## Goals

- Real-time parking slot detection and classification
- Display the number of available and occupied parking spots
- Easy integration with existing monitoring systems

---

## Dataset

- The full dataset includes:
  - Raw video of a parking lot
  - Region-of-interest (mask) image
  - Labeled image dataset of `empty` and `not_empty` parking slots

**Note**: Due to GitHub's file size limitations, the raw video file `parking_1920_1080_loop.mp4` is hosted externally.

1. Download: [Click here to download from Google Drive](https://drive.google.com/drive/folders/1jovc7oBMFV1DutrijBFDbEMIO7fWwh5o)

2. Setup: Place the downloaded file into the dataset/ folder before running the scripts.

**Please refer to the original dataset provider's terms of use for licensing and attribution.**

---

## Video Demo

![Example Prediction](demo/video_pre.gif)

---

## File Structure
- [dataset](./dataset)
  - [not_empty](./dataset/not_empty)
  - [empty](./dataset/empty)
- [detection_parking_ID](./detection_parking_ID) 
  - [parking_spot_ids](./detection_parking_ID/parking_spot_ids.py)
- [processing](./processing) 
  - [cropped_spots_images](./processing/cropped_spots_images.py)
- [demo](./demo)  
  - [video_pre.gif](./demo/video_pre.gif)
- [main.py](./main.py)  
- [train](./train.py)  
- [model.pkl](./model.pkl)
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

- 📧 **Email** — [contact me](mailto:dhhaics2004@gmail.com?subject=Question%20about%20ParkingSpot-ML%20project)
- 🌐 **GitHub** — [@danghohai2004](https://github.com/danghohai2004)

---

# Thank you for your interest in this project!