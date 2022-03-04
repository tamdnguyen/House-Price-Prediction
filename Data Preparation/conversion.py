"""
This file is used to create a new column "date_count" in dataframe.

The date_count value of each row is the number of quarters from 2010Q1 to the corresponding quarter of that row.
"""

import numpy as np
import pandas as pd

def conversion():
    """
    This part reads in the file
    
    we have 
        - the date (quarter) as a list
        - the unique date (quarter as another list)
    """

    df = pd.read_csv("data_raw.csv", encoding = "unicode_escape")

    # change the name of the columns
    df.columns = ["quarter", "address", "type", "price"]

    date_array = df["quarter"]
    date_array_unique = df["quarter"].unique()

    date_array = date_array.tolist()
    date_array_unique = date_array_unique.tolist()


    """
    This part reads in the list of date
    
    we have the dict in which 
        - the key is the date
        - the value is the count of the quarter counts from the first quarter in the list
    """

    quarter_dict = {}

    for count, value in enumerate(date_array_unique):
        quarter_dict[value] = count + 1
    


    """
    This part create the date_count list that we want
    """

    date_count = []

    for date in date_array:
        date_count.append(quarter_dict[date])

    return date_count

conversion()
