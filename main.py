import random
import string
import tkinter as tk


class Backend:
    def randomStringGenerator(self, lengthOfString):
        b = Backend()
        word = ''.join(
            [random.choice(b.parametersForString(True, True, True, True)) for n in range(lengthOfString)])
        return word

    def parametersForString(self, asciiLettersLower, asciiLettersUpper, digits, punctuation):
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
        self.inputForLengthOfPassword = tk.Entry(self).grid(row=0, column=1)

        self.generate_Password = tk.Button(self, text="Generate a password",
                                           command=self.get_password).grid(row=1)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy).grid(row=1, column=1)

    def get_password(self):
        getBackEnd = Backend()
        test = getBackEnd.randomStringGenerator(100)
        print(test)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
