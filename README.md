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

| type/input | 100      | 1000     | 10000    |
| ---------- | -------- | -------- | -------- |
| Insertion  | 0.000013 | 0.000052 | 0.000500 |
| Quick      | 0.000045 | 0.000384 | 0.002873 |
| Merge      | 0.000075 | 0.000555 | 0.007157 |
| Selection  | 0.000093 | 0.007656 | 0.852193 |
| Bubble     | 0.000154 | 0.019936 | 2.143636 |

### Avaitable sorting algorithms for benchmarking

1. Bubble sort
2. Insertion sort
3. Merge sort
4. Quick sort
5. Selection sort
