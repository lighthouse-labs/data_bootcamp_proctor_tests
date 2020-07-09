import pytest
import pandas as pd
from answers.question_03 import compute_agg_stats
import sys
sys.path.append("..")


df = pd.read_excel('../supporting-files/SaleData.xlsx')


def test_on_data_type():
    assert isinstance(compute_agg_stats(df), pd.DataFrame)

def test_on_correct_shape():
    assert compute_agg_stats(df).shape == (4, 2)

def test_on_ordered_values():
    res = compute_agg_stats(df)
    assert res['sale_cnt'].equals(res.sort_values('sale_cnt', ascending=False)['sale_cnt'])

def test_on_correct_answer():
    assert compute_agg_stats(df).equals(df.groupby('Manager').agg(sale_cnt = ('Item', 'count'),
                                                                  sale_mean = ('Sale_amt', 'mean')).sort_values('sale_cnt', ascending=False))
