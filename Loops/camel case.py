def camelCase(word, char):
    result = ""
    for letter in word:
        if letter.isupper():
            result += char + letter
        else:
            result += letter
    return result.lower()


word = input("camelCase: ")
print(camelCase(word, "_"))
