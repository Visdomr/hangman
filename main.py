import random

print("Welcome to Hangman!")

stages_art = [
    """
    ______
    |    |
    O    |
   /|\   |
   / \   |
         |
   =========
""",
    """
    ______
    |    |
    O    |
   /|\   |
   /     |
         |
   =========
""",
    """
    ______
    |    |
    O    |
   /|\   |
         |
         |
   =========
    """,
    """
    ______
    |    |
    O    |
   /|    |
         |
         |
   =========
    """,
    """
    ______
    |    |
    O    |
    |    |
         |
         |
   =========
    """,
    """
    ______
    |    |
    O    |
         |
         |
         |
   =========
    """,
    """
    ______
    |    |
         |
         |
         |
         |
   =========
    """,
]
word_list = [
    "apple",
    "beach",
    "chair",
    "dance",
    "eagle",
    "flame",
    "grape",
    "house",
    "jelly",
    "knife",
    "lemon",
    "music",
    "ocean",
    "piano",
    "queen",
    "river",
    "smile",
    "tiger",
    "umbra",
    "vivid",
]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
placeholder = ""
for position in range(word_length):
    placeholder += "_"

end_of_game = False
lives = 6

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")

        if "_" not in display:
            game_over = True
            print("You win!")

        print(stages_art[lives])
