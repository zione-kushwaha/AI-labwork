""""
Create a class BankAccount with private attributes balance and account_number.
Implement methods deposit() and withdraw() to modify the balance. Ensure that the
balance cannot be accessed directly from outside the class

"""

class bank_account:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.__balance +=amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


b = bank_account(99999999999999, 2244378269001)
b.deposit(100000000000)
print(b.get_balance())

b.withdraw(100000000000)
print(b.get_balance())