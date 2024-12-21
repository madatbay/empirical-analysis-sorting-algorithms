from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from utils.generate_input import generate_random_array
from utils.time_func import time_func


def main():
    arr = generate_random_array(100)

    b_sorted, b_time = time_func(bubble_sort, arr)
    i_sorted, i_time = time_func(insertion_sort, arr)

    print("Bubble sort execution time: ", b_time)
    print("Insertion sort execution time: ", i_time)

    print("All sorted values equal: ", b_sorted == i_sorted)


if __name__ == "__main__":
    main()
