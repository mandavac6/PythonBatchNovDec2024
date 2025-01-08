# assignment - create csv files with all possible delimiters and read the content also


import csv

with open("x_asignment2.csv", mode="w", newline='') as fh:
    header_names = ("jersey_no","name","age","role")

    writer = csv.writer(fh, delimiter="_")

    writer.writerow(header_names)

    # To write a single record
    writer.writerow([12,"TomBrady",45,"QB"])

    # To write multiple records
    writer.writerows(
        [
            [8,"AaronRogers",40,"QB"],
            [97,"NickBosa",28,"DT"],
            [90,"TJWatt",31,"T"],
            [54, "", 32, "LB"],

        ]
    )

with open("x_asignment2.csv", mode="r") as fh:
    file_content = fh.readlines()

names = []
for each_line in file_content[1:]:
    name = each_line.split('_')[1]
    names.append(name)

print(f"{names = }")