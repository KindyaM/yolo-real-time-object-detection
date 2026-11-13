import time
import cv2
from ultralytics import YOLO

# Load the pretrained YOLO model
model = YOLO("yolo26n.pt")

# Open the webcam
cap = cv2.VideoCapture(0)

# Check whether the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not access webcam.")
    exit()

print("Webcam started. Press Q to quit.")
prev_time = time.perf_counter()

try:
    while True:
        # Capture a frame from the webcam
        success, frame = cap.read()

        if not success:
            print("Could not read webcam frame.")
            break

        # Run YOLO object detection
        results = model.predict(frame, conf=0.5, verbose=False)
        for result in results:
            for box in result.boxes:
                print(
                model.names[int(box.cls[0])],
                round(float(box.conf[0]), 3)
        )

        # Draw bounding boxes and labels
        annotated_frame = results[0].plot()
        current_time = time.perf_counter()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        cv2.putText(
            annotated_frame,
            f"FPS: {fps:.2f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # Display the processed frame
        cv2.imshow("YOLO Real-Time Object Detection", annotated_frame)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    # Release webcam and close windows
    cap.release()
    cv2.destroyAllWindows()
