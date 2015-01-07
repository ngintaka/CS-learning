#Examine three variables and print the largest odd number or a msg if there are no odd numbers.

#Ask for three numbers
print("Hi! Please input any three integers and I'll figure out which is the highest odd number")
x = int(raw_input("Give me your first number (x)..."))
y = int(raw_input("Give me your second number (y)..."))
z = int(raw_input("Give me your third number (z)..."))
if x%2 == 0 and y%2 == 0 and z%2 == 0:
    print("All your numbers are even!")
elif x%2 != 0 and ((y%2 == 0 or x > y) and (z%2 == 0 or x > z)):
    print("Your first number (x) is the largest odd number!")
elif y%2 != 0 and (z%2 == 0 or y > z):
    print("Your second number (y) is the largest odd number!")
elif z%2 != 0:
    print("Your third number (z) is the largest odd number!")
