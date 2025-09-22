from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/train4/weights/best.pt")

# Run on one image
results = model.predict(source="train_1/train1/images/000000004_cluttered_hallway.png", save=True)

# Run on all images in a folder
# results = model.predict(source="train_1/train1/images", save=True)

# Run on a video
# results = model.predict(source="test_video.mp4", save=True)

# Run on webcam (0 means default webcam)
# results = model.predict(source=0, show=True)
