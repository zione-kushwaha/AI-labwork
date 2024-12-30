# Write a Python program to create a person class. Include attributes like name, country and date of
# birth. Implement a method to determine the person's age.

# library to import datetime module
import datetime
class person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    
    def age(self):
        today = datetime.datetime.today()
        return today.year - int(self.dob)
    
p = person('John', 'USA', '1990')
print("Age of person is: ", p.age())