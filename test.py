from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/train5/weights/best.pt")

# Use full absolute path (Windows style, raw string to avoid backslash issues)
image_path = r"C:\Users\bhavana reddy\Downloads\hackathon2_train_1\train_1\train1\images\000000022_cluttered_hallway.png"
import os
print(os.path.exists(image_path))  # should print True if the file is found

# Run prediction
results = model.predict(source=image_path, save=True)

print(results)
