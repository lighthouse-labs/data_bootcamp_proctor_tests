import pandas as pd
import sys
sys.path.append("..")

from questioncode.question_02 import compute_total_sale

df = pd.read_excel('../supporting-files/SaleData.xlsx')

import pytest


def test_on_data_type():
    assert isinstance(compute_total_sale(df), pd.DataFrame)

def test_on_correct_shape():
    assert compute_total_sale(df).shape == (8, 1)

def test_on_ordered_values():
    res = compute_total_sale(df)
    assert res['Sale_amt'].equals(res.sort_values('Sale_amt', ascending=False)['Sale_amt'])

def test_on_correct_answer():
    assert compute_total_sale(df).equals(df.groupby(['Region','Manager'])[['Sale_amt']].sum().sort_values('Sale_amt',ascending=False))

