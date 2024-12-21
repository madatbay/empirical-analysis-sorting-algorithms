def selection_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers using the Selection Sort algorithm.

    The algorithm repeatedly selects the minimum element from the unsorted portion of the list
    and swaps it with the first unsorted element.

    Time Complexity:
    - Worst case: O(n^2)
    - Best case: O(n^2)
    - Average case: O(n^2)

    Arguments:
        arr (list[int]): A list of integers to be sorted.

    Returns:
        list[int]: The sorted list of integers.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
