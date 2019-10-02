#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Sept 2019
# This program calculates the surface area of sphere
#     with user input


import math


def main():
    # this function calculates the surface area of sphere

    # input
    radius = int(input("Enter the radius of sphere (m): "))
    print("")

    # process
    surface_area = 4 * math.pi * radius**2

    # output
    print("Surface area of sphere is {}m^2".format(surface_area))

if __name__ == "__main__":
    main()