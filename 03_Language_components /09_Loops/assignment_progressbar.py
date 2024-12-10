data_set = range(0, 10_00_000)
data_set_length = len(data_set)
total = 10

for loop_index, _ in enumerate(data_set):
    percent_completed = (loop_index / data_set_length) * 100
    percent_completed = round(percent_completed, 0)
    filled_length = int(percent_completed // 10)
    progress_bar = "[" + "*" * filled_length + " " * (total - filled_length) + "]"
    print(f"\r{progress_bar} {percent_completed:5} completed", end="")