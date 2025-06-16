# -YZU Smart Trash Bin Detection System

This project is developed as the final assignment for the course **Introduction to Computer Vision and Image Processing (EEB215A)** at Yuan Ze University.

## 📌 Project Objective
To build a Haar Cascade-based object detection system to identify **trash bins** on the YZU campus, using a self-collected dataset and real-time webcam detection.

## 🖼️ Dataset Collection and Annotation
- Collected over 300 images of trash bins using a smartphone across various YZU campus locations.
- Used OpenCV annotation tools to label the positive samples.
- Gathered 200+ negative images with no trash bins for background training.

## 🧠 Haar Cascade Training

**Command to create positive sample vector (.vec):**
```bash
opencv_createsamples -info positive/info.lst -num 500 -w 20 -h 20 -vec positive.vec
```

**Command to train classifier:**
```bash
opencv_traincascade -data classifier -vec positive.vec -bg negative.txt -numPos 450 -numNeg 200 -numStages 10 -w 20 -h 20 -featureType LBP
```

## 👁️ Real-Time Detection

**Run the detection script:**
```bash
python detect_trash_bin.py
```

The webcam will open, and detected trash bins will be highlighted with green rectangles.

## 🗂️ Project Structure

```
project/
├── positive/             # Positive sample images and info.lst
├── negative/             # Negative sample images and negative.txt
├── classifier/           # Trained Haar classifier (contains cascade.xml)
├── detect_trash_bin.py   # Real-time detection script
└── README.md             # This file
```

## 🔗 Demo and Code Access

- 🎥 [Demo Video](https://drive.google.com/file/d/1exampleTrashBinDemoVideo)
- 💻 [GitHub Repository](https://github.com/yowuyu/yzu-trash-bin-detection)

## ⚙️ Environment Requirements

- Python 3.10+
- OpenCV 4.5+

Install dependencies:
```bash
pip install opencv-python
```

## 📚 References

- [OpenCV Haar Cascade Docs](https://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html)
- [OpenCV Train Cascade Guide](https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html)
