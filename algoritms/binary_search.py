"""
Бинарный поиск:

1. Можно совершать при условии, что значения отсортированы.

2. имеет сложность O(Log n)

3. При бинарном поиске, каждый раз исключается половина значений

4. Занимает логарефмическое время
"""


def binary_search(array, num):
    array = sorted(array)
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess < num:
            low = mid + 1
        elif num < guess:
            high = mid - 1
        else:
            return guess


print(binary_search([1, 5, 7, 8, 3, 2, 9, 0, 11, 423], 111))
