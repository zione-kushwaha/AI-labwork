# wap to ask for a sentence and calculate the frequency of characters in the sentences

def character_sum(sentence, character):
    count = 0
    for char in sentence:
        if char == character:
            count += 1
    return count

sentence = input("Enter a sentence: ")
character = input("Enter the character to count: ")
frequency = character_sum(sentence, character)
print('the frequency of the character is ', frequency)