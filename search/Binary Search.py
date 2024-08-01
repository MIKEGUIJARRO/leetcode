from typing import List

metadata = {
    'title': 'Binary Search',
    'link': None,
    'difficulty': 'easy',
    'tags': ['binary_search', 'search']
}

# returns the integer of the searched value
def binary_search(arr: List, search_val: int) -> int:
    low = 0
    high = len(arr) - 1

    while  low <= high:
        mid = int((high + low) / 2)

        guess = arr[mid]

        if guess == search_val:
            return mid
        
        if guess < search_val:
            low = guess + 1
        else:
            high = guess - 1

    return None

arr = [1, 2, 4, 5, 6, 8, 12, 24, 89]

res = binary_search(arr, 24)