import random
import time


def main():
        # generate a random number between 1 and 100
        number = random.randint(1, 100)
        print("Guess the number between 1 and 100!")

        # loop through the numbers until the player presses enter
        while True:
                # generate a random number between 1 and 100
                guess = random.randint(1, 100)
                print(guess)

                # wait for 1 second before printing the next number
                time.sleep(1)

                # check if the player has pressed enter
                if input() == "{}":
                        break

        # print the selected number
        print("You selected:", number)
if __name__ == "__main__":
     main()


