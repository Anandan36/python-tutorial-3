from breezypythongui import EasyFrame
import random

class GuessGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Guess the Number (1-100)")
        self.target = random.randint(1, 100)
        self.guesses = 0

        self.addLabel("Enter your guess:", row=0, column=0)
        self.inputField = self.addIntegerField(0, row=0, column=1)
        self.addButton("Guess", row=1, column=0, columnspan=2, command=self.checkGuess)
        self.output = self.addTextField("", row=2, column=0, columnspan=2)

    def checkGuess(self):
        guess = self.inputField.getNumber()
        self.guesses += 1
        if guess < self.target:
            self.output.setText("Too small, try again.")
        elif guess > self.target:
            self.output.setText("Too large, try again.")
        else:
            self.output.setText(f"Correct! Guessed in {self.guesses} tries.")

app = GuessGame()
app.mainloop()
