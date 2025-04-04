from breezypythongui import EasyFrame

class BouncyBall(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Bouncy Ball Distance")
        self.addLabel("Initial Height (m):", row=0, column=0)
        self.heightField = self.addFloatField(0.0, row=0, column=1)

        self.addLabel("Bounciness Index (0 < b < 1):", row=1, column=0)
        self.bounceField = self.addFloatField(0.0, row=1, column=1)

        self.addLabel("Number of Bounces:", row=2, column=0)
        self.bouncesField = self.addIntegerField(0, row=2, column=1)

        self.addButton("Compute", row=3, column=0, columnspan=2, command=self.compute)
        self.resultField = self.addFloatField(0.0, row=4, column=1)

    def compute(self):
        h = self.heightField.getNumber()
        b = self.bounceField.getNumber()
        n = self.bouncesField.getNumber()
        total = 0.0

        for i in range(n):
            total += h
            h *= b
            total += h
        self.resultField.setNumber(total)

app = BouncyBall()
app.mainloop()
