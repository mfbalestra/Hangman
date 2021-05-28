import random
import string


option = "start"
while option != "exit":
    option = input('Type "play" to play the game, "exit" to quit: ')
    if option == "play":
        lives = 8
        print("H A N G M A N")
        words_list = ["python", "java", "kotlin", "javascript"]
        win_word = random.choice(words_list)
        hint = "-" * (len(win_word))
        hint = list(hint)
        wrong_guesses = []
        while lives != 0:
            if ("".join(hint)) == win_word:
                break
            print("\n")
            print("".join(hint))
            letter = input("Input a letter: ")
            if len(letter) <= 0 or len(letter) > 1:
                print("You should input a single letter")
                continue
            if letter not in string.ascii_lowercase:
                print("Please enter a lowercase English letter")
                continue
            if letter in win_word:
                if letter in hint:
                    print("You've already guessed this letter")
                else:
                    for i in range((len(win_word))):
                        if win_word[i] == letter:
                            hint[i] = letter
            else:
                if letter in wrong_guesses:
                    print("You've already guessed this letter")
                else:
                    wrong_guesses.append(letter)
                    print("That letter doesn't appear in the word")
                    lives -= 1
        if lives == 0:
            print("You lost!")
        else:
            print(f"You guessed the word {win_word}!")
            print("You survived!")

