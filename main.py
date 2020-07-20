import random
import string
import tkinter as tk
from tkinter import Tk


class Backend:
    def randomStringGenerator(self, lengthOfString, bool1, bool2, bool3, boo4):
        try:
            b = Backend()
            word = ''.join(
                [random.choice(b.parametersForString(bool1, bool2, bool3, boo4)) for n in range(lengthOfString)])
            return word
        except IndexError:
            return "Please select atleast one option"

    def parametersForString(self, asciiLettersUpper, asciiLettersLower, digits, punctuation):
        myWord = ""
        if asciiLettersLower:
            myWord += string.ascii_lowercase

        if asciiLettersUpper:
            myWord += string.ascii_uppercase

        if digits:
            myWord += string.digits

        if punctuation:
            myWord += string.punctuation

        return myWord


class Application(tk.Frame):

    def __init__(self, master=None):
        uppercaseVar, lowercaseVar, digitsVar, punctuationVar = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()
        super().__init__(master)
        self.master = master
        self.pack()
        self.GeneratePasswordWidgets(uppercaseVar, lowercaseVar, digitsVar, punctuationVar)
        self.SelectionOfTextForPasswordWidgets(uppercaseVar, lowercaseVar, digitsVar, punctuationVar)
        self.QuitWidgets()

    def GeneratePasswordWidgets(self, uppercaseVar, lowercaseVar, digitsVar, punctuationVar):
        textBox = tk.Label(self, text="Enter Length of password")
        self.inputForLengthOfPasswordE = tk.Entry(self)
        self.inputForLengthOfPasswordE.insert(0, "16")
        generate_PasswordB = tk.Button(self, text="Generate a password",
                                       command=lambda: self.get_password(
                                           self.inputForLengthOfPasswordE.get(), uppercaseVar.get(), lowercaseVar.get(),
                                           digitsVar.get(), punctuationVar.get()))

        generate_PasswordB.grid(row=2)

        textBox.grid(row=0)
        self.inputForLengthOfPasswordE.grid(row=0, column=1)

    def QuitWidgets(self):
        quitB = tk.Button(self, text="QUIT", fg="red",
                          command=self.master.destroy)
        quitB.grid(row=2, column=1)

    def SelectionOfTextForPasswordWidgets(self, uppercaseVar, lowercaseVar, digitsVar, punctuationVar):
        uppercaseCB = tk.Checkbutton(self, text="Uppercase", variable=uppercaseVar)
        lowercaseCB = tk.Checkbutton(self, text="Lowercase", variable=lowercaseVar)
        digitsCB = tk.Checkbutton(self, text="Digits", variable=digitsVar)
        punctuationCB = tk.Checkbutton(self, text="Punctation", variable=punctuationVar)

        uppercaseCB.grid(row=1)
        lowercaseCB.grid(row=1, column=1)
        digitsCB.grid(row=1, column=2)
        punctuationCB.grid(row=1, column=3)

    def get_password(self, stringpasswordLength, bool1, bool2, bool3, boo4):
        try:
            passwordLength = int(stringpasswordLength)
            getBackEnd = Backend()
            password = getBackEnd.randomStringGenerator(passwordLength, bool1, bool2, bool3, boo4)
            outputForPasswordText = tk.Text(self, height=5, width=40)
            outputForPasswordText.grid(row=2,column=5)
            outputForPasswordText.insert('1.0', password)
            copyToClipBoardBT = tk.Button(self, text="Copy to ClipBoard", command=lambda: self.SetClipboard(password))
            copyToClipBoardBT.grid(row=2, column=6)
            return "Password Created"

        except ValueError: print("Invalid Int")

    def SetClipboard(self, message):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(message)
        r.update()  # now it stays on the clipboard after the window is closed
        r.destroy()

        return "Message Set"

    def setLengthOfPassword(self):
        size = 10
        print(size)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
