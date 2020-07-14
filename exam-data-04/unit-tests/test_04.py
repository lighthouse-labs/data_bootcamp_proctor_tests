import pytest
import sqlite3
import pandas as pd
from answers.question_04 import SQL
from supporting_files.data_loader import load_data_from_database

DB = 'supporting_files/hr.db'
ANSWER_SQL = """SELECT d.department_id, 
                d.department_name, 
                e.first_name 
         FROM departments d 
            INNER JOIN employees e 
            ON d.department_id = e.department_id
         ORDER BY first_name"""

df_answer = load_data_from_database(ANSWER_SQL,DB)


def test_on_valid_sql():
    global df_student

    try:
        df_student = load_data_from_database(SQL,DB)
    except:
        df_student = pd.DataFrame()

    assert not df_student.empty

def test_on_number_of_rows():
    assert df_student.shape[0] == df_answer.shape[0]

def test_on_number_of_columns():
    assert df_student.shape[1] == df_answer.shape[1]

def test_on_correct_columns():
    assert list(df_student.columns) == list(df_answer.columns)

def test_on_correct_order():
    assert list(df_student.first_name) == list(df_answer.first_name)

def test_on_correct_answer():
    assert df_student.equals(df_answer)