from ultralytics import YOLO
model = YOLO("yolo26n.pt")
print("YOLO model loaded successfully!")

results = model("images/test.jpg")


for result in results:
    print(result.boxes)