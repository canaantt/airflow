"""
### Oncoscape Testing Pipeline Documentation
Learn more about [Oncoscape](dev.oncoscape.sttrcancer.io)
"""
from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

#seven_days_ago = datetime.combine(datetime.today() - timedelta(7),datetime.min.time())

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 1, 3),
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
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/dataStr/generate_manifestArr.js',
    dag=dag)

t2 = BashOperator(
    task_id='dataStructureSchemaValidation',
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/dataStr/test1.js',
    dag=dag)

t3_0 = BashOperator(
    task_id='geneSymbolsCollection',
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/test0.js > ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/output.json',
    dag=dag)
t3_1 = BashOperator(
    task_id='geneSymbolsProcess1',
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/test1.js > ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/output2.json',
    dag=dag)
t3_2 = BashOperator(
    task_id='geneSymbolsProcess2',
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/test2.js',
    dag=dag)
t3_3 = BashOperator(
    task_id='geneSymbolsProcess3',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/geneSymbols/test3.js',
    dag=dag)

t4_1= BashOperator(
    task_id='patientIDsTest1',
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/ptIDs/test1.js',
    dag=dag)
t4_2 = BashOperator(
    task_id='patientIDsTest2',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/ptIDs/test2.js > ${AIRFLOW_HOME}/docker-airflow/onco-test/ptIDs/output2.json',
    dag=dag)
t4_3 = BashOperator(
    task_id='patientIDsTest3',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/ptIDs/test3.js',
    dag=dag)
t5 = BashOperator(
    task_id='duplicatedFields',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/checkingClinicalFields.js',
    dag=dag)
t6 = BashOperator(
    task_id='validateCalculatedFromMolecular',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/checkingPcaMdsCollectionNaming.js',
    dag=dag)
t7_1_1 = BashOperator(
    task_id='checkingMinMaxValues1',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/checkingminMaxValues_1.js',
    dag=dag)
t7_1_2 = BashOperator(
    task_id='checkingMinMaxValues2',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/checkingminMaxValues_2.js',
    dag=dag)
t7_1_3 = BashOperator(
    task_id='checkingMinMaxValues3',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/checkingminMaxValues_3.js',
    dag=dag)
t7_1_4 = BashOperator(
    task_id='checkingMinMaxValues4',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/checkingminMaxValues_4.js',
    dag=dag)
t7_1_5 = BashOperator(
    task_id='checkingMinMaxValues5',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/checkingminMaxValues_5.js',
    dag=dag)
t7_1_6 = BashOperator(
    task_id='checkingMinMaxValues6',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/checkingminMaxValues_6.js',
    dag=dag)
t7_2 = BashOperator(
    task_id='checkingMinMaxValues_sum',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/checkingminMaxValues_sum.js',
    dag=dag)
t8 = BashOperator(
    task_id='renderPatientXRange',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/renderPatientXRange.js',
    dag=dag)
t_final_report = BashOperator(
    task_id='generatingFinalReport',
    #depends_on_past=False,
    bash_command='node ${AIRFLOW_HOME}/docker-airflow/onco-test/airflow_generate_report.js > ${AIRFLOW_HOME}/docker-airflow/onco-test/report1.md',
    dag=dag)
t2.set_upstream(t1)
t3_0.set_upstream(t2)
t3_1.set_upstream(t3_0)
t3_2.set_upstream(t3_1)
t3_3.set_upstream(t3_2)
t4_1.set_upstream(t2)
t4_2.set_upstream(t4_1)
t4_3.set_upstream(t4_2)
t5.set_upstream(t2)
t7_1_1.set_upstream(t1)
t7_1_2.set_upstream(t1)
t7_1_3.set_upstream(t1)
t7_1_4.set_upstream(t1)
t7_1_5.set_upstream(t1)
t7_1_6.set_upstream(t1)
t7_2.set_upstream(t7_1_1)
t7_2.set_upstream(t7_1_2)
t7_2.set_upstream(t7_1_3)
t7_2.set_upstream(t7_1_4)
t7_2.set_upstream(t7_1_5)
t7_2.set_upstream(t7_1_6)
t8.set_upstream(t1)
t_final_report.set_upstream(t2)
t_final_report.set_upstream(t3_3)
t_final_report.set_upstream(t4_3)
t_final_report.set_upstream(t5)
t_final_report.set_upstream(t6)
t_final_report.set_upstream(t7_2)
t_final_report.set_upstream(t8)
