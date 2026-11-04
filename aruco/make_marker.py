
import cv2

dictionary = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)

toys = {0: "teddy", 1: "car"}

for marker_id, name in toys.items():
    # Generate marker with white border
    marker = cv2.aruco.generateImageMarker(
        dictionary, marker_id, 400
    )
    marker = cv2.copyMakeBorder(
        marker, 50, 50, 50, 50,
        cv2.BORDER_CONSTANT, value=255
    )

    cv2.imwrite(f"{name}_marker.png", marker)
    print(f"Created {name}_marker.png")

