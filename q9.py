from breezypythongui import EasyFrame

class ComputerGuessGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Computer Guesses (1-100)")

        self.low = 1
        self.high = 100
        self.guess = (self.low + self.high) // 2
        self.addLabel(f"Computer's guess: {self.guess}", row=0, column=0, columnspan=3)
        self.label = self.addLabel("", row=1, column=0, columnspan=3)

        self.addButton("Too Small", row=2, column=0, command=self.tooSmall)
        self.addButton("Too Large", row=2, column=1, command=self.tooLarge)
        self.addButton("Correct", row=2, column=2, command=self.correct)

    def updateGuess(self):
        self.guess = (self.low + self.high) // 2
        self.label["text"] = f"Computer's guess: {self.guess}"

    def tooSmall(self):
        self.low = self.guess + 1
        self.updateGuess()

    def tooLarge(self):
        self.high = self.guess - 1
        self.updateGuess()

    def correct(self):
        self.label["text"] = f"Yay! Guessed it: {self.guess}"
        for button in self.buttons:
            button["state"] = "disabled"

app = ComputerGuessGame()
app.mainloop()
