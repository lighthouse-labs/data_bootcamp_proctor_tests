import pandas as pd
import sys
from supporting_files.data_loader import load_excel

df = load_excel('supporting_files/SaleData.xlsx')


"""
Write a Pandas program to count the manager wise sale (sale_cnt)
and mean value of sale amount (sale_mean). 
Order the output dataframe using sale_cnt, starting with the highest.

"""

def compute_agg_stats(df):
    "IMPLEMENT ME"