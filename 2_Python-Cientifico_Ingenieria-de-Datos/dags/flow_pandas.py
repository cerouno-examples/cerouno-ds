import datetime as dt
from time import sleep
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00382/c2k_data_comma.csv"

def download():
    print('1')
    df = pd.read_csv(url)
    df.to_csv('c2k_raw.csv')

def dropn():
    print('2')
    df = pd.read_csv('c2k_raw.csv', index_col='nr')
    sleep(90)
    df.dropna(inplace=True)
    df.to_csv('c2k_dropn.csv')

def fill():
    print('3')
    df = pd.read_csv('c2k_dropn.csv', index_col='nr')
    sleep(90)
    df.replace(to_replace='?', value=0, inplace=True)
    df.to_csv('c2k_fill.csv')

def cast():
    print('4')
    df = pd.read_csv('c2k_fill.csv', index_col='nr')
    sleep(90)
    df = df.astype('float64')
    df.to_csv('c2k_final.csv')


default_args = {
    'owner': 'Israel Z',
    'start_date': dt.datetime(2018, 5, 9),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('flow_pandas',
         default_args=default_args,
         schedule_interval='*/10 * * * *',
         ) as dag:

    download = PythonOperator(task_id='download',
                                 python_callable=download)
    dropn = PythonOperator(task_id='dropn',
                                 python_callable=dropn)
    fill = PythonOperator(task_id='fill',
                                 python_callable=fill)
    cast = PythonOperator(task_id='cast',
                                 python_callable=cast)

# Dependencies

dropn.set_upstream(download)
fill.set_upstream(dropn)
cast.set_upstream(fill)
