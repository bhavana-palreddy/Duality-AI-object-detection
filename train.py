from ultralytics import YOLO

model = YOLO("runs/detect/train4/weights/last.pt")  # replace train4 with your folder

model.train(
    data="data.yaml",
    epochs=50,     # total target = 15
    resume=True   # 👈 treat it as new run, stops at 15/15
)
