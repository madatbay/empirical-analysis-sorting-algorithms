import random


def generate_random_array(size: int, lower: int = 1, upper: int = 1000) -> list[int]:
    """
    Generates a random array of integers within a specified range.

    Parameters:
    - size (int): The size of the array to be generated.
    - lower (int): The lower bound of the random numbers (default is 1).
    - upper (int): The upper bound of the random numbers (default is 1000).

    Returns:
    - list[int]: A list containing 'size' random integers between 'lower' and 'upper'.
    """
    return [random.randint(lower, upper) for _ in range(size)]
