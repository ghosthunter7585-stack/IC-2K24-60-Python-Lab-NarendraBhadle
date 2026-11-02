# Python Lab 3

This folder contains the Python programs completed for Lab 3.

---

## 1. Hollow Diamond

### Aim

To write a Python program that takes a positive odd number `n` from the user and prints a hollow diamond pattern.

### Logic

The program divides the diamond into an increasing section and a decreasing section using loops.
For each row, it calculates the spaces before the stars and the spaces between the two stars to create the hollow shape.

### Sample Input / Output

#### Test 1

Input:

    Enter a positive odd number: 7

Output:

          *
        *   *
      *       *
    *           *
      *       *
        *   *
          *

#### Test 2

Input:

    Enter a positive odd number: 5

Output:

        *
      *   *
    *       *
      *   *
        *

### Input Validation

The program accepts only positive odd numbers. Negative numbers, zero, even numbers, and invalid inputs are rejected.

---

## 2. Butterfly Pattern

### Aim

To write a Python program that takes the number of rows `n` from the user and prints a butterfly star pattern.

### Logic

The pattern is divided into an increasing section and a decreasing section.
Nested loops are used to calculate the number of stars on both sides and the spaces between them for each row.

### Sample Input / Output

#### Test 1

Input:

    Enter the number of rows: 5

Output:

    *        *
    **      **
    ***    ***
    ****  ****
    **********
    ****  ****
    ***    ***
    **      **
    *        *

#### Test 2

Input:

    Enter the number of rows: 3

Output:

    *    *
    **  **
    ******
    **  **
    *    *

### Input Validation

The program accepts only positive integer values for the number of rows.

---

## Concepts Used

- Python functions
- User input
- Input validation
- Nested loops
- Conditional statements
- Pattern printing
- `for` loops
- Spaces and stars for pattern formation

---

## Programs Included

1. `hollow_diamond.py`
2. `butterfly.py`