**Simple Real Time Chat App using Python Sockets + TKinter**

**Introduction**

This is a simple python script used to configure a chat server for inter-client communication over a network. This is achieved by integrating the socket and threading classes of python to control incoming connection, process client message and distribute it on every connected client. This document explains the nature of the script, its operations, and its uses.

**Script Structure**

The code begins by importing the required modules: socket and threading. These involve some of the most crucial aspects regarding the management of network communication and the establishment of many connections happening concurrently. A class named ChatServer encompasses the essence of the script.

**ChatServer Class**

Properties:

host: The IP address in which the server is running, this is how it will be addressed and where it will be accessed. This can be customized at initialisation of a server.
port: Likewise the port attribute represents the port that the server will listen to incoming connections.
connected_clients: This is a table, which includes, all the active client sockets that are currently connected to the server.
server_socket: Server_socket refers to the main socket that connects between the server and clients.

Methods:

1. __init__(self, host, port): It is the constructor which initializes a server instance given a host and port.
2. start(self): The server socket is initialized in the start method followed by binding it to the mentioned host and port, and finally starting to listen for any incoming connections. On connection by a client, one thread is started to take care of it.
3. accept_connections(self): This is an iterative method that will listen on new incoming client connections that may have existed before. A different thread handles each connection so that many clients can communicate concurrently.
4. handle_client(self, client_socket, client_address): Handle_client is a function that deals with communication with a particular client. The server repeatedly monitors messages sent by the client, processes them, and publishes it on a broad scale of clients that are online.
5. disconnect_client(self, client_socket, client_address): This method is known as when a client breaks off and does some clean-up before removing the client’s socket from the list of connected clients.
6. broadcast_message(self, sender_socket, message): The broad-scast_message method is a function that makes one client send a message into all the other clients but the sender.

**Script Usage**

The script’s main execution is in the final section with the if __name__ == “__main__” block. Here you give the host IP address (host_ip) and also provide the port number (port_number) of the server. Once these parameters are defined, the ChatServer is subsequently created and the start call made to commence the server.

**How it Works**

The chat server operates as follows:

A socket is initiated in the server, which binds to the designated IP address and port.
It is a continuous listener and accepts new client connection each time it arrives. For multiple clients communicating without a problem, each client connection is handled within its own thread.
The handle_client method processes information for every customer and sends as well as receives messages to and from them.
The disconnect_client function takes away the client socket from the set of connected clients, thereby closing the client socket.

The code also encompasses the client side functionality on top of the server side implementation. The following paragraph describes the client-side script that makes a connection to the chatting server and creates a GUI for interactive messages, utilizing the Tkinter library.

**Client-Side Code Overview**

The client-side code is mainly involved in providing a user interface for users to communicate with the servers and the other connected clients. Here's a breakdown of the functionalities:

**Establishing Connection**

A client or client or client-side script initializes a socket that is subsequently connected to the specified server’s or client’s IP address/port. It means that the client can communicate with the server via this connection.

**Tkinter GUI Creation**

The script utilizes Tkinter to create a GUI window that consists of several components:

Chat Window: Displays the conversation messages between the client and the server (i.e., shows sent as well as received messages).

Message Entry Field: Enables one give their message to a server.

Send Button: Sends messages sent into the text field.

**Sending Messages**

The send_message operation implements the procedure for transmitting messages from an end to a point. The send button gets the message from the entry field, posts that message into the chat window, ships to the server, and finally empties the entry field ready for a new one.

**Receiving Messages**

The receive_message function constantly monitors messages from the server. It shows on a chat window any message coming from the server or another client connected.

**Threading**

Thread handling is used by the code in taking control of messages arriving in the background. Creates another thread called recv_thread which is always listening to messages and never blocks the main GUI operation for allowing of continuous message reception.

**Client-Server Interaction**

Client- or server-side scripts also known as web scripts interact each other exchanging data messages (Send or receive). The server-side logic ensures that messages received from the client are passed onto the server, which subsequently forwards them to all the connected clients. In a similar way, the client also receives messages only that the messages are sent by the server on behalf of other clients.




