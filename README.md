# Quicksort-Algorithm
Quicksort Algorithm: Deterministic vs Randomized

This repository contains an implementation of the Quicksort algorithm in Python, including both the deterministic and randomized versions. The assignment explores the theoretical foundations of Quicksort, its performance analysis, and the impact of randomization on its efficiency. The main objective of this project was to implement both versions of Quicksort, analyze their time and space complexity, and empirically compare their performance on different input distributions.

Files

quicksort.py: Contains the deterministic and randomized Quicksort implementations.

test_performance.py: Contains code to empirically test the performance of both algorithms with different input sizes and distributions (random, sorted, reverse-sorted).

README.md: This file, which explains the project structure, usage, and results.

quicksort_report.pdf (Optional): A detailed report on the implementation and analysis of Quicksort.

Overview
Quicksort Algorithm

The Quicksort algorithm is a divide-and-conquer sorting algorithm that works by selecting a pivot element, partitioning the array around the pivot, and recursively sorting the subarrays. Its average-case time complexity is O(n log n), but the worst-case time complexity can degrade to O(n²) if the pivot selection is poor.

Two Versions of Quicksort Implemented:

Deterministic Quicksort:

The pivot is chosen as the last element in the array.

A median-of-three pivot selection strategy is used to improve performance on sorted or reverse-sorted arrays.

Randomized Quicksort:

The pivot is chosen randomly to avoid worst-case performance.

This helps in ensuring better partitioning by reducing the likelihood of encountering the worst-case scenario.

How to Run

Clone the repository:

git clone https://github.com/yourusername/quicksort-assignment.git
cd quicksort-assignment


Ensure Python is installed (Python 3.3 or above).

Run the performance tests:

The file test_performance.py will run the performance tests for both Deterministic Quicksort and Randomized Quicksort on different array sizes and distributions.

To run the tests, execute the following command in your terminal:

python test_performance.py


Expected Output:
The script will output the execution times for both Deterministic Quicksort and Randomized Quicksort for array sizes of 100, 1000, 5000, and 10000, as well as for sorted and reverse-sorted arrays. Example output:

Array size: 100
Deterministic Quicksort time: 0.00010 seconds
Randomized Quicksort time: 0.00012 seconds
Array size: 1000
Deterministic Quicksort time: 0.00105 seconds
Randomized Quicksort time: 0.00123 seconds
Sorted Array (size 100)
Deterministic Quicksort time: 0.00015 seconds
Randomized Quicksort time: 0.00010 seconds

Time and Space Complexity
Time Complexity:

Best case: 
O(nlogn) — This occurs when the pivot divides the array into two nearly equal parts.

Average case: 
O(nlogn) — The pivot is typically selected in a way that divides the array evenly.

Worst case: 
𝑂(𝑛^2) — This occurs when the pivot is consistently poorly chosen, resulting in highly unbalanced partitions.

Space Complexity:

Best case: 
O(logn) — The space complexity is dominated by the depth of the recursion stack.

Worst case: 
O(n) — In the worst case, where the array is divided into unbalanced partitions, the recursion depth may reach 
𝑛
Optimization:

The Deterministic Quicksort uses the median-of-three pivot strategy, which reduces the likelihood of worst-case performance when dealing with sorted or reverse-sorted data.

Empirical Results

Both Quicksort versions were tested on arrays of various sizes (100, 1000, 5000, 10000) and input distributions (random, sorted, reverse-sorted). The key results are:

On Random Arrays:

Both Deterministic Quicksort and Randomized Quicksort performed similarly, with minimal difference in execution times.

On Sorted Arrays:

Randomized Quicksort generally outperformed Deterministic Quicksort because the random pivot selection avoids the worst-case scenario for sorted data.

On Reverse-Sorted Arrays:

Deterministic Quicksort with the median-of-three pivot performed better than Randomized Quicksort in most cases. The Randomized Quicksort showed slightly more overhead due to the random pivot selection.

Example Output:
Array size: 100
Deterministic Quicksort time: 0.00012 seconds
Randomized Quicksort time: 0.00009 seconds
Array size: 1000
Deterministic Quicksort time: 0.00105 seconds
Randomized Quicksort time: 0.00123 seconds
Sorted Array (size 100)
Deterministic Quicksort time: 0.00015 seconds
Randomized Quicksort time: 0.00010 seconds
Reverse Sorted Array (size 100)
Deterministic Quicksort time: 0.00018 seconds
Randomized Quicksort time: 0.00013 seconds

Conclusion

Both Deterministic Quicksort and Randomized Quicksort are efficient sorting algorithms with average-case time complexity of O(nlogn). The Randomized Quicksort is more robust in handling worst-case scenarios, making it more suitable for unpredictable data distributions. On the other hand, the Deterministic Quicksort, optimized with the median-of-three pivot strategy, works efficiently on sorted and reverse-sorted data and performs similarly in most cases.
