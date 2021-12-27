texts = eval(input("how many texts you have used : "))
min = eval(input("how many minutes : "))
monthly_cost = 10.00
total_cost = 0.10*min+0.05*texts+monthly_cost

print("{:.2f}".format(total_cost))