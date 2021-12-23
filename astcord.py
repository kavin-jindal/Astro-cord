from tkinter import *
from tkinter import ttk
import ascord
from discord_webhook import DiscordWebhook
root = Tk()
root.geometry("500x700")
root.title("AstroCord by Kavin Jindal")
root.resizable(width=False, height=False)
tabControl = ttk.Notebook(root)
frame1 = Frame(tabControl, bg="black")
tab2 = Frame(tabControl, bg="black")
tabControl.add(frame1, text ='Discord Bot Generator')
tabControl.add(tab2, text ='Webhook Sender')
tabControl.pack(expand = 1, fill ="both")


def webhook(url, content):
    webhook = DiscordWebhook(url=url, content=content)
    sent_webhook = webhook.execute()


font_head = 50
font_normal = 20
label1 = Label(frame1, text="AstroCord", font=("Helvetica", font_head), bg='black', fg='white')
b_label = Label(frame1, text="Enter the bot's name:", font=("Helvetica", font_normal), bg='black', fg='white')
bot_name = Entry(frame1, font=("Helvetica", font_normal), bg='black', fg='white')
p_label = Label(frame1, text="\nEnter the prefix", font=("Helvetica", font_normal), bg='black', fg='white')
prefix = Entry(frame1, font=("Helvetica", font_normal), bg='black', fg='white')
t_label = Label(frame1, text="\nEnter the token", font=("Helvetica", font_normal), bg='black', fg='white')
token = Entry(frame1, font=("Helvetica", font_normal), bg='black', fg='white')
btn = Button(frame1, text="Generate Bot with Cogs", font=("Helvetica", font_normal), bg='white', fg='black', command=lambda: ascord.as_cogs(bot_name.get(), prefix.get(), token.get()))
btn2 = Button(frame1, text="Generate single script Bot", font=("Helvetica", font_normal), bg='white', fg='black', command=lambda: ascord.ncord(bot_name.get(), prefix.get(), token.get()))

# url
name_lab = Label(tab2, text="Enter the webhook name: ", font=("Helvetica", font_normal), bg='black', fg='white')
name = Entry(tab2, font=("Helvetica", font_normal), bg='black', fg='white')
head_label = Label(tab2, text="Webhooker", font=("Helvetica", font_head), bg='black', fg='white')
url_lab = Label(tab2, text="Enter the webhook url", font=("Helvetica", font_normal), bg='black', fg='white')
url = Entry(tab2, font=("Helvetica", font_normal), bg='black', fg='white')
text_lab = Label(tab2, text="Enter the text to send", font=("Helvetica", font_normal), bg='black', fg='white')
cont_label = Label(tab2, text="Enter the content to send", font=("Helvetica", font_normal), bg='black', fg='white')
content = Entry(tab2, font=("Helvetica", font_normal), bg='black', fg='white')
hook_btn = Button(tab2, text="Send", font=("Helvetica", font_normal), bg='white', fg='black', command=lambda: webhook(url.get(), content=content.get()) )

# alignment
label1.pack()
b_label.pack()
bot_name.pack()
p_label.pack()
prefix.pack()
t_label.pack()
token.pack()
btn.pack(pady=20)
btn2.pack()

# webhook
head_label.pack()
url_lab.pack()
url.pack()
#text_lab.pack()
cont_label.pack()
content.pack()
hook_btn.pack(pady=20)
root.mainloop()  