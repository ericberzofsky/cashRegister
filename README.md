# cashRegister
Script to provide answer to interview question simulating a cash register that pays out change in the fewest bills possible.
Testcases are hard-coded in the script for now, but method accepts a dollar amount to payout, as well as list of bill/coin denominations and the quantity of each. Script will payout in the fewest bills/coins possible.

Sample executions:
pay_out("foo","10:2,20:1,5:0,2:2,1:2",".25:1,.1:0,.05:3,.01:9")
    
    AssertionError: Not valid payout amount

pay_out(1.234,"10:2,20:1,5:0,2:2,1:2",".25:1,.1:0,.05:3,.01:9")

    Exception: Three points after decimal

pay_out(6.35,"10:2,20:1,5:0,2:2,1:2",".25:1,.1:0,.05:3,.01:9")

    We currently have the following notes in our cash register:
    1 notes of the $20.00 denomination    
    2 notes of the $10.00 denomination    
    2 notes of the $2.00 denomination    
    2 notes of the $1.00 denomination    
    1 notes of the $0.25 denomination    
    3 notes of the $0.05 denomination    
    9 notes of the $0.01 denomination

    We're able to payout the amount $6.35 in the fewest notes possible by doing:
    2 notes of the $2.00 denomination    
    2 notes of the $1.00 denomination    
    1 notes of the $0.25 denomination    
    2 notes of the $0.05 denomination
    
pay_out(26.35,"10:2,20:1,5:0,2:2,1:2",".25:1,.1:0,.05:3,.01:9")

    We currently have the following notes in our cash register:    
    1 notes of the $20.00 denomination    
    2 notes of the $10.00 denomination    
    2 notes of the $2.00 denomination    
    2 notes of the $1.00 denomination    
    1 notes of the $0.25 denomination    
    3 notes of the $0.05 denomination  
    9 notes of the $0.01 denomination

    We're able to payout the amount $26.35 in the fewest notes possible by doing:
    1 notes of the $20.00 denomination    
    2 notes of the $2.00 denomination    
    2 notes of the $1.00 denomination    
    1 notes of the $0.25 denomination    
    2 notes of the $0.05 denomination
    
pay_out(1026.35,"10:2,20:1,5:0,2:2,1:2",".25:1,.1:0,.05:3,.01:9")

    We currently have the following notes in our cash register:
    1 notes of the $20.00 denomination
    2 notes of the $10.00 denomination
    2 notes of the $2.00 denomination
    2 notes of the $1.00 denomination
    1 notes of the $0.25 denomination
    3 notes of the $0.05 denomination
    9 notes of the $0.01 denomination
    We didn't have enough in cash register to payout the amount $1026.35
