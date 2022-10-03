import pendulum
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='crawler',
    default_args={
        'depend_on_past': False,
        #'email': ['hartono.christson@gmail.com'],
        #'email_on_failure': True,
        #'email_on_retry': True,
        'retries': 0,
        #'retry_delay': timedelta(minutes=5),
    },
    description='Crawler Scheduler DAG',
    schedule_interval=timedelta(minutes=20),
    #schedule_interval="@hourly",
    start_date=datetime(2022, 1, 1),
    #start_date=pendulum.datetime(2022, 9, 1, tz="UTC"),
    catchup=False,
    tags=['crawler']
) as dag:
    task = BashOperator(
        task_id='crawl_and_store',
        bash_command='cd ~/airflow/dags/Crawler-BAGI && python3 main.py'
    )

    task
