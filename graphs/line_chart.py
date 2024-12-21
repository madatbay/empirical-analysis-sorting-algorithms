import matplotlib.pyplot as plt
from graph_data import SAMPLE_DATA

data = SAMPLE_DATA

# Extract reusable variables
input_sizes = data["input_sizes"]
times = data["times"]
algorithms = list(times.keys())

# Line Chart
plt.figure(figsize=(10, 6))

for algorithm in algorithms:
    plt.plot(input_sizes, times[algorithm], marker="o", label=algorithm)

# Formatting
plt.xlabel("Input Size", fontsize=14)
plt.ylabel("Execution Time (seconds)", fontsize=14)
plt.title("Sorting Algorithm Performance (Line Chart)", fontsize=16)
plt.xscale("log")  # Logarithmic scale for input sizes
plt.yscale("log")  # Logarithmic scale for execution time
plt.legend()
plt.grid(True)
plt.show()
