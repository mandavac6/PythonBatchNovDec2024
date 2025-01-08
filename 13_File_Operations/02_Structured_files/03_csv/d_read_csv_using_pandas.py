"""
Purpose: Reading(Parsing) csv using pandas module

    pip install pandas
"""
import pandas as pd

# print(dir(pandas))

# Loading a csv
data_frame = pd.read_csv("my_file.csv")

# print(type(data_frame))
# print(data_frame) prints the whole data in the csv 

# print(data_frame.head()) it only gives 5 vales from the top

print(set(data_frame.name))