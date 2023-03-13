import random
import time
import sys

class recursion_depth:
    def __init__(self, limit):
        self.limit = limit
        self.default_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.default_limit)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def selection_sort(arr):
    for i in range(len(arr)):
        key = i
        for j in range(i+1, len(arr)):
            if arr[key] > arr[j]:
                key = j
        arr[i], arr[key] = arr[key], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot_value = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def counting_sort(arr): #only for positive numbers
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    sorted_arr = [0] * len(arr)
    for val in arr:
        counts[val] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    print(counts)
    for val in arr:
        index = counts[val] - 1
        sorted_arr[index] = val
        counts[val] -= 1
    return sorted_arr

def counting_sort2(arr):
    min_val = min(arr)
    max_val = max(arr)
    shifted_arr = [x - min_val for x in arr]
    k = max_val - min_val + 1
    count = [0] * k
    sorted_arr = [0] * len(arr)
    for x in shifted_arr:
        count[x] += 1
    for i in range(1, k):
        count[i] += count[i - 1]
    for x in shifted_arr:
        sorted_arr[count[x] - 1] = x + min_val
        count[x] -= 1
    return sorted_arr

def countingSortRadix(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = (arr[i] // exp1)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr): #only for positive numbers
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        countingSortRadix(arr, exp)
        exp *= 10
    return arr

def radix_sort2(arr):
    pos_arr = [x for x in arr if x >= 0]
    neg_arr = [-x for x in arr if x < 0]
    pos_max_digits = len(str(abs(max(pos_arr, default=0))))
    neg_max_digits = len(str(abs(max(neg_arr, default=0)) + 1))
    for digit in range(pos_max_digits):
        buckets = [[] for _ in range(10)]
        for x in pos_arr:
            digit_val = x // 10**digit % 10
            buckets[digit_val].append(x)
        pos_arr = []
        for bucket in buckets:
            pos_arr += bucket
    for digit in range(neg_max_digits):
        buckets = [[] for _ in range(10)]
        for x in neg_arr:
            digit_val = x // 10**digit % 10
            buckets[digit_val].append(x)
        neg_arr = []
        for bucket in buckets:
            neg_arr += bucket
    neg_arr = [-x for x in neg_arr[::-1]]
    return neg_arr + pos_arr

def bucket_sort(arr):#only for positive numbers
    arr_min = min(arr)
    arr_max = max(arr)
    bucket_range = arr_max - arr_min
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]
    for x in arr:
        bucket_index = int((x - arr_min) / bucket_range * (num_buckets - 1))
        buckets[bucket_index].append(x)
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])
    sorted_arr = [x for bucket in buckets for x in bucket]
    return sorted_arr

    def bucket_sort(arr):
        arr_min = min(arr)
        arr_max = max(arr)
        bucket_range = arr_max - arr_min
        num_buckets = len(arr)
        buckets = [[] for _ in range(num_buckets)]
        for x in arr:
            bucket_index = int((x - arr_min) / bucket_range * (num_buckets - 1))
            buckets[bucket_index].append(x)
        for i in range(num_buckets):
            buckets[i] = sorted(buckets[i])
        sorted_arr = [x for bucket in buckets for x in bucket]
        return sorted_arr

def insertion_sort2(arr, reverse=False):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and (arr[j] < key if not reverse else arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort2(arr):
    min_val = min(arr)
    max_val = max(arr)
    pos_buckets = [[] for _ in range(max_val+1)]
    neg_buckets = [[] for _ in range(abs(min_val)+1)]
    for x in arr:
        if x >= 0:
            pos_buckets[x].append(x)
        else:
            neg_buckets[abs(x)].append(x)
    for i in range(len(pos_buckets)):
        pos_buckets[i] = insertion_sort2(pos_buckets[i])
    for i in range(len(neg_buckets)-1, -1, -1):
        neg_buckets[i] = insertion_sort2(neg_buckets[i], reverse=True)
    sorted_arr = []
    for bucket in neg_buckets:
        sorted_arr += bucket
    for bucket in pos_buckets:
        sorted_arr += bucket
    return sorted_arr

def generate_data(data_type, size):
    if data_type == "random":
        return [random.randint(-10000, 10000) for _ in range(size)]
    elif data_type == "nearly_sorted":
        arr = [i for i in range(size)]
        for i in range(10):
            j = random.randint(0, size-1)
            k = random.randint(0, size-1)
            arr[j], arr[k] = arr[k], arr[j]
        return arr
    elif data_type == "reversed":
        return [i for i in range(size, 0, -1)]
    elif data_type == "few_unique":
        return [random.randint(0, size//10) for _ in range(size)]
    else:
        raise ValueError("Invalid data type")

def time_algorithms(algorithms, data_types, sizes):
    for data_type in data_types:
        print( )
        print(f"Data type: {data_type}")
        print( )
        for size in sizes:
            data = generate_data(data_type, size)
            for algorithm in algorithms:
                print(f"Algorithm: {algorithm.__name__}")
                print()
                start_time = time.monotonic_ns()
                with recursion_depth(2000):
                    algorithm(data) #algorithm(data,0,len(data)-1) -> for quick_sort
                end_time = time.monotonic_ns()
                execution_time_ns = end_time - start_time
                execution_time_us = execution_time_ns / 1000
                print(f"Size: {size}, Execution time: {execution_time_us:.6f} Micro")
                print( )


algorithms = [bubble_sort,insertion_sort,selection_sort,merge_sort,heap_sort,counting_sort2,radix_sort2,bucket_sort2]
#quick_sort was tested on the same lists but alone because it requires 3 parameters
data_types = ["random","nearly_sorted","reversed","few_unique" ]
sizes = [10,50,100,500,1000,10000,50000,100000]
#Quick_sort stops at 1000 or 10000 (max 2000-only with recursion_depth) because it reaches
#the maximum recursion depth while calling a Python object
time_algorithms(algorithms, data_types, sizes)