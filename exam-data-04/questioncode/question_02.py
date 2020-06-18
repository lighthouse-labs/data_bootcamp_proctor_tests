import pandas as pd
import sys
sys.path.append("..")

df = pd.read_excel('../supporting-files/SaleData.xlsx')

"""
Write a Pandas program to find the total sale amount region wise, manager wise. 
Order the dataframe, starting with the biggest total sale amount.
"""

def compute_total_sale(df):
    "IMPLEMENT ME"