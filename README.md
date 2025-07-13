# Face Mask Detection with Social Distance Monitoring

A real‑time deep learning application that detects whether individuals are wearing face masks, with visual and audible alerts for violations. The system also detects people and estimates proximity for social distance visualization.

## Features
- Real‑time face detection and mask classification  
- Audible alert when a person is not wearing a mask  
- Colored bounding boxes (green = mask, red = no mask)  
- People detection with proximity cues for social distancing  
- Supports webcam and video file input  

## Technologies Used
- Python 3.x  
- OpenCV (DNN module)  
- TensorFlow / Keras (MobileNetV2)  
- Caffe SSD (face detector)  
- MobileNet SSD (person detector)  
- playsound  
