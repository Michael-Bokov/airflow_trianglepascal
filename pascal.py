from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def generate_pascals_triangle(levels):
    triangle = []
    for i in range(levels):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def print_pascals_triangle():
    levels = 10
    triangle = generate_pascals_triangle(levels)
    for row in triangle:
        print(" ".join(map(str, row)))

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 22),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'pascal',
    default_args=default_args,
    description='DAG for Pascal Triangle',
    schedule_interval='44 11 * * *',
    catchup=False
)

task_print_pascals_triangle = PythonOperator(
    task_id='print_pascals_triangle',
    python_callable=print_pascals_triangle,
    dag=dag,
)

task_print_pascals_triangle
