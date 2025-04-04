from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")

        self.addLabel("Fahrenheit", row=0, column=0)
        self.addLabel("Celsius", row=0, column=1)

        self.fField = self.addFloatField(32.0, row=1, column=0)
        self.cField = self.addFloatField(0.0, row=1, column=1)

        self.addButton(">>>>", row=2, column=0, command=self.fToC)
        self.addButton("<<<<", row=2, column=1, command=self.cToF)

    def fToC(self):
        f = self.fField.getNumber()
        self.cField.setNumber((f - 32) * 5 / 9)

    def cToF(self):
        c = self.cField.getNumber()
        self.fField.setNumber((c * 9 / 5) + 32)

app = TemperatureConverter()
app.mainloop()
