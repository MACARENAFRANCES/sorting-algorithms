## Sorting Algorithms Analysis

### Insertion Sort Results:
1. **List 1**: 
   - Sorted List: [3, 4, 11, 12, 16, 32, 34, 59, 63, 97]
   - Operations: 31

2. **List 2**: 
   - Sorted List: [1, 3, 4, 5, 6, 9, 12, 14, 18, 19, 21, 24, 25, 27, 28, 29, 31, 32, 37, 44, 46, 47, 49, 51, 52, 54, 55, 57, 59, 60, 62, 63, 64, 66, 67, 73, 75, 77, 78, 81, 84, 85, 86, 87, 90, 94, 95, 96, 99, 100]
   - Operations: 717

3. **List 3**: 
   - Sorted List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
   - Operations: 2540

### Quicksort Results:
1. **List 1**: 
   - Sorted List: [3, 4, 11, 12, 16, 32, 34, 59, 63, 97]
   - Operations: 40

2. **List 2**: 
   - Sorted List: [1, 3, 4, 5, 6, 9, 12, 14, 18, 19, 21, 24, 25, 27, 28, 29, 31, 32, 37, 44, 46, 47, 49, 51, 52, 54, 55, 57, 59, 60, 62, 63, 64, 66, 67, 73, 75, 77, 78, 81, 84, 85, 86, 87, 90, 94, 95, 96, 99, 100]
   - Operations: 456

3. **List 3**: 
   - Sorted List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
   - Operations: 921

### Computational Cost Analysis:

#### Insertion Sort:
- **Time Complexity**: 
  - Best Case: \( O(n) \)
  - Worst Case: \( O(n^2) \)
  - Average Case: \( O(n^2) \)

- **Space Complexity**: \( O(1) \) (in-place sorting)

#### Quicksort:
- **Time Complexity**: 
  - Best Case: \( O(n \log n) \)
  - Worst Case: \( O(n^2) \)
  - Average Case: \( O(n \log n) \)

- **Space Complexity**: 
  - Worst Case: \( O(n) \) (due to recursion stack, can be \( O(\log n) \) with optimizations)

### Analysis:
- **Insertion Sort** is efficient for small lists or nearly sorted data but becomes impractical for large datasets due to its quadratic time complexity in the worst case.
- **Quicksort** performs well across various scenarios with its average \( O(n \log n) \) time complexity, making it suitable for sorting large datasets efficiently. However, it may degrade to \( O(n^2) \) in rare cases.
