from algorithms.bubble_sort import bubble_sort
from utils.generate_input import generate_random_array
from utils.time_func import time_func


def main():
    arr = generate_random_array(100)
    arr_c = generate_random_array(1000)
    arr_d = generate_random_array(10000)

    b_sorted, b_time = time_func(bubble_sort, arr)
    b_sorted, c_time = time_func(bubble_sort, arr_c)
    b_sorted, d_time = time_func(bubble_sort, arr_d)
    print("Bubble sort execution time,", b_time)
    print("Bubble sort execution time,", c_time)
    print("Bubble sort execution time,", d_time)


if __name__ == "__main__":
    main()
