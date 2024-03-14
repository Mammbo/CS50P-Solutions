# Create our own function
def convert(word): 
        if ":)" in word and ":(" in word: 
             print(word.replace(":)", '🙂').replace(":(", '🙁'))
        elif ":)" in word: 
            print(word.replace(":)", '🙂'))
        elif ":(" in word: 
            print(word.replace(":(", '🙁'))

              

word = input("Say a word and a face like, :) or :(  ")
convert(word)

# Output using our own functi