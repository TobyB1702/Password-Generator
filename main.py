import random
import string
import tkinter as tk


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
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.textBox = tk.Label(self, text="Enter Length of password").grid(row=0)

        self.inputForLengthOfPasswordE = tk.Entry(self)
        self.inputForLengthOfPasswordE.grid(row=0, column=1)
        self.inputForLengthOfPasswordE.insert(0, "16")

        uppercaseVar, lowercaseVar, digitsVar, punctuationVar = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()

        self.uppercaseCB = tk.Checkbutton(self, text="Uppercase", variable=uppercaseVar, command=lambda: self.cb(uppercaseVar)).grid(row=3)
        self.lowercaseCB = tk.Checkbutton(self, text="Lowercase", variable=lowercaseVar, command=lambda: self.cb(lowercaseVar)).grid(row=3, column=1)
        self.digitsCB = tk.Checkbutton(self, text="Digits", variable=digitsVar, command=lambda: self.cb(digitsVar)).grid(row=3, column=2)
        self.punctuationCB = tk.Checkbutton(self, text="Punctation", variable=punctuationVar, command=lambda: self.cb(punctuationVar)).grid(row=3, column=3)

        self.generate_PasswordB = tk.Button(self, text="Generate a password",
                                           command=lambda: self.get_password(
                                               int(self.inputForLengthOfPasswordE.get()), uppercaseVar.get(), lowercaseVar.get(), digitsVar.get(), punctuationVar.get())).grid(row=1)

        self.quitB = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy).grid(row=1, column=1)

#refactor this
    def get_password(self, passwordLength, bool1, bool2, bool3, boo4):
        getBackEnd = Backend()
        test = getBackEnd.randomStringGenerator(passwordLength, bool1, bool2, bool3, boo4)
        print(test)

    def setLengthOfPassword(self):
        size = 10
        print(size)

    def cb(self,var):
        print("variable is {0}".format(var.get()))


root = tk.Tk()
app = Application(master=root)
app.mainloop()
