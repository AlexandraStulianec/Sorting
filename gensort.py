import random
import csv
import time


def BubbleSort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                k = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = k


def SelectionSort(arr, n):
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                k = arr[min_index]
                arr[min_index] = arr[i]
                arr[i] = k


def InsertionSort(arr, n):
    for i in range(n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


def QuickSort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        left, right = stack.pop()

        if left >= right:
            continue

        pivot = arr[right]
        i = left - 1

        for j in range(left, right):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[right] = arr[right], arr[i + 1]

        stack.append((left, i))
        stack.append((i + 2, right))

    return arr


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def MergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        MergeSort(arr, l, m)
        MergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)


def HeapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)


def CountingSort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    sorted_arr = [0] * len(arr)
    for val in arr:
        counts[val] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    print(counts)
    for val in arr:
        index = counts[val] - 1
        sorted_arr[index] = val
        counts[val] -= 1
    return sorted_arr


def countingSortradix(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def RadixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        countingSortradix(arr, exp)
        exp *= 10


def BucketSort(arr):
    max_ele = max(arr)
    min_ele = min(arr)
    noOfBuckets = min(len(arr), 10)

    rnge = (max_ele - min_ele) / noOfBuckets

    temp = []

    for i in range(noOfBuckets):
        temp.append([])

    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)

        if (diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])

        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])

    # Sort each bucket individually
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()

    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k + 1
    return arr


MINIMUM = 32

def find_minrun(n):
    r = 0
    while n >= MINIMUM:
        r |= n & 1
        n >>= 1
    return n + r

def InsertionSortt(array, left, right):
    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

def TimSort(arr):
    n = len(arr)
    minrun = find_minrun(n)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        InsertionSortt(arr, start, end)

    size = minrun
    while size < n:

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            merge(arr, left, mid, right)

        size = 2 * size



    # INITIAL INPUTS

print("Write a file name (ex: file.csv):")
f_name = input()

print("Number of lists you want to generate:")
run = int(input())

print("List length:")
list_len = int(input())

# FILE

f = open(f_name, 'w', newline='')
writer = csv.writer(f)

header = ["List","BubbleSort","SlectionSort","InsertionSort","QuickSort","MergeSort","HeapSort","CountingSort","RadixSort","BucketSort","Timsort"]
writer.writerow(header)

times = []
output = []
a = []


while run:


    times.clear()
    output.clear()
    a.clear()

    # LIST GENERATION

    # FULL RANGE RANDOM
    for i in range(list_len):
        a.append(i)
    random.shuffle(a)

    # ALMOST SORTED
    for i in range(list_len):
        a.append(i)
    mm = random.choice(a)
    mn = random.choice(a)
    a[mm],a[mn]=a[mn],a[mm]

    # FLAT LISTS
    mm = random.randint(0, 10000)
    mn = mm + random.randint(1,4)
    for i in range(list_len):
        a.append(random.randint(mm, mn))

    # REVERSE SORTED
    for i in range(list_len):
       a.append(list_len-i-1)


    # SORT LISTS

    # I'm working with copies of the generated list so that I can apply different
    # sorting methods on the same list
    # i am using the function time.perf_counter_ns() to get the perfect time in nanoseconds
    # and i converted it to seconds.
    
    b = a.copy()
    t_start = time.perf_counter_ns()
    BubbleSort(b, len(b))
    t_end = time.perf_counter_ns()
    times.append((t_end - t_start) / 1000000000)

    b = a.copy()
    t_start = time.perf_counter_ns()
    SelectionSort(b, len(b))
    t_end = time.perf_counter_ns()
    times.append((t_end - t_start) / 1000000000)

    b = a.copy()
    t_start = time.perf_counter_ns()
    InsertionSort(b, len(b))
    t_end = time.perf_counter_ns()
    times.append((t_end - t_start) / 1000000000)

    # Because of python's recursion depth error I had to do another algorithm for QuickSort
    # bcs it didn't work for more than 1000 elements on certain cases, bcs it it inefficient
    # on those and the recursion it's done multiple times
    
    b = a.copy()
    t_start = time.perf_counter_ns()
    QuickSort(b)
    t_end = time.perf_counter_ns()
    times.append((t_end - t_start) / 1000000000)

    b = a.copy()
    t_start = time.perf_counter_ns()
    MergeSort(a, 0, len(b) - 1)
    t_end = time.perf_counter_ns()
    times.append((t_end - t_start) / 1000000000)

    b = a.copy()
    t_start = time.perf_counter_ns()
    HeapSort(b)
    t_end = time.perf_counter_ns()
    times.append((t_end - t_start) / 1000000000)


    b = a.copy()
    t_start = time.perf_counter_ns()
    CountingSort(b)
    t_end = time.perf_counter_ns()
    times.append((t_end - t_start) / 1000000000)


    b = a.copy()
    t_start = time.perf_counter_ns()
    RadixSort(b)
    t_end = time.perf_counter_ns()
    times.append((t_end - t_start) / 1000000000)


    b = a.copy()
    t_start = time.perf_counter_ns()
    BucketSort(b)
    t_end = time.perf_counter_ns()
    times.append((t_end - t_start) / 1000000000)


    b = a.copy()
    t_start = time.perf_counter_ns()
    TimSort(b)
    t_end = time.perf_counter_ns()
    times.append((t_end - t_start) / 1000000000)

    # WRITE TO FILE

    output.append(list_len)
    for i in range(len(times)):
        output.append(times[i])
    writer.writerow(output)

    run -= 1

f.close()
