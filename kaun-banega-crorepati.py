# ================= QUESTIONS ANSWERS WITH PRIZE DETAILS =================

questionBanks = [
    {
        "question": "Who developed Python?",
        "options": {
            "A": "James Gosling",
            "B": "Guido van Rossum",
            "C": "Dennis Ritchie",
            "D": "Bjarne Stroustrup"
        },
        "correctAns": "B",
        "prize": 1000
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "A": "//",
            "B": "/* */",
            "C": "#",
            "D": "<!-- -->"
        },
        "correctAns": "C",
        "prize": 2000
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "function",
            "B": "def",
            "C": "define",
            "D": "fun"
        },
        "correctAns": "B",
        "prize": 3000
    },
    {
        "question": "Which data type stores True or False values?",
        "options": {
            "A": "String",
            "B": "Integer",
            "C": "Boolean",
            "D": "List"
        },
        "correctAns": "C",
        "prize": 5000
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": {
            "A": "input()",
            "B": "print()",
            "C": "output()",
            "D": "display()"
        },
        "correctAns": "B",
        "prize": 10000
    },
    {
        "question": "Which collection is used to store multiple items in Python?",
        "options": {
            "A": "List",
            "B": "Integer",
            "C": "Float",
            "D": "Boolean"
        },
        "correctAns": "A",
        "prize": 20000
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": {
            "A": "%",
            "B": "//",
            "C": "**",
            "D": "/"
        },
        "correctAns": "C",
        "prize": 40000
    },
    {
        "question": "Which method converts a string to lowercase?",
        "options": {
            "A": "upper()",
            "B": "lower()",
            "C": "capitalize()",
            "D": "title()"
        },
        "correctAns": "B",
        "prize": 80000
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": {
            "A": "catch",
            "B": "error",
            "C": "except",
            "D": "final"
        },
        "correctAns": "C",
        "prize": 160000
    },
    {
        "question": "Which of these is an immutable data type?",
        "options": {
            "A": "List",
            "B": "Dictionary",
            "C": "Set",
            "D": "Tuple"
        },
        "correctAns": "D",
        "prize": 320000
    }
]


# ================= TERNIMAL WIDTH TO SHOW TEXT DETAILS =================

WIDTH = 64


# Common border throughout the game
def show_line():
    print("=" * WIDTH)


# Welcome message and game instructions
def show_welcome():

    print("\n")
    show_line()

    print("\n  KAUN BANEGA CROREPATI")

    print("\n  Welcome! Test your knowledge and win big.\n")

    print("  GAME INSTRUCTIONS")
    print("  " + "-" * 60)

    print("  1. Answer the multiple-choice questions.")
    print("  2. Select your answer using A, B, C or D.")
    print("  3. One wrong answer ends the game.")
    print("  4. Your prize money increases with every correct answer.")

    show_line()


# Display the current question and its options
def show_question(index, total, question):

    print("\n")
    show_line()

    leftText = f"  QUESTION {index:02} / {total:02}"
    rightText = f"PRIZE: Rs. {question['prize']:,}"

    print(leftText.ljust(45) + rightText.rjust(19))

    show_line()

    print()
    print(f"  {question['question']}\n")

    for key, answer in question["options"].items():
        print(f"  [{key}]  {answer}\n")

    print("-" * WIDTH)


# Display the player's total winning amounts
def show_winnings(amount):

    leftText = "  CURRENT WINNINGS:"
    rightText = f"Rs. {amount:,}"

    print(leftText.ljust(45) + rightText.rjust(19))

    print("-" * WIDTH)


# Display a message when the player answers correctly
def show_correct_answer(amount):

    print("\n")
    show_line()

    print("  CORRECT ANSWER!")

    print("-" * WIDTH)

    show_winnings(amount)

    print()
    print("  Congratulations! Moving to the next question.")

    show_line()


# Display the final result when the game ends
def show_final_result(amount, gameWon):

    print("\n")
    show_line()

    if gameWon:
        print("  GAME COMPLETED!")
        print("\n  Congratulations! You answered all questions correctly.")
    else:
        print("  GAME OVER!")
        print("\n  You have given an incorrect answer.")

    print()

    leftText = "  YOUR TOTAL WINNINGS:"
    rightText = f"Rs. {amount:,}"

    print(leftText.ljust(45) + rightText.rjust(19))

    show_line()

    print()
    print("              THANK YOU FOR PLAYING!")
    print("           We hope you enjoyed the game.")

    print()


# Combined logic to show questions and answers
def start_game():

    totalPrize = 0
    gameWon = True

    totalQuestions = len(questionBanks)

    # Go through each question one by one
    for index, question in enumerate(questionBanks, start=1):

        # Display the current question
        show_question(index, totalQuestions, question)

        # Keep asking until the player enters a valid option
        while True:

            userAnswer = input(
                "\n  Enter your final answer (A/B/C/D): "
            ).strip().upper()

            if userAnswer in question["options"]:
                break

            print("  Invalid option! Please enter A, B, C or D.")

        # Check whether the player's answer is correct
        if userAnswer == question["correctAns"]:

            # Add the prize money to the total winnings
            totalPrize += question["prize"]

            show_correct_answer(totalPrize)

        else:

            # Display the correct answer when the player is wrong
            print("\n  WRONG ANSWER!")

            print(
                f"  Correct answer: {question['correctAns']}. "
                f"{question['options'][question['correctAns']]}"
            )

            gameWon = False

            # End the current game
            break

    # Show the final winnings after the game ends
    show_final_result(totalPrize, gameWon)


# Ask the player if they want to start another game
def play_again():

    show_line()

    print("                     PLAY AGAIN?")

    show_line()

    print("\n  Would you like to play another round?\n")

    print("  [Y] Yes, let's play again!")
    print("  [N] No, exit the game.")

    while True:

        choice = input("\n  Enter your choice (Y/N): ").strip().upper()

        if choice == "Y" or choice == "YES":
            return True

        elif choice == "N" or choice == "NO":
            return False

        else:
            print("  Invalid choice! Please enter Y or N.")


# main function of the program to start the game
def main():

    # Keep running the game until the player chooses to exit
    while True:

        # Display the welcome screen
        show_welcome()

        # Start a new game
        start_game()

        # Ask whether the player wants to play again
        if not play_again():

            print("\n")
            show_line()

            print("          THANK YOU FOR PLAYING KBC!")
            print("                 SEE YOU AGAIN!")

            show_line()

            break


if __name__ == "__main__":
    main()
