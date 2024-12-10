"""
Purpose: Progress Status Bar Implementation

    Escape Sequences
        \t - tab space
        \n - new line
        \r - rare feed
"""
print("Tom Brady")
print("Tom\tBrady")
print("Tom\nBrady")
print()

print("Tom\rBrady")
print("Brady\rTom")

data_set = range(0, 10_00_000)
data_set_length = len(data_set)

for loop_index, _ in enumerate(data_set):
    percent_completed = (loop_index / data_set_length) * 100
    percent_completed = round(percent_completed, 0)

    print(f"\r{percent_completed:5} completed", end="")