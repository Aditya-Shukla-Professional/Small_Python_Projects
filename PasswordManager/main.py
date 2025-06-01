from tkinter import *
from tkinter import messagebox
import pyperclip
import random

FILE=r"DAY29\passwords.txt"
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    try:
        with open(FILE,"r") as file:
            main_data=file.readlines()
            web=web_entry.get()
            for line in main_data:
                if (web!="") and (web.lower() in line.lower()):
                    passcode=line.split("|")[2].strip()
                    mail=line.split("|")[1].strip()
                    messagebox.showinfo(title=web,message=f"Email: {mail}\nPassword: {passcode}")
    except FileNotFoundError:
        with open(FILE,"w") as file:
            pass
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', '.', '<', '>', '/', '?', '`', '~']
password=""
for _ in range(5):
    password+=alphabets[random.randint(0,len(alphabets)-1)]
for _ in range(5):
    password+=num[random.randint(0,len(num)-1)]
for _ in range(5):
    password+=symbols[random.randint(0,len(symbols)-1)]

def shuffle(s):
    word=list(s)
    random.shuffle(word)
    shuffled_list="".join(word)
    return shuffled_list
def password_generator():
    pass_entry.delete(0,"end")
    pass_entry.insert(0,shuffle(password))
# ---------------------------- SAVE PASSWORD ------------------------------- #
def pass_save():
    email=email_entry.get()
    passw=pass_entry.get()
    if email!="" and passw!="" and web_entry.get()!="":
        popup=messagebox.askquestion("confirmation",f"Email: {email}\nPassword: {passw}\nIs this ok?")
        if popup=="yes":
            with open(FILE,"a") as file:
                file.write(f"{web_entry.get()} | {email} | {passw}\n")
            pyperclip.copy(passw)
    else:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(width=200,height=189)
pass_img=PhotoImage(file=r"DAY29\logo.png")
canvas.create_image(100,95,image=pass_img)
canvas.grid(row=0,column=1)

website=Label(text="Website:")
website.grid(row=1,column=0)

web_entry=Entry(width=20)
web_entry.grid(row=1,column=1)

search_btn=Button(text="Search",command=search)
search_btn.config(padx=30)
search_btn.grid(row=1,column=2)

emailuser=Label(text="Email/Username:")
emailuser.grid(row=2,column=0)

email_entry=Entry(width=40)
email_entry.insert(0,"lalitshuklapiyus@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)

pass_label=Label(text="Password:")
pass_label.grid(row=3,column=0)

pass_entry=Entry()
pass_entry.grid(row=3,column=1)

gen_btn=Button(text="Generate Password",command=password_generator)
gen_btn.grid(row=3,column=2)

add=Button(text="Add",padx=100,command=pass_save)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()