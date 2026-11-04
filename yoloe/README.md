# YOLOE Toy Detection

This prototype uses a pretrained YOLOE-26n model to recognize real objects through a Mac webcam, without printed markers or custom training.

## Files
- `detect_toys.py` — Runs webcam-based object detection.
- The pretrained model (`yoloe-26n-seg.pt`) is downloaded automatically and does not need to be uploaded.

## Setup and Run

Install dependencies:

```bash
pip install ultralytics opencv-python
```

Run:

```bash
python detect_toys.py
```

**Controls:** Press Q to close the webcam window.

Object categories can be changed in the `model.set_classes()` list.

## Next Steps

Explore integrating object recognition into Meta Quest 3 using Unity, the Passthrough Camera API, and Unity Inference Engine. Add interaction tracking to trigger audiovisual memories when visitors pick up toys.

**Code:** Generated using the [Ultralytics YOLOE documentation](https://docs.ultralytics.com/models/yoloe/) 

**Quest reference:** [Meta Passthrough Camera API Samples](https://github.com/oculus-samples/Unity-PassthroughCameraApiSamples).
