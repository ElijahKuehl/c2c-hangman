from random import randint

# list of the body parts that will appear when a wrong guess is entered
hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]

num_wrong_guesses_allowed = len(hangman_parts)  # notice: len() gets us the length of the list

# words that our program chooses between to guess
words = [
    "apple",
    "butterfly",
    "car",
    "pajama",
    "kayak",
    "zigzag",
    "zombie",
    "oxygen",
    "able",
    "baby",
    "lock",
    "ornament",
    "quality",
    "liquid",
    "suggestion",
    "weather",
    "twist"
    ]

# convenience function provided to
def draw_hangman(num_wrong_guesses):
    if num_wrong_guesses > num_wrong_guesses_allowed:
        # increment the count if wrong guess
        num_wrong_guesses = num_wrong_guesses_allowed

    hangman_characters = {
        "head" : "  O",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }

    hangman_newlines = [ "head", "right arm", "right leg" ]
    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(num_wrong_guesses):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)

# prompt player for her/his name
name = input("What is your name? ")

print("Hello " + name + ", let's play Hangman!")

# need to track the number of incorrect guesses made so far
wrong_guesses = 0
word = words[randint(0, len(words))]
guess = " "
user_guesses = []
blank_dict = {}
for i in word:
    if i in blank_dict.keys():
        i = i + "2"
    blank_dict[i] = "_"

while wrong_guesses < num_wrong_guesses_allowed:
    mystery_word = ""
    blank_dict_list = str(blank_dict.values()).split("[")[1].split("]")[0].split("'")
    for letter in blank_dict_list:
        if "," not in letter:
            mystery_word += letter + " "
    print(mystery_word)

    guess = input("Guesses: " + str(user_guesses) + "\nWhat is your guess?  ").lower()  # .lower()
    user_guesses.append(guess)

    if guess in word:
        if guess + "2" in blank_dict.keys():
            blank_dict[(guess + "2")] = guess
        blank_dict[guess] = guess
        print("Correct")
    else:
        print("Wrong")
        wrong_guesses += 1
    draw_hangman(wrong_guesses)

    if "_" not in blank_dict.values():
        print("You Win!")
        print(mystery_word)
        break

if wrong_guesses == num_wrong_guesses_allowed:
    print("GAME OVER")
