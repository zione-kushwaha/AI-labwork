# Wap to calculate the sum, diff, prduct and quotient between two input numbers using a single function

def calculate_operations(a, b):
    'calculating the sum, diff,mul, divide'
    if b != 0:
        quotient = a / b
    else:
        quotient = "Not divisible by zero"

    return (a + b, a - b, a * b, quotient)


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
results = calculate_operations(num1, num2)
print("Sum: ",results[0])
print("Difference: ",results[1])
print("Product: ",results[2])
print("Quotient: ",results[3])


