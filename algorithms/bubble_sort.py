def bubble_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers using the Bubble Sort algorithm.

    The function repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. The process is repeated until
    the list is sorted.

    Time Complexity:
    - Worst case: O(n^2)
    - Best case: O(n) when the array is already sorted
    - Average case: O(n^2)

    Parameters:
        arr (list[int]): A list of integers to be sorted.

    Returns:
        list[int]: The sorted list of integers.

    """
    n = len(arr)
    for i in range(n):
        # Flag to check if any swap happened
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the list is already sorted
        if not swapped:
            break
    return arr
