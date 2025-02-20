def is_palidrome(word):
    cleaned_word = word.replace(" ", "")
    cleaned_word.lower()
    if cleaned_word == cleaned_word[::-1]:
        return True
    return False

word=input("Eneter a word or phrase to check if it is a palidrome: ")
if is_palidrome(word):
    print(f"The word {word} is a palidrome.")
else:
    print(f"The word {word} is not a palidrome")
