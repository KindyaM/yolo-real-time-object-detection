
from ultralytics import YOLO


model = YOLO("yolo26n.pt")


results = model("images/test.jpg")


for result in results:
    
    print(f"Detected {len(result.boxes)} objects")

    
    result.save(filename="images/detection_result.jpg")

print("Detection image saved successfully!")
