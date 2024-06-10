1- PowerShell: Set-ExecutionPolicy RemoteSigned
2- PowerShell: Get-ExecutionPolicy
    RemoteSigned

3- python -m venv airflow_env
    .\airflow_env\Scripts\activate

4- mkdir -p ./dags ./logs ./plugins ./config

    ./dags - you can put your DAG files here.
    ./logs - contains logs from task execution and scheduler.
    ./config - add custom log parser or add airflow_local_settings.py to configure cluster policy.
    ./plugins - you can put your custom plugins here.

5- Download and save below link in your local:
    https://airflow.apache.org/docs/apache-airflow/2.9.1/docker-compose.yaml

6- docker compose up airflow-init

7- docker-compose up

8- docker-compose.yaml:
    AIRFLOW__CORE__LOAD_EXAMPLES: 'true' >> 'false'

9- http://localhost:8080/

10- sign in:
    user: airflow
    pass: airflow

Good luck.
Sincerely, Kian Ara.
