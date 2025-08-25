# **Algorithm-Design-with-Python-Lab**
This repository contains implementations as part of the **Algorithm Design Lab**.

## **Labs**
1. **Optimization of Insertion Sort**
   - using binary search instead of linear search
   - shifting two elements instead of one
       - two elements were shifted by first shifting the max element to its place then searching the array till max element and then placing the min element
2. **Optimization of Quick Sort**
   - taking a pivot which is median of three random elements chosen from the array, this avoids the worst case time complexity
   - for smaller values of n (size of array), insertion sort was used.
   - the size of n was mathematically and manually calculated.
### 3. Heap-based Merge of *m* Sorted Pieces  
- Implemented a **min-heap** to merge `m` sorted subarrays efficiently.  
- Each subarray contributes its smallest unmerged element into the heap.  
- Time complexity: **O(n log m)**.  

---

### 4. Selection using Median of Medians  
- Implemented the **SELECT** algorithm to find the *k-th* smallest element:  
  - Pivot chosen using **Median of Medians** for worst-case `O(n)` guarantee.  
  - Uses optimized insertion sort for small groups.  
- Application: finding IDs near the **Income Median**.  

---

### 5. Equity Calculation in Binary Search Tree  
- Constructed a **Binary Search Tree** from input data.  
- Defined **Equity of a node** as:  

  \[
  \text{Equity} = 1 - \Bigg| \frac{\text{avg}(L)}{\max(L)} - \frac{\text{avg}(R)}{\max(R)} \Bigg|
  \]

  where `L` and `R` are the left and right subtrees.  
- Computed equity for each non-leaf node and identified nodes with **maximum equity**.  

---
