import socket
from threading import Thread
import tkinter as tk

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the server's IP address and port
host_ip = "192.168.141.187"
port_number = 5050

# Connect to the server
client_socket.connect((host_ip, port_number))

# Create the Tkinter GUI window
window = tk.Tk()
window.title("Chat with: " + host_ip + ":" + str(port_number))

# Text area for displaying chat messages
txt_messages = tk.Text(window, width=50, height=20)
txt_messages.pack(padx=10, pady=10)

# Entry field for typing messages
txt_your_message = tk.Entry(window, width=50)
txt_your_message.insert(0, "Your message")
txt_your_message.pack(pady=10)

# Function to send messages to the server
def send_message():
    client_message = txt_your_message.get()
    if client_message:
        txt_messages.insert(tk.END, "You: " + client_message + "\n")
        client_socket.send(client_message.encode("utf-8"))
        txt_your_message.delete(0, tk.END)

# Button to send messages
btn_send_message = tk.Button(window, text="Send", width=20, command=send_message)
btn_send_message.pack(pady=10)

# Function to receive and display messages from the server
def receive_message():
    while True:
        server_message = client_socket.recv(1024).decode("utf-8")
        if not server_message:
            break
        txt_messages.insert(tk.END, "Server: " + server_message + "\n")

# Create a thread to receive messages from the server
recv_thread = Thread(target=receive_message)
recv_thread.daemon = True
recv_thread.start()

# Start the Tkinter GUI
window.mainloop()
