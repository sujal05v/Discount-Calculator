 #Discount Calculation
"""
Rs 0 - Rs999 -> No discount 
Rs1000-Rs4999 -> 10% discount
Rs5000-Rs9999 -> 20% discount
Rs10000 and above -> 30% discount
Get the original price from the user

"""

total = int(input("Enter the total amount Rs: "))

if (total >= 0 and total <= 999):
  discount = 0
  print("There is no Discount Avaliable at your range")
  print("Your Total Bill is :",total - discount)

elif(total >= 1000 and total <= 4999):
  discount = 0.10*total
  print("10% discount Avaliable at your range")
  print("Your Total Bill is :",total - discount)

elif(total>=5000 and total<=9999):
  discount = 0.20*total
  print("20% discount Avaliable at your range")
  print("Your Total Bill is :",total - discount)

elif(total>=10000):
  discount = 0.30*total
  print("30% Discount avaliable at yout range")
  print("Your Total Bill is :",total - discount)

else:
  print("Enter Valid Amount Sir/Madam Please")