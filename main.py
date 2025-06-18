from datetime import timedelta
import pendulum
from airflow.decorators import dag, task

@dag(
    dag_id='simple_core_dag',
    schedule="@daily",
    start_date=pendulum.datetime(2025, 6, 18, tz="America/Argentina/Tucuman"),
    catchup=False,
    default_args={'retries': 0, 'retry_delay': timedelta(minutes=1)},
    tags=['basic']
)
def simple_core_dag():
    @task()
    def inicio():
        msg = "Hola, DAG mínimo"
        print(msg)
        return msg

    @task()
    def fin(valor: str):
        print(f"Fin de DAG. Recibido: {valor}")

    resultado = inicio()
    fin(resultado)

dag = simple_core_dag()
