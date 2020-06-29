import os

# You can write up to 5GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

os.system("git clone https://github.com/ultralytics/yolov5")
os.system("mv yolov5/* ./")
os.system("pip install -r requirements.txt")