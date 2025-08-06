import random
import time

def binarySearch( arr, key, srtdLen ) -> int:
    low = 0
    high = srtdLen - 1
    while ( low <= high ):
        mid = ( low + high ) // 2
        if ( key == arr[mid] ):
            return mid
        if ( key < arr[mid] ):
            high = mid - 1
        else :
            low = mid + 1
    return low

def OptInsertionSort(arr) :
    # sorting initial two elements
    if ( len(arr) >= 2 ):
        if ( arr[0] > arr[1] ):
            arr[0], arr[1] = arr[1] , arr[0] #swap
        srtdLen = 2 # length of sorted array
    else :
        return arr
    # sorting, shifting
    while (srtdLen < len(arr)):
        # checking if we have 2 elements (even array case)
        if srtdLen + 1 < len(arr) :
            elements = [arr[srtdLen], arr[srtdLen+1]]
            elements.sort()
            arr = arr[:srtdLen]+arr[srtdLen+2:]
            indexLarge = binarySearch( arr, elements[1], srtdLen )
            arr = arr[:indexLarge] + [elements[1]] + arr[indexLarge:]
            srtdLen+=1
            indexSmall = binarySearch( arr, elements[0], indexLarge )
            arr = arr[:indexSmall] + [elements[0]] + arr[indexSmall:]
            srtdLen+=1
        else: # if only 1 element (odd array case)
            element = arr[srtdLen]
            arr = arr[:srtdLen]+arr[srtdLen+1:]
            indexEle = binarySearch( arr, element, srtdLen )
            arr = arr[:indexEle] + [element] + arr[indexEle:]
            srtdLen+=1
    return arr

def main():
    numTest=int(input("Enter the Number of test cases: "))
    while(numTest):        
        size = int(input("Enter the size of array: "))
        arr = []
        for i in range(size):
            arr.append(random.random())
        start = time.time()
        arr = OptInsertionSort(arr)
        end = time.time()
        print(f"Time taken: {end - start}")
        numTest-=1

main()