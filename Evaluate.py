from ultralytics import YOLO

# Load your trained model
model = YOLO("runs/detect/train4/weights/best.pt")

# Evaluate on validation set
metrics = model.val(data="data.yaml")

print("Precision:", metrics.box.map)      # mAP@0.5
print("mAP50:", metrics.box.map50)        # mAP@50
print("mAP50-95:", metrics.box.map75)     # mAP@50-95
