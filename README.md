# **Algorithm-Design-with-Python-Lab**

This repository contains implementations developed as part of the **Algorithm Design Lab**.  

## **Labs**  

### 1. Optimization of Insertion Sort  
- Used **binary search** instead of linear search to find the insertion point.  
- Optimized shifting by handling **two elements at a time**:  
  - First shift the maximum element to its correct position.  
  - Then search the subarray (till max element) to place the minimum element.  

---

### 2. Optimization of Quick Sort  
- Chose pivot as the **median of three random elements** from the array → reduces chance of worst-case `O(n²)`.  
- For small array sizes `n`, the algorithm switches to **Insertion Sort** for efficiency.  
- The threshold value of `n` was **calculated mathematically and verified manually**.  

---

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
