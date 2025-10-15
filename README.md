# 🚀 AWS Serverless Data Pipeline Project

A simple end-to-end **data engineering pipeline** built entirely with **AWS Serverless services**.  
This project demonstrates how to automatically process, clean, and analyze event data using **Lambda, S3, Glue, Athena,** and **QuickSight** — without managing any servers.

---

## 🧩 Architecture Overview

**Services used:**
- **Amazon S3** – stores raw and processed data  
- **AWS Lambda** – automatically triggered when new data arrives, cleans & writes output  
- **AWS Glue** – catalogs processed data for easy querying  
- **Amazon Athena** – runs SQL queries on top of processed S3 data  
- **Amazon QuickSight** – visualizes insights from Athena queries  

---

## 📊 Data Flow Diagram

```text
S3 (raw events) 
   │
   ▼
Lambda Function (cleans CSV)
   │
   ▼
S3 (processed)
   │
   ▼
Glue Crawler → Glue Catalog → Athena → QuickSight
