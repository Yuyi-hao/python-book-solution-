# Financial application: calculate tips

subtotal,gratuityRate = eval(input("Enter the subtotal and a gratuity rate : "))
gratuity = (gratuityRate*subtotal)/100
total = subtotal+gratuity

print('The gratuity is {:.2f} and the total is {:.2f}'.format(gratuity,total))