# YOLO Object Detection – Experiment Log

**Project:** Real-Time Object Detection in Images and Video Using YOLO  
**Model:** YOLO26n  
**Framework:** Ultralytics  
**Language:** Python  
**Input:** Static images and live webcam feed

---

## Experiment 1: Static Image Detection

**Objective:** Test whether YOLO can identify multiple objects in a static image.

- Input: `images/test.jpg`
- Result: The model detected approximately 20 objects.
- Observations: Predictions included people, cars, motorcycles, buses, trucks and traffic lights.
- Evidence: `images/detection_result.jpg`

**My evaluation:**
- YOLO successfully processed the static test image and detected approximately 20 objects.
- It identified several different object categories, including people, cars, motorcycles, buses, trucks and traffic lights.
- This demonstrated that the pretrained model could detect multiple objects within a single image without requiring additional training.
- The experiment provided a baseline for testing the model with live webcam input.

---

## Experiment 2: Live Webcam Detection

**Objective:** Test object detection using a live webcam feed.

- Input: Webcam (`cv2.VideoCapture(0)`)
- Result: YOLO processed live frames and displayed bounding boxes, labels and confidence scores.

**My evaluation:**
- YOLO successfully identified a person and a cellphone. 
- It misclassified a pen as a toothbrush 
- It failed to identify eyeglasses.

- The model could recognise some everyday objects in a live webcam feed.
- Recognition was not equally reliable across all objects.
- Some objects were misclassified or not detected.
- This may be related to the model's pretrained COCO dataset, which has a fixed set of object categories. Eyeglasses and pens are not dedicated classes in the standard COCO 80-class dataset.

---

## Experiment 3: Object Recognition

**Objective:** Investigate whether YOLO correctly classifies different everyday objects.

| Actual object | Observed prediction | Result |
|---|---|---|
| Phone | Initially skateboard; later cell phone | Inconsistent |
| Pen | Toothbrush | Misclassification |
| Chair | Initially airplane; later chair | Inconsistent |
| Book | Initially donut and hot dog | Misclassification |

**My evaluation:**
- YOLO demonstrated that it could recognise several objects, but its predictions were not always accurate.
- Some objects were initially assigned incorrect labels before being recognised correctly.
- The model's predictions varied depending on how the objects appeared in the webcam feed.
- The results demonstrate limitations in the pretrained model's ability to distinguish visually similar or unfamiliar objects.


---

## Experiment 4: Confidence Threshold

**Objective:** Investigate how changing the confidence threshold affects predictions.

- Threshold 1: 0.25
- Threshold 2: 0.50
- Correct chair detections were observed at both thresholds.
- Incorrect predictions were also observed at the higher threshold.

**My evaluation:**
- The application successfully processed webcam frames continuously.
- Processing speed fluctuated during operation rather than remaining constant.
- The observed 21–30 FPS demonstrates that the lightweight YOLO26n model can support real-time object detection on your computer.
- Performance may vary depending on hardware capabilities, image complexity and processing workload.

---

## Experiment 5: Real-Time Performance

**Objective:** Measure the processing speed of the webcam detection system.

- Earlier FPS reading: 26.11
- Observed range: 21–30 FPS
- Highest observed FPS: 30

**My evaluation:**
- The application processed webcam frames continuously, achieving real-time performance. However, FPS fluctuated during operation.

---

## Experiment 6: Low-Light Detection

**Objective:** Investigate how reduced lighting affects object recognition.

- Test object: Chair
- Confidence threshold: 0.50
- Chair confidence observed: approximately 0.501–0.759
- Other predictions included TV and microwave.

**My evaluation:**
- YOLO continued recognising the chair under reduced lighting.
- Confidence varied across frames.
- Some false-positive detections remained.
- The model demonstrated some robustness to reduced lighting, although recognition was not perfect.

---

## Experiment 7: Partial Occlusion

**Objective:** Investigate whether YOLO can recognise an object when part of it is hidden.

- Test object: Chair
- Test condition: Approximately half of the chair was covered.
- Result: The chair was still detected.

**My evaluation:**
- YOLO was able to recognise the chair despite part of it being obscured.
- This suggests the model can use the visible features of an object to classify it.
- The experiment demonstrates some robustness to partial occlusion.
- However, only one object and one level of occlusion were tested, so further testing would be needed to establish how well the model handles more severe occlusion.

---

## Experiment 8: Distance Testing


**Objective:** Investigate how the distance between the camera and an object affects detection.

**Results:**
Test Subject: Chair
Approximate distance: about 0.5m and 2.0m from my laptop
Result: Chair was consistently identified
Confidence threshold: 0.5
Highest chair confidence: 0. for 0.5m and 0.6 for 2.0m
False positives included bench and airplane.

**My evaluation:**
- YOLO consistently recognised the chair at close range.
- Confidence reached 0.909, indicating a strong prediction.
- Some incorrect predictions were also produced.
- The results establish a baseline for comparison with greater distances.

---

