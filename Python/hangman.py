word = ""
guess = ""
answer = ""
original = ""
wrong = ""
misses = 0;

word = input()
original = word

answer = "_" * len(word)

while not (misses == 4) and not (answer == original):
    guess = input();
    if word.find(guess) > -1:
        while word.find(guess) > -1:
            answer = answer[0: word.find(guess)] + guess + answer[word.find(guess) + 1: len(word)]
            word = word[0: word.find(guess)] + "_" + word[word.find(guess) + 1: len(word)]
    else:
        misses += 1
        wrong +=  guess + " "

    print(answer);
    print("You have " + str(4 - misses) + " lives left.");
    print("Wrong letters: " + wrong);

if (misses == 4):
    print("You didn't guess the word")
else:
    print("You guessed the word!")
