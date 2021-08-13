import os
from airflow import models
from airflow.providers.google.cloud.operators.gcs import GCSSynchronizeBucketsOperator
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
from airflow.utils.dates import days_ago

BUCKET_1_SRC = os.environ.get("GCP_GCS_BUCKET_1_SRC", "source bucket")
BUCKET_1_DST = os.environ.get("GCP_GCS_BUCKET_1_DST", "destination bucket")
with models.DAG(
    "example_gcs_to_gcs", start_date=days_ago(1), schedule_interval=None, tags=['example']
) as dag:
 # [START howto_synch_bucket]
    sync_bucket = GCSSynchronizeBucketsOperator(
        task_id="sync_bucket", source_bucket=BUCKET_1_SRC, destination_bucket=BUCKET_1_DST
    )
    # [END howto_synch_bucket]
