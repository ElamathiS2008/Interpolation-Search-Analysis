#Interpolation Search Analysis

Objective

To implement the Interpolation Search algorithm in Python and compare its performance with Binary Search using execution time and number of comparisons.

Project Description

This project demonstrates the working of the Interpolation Search algorithm on sorted arrays. It also compares the performance of Interpolation Search and Binary Search for different input sizes.

Interpolation Search estimates the probable position of the target element using an interpolation formula, making it faster than Binary Search for uniformly distributed sorted data.

Features

- Implementation of Interpolation Search
- Implementation of Binary Search
- Comparison of execution time
- Comparison of number of comparisons
- Performance analysis on different array sizes
- User input for custom search operations

Algorithms Used

Interpolation Search

1. Initialize low and high indices.
2. Estimate the probable position using the interpolation formula.
3. Compare the target with the estimated position.
4. If found, return the index.
5. Otherwise, update low or high and repeat.
6. Return -1 if the element is not present.

Binary Search

1. Find the middle element.
2. Compare the target with the middle element.
3. Search the left or right half accordingly.
4. Repeat until the element is found or the search space becomes empty.

Time Complexity

Algorithm| Best Case| Average Case| Worst Case
Interpolation Search| O(1)| O(log log n)| O(n)
Binary Search| O(1)| O(log n)| O(log n)

Space Complexity

- Interpolation Search: O(1)
- Binary Search: O(1)

Requirements

- Python 3.x

How to Run

1. Open Terminal or Command Prompt.
2. Navigate to the project folder.
3. Execute:

python task1.py

Sample Input

Enter sorted array elements separated by space:
10 20 30 40 50 60 70

Enter target element:
40

Sample Output

Array: [10, 20, 30, 40, 50, 60, 70]
Searching for: 40
Found at index: 3, Comparisons: 1

Performance Analysis

The program automatically generates arrays of different sizes and compares:

- Execution Time (milliseconds)
- Number of Comparisons

for both Interpolation Search and Binary Search.

##Author

Elamathi S
