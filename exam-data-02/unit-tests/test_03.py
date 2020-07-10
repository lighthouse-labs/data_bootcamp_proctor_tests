import pytest
import sys
import sqlite3
import pandas as pd
sys.path.append("..")
from answers.question_03 import SQL

ANSWER_SQL = """SELECT first_name,
                last_name,
                salary, 
                0.12*salary as PF
         FROM employees
"""

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

def test_on_correct_answer():
    assert df_student.equals(df_answer)

