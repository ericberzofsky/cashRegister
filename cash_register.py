####################################################
# Script to provide answer to interview question simulating a cash register
####################################################
import argparse
import os
import subprocess

def pay_out(amount, bills_available, coins_available):
    ####################################################
    # Check that amount provided is float
    ####################################################
    assert (type(amount) == float)
    ####################################################
    # Check that entered payout amount just has two decimal positions for cents
    ####################################################
    assert (len(str(amount).strip().split(".")[1]) == 2)

    ####################################################
    # Keys of cash_register are the provided denominations
    # multiplied by 100 for easier division. It also allows
    # us to keep track of bills and coins in the same dict
    ####################################################
    cash_register = dict()
    ####################################################
    # Parse bills string provided into dictionary
    # Denomination of bills can only be integers
    ####################################################
    for denomination in bills_available.split(","):
        denomination_to_add = int(denomination.split(":")[0]) * 100
        assert(denomination_to_add not in list(cash_register.keys()))
        ####################################################
        # Only include denomination if we have some
        ####################################################
        if int(denomination.split(":")[1]) > 0:
            cash_register[denomination_to_add] = int(denomination.split(":")[1])

    ####################################################
    # Parse coins string provided into dictionary
    # Denomination of coins should be converted to integers
    # for easier division later
    ####################################################
    for denomination in coins_available.split(","):
        denomination_to_add = int(float(denomination.split(":")[0]) * 100)
        assert(denomination_to_add not in list(cash_register.keys()))
        ####################################################
        # Only include denomination if we have some
        ####################################################
        if int(denomination.split(":")[1]) > 0:
            cash_register[denomination_to_add] = int(denomination.split(":")[1])

    ####################################################
    # Sort the denomination of bills we have in
    # decreasing order and start paying out the bills
    ####################################################
    pay_out_dict = dict()
    amount_to_pay = int(amount * 100)
    sorted_denominations = list(cash_register.keys())
    sorted_denominations.sort(reverse=True)

    ####################################################
    # Pretty print the cash_register
    ####################################################
    print("We currently have the following notes in our cash register:")
    for sorted_denomination in sorted_denominations:
        print("    {0} notes of the ${1:.2f} denomination".format(cash_register[sorted_denomination], float(sorted_denomination/100)))

    for denomination in sorted_denominations:
        if amount_to_pay == 0:
            break
        num_bills_needed = int(amount_to_pay / denomination)
        if num_bills_needed >= 1:
            ####################################################
            # If we have enough bills to ensure minimum payout,
            # do it, otherwise, pay what we have
            ####################################################
            if cash_register[denomination] >= num_bills_needed:
                pay_out_dict[denomination] = num_bills_needed
                cash_register[denomination] = cash_register[denomination] - num_bills_needed
                amount_to_pay = amount_to_pay - (denomination * num_bills_needed)
            else:
                pay_out_dict[denomination] = cash_register[denomination]
                amount_to_pay = amount_to_pay - (denomination * cash_register[denomination])
                cash_register[denomination] = 0

    if amount_to_pay > 0:
        print("We didn't have enough in cash register to payout the amount ${0:.2f}".format(amount))
    else:
        ####################################################
        # Pretty print the payout
        ####################################################
        print("We're able to payout the amount ${0:.2f} in the fewest notes possible by doing:".format(amount))
        for denomination in list(pay_out_dict.keys()):
            print("    {0} notes of the ${1:.2f} denomination".format(pay_out_dict[denomination], float(denomination/100)))

#### Main body starts here #####
try:
    pay_out("foo","10:2,20:1,5:0,2:2,1:2",".25:1,.1:0,.05:3,.01:9")
except (AssertionError):
    print("Expected failure seen")

try:
    pay_out(1.234,"10:2,20:1,5:0,2:2,1:2",".25:1,.1:0,.05:3,.01:9")
except (Exception):
    print("Expected failure seen")
pay_out(6.35,"10:2,20:1,5:0,2:2,1:2",".25:1,.1:0,.05:3,.01:9")
print("\n")
pay_out(26.35,"10:2,20:1,5:0,2:2,1:2",".25:1,.1:0,.05:3,.01:9")
print("\n")
pay_out(1026.35,"10:2,20:1,5:0,2:2,1:2",".25:1,.1:0,.05:3,.01:9")
print("Have a nice day!")