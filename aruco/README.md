# ArUco Marker Detection

This experiment uses OpenCV and a Mac webcam to recognize physical toys through printed ArUco markers.

### Files
- `make_marker.py` — Generates unique markers for each toy.
- `detect_toy.py` — Detects markers in real time using the webcam.
- `teddy_marker.png` — Marker ID 0, teddy bear.
- `car_marker.png` — Marker ID 1, toy car.

### How to Run
Install the required library:

```bash
pip install opencv-contrib-python
```

Generate the markers:

```bash
python make_marker.py
```

Run webcam detection:

```bash
python detect_toy.py
```

Press **Q** to close the webcam window.

### Results
Successfully detected two physical toys using individual ArUco markers. However, detection becomes less reliable when markers are small or far from the camera.

### References
- [OpenCV ArUco Documentation](https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html)
- Code generated using OpenCV's documented functions 
