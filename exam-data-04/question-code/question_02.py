import pandas as pd
import sys
from supporting_files.data_loader import load_excel

df = load_excel('supporting_files/SaleData.xlsx')


"""
Write a Pandas program to find the total sale amount region wise, manager wise. 
Order the dataframe, starting with the biggest total sale amount.
"""

def compute_total_sale(df):
    "IMPLEMENT ME"