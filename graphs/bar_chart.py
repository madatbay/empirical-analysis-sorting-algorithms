import matplotlib.pyplot as plt
import numpy as np
from graph_data import SAMPLE_DATA

data = SAMPLE_DATA

# Extract reusable variables
input_sizes = data["input_sizes"]
times = data["times"]
algorithms = list(times.keys())

# Extract reusable variables
input_sizes = data["input_sizes"]
times = data["times"]
algorithms = list(times.keys())

# Bar Chart
x = np.arange(len(input_sizes))  # Bar positions
bar_width = 0.15
fig, ax = plt.subplots(figsize=(10, 6))

for i, algorithm in enumerate(algorithms):
    ax.bar(x + i * bar_width, times[algorithm], bar_width, label=algorithm)

# Formatting
ax.set_xlabel("Input Size", fontsize=14)
ax.set_ylabel("Execution Time (seconds)", fontsize=14)
ax.set_title("Sorting Algorithm Performance (Bar Chart)", fontsize=16)
ax.set_xticks(x + bar_width * (len(algorithms) - 1) / 2)
ax.set_xticklabels(input_sizes)
ax.legend()
plt.show()
