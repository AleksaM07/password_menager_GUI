from tkinter import *
from tkinter import messagebox
import random
import pyperclip
FONT_NAME = "Courier"


def dropdown(event):
    dropdown_menu.delete(0, "end") # clears our menu
    for entry in recent_entries[-2:]: # we are looping through our list nad getting two most recent hits
        dropdown_menu.add_command(label=entry, command=lambda: text_user.insert("end", entry)) # add_command(label, command)
    dropdown_menu.post(event.x_root, event.y_root) # we are opening our window at the position of our mouse

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    text_password.delete(0, END)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '!', '#', '$', '%', '&', "'", '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    lenght = random.randint(12, 20)
    new_word = ""
    for i in range(lenght):
        pos_letter = random.randint(0, 63)
        if pos_letter < 25:
            if random.randint(0, 100) > 50:
                new_word += alphabet[pos_letter].upper()
            else:
                new_word += alphabet[pos_letter]
        else:
            new_word += alphabet[pos_letter]
    text_password.insert(0, new_word)
    pyperclip.copy(new_word)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if text_website.get() == "" or text_user.get() == "" or text_password.get() == "":
        messagebox.showinfo(title="Window", message="Hey, please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title="Window",
                                       message=f"These are the details you entered: \nWebsite: {text_website.get()} \n"
                                               f"User: {text_user.get()} \n"
                                               f"Password: {text_password.get()}\nIs it okay to save?")

        if is_ok:
            with open("pmd.txt", mode="a") as file1, open("entries.txt", mode="a") as file2:
                file1.write(f"{text_website.get()} | {text_user.get()} | {text_password.get()}\n")
                file2.write(f"{text_user.get()}\n")
            text_website.delete(0, END)
            text_user.delete(0, END)
            text_password.delete(0, END)
            with open("entries.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    recent_entries.append(line.strip())
        else:
            text_website.focus()
            text_website.delete(0, END)
            text_user.delete(0, END)
            text_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pasword manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

text_website = Entry(width=50)
text_website.grid(row=1, column=1, columnspan=2)
text_website.focus()

label_user = Label(text="Email/Username:")
label_user.grid(row=2, column=0)

text_user = Entry(width=50)
text_user.grid(row=2, column=1, columnspan=2)
text_user.insert(0, "aleksa@gmail.com")

# making a dropdown menu for text_user
recent_entries = []
dropdown_menu = Menu(tearoff=0)
text_user.bind("<Button-3>", dropdown)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

text_password = Entry(width=31)
text_password.grid(row=3, column=1)

button_generate = Button(text="Generate Password", command=generate)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=43, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()