## Sorting Algorithms Analysis

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
