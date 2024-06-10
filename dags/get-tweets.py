from airflow import DAG
from airflow.operators.bash_operator import BashOperator 
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "DSG-Fozouni",
    "depends_on_past": False,
    'start_date': datetime(2024, 4, 17, 0, 0),
    "email": ["fozouni@gonbad.ac.ir"],
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG("Get-Tweets", default_args=default_args, schedule_interval="* * * * *" , catchup=False);

#-------------Operators--------------------------------

get_tweets = BashOperator(
    task_id='Get-Sahamyab-Tweets',
    bash_command= "/usr/bin/curl -s -H 'User-Agent:Chrome/123.0' https://www.sahamyab.com/guest/twiter/list?v=0.1 | "
                  "/usr/bin/jq \'.items[0,2,3,4,5,6,7,8,9,10] | [.id, .sendTime, .sendTimePersian, .senderName, "
                  ".senderUsername, .type, .content] | join(\",\") \' > /home/amin/data/stage/step1/$(date +%s).csv" ,
    dag=dag,
)

task_dummy = DummyOperator(task_id="Dummy-Operator", dag=dag)

#----------------------- DAG Structure -------------------------------

get_tweets >> task_dummy
    