def word_lengths(sentence):
    words = sentence.split()
    lengths = {word:len(word) for word in words}
    return lengths

sentence = input("Enter a sentence: ")
length_dict = word_lengths(sentence)
print(length_dict)