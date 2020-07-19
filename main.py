import random
import string
import tkinter as tk
from tkinter import Tk


class Backend:
    def randomStringGenerator(self, lengthOfString, bool1, bool2, bool3, boo4):
        b = Backend()
        word = ''.join(
            [random.choice(b.parametersForString(bool1, bool2, bool3, boo4)) for n in range(lengthOfString)])
        return word

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
        generate_PasswordB = tk.Button(self, text="Generate a password",
                                           command=lambda: self.get_password(
                                               int(self.inputForLengthOfPasswordE.get()), uppercaseVar.get(), lowercaseVar.get(), digitsVar.get(), punctuationVar.get()))


        textBox = tk.Label(self, text="Enter Length of password")
        self.inputForLengthOfPasswordE = tk.Entry(self)
        self.inputForLengthOfPasswordE.insert(0, "16")

        generate_PasswordB.grid(row=1)

        textBox.grid(row=0)
        self.inputForLengthOfPasswordE.grid(row=0, column=1)


    def QuitWidgets(self):
        quitB = tk.Button(self, text="QUIT", fg="red",
                               command=self.master.destroy)
        quitB.grid(row=1, column=1)

    def SelectionOfTextForPasswordWidgets(self,  uppercaseVar, lowercaseVar, digitsVar, punctuationVar):
        uppercaseCB = tk.Checkbutton(self, text="Uppercase", variable=uppercaseVar,
                                          command=lambda: self.cb(uppercaseVar))

        lowercaseCB = tk.Checkbutton(self, text="Lowercase", variable=lowercaseVar,
                                          command=lambda: self.cb(lowercaseVar))

        digitsCB = tk.Checkbutton(self, text="Digits", variable=digitsVar,
                                       command=lambda: self.cb(digitsVar))

        punctuationCB = tk.Checkbutton(self, text="Punctation", variable=punctuationVar,
                                            command=lambda: self.cb(punctuationVar))
        uppercaseCB.grid(row=3)
        lowercaseCB.grid(row=3, column=1)
        digitsCB.grid(row=3, column=2)
        punctuationCB.grid(row=3, column=3)


    def get_password(self, passwordLength, bool1, bool2, bool3, boo4):
        getBackEnd = Backend()
        password = getBackEnd.randomStringGenerator(passwordLength, bool1, bool2, bool3, boo4)

        outputForPasswordText = tk.Text(self, height=5, width=40)
        outputForPasswordText.grid(row=4)
        outputForPasswordText.insert('1.0', password)

        copyToClipBoardBT = tk.Button(self, text="Copy to ClipBoard", command=lambda: self.SetClipboard(password))
        copyToClipBoardBT.grid(row=4,column=1)
        return "Password Created"

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

    def cb(self, var):
        print("variable is {0}".format(var.get()))


root = tk.Tk()
app = Application(master=root)
app.mainloop()
