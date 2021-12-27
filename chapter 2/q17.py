# Health application: compute BMI

# convert pounds into kilograms 
weight = eval(input("Enter weight in pounds : "))
kilo = weight*0.45359237


# convert feet into meters 
height = eval(input("Enter length in inches : "))
meter =  height*0.0254

# calculate BMI
BMI = kilo/(meter**2)
print('BMI is {:.4f}'.format(BMI))