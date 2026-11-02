# Python Lab 4

This folder contains the Python programs completed for Lab 4.

---

## 1. Star Pattern

### Aim

To write a Python program that takes a positive integer `n` from the user and prints a star pattern using nested loops.

### Logic

The program takes the number of rows from the user and uses nested loops to print an increasing number of stars in each row.
The inner loop controls the number of stars, while the outer loop controls the rows.

### Sample Input / Output

#### Test 1

Input:

    Enter the number of rows: 5

Output:

    *
    **
    ***
    ****
    *****

#### Test 2

Input:

    Enter the number of rows: 3

Output:

    *
    **
    ***

### Input Validation

The program accepts only positive integers. Zero, negative numbers, and invalid inputs are rejected.

---

## 2. Matrix Operations

### Aim

To input a 3 × 3 matrix and perform different matrix operations using Python lists and loops without using NumPy.

### Operations Performed

1. Display the matrix in proper row-and-column form.
2. Calculate and display the sum of all elements.
3. Calculate and display the sum of the main diagonal elements.
4. Find and display the largest and smallest elements.
5. Display the transpose of the matrix.

### Logic

The matrix is stored as a list of lists, with each inner list representing one row.
Nested loops are used to traverse the matrix and perform calculations such as summation, finding the largest and smallest values, and constructing the transpose.

### Sample Input / Output

#### Test 1

Input:

    1
    2
    3
    4
    5
    6
    7
    8
    9

Output:

    Original Matrix:
    1 2 3
    4 5 6
    7 8 9

    Sum of all elements: 45
    Sum of main diagonal elements: 15
    Largest element: 9
    Smallest element: 1

    Transpose of the Matrix:
    1 4 7
    2 5 8
    3 6 9

#### Test 2

Input:

    9
    2
    5
    1
    8
    3
    4
    6
    7

Output:

    Original Matrix:
    9 2 5
    1 8 3
    4 6 7

    Sum of all elements: 45
    Sum of main diagonal elements: 24
    Largest element: 9
    Smallest element: 1

    Transpose of the Matrix:
    9 1 4
    2 8 6
    5 3 7

### Requirement

The program uses Python lists and loops only. NumPy is not used.

---

## Concepts Used

- Python lists
- Nested loops
- Functions
- User input
- Input validation
- Matrix traversal
- Main diagonal
- Transpose of a matrix
- Finding maximum and minimum values

---

## Programs Included

1. `star_pattern.py`
2. `matrix_operations.py`