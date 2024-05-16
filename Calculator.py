# Calculator------------task2
def add(a, y):
    return a + y

def subtract(a, y):
    return a - y

def multiply(a, y):
    return a * y

def divide(a, y):
    if y == 0:
        return "Error!! Division by zero."
    return a / y

print("Select any one operation:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
number1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(number1, "+", num2, "=", add(number1, num2))

elif choice == '2':
    print(number1, "-", num2, "=", subtract(number1, num2))

elif choice == '3':
    print(number1, "*", num2, "=", multiply(number1, num2))

elif choice == '4':
    print(number1, "/", num2, "=", divide(number1, num2))

else:
    print("Invalid input")