# wap to calculate the factorial of a number using a single function

def calculate_factorial(n):
    "Calculate the factorial of a number "
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1);

num = int(input("Enter the number: "));
result = calculate_factorial(num);
print('factorial of ', num, ' is ', result);