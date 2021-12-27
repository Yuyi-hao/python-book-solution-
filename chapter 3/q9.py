# financial application : payroll 

import time

name = str(input("Enter employee's name: "))

work_hours = float(input("Enter number of hours worked in a week: "))

pay_rate = float(input("Enter hourly pay rate: "))

federal_tax = float(input("Enter federal tax withholding rate: "))

state_tax = float(input("Enter state tax withholding rate: "))

print('\nEmployee Name: {}'.format(name))


print("Hours Worked: {:.1f}".format(work_hours))

print("Pay Rate: ${:.2f}".format(pay_rate))

gross_pay = work_hours * pay_rate
print("Gross Pay: ${:.1f}".format(gross_pay))

print("Deductions: ")
federal = gross_pay * federal_tax

print("\tFederal Withholding (20.0%): ${:.1f}".format(federal))
state = gross_pay * state_tax
print("\tState Withholding (9.0%): ${:.2f}".format(state))
total_tax = federal + state
print("\tTotal Deduction: ${:.2f}".format(total_tax))

net_pay = gross_pay - total_tax
print("Net Pay: ${:.2f}".format(net_pay))