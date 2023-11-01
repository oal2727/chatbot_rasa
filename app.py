import tkinter
from tkinter import *
import requests

rasa_server_url = "http://192.168.0.8:5005/webhooks/rest/webhook"

def chatbot_response(msg):
    response = requests.post(rasa_server_url, json={"sender": "user", "message": msg})
    rasa_response = response.json()
    bot_response = rasa_response[0].get("text", "Bot: No se encontró una respuesta.")
    return bot_response

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Tú: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: \n " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


base = Tk()
base.title("ChatBot")
base.geometry("400x450")
base.resizable(width=FALSE, height=FALSE)
base.iconbitmap("logo.ico")

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Enviar", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )
# SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=3,
#                     bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
#                     command= send )
# SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=1,  # Ajusta el valor de height a 1
# bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
# command=send)

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
# EntryBox = Text(base, bd=0, bg="white",width="29", height="3", font="Arial")
# EntryBox = Text(base, bd=0, bg="white", width="29", height=1, font="Arial")  # Ajusta el valor de height a 1

#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
# EntryBox.place(x=128, y=401, height=90, width=265)
# SendButton.place(x=6, y=401, height=90)

EntryBox.place(x=120, y=401, height=40, width=260)
SendButton.place(x=6, y=401, height=40)

base.bind("<Return>", lambda event=None: SendButton.invoke())

base.mainloop()