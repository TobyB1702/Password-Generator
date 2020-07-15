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

a = Backend()
print(a.randomStringGenerator(100))

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.get_password
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def get_password(self):
        getBackEnd = Backend()
        test = getBackEnd.randomStringGenerator(100)
        print(test)

root = tk.Tk()
app = Application(master=root)
app.mainloop()