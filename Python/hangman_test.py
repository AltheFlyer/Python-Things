secretWord = "thelastairbender"
MISTAKE_LIMIT = 6
mistakes = 0
usedLetters = ""
letterGuess = ""
guessed = True
newWord = ""
counter = 0

print("Let's play Hangman! I'm thinking of a word.")
for char in secretWord:
    counter = counter + 1
print("_" * counter)
print(" ")

while usedLetters != secretWord and mistakes <= MISTAKE_LIMIT:
    letterGuess = input("\nGuess a letter. ")
    usedLetters = usedLetters + letterGuess
    for letter in secretWord:
        if letter in letterGuess:
            newWord = newWord + letterGuess
        elif letter not in letterGuess:
            newWord = newWord + "_ "
    print (newWord)


if mistakes < MISTAKE_LIMIT:
    print("Sorry, you used up all your tries!")
