from breezypythongui import EasyFrame

class UppercaseConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Uppercase Converter")

        self.addLabel("Input:", row=0, column=0)
        self.inputField = self.addTextField("", row=0, column=1)

        self.addButton("Convert", row=1, column=0, columnspan=2, command=self.convert)

        self.addLabel("Uppercase:", row=2, column=0)
        self.outputField = self.addTextField("", row=2, column=1)

    def convert(self):
        text = self.inputField.getText()
        self.outputField.setText(text.upper())

app = UppercaseConverter()
app.mainloop()
