#!/usr/bin/env python3
# Created By: Kaylee Ralejoe
# Date: 26,09,2026
# The program calculates pizza cost.
# It asks the user for the diameter of the pizza.
# It calculates and displays the tottal cost
# of the pizza with tax

import constants_pizza_cost


def main():
    # user input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # calculation process
    subtotal = (
        constants_pizza_cost.LABOUR_COST
        + constants_pizza_cost.RENTAL_COST
        + constants_pizza_cost.INGRI_COST * diameter
    )
    total = subtotal * (1 + constants_pizza_cost.HST)

    # output
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
