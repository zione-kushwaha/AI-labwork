# You are given a string and your task is to swap cases. In other words, convert all lowercase letters
#   to uppercase letters and vice versa.


def swap_case(s):
    for i in s:
        if i.isupper():
            print(i.lower(), end="")
        else:
            print(i.upper(), end="")

s = input("Enter the string: ")
result = swap_case(s)
