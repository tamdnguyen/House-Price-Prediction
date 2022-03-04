"""
This file creates the number of room in numerical form of a row in the dataframe
from the corresponding type of flat in that row.
"""

import pandas as pd

"""
Dictionary in which
    - Keys are the type of flat in the dataframe
    - Values are the number of room (int) of the flat
"""
FLAT = {"Blocks of flats, one-room flat": 1,
        "Blocks of flats, two-room flat": 2,
        "Blocks of flats, three-room flat+": 3}


def get_room():
    """
    This part reads in the file
    
    we have 
        - the flat type as a list
    """

    df = pd.read_csv("data_raw.csv", encoding = "unicode_escape")

    # change the name of the columns
    df.columns = ["quarter", "address", "type", "price"]

    type = df["type"]

    type = type.tolist()


    """
    This part create the room list that we want
    """

    room = []

    for flat in type:
        room.append(FLAT[flat])

    return room
    
