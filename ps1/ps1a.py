#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:03:03 2020

@author: jordyn-young
"""

annual_salary = int(input("Enter your annual salary: ")) # user inputs
monthly_salary = annual_salary/12 # calculated based on user input
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) # user input
monthly_savings = monthly_salary * portion_saved # calculated based on user input
total_cost = int(input("Enter the cost of your dream home: ")) # user input

portion_down_payment = 0.25 # given in ps1
down_payment = portion_down_payment * total_cost # calculates down payment needed based on total_cost of dream home
current_savings = 0 # starts at 0, given in ps1
r = 0.04 # annual savings return rate, given in ps1
monthly_return = (current_savings*r)/12
months = 0 # starting at 0 months (no monthly_savings yet, so current_savings is 0)

while current_savings < down_payment: # runs loop until the current_savings can cover the down_payment
    months += 1 # adds another month
    current_savings += monthly_savings + ((current_savings*r)/12) # adds monthly salary and savings return to current savings

print(f"Number of months: {months}")