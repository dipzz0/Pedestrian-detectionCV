# Install Library
!pip install ultralytics opencv-python-headless pillow -q

# Import Libraries
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
from google.colab import files
from google.colab.patches import cv2_imshow

# Load YOLO Model
model = YOLO("yolov8n.pt")

# Upload Image
uploaded = files.upload()

# Image Name
image_name = list(uploaded.keys())[0]

# Read Image using PIL
image = Image.open(image_name).convert("RGB")

# Convert PIL to OpenCV
img = np.array(image)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Detect Objects
results = model(img)

# Draw Only Person Boxes
for box in results[0].boxes:

    if int(box.cls[0]) == 0:

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(img, "Person", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0,255,0), 2)

# Show Output
cv2_imshow(img)
