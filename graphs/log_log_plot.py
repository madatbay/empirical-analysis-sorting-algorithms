import matplotlib.pyplot as plt
import numpy as np
from graph_data import SAMPLE_DATA

data = SAMPLE_DATA

# Extract reusable variables
input_sizes = data["input_sizes"]
times = data["times"]
algorithms = list(times.keys())

# Log-Log Line Chart
plt.figure(figsize=(10, 6))

# Plot empirical data for each algorithm
for algorithm in algorithms:
    plt.plot(input_sizes, times[algorithm], marker="o", label=algorithm)

# Plot theoretical complexity lines (for comparison)
# Example: O(n) - linear, O(n^2) - quadratic, O(log n) - logarithmic
input_sizes_for_theory = np.linspace(min(input_sizes), max(input_sizes), 100)

# O(n)
plt.plot(
    input_sizes_for_theory,
    input_sizes_for_theory * 1e-5,
    "--",
    label="O(n)",
    color="black",
)

# O(n^2)
plt.plot(
    input_sizes_for_theory,
    (input_sizes_for_theory**2) * 1e-9,
    "--",
    label="O(n^2)",
    color="red",
)

# O(log n)
plt.plot(
    input_sizes_for_theory,
    np.log(input_sizes_for_theory) * 1e-6,
    "--",
    label="O(log n)",
    color="blue",
)

# Formatting
plt.xlabel("Input Size", fontsize=14)
plt.ylabel("Execution Time (seconds)", fontsize=14)
plt.title("Sorting Algorithm Performance with Asymptotic Notation", fontsize=16)
plt.xscale("log")  # Logarithmic scale for input size
plt.yscale("log")  # Logarithmic scale for execution time
plt.legend()
plt.grid(True)
plt.show()
