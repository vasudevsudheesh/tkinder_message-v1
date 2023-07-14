import socket
from tkinter import Tk, Entry, Button, Listbox, END


def send(listbox, entry, client):
    message = entry.get()
    listbox.insert(END,'clientout:' + message)
    entry.delete(0, END)
    client.send(bytes( message, 'utf-8'))


def receive(listbox, client):
    message = client.recv(100).decode('utf-8')
    listbox.insert(END, 'Serverin: ' + message)


root = Tk()

entry = Entry(root)
entry.pack()

listbox = Listbox(root)
listbox.pack()

send_button = Button(root, text='Send', command=lambda: send(listbox, entry, client))
send_button.pack()

receive_button = Button(root, text='Receive', command=lambda: receive(listbox, client))
receive_button.pack()

HOST_NAME = socket.gethostname()
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST_NAME, PORT))

root.mainloop()
