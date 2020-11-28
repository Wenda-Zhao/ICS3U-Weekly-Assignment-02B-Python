#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Nov 2020
# This program calculates the length of triangular prism base side
#     where the user gets to enter the length, surface area and height in mm

import math


def main():
    # main function
    print("We will be calculating the length of triangular prism base side. ")
    # input
    length_b = int(input("Enter the length_b (mm): "))
    length_c = int(input("Enter the length_c (mm): "))
    height = int(input("Enter the height (mm): "))
    surface_area = int(input("Enter the surface_area (mm²): "))
    # process
    length_a = surface_area/height - length_c - length_b
    # output
    print("Area is {} mm²".format(length_a))


if __name__ == "__main__":
    main()
