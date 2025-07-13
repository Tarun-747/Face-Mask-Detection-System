import os
import urllib.request

# Create directory if it doesn't exist
os.makedirs("face_detector", exist_ok=True)

# URLs of the model files
prototxt_url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt"
caffemodel_url = "https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel"

# Destination paths
prototxt_path = os.path.join("face_detector", "deploy.prototxt")
caffemodel_path = os.path.join("face_detector", "res10_300x300_ssd_iter_140000.caffemodel")

# Download files
print("[INFO] Downloading deploy.prototxt...")
urllib.request.urlretrieve(prototxt_url, prototxt_path)
print("[INFO] deploy.prototxt downloaded successfully.")

print("[INFO] Downloading res10_300x300_ssd_iter_140000.caffemodel...")
urllib.request.urlretrieve(caffemodel_url, caffemodel_path)
print("[INFO] caffemodel downloaded successfully.")
