a = int(input("enter number for a = "))
b = int(input("enter number for b = "))
c = int(input("enter number for c = "))

max = a
if max < b:
    max = b
if max < c:
    max = c 

a1 = int(input("enter number for a1 = "))
b1 = int(input("enter number for b1 = "))
c1 = int(input("enter number for c1 = "))

max1 = a1
if max1 < b1:
    max1 = b1
if max1 < c1:
    max1 = c1    

print("Max number = ", max)  
print("Max number1 = ", max1)

if max > max1:
    print("max больше чем max1 => max =", max , "=> first number won!!!")
else:
    print("max меньше чем max1 => max1 =", max1, "=> second number won!!!")