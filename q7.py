from breezypythongui import EasyFrame
import math

class SqrtCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Square Root Calculator")
        self.addLabel("Enter Integer:", row=0, column=0)
        self.inputField = self.addIntegerField(0, row=0, column=1)
        self.addButton("Compute", row=1, column=0, columnspan=2, command=self.compute)
        self.outputField = self.addFloatField(0.0, row=2, column=1)

    def compute(self):
        try:
            value = self.inputField.getNumber()
            if value < 0:
                self.messageBox("Error", "Enter a non-negative number.")
            else:
                self.outputField.setNumber(math.sqrt(value))
        except:
            self.messageBox("Error", "Invalid input!")

app = SqrtCalculator()
app.mainloop()
