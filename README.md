### Set up Apache Airflow using Docker on Windows

#apache #airflow #docker

![1718041448475](image/README/1718041448475.png)

Setting up Apache Airflow using Docker containers on Windows involves a series of steps to ensure a seamless orchestration of workflows. Setting up manually usually takes time, and there may be inconsistencies of the adaptation in the versions. So, using Docker can be helpful and save time. With the guidance of this repository and following a few steps, you can run Airflow locally easily.

1- Open Windows PowerShell and run the below code.

```
set-executionPolicy RemoteSigned
```

2- To ensure the above command is set, run below code and will be returned "RemoteSigned"

```
get-executionPolicy
```

3- In your Python editor,  make a virtual environment.

```
python -m venv airflow_env
```

4- Activate it.

```
.\airflow_env\Scripts\activate
```

5- Create four folders with these names. (These folders are the default. Do not change names.

```
mkdir -p ./dags ./logs ./plugins ./config
```

* ./dags - you can put your DAG files here.
* ./logs - contains logs from task execution and scheduler.
* ./config - add custom log parser or add airflow_local_settings.py to configure cluster policy.
* ./plugins - you can put your custom plugins here.

6- Download and save below link in your Python editor.

https://airflow.apache.org/docs/apache-airflow/2.9.1/docker-compose.yaml

7- Inactive dag examples in docker-compose.yaml.

AIRFLOW__CORE__LOAD_EXAMPLES: 'true' >> 'false'

8- Run docker compose command. (It takes some time)

```
docker compose up airflow-init
```

9- After completing the last step successfully, run the following code to create containers.

```
docker-compose up -d
```

10- Open your browser and connect to the airflow port.

```
http://localhost:8080/
```

11- Sign in:

```
    user: airflow
    pass: airflow
```

Good luck.
Sincerely, [Kian Ara](https://www.linkedin.com/in/hossein-kian-ara/ "Linkdin").
