from tkinter import *
import tkinter.messagebox as tmsg
import random

password_gen = Tk()
username = StringVar()

options = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "18", "19", "20"]
clicked = StringVar()
clicked.set("5")

def show(*args):
    choice = clicked.get()
    print(choice)

def generate_password():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    chars = "!@#$%^*+-?/?"
    numbers = "1234567890"
    upper = list(upper)
    lower = list(lower)
    chars = list(chars)
    numbers = list(numbers)
    name = textfield.get()
    length = int(clicked.get())

    if name == "":
        tmsg.showerror("error", "please enter username")
        return
    if name.isalpha() == False:
        tmsg.showerror("error", "username must be alphabets")
        return

    u = random.randint(1, length - 3)
    l = random.randint(1, length - 2 - u)
    c = random.randint(1, length - 1 - u - l)
    n = length - u - l - c

    password = random.sample(upper, u) + random.sample(lower, l) + random.sample(chars, c) + random.sample(numbers, n)

    random.shuffle(password)
    gen_pass = "".join(password)
    generated_password.delete(0, END)  # Clear previous content
    generated_password.insert(0, gen_pass)

password_gen.geometry("800x500")
password_gen.title("Password Generator")
password_gen.configure(bg="#f8f1cd")
password_gen.resizable(False, False)

header_label = Label(text="THIS IS YOUR GUI BASED \n RANDOM PASSWORD GENERATOR", font='arial 20 bold underline',
                     bg="#f8f1cd", anchor=N)
header_label.grid(row=0, column=1)
label1 = Label(text="", bg="#f8f1cd")
label1.grid(row=1, column=0, columnspan=2)
label2 = Label(text="", bg="#f8f1cd")
label2.grid(row=2, column=0, columnspan=2)
label3 = Label(text="", bg="#f8f1cd")
label3.grid(row=3, column=0, columnspan=2)

user = Label(text="Enter user name: ", font=("Bodoni MT", "15"))
user.grid(row=4, column=0)

textfield = Entry(textvariable=username, font=("Bodoni MT", "15"), bd=2, relief=GROOVE)
textfield.grid(row=4, column=1)

label4 = Label(text="", bg="#f8f1cd")
label4.grid(row=5, column=0, columnspan=2)

length_label = Label(text="select the length", font=("Bodoni MT", "15"))
length_label.grid(row=6, column=0)

# Use a different variable name for the OptionMenu
length_option_menu = OptionMenu(password_gen, clicked, *options, command=show)
length_option_menu.grid(row=6, column=1)

label5 = Label(text="", bg="#f8f1cd")
label5.grid(row=7, column=0, columnspan=2)

button1 = Button(password_gen, text="SELECT", command=show)
button1.grid(row=8, column=1)

label5 = Label(text="", bg="#f8f1cd")
label5.grid(row=9, column=0, columnspan=2)

generated_password = Entry(font=("Bodoni MT", "15"), bd=2, relief=GROOVE)
generated_password.grid(row=10, column=1)

generate_label = Label(text="Generated Password", font=("Bodoni MT", "15"), bd=2)
generate_label.grid(row=10, column=0)

label5 = Label(text="", bg="#f8f1cd")
label5.grid(row=11, column=0, columnspan=2)

button2 = Button(password_gen, text="GENERATE PASSWORD", relief='solid', padx=1, pady=1, fg='white',
                 bg='black', command=generate_password)
button2.grid(row=12, column=1)

password_gen.mainloop()
