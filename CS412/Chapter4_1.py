import time
import random


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


# * linear search vs binary search

# T(n) = O(n)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


# T(n) = O(log n)
def binary_search(arr, target, low, high):

    if (low > high):
        return -1

    mid = (low + high) // 2

    if (arr[mid] == target):
        return mid

    elif (arr[mid] < target):
        return binary_search(arr, target, mid+1, high)

    elif (arr[mid] > target):
        return binary_search(arr, target, low, mid-1)


def main():
    # arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    # target = 13

    # print()
    # print(arr)
    # print()
    # print("the targe location is: ", binary_search(arr, target, 0, len(arr)-1))
    # print(f'at the {binary_search(arr, target, 0, len(arr)-1)+1}th character')
    # print()

    input_sequence = [i for i in range(100000000)]
    target = (random.randint(0, 100000000))

    start_time = time.time()
    linear_search_result = linear_search(input_sequence, target)
    end_time = time.time()

    linear_search_time = end_time - start_time
    print("Linear search time: ", linear_search_time)

    start_time = time.time()
    binary_search_result = binary_search(
        input_sequence, target, 0, len(input_sequence)-1)
    end_time = time.time()

    binary_search_time = end_time - start_time
    print("Binary search time: ", binary_search_time)

    print("Linear search result: ", linear_search_result)
    print("Binary search result: ", binary_search_result)


if __name__ == "__main__":
    main()


# * linear search in using recursion

# T(n) = O(n)
def linear_search(arr, target, index):
    if index >= len(arr):  # base case
        return -1

    if arr[index] == target:
        return index

    return linear_search(arr, target, index+1)


arr = [1, 3, 5, 7, 9, 11, 13, 56, 15, 17]
target = 56

print()
print(arr)
print(linear_search(arr, target, 0))
