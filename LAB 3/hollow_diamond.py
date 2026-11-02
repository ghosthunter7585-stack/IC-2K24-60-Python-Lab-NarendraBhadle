# This program prints a hollow diamond pattern.
# The input must be a positive odd number.


def get_odd_number():
    """Take and validate a positive odd number from the user."""

    while True:
        try:
            n = int(input("Enter a positive odd number: "))

            if n <= 0:
                print("Please enter a positive number.")

            elif n % 2 == 0:
                print("Please enter an odd number.")

            else:
                return n

        except ValueError:
            print("Invalid input. Please enter an integer.")


n = get_odd_number()

middle = n // 2

for row in range(n):
    if row <= middle:
        stars = row + 1
        spaces_before = middle - row
    else:
        stars = n - row
        spaces_before = row - middle

    # Print spaces before the first star.
    for _ in range(spaces_before):
        print(" ", end=" ")

    # First star.
    print("*", end="")

    # Print the inside space between the two stars.
    if stars > 1:
        for _ in range(2 * stars - 3):
            print(" ", end=" ")

        # Second star.
        print("*", end="")

    print()