from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.selection_sort import selection_sort
from utils.generate_input import generate_random_array
from utils.time_func import time_func


def main():
    arr_100 = generate_random_array(100)
    arr_1000 = generate_random_array(1000)
    arr_10000 = generate_random_array(10000)

    sorting_functions = (
        ("Bubble sort", bubble_sort),
        ("Insertion sort", insertion_sort),
        ("Merge sort", merge_sort),
        ("Quick sort", quick_sort),
        ("Selection sort", selection_sort),
    )

    time_values = {}

    # Run each sorting algorithm for every array value
    for v in sorting_functions:
        label, func = v
        _, time_1 = time_func(func, arr_100)
        _, time_2 = time_func(func, arr_1000)
        _, time_3 = time_func(func, arr_10000)

        time_values[label] = [time_1, time_2, time_3]

    print("Listing all sorting algorithms in sorted from the best to the worst:")
    for idx, key in enumerate(sorted(time_values.keys(), key=lambda x: time_values[x])):
        print(f"{idx + 1}.", f"{key}: ")
        for idy, value in enumerate(time_values[key]):
            print(f"\t{idy + 1}.", f"{value:.6f}")


if __name__ == "__main__":
    main()
