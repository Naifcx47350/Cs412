
# * input / output relation

import random
import time
a = int(input("Enter a number: "))


def add10(a):
    a += 10
    return a


print(add10(a))


# * bubble sort vs merge sort in terms of time complexity


def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if (arr[j] > arr[j + 1]):
                x = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = x

    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


input_sequence = [random.randint(0, 1000) for i in range(1000)]

start_time = time.time()
sorted_sequence = bubble_sort(input_sequence.copy())
end_time = time.time()

bubble_sort_time = end_time - start_time

print("Bubble sort time: ", bubble_sort_time)

start_time = time.time()
sorted_sequence = merge_sort(input_sequence.copy())
end_time = time.time()

merge_sort_time = end_time - start_time

print("Merge sort time: ", merge_sort_time)
