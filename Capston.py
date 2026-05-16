import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There are currently no high scores, its yours for the taking!")
    else:
        print("The current HIGH score is {} attempts".format(min(attempts_list)))
        def start_game():
            random_number = int(random.randint(1, 10))
            print("Hey there! Welcome to the game of guesses!")
            player_name = input("Enter YOUR name!!!")
            wanna_play = input("HI, {}, would you like to play the guessing game? (Enter YES/NO)".format(player_name))
            attempts = 0
            show_score()
            while wanna_play.lower() == "yes":
                try:
                    guess input("Pick a number betweeen 1 and 10.")
                    i= int(guess) < 1 or int(guess) > 10:
                    raise ValueError("Please guess a number within the given range.")
                if int(guess) == random_number:
                    print("CONGRATS YOU GUESSED IT!!!")

                    attempts += 1
                    attempts_list.apppend(attempts)
                    print("It took you {} attempts".format(attempts))
                    play_again = input("would you like to play again? Enter YES/NO")
                    attempts = 0
                    show_score()
                    random_number = int(random.randint(1, 10))
                    if play_again.lower() == "no":
                        print("Thats cool, have a nice day!")
                        break
                    elif int(guess) < random_number:
                        print("Its lower.")
                        attempts += 1
                    elif int(guess) > random_number:
                        print("Its higher.")
                        attempts += 1
                except ValueError as err:
                print("Oh!, that is not a valid value. try again...")



