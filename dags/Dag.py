from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('spark_job_dag', description='DAG to trigger pySpark job',
          schedule_interval='0 12 * * *',
          start_date=datetime(2020, 3, 20), catchup=False)

start_task = DummyOperator(task_id='start_task', dag=dag)

commands = """
    cd /Documents/Airflow/Data;
   /opt/bitnami/spark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 save_data.py;
    """

fetch_data = BashOperator(
    task_id='spark-task',
    bash_command=commands,
    dag=dag)

start_task >> fetch_data
