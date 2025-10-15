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
```
### ⚙️ How It Works

Upload raw CSV (e.g., events_sample.csv) to the raw S3 bucket.
Example bucket: my-datapipeline-raw-data/

S3 triggers the Lambda function.

Lambda reads the file, filters out missing or invalid rows, and writes a cleaned version to:

```

my-datapipeline-processed-data/year=2025/month=10/day=14/         

```

AWS Glue Crawler runs and detects the schema.

Athena queries the processed data using SQL.

QuickSight visualizes trends (e.g., total purchases, user activity).

### 🧠 Lambda Function Overview
Main Steps

Triggered by S3 event

Downloads CSV from the raw bucket

Cleans data (removes invalid rows, fills missing values)

Uploads cleaned CSV to the processed bucket
