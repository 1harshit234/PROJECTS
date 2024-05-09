import math
#taking to input
x = float(input("write the number you want1"))
y = float(input("write the number you want2"))
#selecting the operation you want
print("1 = add,2 = subtract,3 = multiply,4= division,5 = power, 6 = sqrt ")
#taking the operation which the user wanna do it
z = int(input("write the operation u want to do with the numbers you want "))
#condition for different different type of the operations
if z ==1:
 print(x+y)
elif z == 2 :
 print(x-y )
elif z == 3 :
 print(x*y )
elif z == 4 :
 print(x/y )
elif z == 5 :
  print(pow(x,y))
else:
  print(math.sqrt(x),math.sqrt(y))