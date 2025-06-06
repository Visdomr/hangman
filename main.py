import random

print("Welcome to Hangman! You get 6 wrong guesses to find the word. Good Luck!")
print("""
    ______
    |    |
         |
         |
         |
         |
   =========
""")

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

lives = 6

game_over = False
correct_letters = []

while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

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
            print(f"The word was: {chosen_word}")
            print("You lose!")
        if not game_over:
            print(stages_art[lives])

    if "_" not in display:
        game_over = True
        print("You win!")
