Pedestrian Detection is a computer vision technique used to identify and locate pedestrians in an image or video. It detects each pedestrian by drawing a bounding box around the person. This technology is widely used in intelligent transportation systems, autonomous vehicles, surveillance systems, and public safety applications.
In this project, the YOLOv8 (You Only Look Once Version 8) model is used for pedestrian detection. YOLOv8 is a state-of-the-art object detection model capable of detecting multiple objects in a single image. Since the objective is pedestrian detection, the program filters the detection results and displays only the "person" class while ignoring other detected objects such as cars, buses, bicycles, and animals.
YOLOv8 performs detection in a single pass, making it fast, accurate, and suitable for real-time pedestrian detection applications.

Software Requirements
- Google Colab
- Python 3.x
- Ultralytics YOLOv8
- OpenCV
- NumPy
- Pillow (PIL)
- Image containing one or more pedestrians

Procedure (Step-by-Step)

Step 1:
Open Google Colab.

Step 2:
Install the required libraries such as Ultralytics, OpenCV, and Pillow.

Step 3:
Import the required Python libraries.

Step 4:
Load the pre-trained YOLOv8 model.

Step 5:
Upload an image containing pedestrians.

Step 6:
Read the uploaded image and convert it into OpenCV format.

Step 7:
Apply the YOLOv8 model to detect objects.

Step 8:
Filter only the Person class from all detected objects.

Step 9:
Draw green bounding boxes around the detected pedestrians.

Step 10:
Display the final output image.

Example

Input Image

Original image containing pedestrians

<img width="616" height="411" alt="image" src="https://github.com/user-attachments/assets/c0c5e0ea-6905-497e-9fae-41f0e43bc91a" />

Output Image

Image with detected pedestrians highlighted using bounding boxes

<img width="667" height="445" alt="image" src="https://github.com/user-attachments/assets/8f89be78-a116-4ad4-9f39-4400d81c745b" />

Result

The YOLOv8 model successfully detects pedestrians in the input image and highlights each detected person with a bounding box.



