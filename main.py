from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from utils.generate_input import generate_random_array
from utils.time_func import time_func


def main():
    arr = generate_random_array(100)

    b_sorted, b_time = time_func(bubble_sort, arr)
    i_sorted, i_time = time_func(insertion_sort, arr)
    m_sorted, m_time = time_func(merge_sort, arr)

    execution_durations = (
        ("Bubble sort", b_time),
        ("Insertion sort", i_time),
        ("Merge sort", m_time),
    )

    print("Listing all sorting algorithms in sorted from the best to the worst:")
    for index, value in enumerate(sorted(execution_durations, key=lambda x: x[1])):
        name, time = value
        print(index + 1, name, f": {time:.6f}")

    print("\nAll sorted values equal: ", b_sorted == i_sorted == m_sorted)


if __name__ == "__main__":
    main()
