import pytest
import sys
import sqlite3
import pandas as pd
sys.path.append("..")
from answers.question_03 import SQL

ANSWER_SQL = """SELECT first_name,
                       last_name,
                       manager_id
                FROM employees
                WHERE manager_id IN (SELECT employee_id
                                    FROM employees
                                    WHERE department_id IN (SELECT department_id 
                                                            FROM departments 
                                                            WHERE location_id IN (SELECT location_id 
                                                                                    FROM locations 
                                                                                    WHERE country_id = 'US')))""" 

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

def test_on_join():
    assert 'join' not in SQL.lower()

def test_on_correct_answer():
    assert df_student.equals(df_answer)

