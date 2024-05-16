from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# Defina o DAG (Directed Acyclic Graph)
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 15),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'meu_primeiro_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

# Tarefas
def tarefa1():
    print("Executando a Tarefa 1")

def tarefa2():
    print("Executando a Tarefa 2")

inicio = DummyOperator(task_id='inicio', dag=dag)
tarefa1 = PythonOperator(task_id='tarefa1', python_callable=tarefa1, dag=dag)
tarefa2 = PythonOperator(task_id='tarefa2', python_callable=tarefa2, dag=dag)
fim = DummyOperator(task_id='fim', dag=dag)

# Defina a ordem das tarefas
inicio >> tarefa1 >> tarefa2 >> fim
