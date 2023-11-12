import socket
from threading import Thread

#Server
class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected_clients = set()
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server is running on {self.host}:{self.port}")
        self.accept_connections()

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.connected_clients.add(client_socket)
            print(f"Connection established with: {client_address[0]}:{client_address[1]}")
            client_thread = Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()

    def handle_client(self, client_socket, client_address):
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                self.disconnect_client(client_socket, client_address)
                break
            print(f"{client_address[0]}:{client_address[1]}: {message}")
            self.broadcast_message(client_socket, f"{client_address[0]}:{client_address[1]}: {message}")

    def disconnect_client(self, client_socket, client_address):
        self.connected_clients.remove(client_socket)
        print(f"{client_address[0]}:{client_address[1]} disconnected")
        client_socket.close()

    def broadcast_message(self, sender_socket, message):
        for client_socket in self.connected_clients:
            if client_socket is not sender_socket:
                client_socket.send(message.encode("utf-8"))

if __name__ == "__main__":
    host_ip = "192.168.141.187"
    port_number = 5050

    chat_server = ChatServer(host_ip, port_number)
    chat_server.start()
