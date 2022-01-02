weight = eval(input('Enter weight in pounds : '))
print("Enter height: ")
feet = eval(input('Enter feet : '))
inches = (input('Enter inches : '))

KILOGRAM_PER_POUNDS = 0.45659237
METER_PER_INCH = 0.0254

weightInKilo = weight*KILOGRAM_PER_POUNDS
heightInMeter = ((feet*12)+inches)*METER_PER_INCH

bmi = weightInKilo/(heightInMeter**2)

print('Your BMI is {:.3f}'.format(bmi))

if bmi <18.5 :
    print("You are underweight")
elif bmi <25 :
    print("You are normal")
else :
    print("You are Obese")