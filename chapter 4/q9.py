weight1, price1 = eval(input("Enter weight and price for package 1 : "))
weight2, price2 = eval(input("Enter weight and price for package 2 : "))

pricePerKG1 = weight1/price1
pricePerKG2 = weight2/price2

best = 1 if(pricePerKG1>pricePerKG2) else 2

print("Package {} has better price".format(best))

