import boto3
import csv
import io
import uuid
from datetime import datetime

s3 = boto3.client('s3')

PROCESSED_BUCKET = 'your bucket name'  # replace

def lambda_handler(event, context):
    # event from S3: get bucket and key
    for rec in event.get('Records', []):
        src_bucket = rec['s3']['bucket']['name']
        key = rec['s3']['object']['key']
        print(f"Processing s3://{src_bucket}/{key}")

        obj = s3.get_object(Bucket=src_bucket, Key=key)
        body = obj['Body'].read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(body))

        out_buffer = io.StringIO()
        writer = None
        count = 0

        for row in reader:
            if not row.get('event_id') or not row.get('event_time'):
                continue
            try:
                dt = datetime.fromisoformat(row['event_time'].replace('Z','+00:00'))
            except Exception as e:
                print("bad time:", row.get('event_time'))
                continue

            try:
                row['amount'] = str(float(row.get('amount',0)))
            except:
                row['amount'] = "0"

            if writer is None:
                writer = csv.DictWriter(out_buffer, fieldnames=list(row.keys()))
                writer.writeheader()

            writer.writerow(row)
            count += 1

        if count == 0:
            print("no valid rows, skipping upload")
            continue

        out_buffer.seek(0)
        now = datetime.utcnow()
        part_prefix = f"year={now.year}/month={now.month:02d}/day={now.day:02d}/"
        out_key = part_prefix + f"part-{uuid.uuid4().hex}.csv"

        s3.put_object(Bucket=PROCESSED_BUCKET, Key=out_key, Body=out_buffer.getvalue().encode('utf-8'))
        print(f"Wrote {count} rows to s3://{PROCESSED_BUCKET}/{out_key}")

    return {"status": "ok"}
