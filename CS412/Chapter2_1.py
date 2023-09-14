import time
import random

# * insertion_sort


def insertion_sort(arr):
    for i in range(1, len(arr)):

        key = arr[i]  # key = 11
        j = i - 1  # j = 0
        while j >= 0 and key < arr[j]:  # 11 < 12

            arr[j + 1] = arr[j]  # arr[1] = 12
            j -= 1  # j = -1
            print(arr)
        arr[j + 1] = key


my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array:", my_list)


# * bubble sort
def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if (arr[j] > arr[j + 1]):
                x = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = x


my_list = [12, 11, 13, 5, 6]
bubble_sort(my_list)
print("Sorted array:", my_list)


def selection_sort(arr):

    for i in range(len(arr)):

        min_idx = i

        for j in range(i + 1, len(arr)):

            if arr[min_idx] > arr[j]:
                min_idx = j

        x = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = x  # [5 , 11, 13, 12, 6]


my_list = [12, 11, 13, 5, 6]
selection_sort(my_list)
print("Sorted array:", my_list)


# * merge sort with recursion
def merge_sort(arr):
    if len(arr) > 1:  # [12], [11], [13], [5], [6] [7]
        mid = len(arr) / 2

        if len(arr) % 2 != 0:
            mid = int(mid + 0.5)
        else:
            mid = int(mid)

        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array is:", arr)
