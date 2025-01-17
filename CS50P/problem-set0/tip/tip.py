#!/usr/bin/env python3

"""
File: tip.py
Description:
    A tip calculator. Receiving dollars costed and percent of tip.
    return tips leaved.

"""

def main():
    dollars = dollars_to_float(input("How much was the meal?"))
    percent = percent_to_float(input("What percentage would you like to tip"))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # TODO
    dollars = float(d[1:])
    return dollars

def percent_to_float(p):
    # TODO
    percent = float(p[:-1]) * 0.01
    return percent


if __name__ == '__main__':
    main()
