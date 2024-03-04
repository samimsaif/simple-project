word = "saif"
chances = 5
Guessed = []
done = False

while not done:
    for letter in word:
        if letter.lower()   in Guessed:
            print(letter, end= " ")
        else:
            print("_", end= " ")

    Myguess = input(f" Your chances is {chances} , Guessed the letter:")
    Guessed.append(Myguess.lower())
    if Myguess.lower() not in word.lower():
        chances -=  1
        if chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in Guessed:
            done = False


if done:
    print(f" Yes! You Have won the game. the word is {word}.")


