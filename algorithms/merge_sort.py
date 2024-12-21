def merge_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers using the Merge Sort algorithm.

    Merge Sort is a divide and conquer algorithm that splits the list into two halves,
    sorts each half recursively, and then merges the sorted halves.

    Time Complexity:
    - Worst case: O(n log n)
    - Best case: O(n log n)
    - Average case: O(n log n)

    Parameters:
        arr (list[int]): A list of integers to be sorted.

    Returns:
        list[int]: The sorted list of integers.

    """
    if len(arr) <= 1:
        return arr

    # Find the middle of the list
    mid = len(arr) // 2

    # Recursively split and merge
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merges two sorted lists into one sorted list.

    Parameters:
        left (list[int]): The left sorted half.
        right (list[int]): The right sorted half.

    Returns:
        list[int]: The merged sorted list.
    """
    sorted_list = []
    i = j = 0

    # Merge elements from both halves in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list
