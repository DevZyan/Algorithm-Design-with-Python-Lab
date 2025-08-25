import time
import random

# COPYING BINARY SEARCH AND OPTINSERTIONSORT FROM ASSIGNMENT 1

def binarySearch( arr, key, srtdLen ) -> int:
    low = 0
    high = srtdLen - 1
    while ( low <= high ):
        mid = ( low + high ) // 2
        # Comparing Income
        if ( key == arr[mid][1] ):
            return mid
        if ( key < arr[mid][1] ):
            high = mid - 1
        else :
            low = mid + 1
    return low

def OptInsertionSort(arr,li,ri) :
    size = ri - li + 1
    if ( size >= 2 ):
        if ( arr[0][1] > arr[1][1] ):
            arr[0], arr[1] = arr[1] , arr[0]
        srtdLen = 2
    else :
        return arr
    # sorting, shifting
    while (srtdLen < size):
        if srtdLen + 1 < size :
            elements = [arr[srtdLen][1], arr[srtdLen+1][1]]
            element_items = [arr[srtdLen], arr[srtdLen+1]]
            element_items.sort(key=lambda x: x[1]) # Sorting Incomes
            arr = arr[:srtdLen] + arr[srtdLen+2:]
            indexLarge = binarySearch(arr, element_items[1][1], srtdLen)
            arr = arr[:indexLarge] + [element_items[1]] + arr[indexLarge:]
            srtdLen += 1
            indexSmall = binarySearch(arr, element_items[0][1], indexLarge)
            arr = arr[:indexSmall] + [element_items[0]] + arr[indexSmall:]
            srtdLen += 1
        else:
            element_item = arr[srtdLen]
            arr = arr[:srtdLen] + arr[srtdLen+1:]
            indexEle = binarySearch(arr, element_item[1], srtdLen)
            arr = arr[:indexEle] + [element_item] + arr[indexEle:]
            srtdLen += 1
    return arr

# SELECT ALGO FROM THE BOOK

def PARTITION(A, p, r):
    x = A[r][1] # income
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def RANDOMIZED_PARTITION(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return PARTITION(A, p, r)

def MEDIANS(A):
    n = len(A)
    if n <= 5:
        # Insertion Sort
        srtdA = OptInsertionSort(A, 0, n - 1)
        return srtdA[n // 2][1]
    #A into groups of 5
    grps = [A[j:j + 5] for j in range(0, n, 5)]
    # Find median of each group
    medians = []
    for grp in grps:
        srtdgrp = OptInsertionSort(grp, 0, len(grp) - 1)
        medians.append(srtdgrp[len(grp) // 2])
    # Recursion Call to get medians of medians
    return MEDIANS(medians)


def SELECT(A, i):
    n = len(A)
    if n <= 5:
        sorted_A = OptInsertionSort(A, 0, n - 1)
        return sorted_A[i-1]
    val_pivot = MEDIANS(A)
    idx_pivot = -1
    for idx, item in enumerate(A):
        if item[1] == val_pivot:
            idx_pivot = idx
            break
    A[idx_pivot], A[n-1] = A[n-1], A[idx_pivot]
    q = RANDOMIZED_PARTITION(A, 0, n - 1)
    k = q + 1

    if i == k:
        return A[q]
    elif i < k:
        return SELECT(A[:q].copy(), i)
    else:
        return SELECT(A[q+1:].copy(), i - k)

filename = input('Enter the filename: ')
k = int(input('Enter the value of k: '))
data0 = []
with open(filename,'r') as file:
  for line in file:
    row = [float(num) for num in line.strip().split()]
    data0.append(row)
data1 = data0.copy()
print("k-ID's near IncomeMedian:")
start = time.time()
for i in range(-1,-(k+1)//2,-1):
  print(SELECT(data1,(len(data1)//2) + (i+1))[0])
for i in range((k+1)//2):
  print(SELECT(data1,(len(data1)//2) + (i+1))[0])
end = time.time()
print(f"Time taken: {end - start}")
