import time

def PARENT(i): # O(1)
    return (i - 1) // 2

def LEFT(i): # O(1)
    return 2 * i + 1

def RIGHT(i): # O(1)
    return 2 * i + 2

def MIN_HEAPIFY(H, i, heap_size): # O(log n)
    l = LEFT(i); r = RIGHT(i); smallest = i
    if l < heap_size and H[l][0] < H[smallest][0]: smallest = l
    if r < heap_size and H[r][0] < H[smallest][0]: smallest = r
    if smallest != i:
        H[i], H[smallest] = H[smallest], H[i]
        MIN_HEAPIFY(H, smallest, heap_size)

def MIN_HEAP_INSERT(H, key): # O(log n)
    H.append(key)
    i = len(H) - 1
    while i > 0 and H[PARENT(i)][0] > H[i][0]:
        H[i], H[PARENT(i)] = H[PARENT(i)], H[i]
        i = PARENT(i)

def HEAP_EXTRACT_MIN(H, heap_size): # O(log n)
    if heap_size == 0:
        return None, 0
    min_elem = H[0]
    H[0] = H[heap_size - 1]
    H.pop()
    heap_size -= 1
    if heap_size > 0:
        MIN_HEAPIFY(H, 0, heap_size)
    return min_elem, heap_size

def MERGE_M_SORTED_PIECES(A, m): # O(n log m)
    n = len(A)
    if n == 0 or m <= 1:
        return list(A) 

    piece_size = n // m
    pieces = []
    for i in range(m):
        start = i * piece_size
        if i < (m-1):
            end = start + piece_size
        else:
            end = n
        pieces.append(A[start:end])  

    heap = []
    for piece_idx, piece in enumerate(pieces):
        if piece:  
            MIN_HEAP_INSERT(heap, (piece[0], piece_idx, 0))
    heap_size = len(heap)

    merged = []
    while heap_size > 0:
        smallest, heap_size = HEAP_EXTRACT_MIN(heap, heap_size)
        if smallest is None:
            break
        value, piece_idx, idx_in_piece = smallest
        merged.append(value)

        next_idx = idx_in_piece + 1
        if next_idx < len(pieces[piece_idx]):
            MIN_HEAP_INSERT(heap, (pieces[piece_idx][next_idx], piece_idx, next_idx))
            heap_size += 1

    return merged


if __name__ == "__main__":
    filename = input("Enter the filename: ")
    m = int(input("Enter (M) the number of pieces: "))

    with open(filename, 'r') as f:
        A = [int(line.strip()) for line in f]

    start = time.time()
    sorted_A = MERGE_M_SORTED_PIECES(A, m)
    end = time.time()

    print(f"Sorting took {end - start:.4f} seconds")
    print(f"sorted?: {(sorted_A == sorted(A))}")

