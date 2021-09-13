#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program finds the area and the perimeter of a circle with a 15 mm radius.

import math


def main():
    # this function calculates the area and perimeter

    print("If a circle has a radius of: ")
    print("15 mm")
    print(" ")
    print("The area is {} mm².".format(math.pi * 15 ** 2))
    print("The perimeter is {} mm.".format(2 * math.pi * 15))
    print(" ")
    print("Done.")


if __name__ == "__main__":
    main()
