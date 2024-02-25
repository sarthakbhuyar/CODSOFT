print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
while True:
choice = input("Enter choice(1/2/3/4): ")
if choice in ('1', '2', '3', '4'):
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
if choice == '1':
print(n1, "+", n2, "=", (n1+n2))
elif choice == '2':
print(n1, "-", n2, "=",(n1- n2))
elif choice == '3':
print(n1, "*", n2, "=",(n1* n2))
elif choice == '4':
print(n1, "/", n2, "=",(n1/n2))
next_calculation = input("Let's do next calculation? (yes/no): ")
if next_calculation.lower() != "yes":
break
else:
print("Invalid input")