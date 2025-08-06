from random import random,randint
import time
def insertionSort(arr, li, ri):
    for i in range(li + 1, ri + 1):
        target = arr[i]
        j = i - 1
        while j >= li and arr[j] > target:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = target

def pivotSelection(arr,li,ri):
    ind = [randint(li, ri) for _ in range(3)]
    return sorted([arr[ind[0]], arr[ind[1]], arr[ind[2]]])[1]

def partition(arr, li, ri):
    pivot =  pivotSelection(arr,li,ri)
    i = li - 1
    j = ri + 1
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j :
            return j
        arr[i],arr[j] = arr[j], arr[i]

def optQuickSort(arr, li ,ri,threshold):  
    if (li >= ri):
            return
    # THRESHOLD - MATHEMATICALLY 1305
    # THRESHOLD - MANUALLY 100
    if (ri - li+1) < threshold:
        insertionSort(arr,li,ri)
    else:
        p = partition(arr,li,ri)
        optQuickSort(arr,li,p,threshold)
        optQuickSort(arr,p+1,ri,threshold)

def main():
    n = int(input("Enter number of intergers in arr:"))
    arr = [random() for _ in range(n)]
    # MATHEMATICAL THRESHOLD
    start = time.time()
    optQuickSort(arr,0,len(arr)-1,1305)
    end = time.time()
    print("Time taken with threshold 1305: ", end-start)

    # MANUAL THRESHOLD
    time100 = []
    for i in range(100):       
        start = time.time()
        optQuickSort(arr,0,len(arr)-1,100)
        end = time.time()
        time_taken = end - start
        time100.append(time_taken)
        #print("Time taken with threshold 100:", end-start)
    print("Minimum time for threshold 100:", min(time100))

    # BELOW IS THE CODE I USED TO CHECK THE OPTIMAL THRESHOLD
    # for i in range(2,101):
    #     time_thres = []
    #     for j in range(100):       
    #         start = time.time()
    #         optQuickSort(arr,0,len(arr)-1,i)
    #         end = time.time()
    #         time_taken = end - start
    #         time_thres.append(time_taken)
    #     print("Minimum time for threshold",i,":", min(time_thres))

main()
