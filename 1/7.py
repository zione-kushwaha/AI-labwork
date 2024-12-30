# WAP to ask for a sentence and count the number of words.

def count_words(sentence):
    "the number of the words in the sentence is"
    return len(sentence.split())

sentence = input("Enter the sentence: ")
result = count_words(sentence)
print("the number os sentence is ", result)