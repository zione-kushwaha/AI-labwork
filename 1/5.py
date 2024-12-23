# wap to enter the marks of 10 students and display it


def  get_number(n):
    inp = input("Enter the {n} number seperated by space")
    after_inp = inp.split()
    converted = [float(val) for val in after_inp]

    return converted;

result = get_number(5);
print(result)