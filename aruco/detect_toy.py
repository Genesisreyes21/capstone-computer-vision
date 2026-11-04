
import cv2

# Markers and toy names
toys = {0: "TEDDY BEAR", 1: "TOY CAR"}

dictionary = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)

parameters = cv2.aruco.DetectorParameters()

# Allow smaller markers to be detected
parameters.minMarkerPerimeterRate = 0.01
parameters.adaptiveThreshWinSizeMin = 3
parameters.adaptiveThreshWinSizeMax = 35
parameters.adaptiveThreshWinSizeStep = 4
parameters.cornerRefinementMethod = cv2.aruco.CORNER_REFINE_SUBPIX

detector = cv2.aruco.ArucoDetector(
    dictionary, parameters
)

# Keep your previously working camera index
camera = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

# Request higher resolution
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

print("Press Q to quit")

while True:
    success, frame = camera.read()
    if not success:
        break

    corners, ids, _ = detector.detectMarkers(frame)

    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        for marker_id, points in zip(ids.flatten(), corners):
            name = toys.get(int(marker_id), "UNKNOWN")

            # Display label near each marker
            x, y = points[0][0].astype(int)
            cv2.putText(
                frame, name, (x, max(25, y - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2
            )

    cv2.imshow("Small Toy Marker Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
