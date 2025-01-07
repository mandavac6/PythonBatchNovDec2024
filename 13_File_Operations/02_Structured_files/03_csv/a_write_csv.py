"""
Purpose: writing(creating) a CSV, like unstructured data
"""

with open("my_file.csv", "w") as fh:
    fh.write("jersey_no,name,age,role\n")
    fh.write("8,Aaron Rogers,40,QB\n")
    fh.write("12,Tom Brady,45,QB\n")
    fh.write("97,Nick Bosa,28,DT\n")
    fh.write("90,TJ Watt,31,T\n")

    fh.flush()
    fh.close()