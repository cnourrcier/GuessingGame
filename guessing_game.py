import random
import json

class GuessingGame():
    def __init__(self, difficulty="medium"):
        # Initialize the game with a random target number and set attempts to 0
        self.target_number = random.randint(1,100)
        self.attempts = 0
        self.max_attempts = self.difficulty_to_attempts(difficulty)  # Set maximum attempts based on difficulty
        self.load_leaderboard()  # Load existing leaderboard or create an empty one

    def set_difficulty(self):
        # Allow the player to choose the game's difficulty level
        difficulty_levels = ["easy", "medium", "hard"]
        print("Choose a difficulty level: ")
        for i, level in enumerate(difficulty_levels, 1):
            print(f"{i}. {level}")
        choice = int(input("Enter the number corresponding to your choice: "))
        chosen_difficulty = difficulty_levels[choice - 1]
        self.max_attempts = self.difficulty_to_attempts(chosen_difficulty)  # Update max attempts based on chosen difficulty
    
    def difficulty_to_attempts(self, difficulty):
        # Map difficulty levels to the corresponding maximum attempts
        difficulty_levels = {
            "easy":   15,
            "medium": 10,
            "hard":    5
        }
        return difficulty_levels[difficulty]

    def load_leaderboard(self):
        # Load existing leaderboard data from a file or create an empty dictionary
        try:
            with open("leaderboard.json", "r") as file:
                self.leaderboard = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.leaderboard = {}

    def save_leaderboard(self):
        # Save the current leaderboard data to a file
        with open("leaderboard.json", "w") as file:
            json.dump(self.leaderboard, file)

    def update_leaderboard(self, name):
        # Update the leaderboard with the player's name and attempts
        if name not in self.leaderboard:
            self.leaderboard[name] = []
        self.leaderboard[name].append(self.attempts)
        self.save_leaderboard()

    def display_leaderboard(self):
        # Display the leaderboard with player names and attempts
        print("Leaderboard: ")
        for name, attempts in self.leaderboard.items():
            print(f"{name}: {attempts} attempts")

    def replay_game(self):
        # Replay game with the option to change the difficulty
        self.target_number = random.randint(1,100)
        self.attempts = 0
        self.set_difficulty()
        self.play()

    def start(self):
        # Start the game by welcoming the player and setting the difficulty level
        print("Welcome to the Guessing Game!")
        self.set_difficulty()
        self.play()  # Start playing the game
    
    def play(self):
        # Main game loop where the player guesses the number
        while self.attempts < self.max_attempts:
            guess = self.get_valid_guess()  # Get a valid guess from the player
            self.attempts += 1
            self.check_guess(guess)  # Check if the guess is correct
        
        print("Game over! The number was", self.target_number,".")
        self.display_leaderboard()  # Display the leaderboard at the end of the game

        replay = input("Do you want to play again? (yes / no)")
        if replay.lower() == 'yes':
            self.replay_game()  # Initialize a new game session
        else:
            print("Thanks for playing!")

    def get_valid_guess(self):
        # Get a valid guess from the player, handling invalid inputs
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
        # Check the player's guess against the target number and provide feedback
        if guess < self.target_number:
            print("Try higher.")
        elif guess > self.target_number:
            print("Try lower.")
        else:
            print("Congratulations! You guessed the correct number.")
            self.update_leaderboard(input("Enter your name for the leaderboard: "))
            self.attempts = self.max_attempts  # End the game by setting attempts to max_attempts
    
if __name__ == "__main__":
    # Create an instance of the GuessingGame class and start the game
    game = GuessingGame()
    game.start()