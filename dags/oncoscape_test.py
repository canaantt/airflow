"""
### Tutorial Documentation
Documentation that goes along with the Airflow tutorial located
[here](http://pythonhosted.org/airflow/tutorial.html)
"""
from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

#seven_days_ago = datetime.combine(datetime.today() - timedelta(7),datetime.min.time())

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 11, 29),
    'email': ['jzhang23@fredhutch.org'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'schedule_interval': timedelta(1),
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('oncoscape_test', default_args=default_args)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='getManifest',
    bash_command='node /Users/zhangj4/Desktop/canaantt_git/oncoscape_api_explorer/test/datasourceTesting/generate_manifestArr.js',
    dag=dag)

t2 = BashOperator(
    task_id='dataStructureSchemaValidation',
    #depends_on_past=False,
    bash_command='node /Users/zhangj4/Desktop/canaantt_git/oncoscape_api_explorer/test/datasourceTesting/test1.js',
    dag=dag)

t2.set_upstream(t1)
