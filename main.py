import random
import wordlist


def print_welcome():
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

while True:
    print_welcome()

    chosen_word = random.choice(wordlist.word_list)
    word_length = len(chosen_word)
    placeholder = ""
    for position in range(word_length):
        placeholder += "_"

    lives = 6
    game_over = False
    correct_letters = []
    all_guesses = []
    user_quit = False
    print("Word to guess: " + placeholder)

    while not game_over:
        display = ""
        guess = input("\n Guess a letter: ").lower()

        if guess == "quit" or guess == ":q":
            print("Quitting game...")
            user_quit = True
            break

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in all_guesses:
            print("You already guessed that letter!")
            continue

        all_guesses.append(guess)

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
        print("Word to guess: " + display)

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
            print("You filled the word! You win!")

    if user_quit:
        print("Thanks for playing!")
        exit()

    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "y"]:
            break
        elif play_again in ["no", "n"]:
            print("Thanks for playing!")
            exit()
        else:
            print("Please enter 'yes' or 'no'.")
