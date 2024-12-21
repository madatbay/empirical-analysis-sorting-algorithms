def insertion_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers using the Insertion Sort algorithm.

    The algorithm builds the sorted list one element at a time by comparing the current element with the previous ones,
    and inserting it in the correct position.

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
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key after the element smaller than it
        arr[j + 1] = key

    return arr
