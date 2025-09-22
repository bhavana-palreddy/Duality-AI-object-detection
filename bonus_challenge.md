# 🎯 Bonus Challenge: Real-Time Helmet Detection for Worker Safety  

##  Problem:  
In construction sites and industrial environments, accidents often happen because workers fail to wear Personal Protective Equipment (PPE) like helmets.  
Manual monitoring is time-consuming, error-prone, and difficult to scale when there are many workers on site.  

## Solution  
We propose a **YOLOv8-based real-time helmet detection system** that automatically checks if workers are wearing helmets using CCTV or live video feeds.  
The system can instantly alert supervisors when a violation is detected, ensuring compliance and improving safety.  

## Key Features  
-  Real-time detection using cameras or CCTV footage  
-  Automated alerts via email, SMS, or dashboard notifications when a worker is not wearing a helmet  
-  Analytics dashboard showing helmet compliance statistics over time  
- Scalable deployment across multiple worksites  

##  Impact  
- Improves worker safety and reduces accident risks  
-  Ensures regulatory compliance for PPE usage  
-  Reduces manual monitoring effort and cost  
-  Helps avoid penalties/fines and promotes a safer workplace culture  

---

##  Workflow (Flowchart)


         [ CCTV / Camera Feed ]
                    │
                    ▼
         [ YOLOv8 Helmet Detection ]
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
 [ Helmet Detected ✅ ]   [ No Helmet ❌ ]
          │                   │
          ▼                   ▼
   [ Safe - No Action ]   [ Trigger Alert 🚨 ]
                                │
                                ▼
                  [ Dashboard / Supervisor Notification ]
