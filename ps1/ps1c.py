#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:07:47 2020

@author: jordyn-young
"""

semi_annual_raise = .07 # 7%, given in ps1c
r = .04 # 4%, given in ps1c
portion_down_payment = 0.25 # 25%, given in ps1c
total_cost = 1000000 # $1,000,000, given in ps1c
down_payment = portion_down_payment * total_cost # calculated using given info

annual_salary = int(input("Enter the starting salary: ")) # user inputs
monthly_salary = annual_salary / 12 # calculated using given info

# calculate best savings rate w/2 decimals of accuracy

epsilon = 100
high = 10000
low = 0

savings = 0
steps = 0

while (savings - down_payment) > epsilon or (savings - down_payment) < 0:    
    test_whole_salary = annual_salary
    test_savings = 0
    test_monthly_salary = test_whole_salary / 12
    for test_months in range(1, 37):
        if test_months % 6 == 1 and test_months != 1:
            test_monthly_salary *= 1 + semi_annual_raise
        test_monthly_savings = test_monthly_salary
        test_savings += test_monthly_savings + ((test_savings * r) / 12)
    if test_savings < down_payment:
       print("It is not possible to pay the down payment in three years.") 
       break
    steps += 1
    guess = low + (high - low)/2
    savings_rate = (guess / 10000)
    savings = 0
    monthly_salary = annual_salary / 12
    for months in range(1, 37):
       if months % 6 == 1 and months != 1:
           monthly_salary *= 1 + semi_annual_raise
       monthly_savings = monthly_salary * savings_rate
       savings += monthly_savings + ((savings * r) / 12)
    if abs(savings - down_payment) <= epsilon:
        if savings > down_payment:
            print("Best savings rate: ", savings_rate)
            print("Steps in bisection search: ", steps)
            break
        else:
            low = guess
    elif abs(savings - down_payment) > epsilon:
        if savings > down_payment:
            high = guess 
        else:
            low = guess
    else:
        print("fix something!")