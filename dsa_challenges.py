def filter_and_sort_evens(numbers):
    """
    Returns a sorted list containing only even numbers.
    """
    evens = [num for num in numbers if num % 2 == 0]
    return sorted(evens)


def count_character_frequency(text):
    """
    Returns a dictionary with character frequencies.
    Counting is case-insensitive.
    """
    frequency = {}

    for char in text.lower():
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


# Example calls
numbers = [5, 2, 8, 1, 4, 7, 6]

print("Filtered and sorted evens:")
print(filter_and_sort_evens(numbers))

text = "Hello World"

print("Character frequency:")
print(count_character_frequency(text))