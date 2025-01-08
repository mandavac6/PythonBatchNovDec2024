"""
Purpose: Writing csv using csv module using different delimiter

"""
import csv

with open("fourth.csv", mode="w", newline='') as fh:
    header_names = ("jersey_no","name","age","role")

    writer = csv.writer(fh, delimiter="/")

    writer.writerow(header_names)

    # To write a single record
    writer.writerow([12,"Tom Brady",45,"QB"])

    # To write multiple records
    writer.writerows(
        [
            [8,"Aaron Rogers",40,"QB"],
            [97,"Nick Bosa",28,"DT"],
            [90,"TJ Watt",31,"T"],
            [54, "", 32, "LB"],

        ]
    )