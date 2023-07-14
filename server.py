import socket
from tkinter import Tk, Entry, Listbox, Button, END


def send(listbox, entry, client):
    message = entry.get()
    listbox.insert(END, 'serverout:'+message)
    entry.delete(0, END)
    client.send(bytes(message, 'utf-8'))


def recieve(listbox, client):
    message_from_client = client.recv(50)
    listbox.insert(END, 'clientin:' + message_from_client.decode("utf-8"))


root = Tk()

entry = Entry()
entry.pack(side='bottom')
listbox = Listbox(root)
listbox.pack()

button = Button(root, text='Send', command=lambda: send(listbox, entry, client))
button.pack(side='bottom')

rbutton = Button(root, text='Receive', command=lambda: recieve(listbox, client))
rbutton.pack(side='bottom')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))
s.listen(4)

client, address = s.accept()

root.mainloop()
