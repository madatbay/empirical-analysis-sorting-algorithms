# Empirical analysis of Sorting Algorithms in Python

## Prerequirements

1. uv package manager needs to be installed.
2. required python version needs to be installed specified in `.python-version` file.

## How to run

To run empirical benchmarking for every sorting algorithm with preconfigured inputs

```bash
uv run main.py
```

### Example output

```bash
Listing all sorting algorithms in sorted from the best to the worst:
1. Bubble sort:
	1. 0.000242
	2. 0.024012
	3. 2.099213
2. Insertion sort:
	1. 0.000013
	2. 0.000050
	3. 0.000543
3. Merge sort:
	1. 0.000097
	2. 0.000528
	3. 0.006783
4. Quick sort:
	1. 0.000040
	2. 0.000345
	3. 0.002616
5. Selection sort:
	1. 0.000091
	2. 0.008088
	3. 0.817163
```

### Avaitable sorting algorithms for benchmarking

1. Bubble sort
2. Insertion sort
3. Merge sort
4. Quick sort
5. Selection sort
