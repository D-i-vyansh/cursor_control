# 🖌️ Virtual Painter using Hand Gestures

## Overview

This is a Python-based virtual painting application that uses hand tracking with MediaPipe and OpenCV. You can draw on the screen by using your index finger and clear the canvas with a hand gesture—no mouse or touchscreen required!

---

## ✨ Features

- Draw using your **index finger** in the air
- **Clear the canvas** with an open palm gesture
- Real-time **hand tracking** using [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands)
- Smooth drawing using OpenCV
- Fun and intuitive way to interact with your computer

---

## 🛠️ Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy

---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/divyanshsinghal067/virtual-painter.git
cd virtual-painter

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt
