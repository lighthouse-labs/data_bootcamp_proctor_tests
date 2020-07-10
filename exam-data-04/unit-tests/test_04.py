import pytest
import sys
import sqlite3
import pandas as pd
sys.path.append("..")
from answers.question_04 import SQL

ANSWER_SQL = """SELECT d.department_id, 
                d.department_name, 
                e.first_name 
         FROM departments d 
            INNER JOIN employees e 
            ON d.department_id = e.department_id
         ORDER BY first_name"""

with sqlite3.connect('../supporting-files/hr.db') as con:
    df_answer = pd.read_sql(ANSWER_SQL, con)


def test_on_valid_sql():
    global df_student

    try:
        with sqlite3.connect('../supporting-files/hr.db') as con:
            df_student = pd.read_sql(SQL,con)
    except:
            df_student = pd.DataFrame()

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