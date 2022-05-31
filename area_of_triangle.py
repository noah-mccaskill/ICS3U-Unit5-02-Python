#!/usr/bin/env python3

# Created by Noah McCaskill
# Created May 2022
# This program calculates area of a triangle using parameters


def triangle_area(base, height):
    # this function calculates area of a triangle

    # process
    area = (base * height) / 2

    # output
    print("The area of your triangle is {0} cm².".format(area))


def main():
    # this function gets input, calls a function, gives output

    # input
    base_string = input("Enter the base of your triangle (cm): ")
    height_string = input("Enter the height of your triangle (cm): ")

    try:
        base_from_user = float(base_string)
        height_from_user = float(height_string)
        # call function
        triangle_area(base_from_user, height_from_user)

    except Exception:
        # output
        print("\nYour values are invalid. Please Re-Run.")

    print("\nDone.")


if __name__ == "__main__":
    main()
