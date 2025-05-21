from airflow import DAG
from datetime import datetime

with DAG(
    dag_id="weather_etl",
    start_date=datetime(year=2024, month=1, day=1, hour=9, minute=0),
    schedule="@daily",
    catchup=True,
    max_active_runs=1,
    render_template_as_native_obj=True
) as dag:
    pass