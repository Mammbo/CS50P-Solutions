def remove_vowels(word, vowels):
    for letter in word:
        if letter in vowels:
            if letter in word:
                word = word.replace(letter, '')
    return word

word = input("Input: ")
vowels = ["a", "e", "i", "o", 'u', "A", "E", "I", "O", "U"]

new_word = remove_vowels(word, vowels)

print(f"Output: {new_word}")