import os

paths = [
    "C:/Users/bhavana reddy/Downloads/hackathon2_train_1/train_1/train1/images",
    "C:/Users/bhavana reddy/Downloads/hackathon2_train_1/train_1/train1/labels",
    "C:/Users/bhavana reddy/Downloads/hackathon2_train_1/train_1/val1/images",
    "C:/Users/bhavana reddy/Downloads/hackathon2_train_1/train_1/val1/labels",
]

for p in paths:
    print(p, "exists:", os.path.exists(p))
    if os.path.exists(p):
        print("Files inside:", len(os.listdir(p)))
