# AI– Object Detection (Duality Hackathon)

## Problem Statement
Research and report writing is time-consuming, with people spending hours searching through documents, PDFs, and multiple tools. Current tools are fragmented and inefficient.  
We propose a **Smart Research Assistant** powered by **YOLOv8 object detection**, enabling automated document/image analysis and faster research support.

---

##  Methodology
1. **Dataset Preparation** – Organized images and labels in YOLO format (`train/`, `val/`).  
2. **Model Training** – Fine-tuned YOLOv8 on the dataset.  
3. **Evaluation** – Measured precision, recall, and mAP scores.  
4. **Inference** – Tested on new images for real-world predictions.  
5. **Bonus Challenge** – Proposed *Real-Time Helmet Detection for Worker Safety*.  

---

## 🛠 Technologies Used
- Python 3.11  
- PyTorch  
- Ultralytics YOLOv8  
- OpenCV  
- Git & GitHub  

---

## 📂 Project Structure
```
.
├── train.py              # Training script
├── test.py               # Testing script
├── demo.py               # Demo script for inference
├── Evaluate.py           # Evaluation script
├── data.yaml             # Dataset config file
├── bonus_challenge.md    # Bonus challenge proposal
├── results.csv           # Training results
├── runs/                 # Training results (ignored in git)
├── venv/                 # Virtual environment (ignored in git)
└── README.md             # Project documentation
```

---

## Results
- **mAP50:** 0.736  
- **mAP50-95:** 0.581  
(Values will be verified during submission using your repo and weights.)  

---

## Dataset
The dataset is **not uploaded to GitHub** (due to size).  
👉 Download it here: [Dataset Google Drive Link](YOUR_DATASET_LINK_HERE)  

---

## Trained Weights
The trained YOLOv8 weights (`best.pt`) are also stored on Google Drive.  
👉 Download here: [Trained Weights Link](YOUR_WEIGHTS_LINK_HERE)  

Place them inside:
```
runs/detect/trainX/weights/best.pt
```

---

## ▶️ Running the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/SmartResearchAssistant.git
   cd SmartResearchAssistant
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model:
   ```bash
   python train.py
   ```
4. Run inference:
   ```bash
   python test.py
   ```

---

## 🎯 Bonus Challenge
See [bonus_challenge.md](bonus_challenge.md) for our **Real-Time Helmet Detection for Worker Safety** use case proposal.  
