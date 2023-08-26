import random
import json

class GuessingGame():
    def __init__(self, difficulty="medium"):
        self.target_number = random.randint(1,100)
        self.attempts = 0
        self.max_attempts = self.difficulty_to_attempts(difficulty)
        self.load_leaderboard()

    def set_difficulty(self):
        difficulty_levels = ["easy", "medium", "hard"]
        print("Choose a difficulty level: ")
        for i, level in enumerate(difficulty_levels, 1):
            print(f"{i}. {level}")
        choice = int(input("Enter the number corresponding to your choice: "))
        chosen_difficulty = difficulty_levels[choice - 1]
        self.max_attempts = self.difficulty_to_attempts(chosen_difficulty)
    
    def difficulty_to_attempts(self, difficulty):
        difficulty_levels = {
            "easy":   15,
            "medium": 10,
            "hard":    5
        }

        return difficulty_levels[difficulty]


    def load_leaderboard(self):
        try:
            with open("leaderboard.json", "r") as file:
                self.leaderboard = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.leaderboard = {}

    def save_leaderboard(self):
        with open("leaderboard.json", "w") as file:
            json.dump(self.leaderboard, file)

    def update_leaderboard(self, name):
        if name not in self.leaderboard:
            self.leaderboard[name] = []
        self.leaderboard[name].append(self.attempts)
        self.save_leaderboard()

    def display_leaderboard(self):
        print("Leaderboard: ")
        for name, attempts in self.leaderboard.items():
            print(f"{name}: {attempts} attempts")


    def start(self):
        print("Welcome to the Guessing Game!")
        self.set_difficulty()
        self.play()
    
    def play(self):
        while self.attempts < self.max_attempts:
            guess = self.get_valid_guess()
            self.attempts += 1
            self.check_guess(guess)
        
        print("Game over! The number was", self.target_number,".")
        self.display_leaderboard()

        replay = input("Do you want to play again? (yes / no)")
        if replay.lower() == 'yes':
            self.__init__(self.max_attempts)
            self.start()
        else:
            print("Thanks for playing!")

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
            self.update_leaderboard(input("Enter your name for the leaderboard: "))
            self.attempts = self.max_attempts
    
if __name__ == "__main__":
    game = GuessingGame()
    game.start()