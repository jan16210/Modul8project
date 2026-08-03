import time
print("Welcome to the Quiz App!")
print("Please answer the following questions:")

checking_for_value = 0
lives = 3

website_url = "https://www.un.org/en/climatechange/paris-agreement"

questions = [
    "1. What country is the Paris climate agreement held in?",
    "2. What is the cap for the temperature increase set by the Paris climate agreement?",
    "3. What is the target year for countries to achieve net-zero emissions under the Paris climate agreement?",
]

while True:
    if lives > 0:
        for question in questions:

            if lives <= 0:
                break

            answer = input(question + " ")

            if question.startswith("1"):
                if answer.lower() == "france" or answer.lower() ==  "francja":
                    time.sleep(0.25)
                    print("Correct!")
                    checking_for_value += 1

                else:
                    lives -= 1
                    time.sleep(0.25)
                    print(f"Incorrect! You have {lives} lives remaining.")
                    checking_for_value += 1

            elif question.startswith("2"):
                if answer in [
                    "2c",
                    "2C",
                    "2°C",
                    "2°c",
                    "2 degrees",
                    "Two degrees",
                    "two degrees",
                    "Two degrees warmer",
                    "two degrees warmer",
                ]:
                    print("Correct!")
                    time.sleep(0.25)
                    checking_for_value += 1
                else:
                    lives -= 1
                    print(f"Incorrect! You have {lives} lives remaining.")
                    checking_for_value += 1

            elif question.startswith("3"):
                if answer == "2050":
                    print("Correct!")
                    checking_for_value += 1
                else:
                    lives -= 1
                    print(f"Incorrect! You have {lives} lives remaining.")
                    checking_for_value += 1

        if lives > 0:
            print("\nCongratulations! You completed the quiz.")
            print(f"Your score was {checking_for_value}/{len(questions)}")

            retry = input("Do you want to play again? (yes/no) ")

            if retry.lower() == "yes":
                lives = 3
                checking_for_value = 0
                print("\nStarting a new game...\n")
                continue
            else:
                print("Thanks for playing!")
                break

    else:
        print("Game over! You have no lives remaining.")
        question = input("Do you want to find out more about the Paris climate agreement? (yes/no) ")
        if question.lower() == "yes":
            print(f"You can learn more about the Paris climate agreement at {website_url}")

        retry = input("Do you want to try the quiz again? (yes/no) ")

        if retry.lower() == "yes":
            lives = 3
            checking_for_value = 0
            print("Great! Let's start the quiz again.")
        else:
            print("Ok, see you next time!")
            break
if checking_for_value == 3:
    print("Okay, you passed the test")
    print("Here is the next quiz with 5 even harder questions: ")
intermediate_questions = [
    "1. Which greenhouse gas is the largest contributor to human-caused climate change?"
    "2. What is the type of energy used to create greenhouse gases? (hint: it can't be remade)"
]