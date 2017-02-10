"""
### Oncoscape Testing Pipeline Documentation
Learn more about [Oncoscape](prod.oncoscape.sttrcancer.io)
"""
from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

#seven_days_ago = datetime.combine(datetime.today() - timedelta(7),datetime.min.time())

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 2, 9),
    'email': 'jzhang23@fredhutch.org',
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

dag = DAG('mongo_prod_testing', default_args=default_args)


# t1, t2 and t3 are examples of tasks created by instantiating operators

t1 = BashOperator(
    task_id='getMetaCollections',
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/prod_testing/airflow_prod_MetaCollections.js',
    dag=dag)

t2 = BashOperator(
    task_id='dataStructureSchemaValidation',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/prod_testing/airflow_prod_SchemaValidation.js',
    dag=dag)
t3_0 = BashOperator(
    task_id='geneSymbolsCollection',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/test0.js > ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/output.json',
    dag=dag)
t3_1 = BashOperator(
    task_id='geneSymbolsProcess1',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/test1.js > ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/output2.json',
    dag=dag)
t3_2 = BashOperator(
    task_id='geneSymbolsProcess2',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/test2.js',
    dag=dag)
t3_3 = BashOperator(
    task_id='geneSymbolsProcess3',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/test3.js',
    dag=dag)

t2.set_upstream(t1)
t3_0.set_upstream(t2)
t3_1.set_upstream(t3_0)
t3_2.set_upstream(t3_1)
t3_3.set_upstream(t3_2)
