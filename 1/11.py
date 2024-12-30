# wap to ask for a sentence and calculate the frequency of characters in the sentences

def cal_char_freq(sentence):
    frequency = {}
    for char in sentence:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

sentence = input("Enter a sentence: ")
freq = cal_char_freq(sentence)
print("The character in the sentence is", freq)