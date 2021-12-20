from tkinter import *
import ascord

root = Tk()
root.title("AstroCord by Kavin Jindal")
root.configure(background='black')
root.resizable(width=False, height=False)
root.geometry("500x700")
font_head = 50
font_normal = 20
label1 = Label(root, text="AstroCord", font=("Helvetica", font_head), bg='black', fg='white')
label1.pack()

b_label = Label(root, text="Enter the bot's name:", font=("Helvetica", font_normal), bg='black', fg='white')
b_label.pack()

bot_name = Entry(root, font=("Helvetica", font_normal), bg='black', fg='white')
bot_name.pack()

p_label = Label(root, text="\nEnter the prefix", font=("Helvetica", font_normal), bg='black', fg='white')
p_label.pack()

prefix = Entry(root, font=("Helvetica", font_normal), bg='black', fg='white')
prefix.pack()

t_label = Label(root, text="\nEnter the token", font=("Helvetica", font_normal), bg='black', fg='white')
t_label.pack()

token = Entry(root, font=("Helvetica", font_normal), bg='black', fg='white')
token.pack()


btn = Button(root, text="Generate Bot with Cogs", font=("Helvetica", font_normal), bg='white', fg='black', command=lambda: ascord.as_cogs(bot_name.get(), prefix.get(), token.get()))
btn.pack(pady=20)

btn2 = Button(root, text="Generate single script Bot", font=("Helvetica", font_normal), bg='white', fg='black', command=lambda: ascord.ncord(bot_name.get(), prefix.get(), token.get()))
btn2.pack()

root.mainloop()