"""
Purpose: Writing csv using csv module

"""
import csv

with open("second.csv", mode="w", newline='') as fh:
    header_names = ("jersey_no","name","age","role")
    writer = csv.DictWriter(fh, delimiter=",", fieldnames=header_names)

    # To write the headers
    writer.writeheader()

    # To write a single record
    writer.writerow({"jersey_no": 12, "name": "TOM", "age": 45, "role": "QB"})

    # To write multiple records
    writer.writerows(
        [
            {"jersey_no": 97, "name": "Nick", "age": 28, "role": "DT"},
            {"jersey_no": 1, "name": "Deebo", "age": 31, "role": "WR"},
            {"jersey_no": 1, "name": "Deebo", "age": 31},  # , "role": "WR"},
            {"jersey_no": 17, "name": "Deebo"},  # , "age": 31} #, "role": "WR"},
            {"jersey_no": 6, "role": "WR"},
        ]
    )