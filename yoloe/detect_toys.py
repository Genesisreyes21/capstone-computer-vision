#to detect toys in real time using webcam and YOLOE model
import cv2
from ultralytics import YOLOE

# Load pretrained model
model = YOLOE("yoloe-26n-seg.pt")

# Objects to recognize
model.set_classes([
    "teddy bear",
    "toy car",
    "doll",
    "toy train",
    "action figure",
    "building blocks",
    "storybook",
    "pencil",
    "backpack",
    "pillow",
    "lamp",
    "television",
    "video game controller",
    "phone",
    "cup",
    "person",
    "hand",
    "cat",
    "dog"
])

# Open Mac webcam
camera = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not camera.isOpened():
    raise RuntimeError("Camera not available")

print("Webcam running! Press Q to quit.")

while True:
    success, frame = camera.read()
    if not success:
        break

    # Detect objects
    results = model.predict(
        frame, conf=0.25, verbose=False
    )

    # Show detections
    cv2.imshow("YOLOE Toy Tracking", results[0].plot())

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

