import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

print("Camera opened successfully")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Could not read frame")
        break

    cv2.imshow(
        "Live Camera",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()