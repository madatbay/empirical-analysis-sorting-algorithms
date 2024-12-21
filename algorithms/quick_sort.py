def quick_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers using the QuickSort algorithm.

    QuickSort is a divide and conquer algorithm. It selects a 'pivot' element from the list
    and partitions the other elements into two sublists, according to whether they are less than
    or greater than the pivot. The sublists are then sorted recursively.

    Time Complexity:
    - Worst case: O(n^2) (when the pivot is the smallest or largest element)
    - Best case: O(n log n)
    - Average case: O(n log n)

    Arguments:
        arr (list[int]): A list of integers to be sorted.

    Returns:
        list[int]: The sorted list of integers.

    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
