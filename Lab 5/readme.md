🔢 Concentric Number Square Pattern

A Python program that prints a square pattern of concentric numbers.





📌 About the Project

This program takes a positive integer from the user and prints a
concentric number square.

The entered number appears on the outer border. Each layer moving
towards the centre decreases by one.

For an input of 5, the program prints a square with 9 rows and 9
columns.

✨ Sample Output

Input

Enter the number: 5

Output

5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5

💻 Source Code

# This program prints a concentric number square pattern.

def get_positive_integer(prompt):
    """Take and validate a positive integer from the user."""

    while True:
        try:
            number = int(input(prompt))

            if number <= 0:
                print("Please enter a positive integer.")
            else:
                return number

        except ValueError:
            print("Invalid input. Please enter an integer.")


n = get_positive_integer("Enter the number: ")

size = 2 * n - 1

for row in range(size):
    for column in range(size):

        distance_from_edge = min(
            row,
            column,
            size - 1 - row,
            size - 1 - column
        )

        value = n - distance_from_edge

        print(value, end=" ")

    print()

🧠 How It Works

The program asks the user to enter a number.

The get_positive_integer() function validates the input.

A non-integer input displays an error message.

Zero or a negative number is rejected.

The square's dimensions are calculated:

size = 2 * n - 1

Two nested for loops visit each position in the square.

min() finds the position's minimum distance from the four edges.

The value for that position is calculated:

value = n - distance_from_edge

📐 Pattern Logic

For an input value n:

Property            Formula / Result

Number of rows      2 * n - 1
Number of columns   2 * n - 1
Outer layer         n
Centre value        1

Each inner layer decreases by one.

📚 Python Concepts Used

Functions

User input with input()

while loop

Nested for loops

if-else conditions

Exception handling (try-except)

min() function

▶️ How to Run

Requirement: Python 3.x

Save the program in a file named main.py.

Open a terminal in the folder containing the file.

Run:

python main.py

Enter a positive integer when prompted.

If your Python file has a different name, replace main.py with that
filename.

⭐ If you find this project useful, give the repository a star!

Made with 🐍 Python