# program to sum all the items in the dictionay

def sum_dictionary_items(dictionary):
    total = sum(dictionary.values())
    return total

dictionary = {'a': 10, 'b': 20, 'c': 30}
print("The sum ", sum_dictionary_items(dictionary))