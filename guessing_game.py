import random


def get_guess():
    while True:
        try:
            response = int(input("Pick a number between 1 and 10:  "))
            if response < 1 or response > 10:
                raise ValueError("Number should be between 1 and 10!")
        except ValueError as err:
            print("Invalid Numer. Please retry!")
            print("{}".format(err))
        else:
            return response


def generate_random_number():
    return random.randrange(1, 10)


def play_game():
    correct = False
    answer = random.randrange(1, 10)
    attempts = 0
    while not correct:
        response = get_guess()
        if response > answer:
            attempts += 1
            print("# It is higher!")
        elif response < answer:
            attempts += 1
            print("# It is lower!")
        else:
            attempts += 1
            print("-" * 30)
            print("You got it! It tooks {} tries".format(attempts))
            print("-" * 30)
            correct = False
            return attempts


def start_game():
    print("=" * 40)
    print("Welcome to the number guessing game!")
    print("=" * 40)
    score = 0
    while True:
        game_score = play_game()
        if game_score:
            if score != 0 and game_score < score:
                score = game_score
            elif score == 0:
                score = game_score
            prompt = input("Would you like to play again? [y]es/[n]o: ")
            if prompt == "n":
                print("*" * 30)
                print("Closing game! See you next time!")
                print("Highest Score: {}".format(score))
                print("*" * 30)
                break
            elif prompt == "y":
                print("*" * 30)
                print("Highest Score: {}".format(score))
                print("*" * 30)
            else:
                print("*" * 30)
                print("Invalid entry!. Closing game! See you next time!")
                print("Highest Score: {}".format(score))
                print("*" * 30)
                break


if __name__ == '__main__':
    start_game()
