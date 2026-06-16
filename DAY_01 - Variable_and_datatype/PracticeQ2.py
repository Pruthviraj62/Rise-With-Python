# Swap Two Variables ⭐⭐
print(" without using 3rd var ")


num1 = 10 
num2 = 20 

print(f"Num1 before swaping : {num1}")
print(f"Num2 before swaping : {num2}")
 
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"Num1 after swaping : {num1}")
print(f"Num2 after swaping : {num2}")


print("")
print("Swaping by using third variable")

num3 = 30 
num4 = 40 

print(f"Num3 before swaping : {num3}")
print(f"Num4 before swaping : {num4}")

temp = num3
num3 = num4
num4 = temp

print(f"Num3 after swaping : {num3}")
print(f"Num4 after swaping : {num4}")
