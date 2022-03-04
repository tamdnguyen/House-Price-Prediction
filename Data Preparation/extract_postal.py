"""
This file separates the numerical postal_code and the city from the postal_code column
"""

import re
import pandas as pd

def get_postal(line):
    """
    This function returns the numerical postal_code from the address column
    """
    postal = re.search(r"(\d+)", line).group(1)

    return str(postal)


def get_city(line):
    """
    This function returns the city from the address column
    """ 
    city = re.search(r"\((.*?)\)", line).group(1)

    return str(city)

def extract():
    df = pd.read_csv("data_raw.csv", encoding = "unicode_escape")

    # change the name of the columns
    df.columns = ["quarter", "address", "type", "price"]

    # get all the rows from the column address
    address = df["address"].tolist()

    postal_code = []
    city = []

    for value in address:
        postal_code.append(get_postal(value))
        city.append(get_city(value))

    return postal_code, city



