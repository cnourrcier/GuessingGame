import random

class GuessingGame():
    def __init__(self):
        self.target_number = random.randint(1,100)
        self.attempts = 0
        self.max_attempts = 10

    def start(self):
        print("Welcome to the Guessing Game!")
        self.play()
    
    def play(self):
        while self.attempts < self.max_attempts:
            guess = self.get_valid_guess()
            self.attempts += 1
            self.check_guess(guess)
        
        print("Game over! The number was", self.target_number,".")

    def get_valid_guess(self):
        while True:
            try:
                guess = int(input("Guess a number between 1 and 100: "))
                if guess < 1 or guess > 100:
                    print("Invalid number. Please try again.")
                    continue
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def check_guess(self, guess):
        if guess < self.target_number:
            print("Try higher.")
        elif guess > self.target_number:
            print("Try lower")
        else:
            print("Congratulations! You guessed the correct number.")
            self.attempts = self.max_attempts
    
if __name__ == "__main__":
    game = GuessingGame()
    game.start()