def display_division(percentage):
    "Your grade is "
    if percentage >= 80:
        print("Distinction")
    elif percentage >= 60:
        print("First Division")
    elif percentage >= 50:
        print("Second Division")
    elif percentage >= 40:
        print("Third Division")
    else:
        print("Fail")


n = int(input("Enter your percentage :"))

display_division(n)

