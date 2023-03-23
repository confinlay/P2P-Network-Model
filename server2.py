import socket
import threading
import time

HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5051
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
file_found = False
location_found = False
file = ""

# bind the ADDR to the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Generates a list of files on this server, as well as the locations of a few files not on this server.
files = {"A fallen leaf" : "A trusting little leaf of green, \nA bold audacious frost; \nA rendezvous, a kiss or two, \nAnd youth for ever lost. \nAh, me! \nThe bitter, bitter cost. \n\nA flaunting patch of vivid red, \nThat quivers in the sun; \nA windy gust, a grave of dust, \nThe little race is run. \nAh, me! \nWere that the only one.", "Camouflaged" : "A trusting little leaf of green, \nA bold audacious frost; \nA rendezvous, a kiss or two, \nAnd youth for ever lost. \nAh, me! \nThe bitter, bitter cost. \n\nA flaunting patch of vivid red, \nThat quivers in the sun; \nA windy gust, a grave of dust, \nThe little race is run. \nAh, me! \nWere that the only one."}
file_locations = {"Nothing gold can stay" : "1", "Little baby" : "5", "The dark days will pass" : "5", "Drowning" : "3", "Marigold" : "6"} 

# Handle a client.
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.") 

    connected = True
    while connected :
        file_found = location_found = False
        # Receive and decode the header, which contains the message length.
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            # Receive a message from the client.
            msg = conn.recv(msg_length).decode(FORMAT)
            # If disconnect message recieved, disconnect from client
            if msg == DISCONNECT_MESSAGE:
                connected = False
            # Check if requested file is on this server
            for x in files:
                if msg == x:
                    file_found = True
                    file = x
            # Check if location of requested file is on this server.
            for x in file_locations :
                if msg == x :
                    location_found = True
                    location = x
            # Respond with appropriate message
            if file_found:
                conn.send(f"\nFILE FOUND:\n\n{files[file]}\n".encode(FORMAT))
            elif location_found == True : 
                conn.send(f"\nFILE LOCATED AT PEER {file_locations[location]}, TRY CONNECTING THERE.\n".encode(FORMAT))
            elif msg == DISCONNECT_MESSAGE:
                conn.send(f"\nDISCONNECT REQUEST RECIEVED.".encode(FORMAT))
            else :
                conn.send(f"\nFILE UNKNOWN. TRY MY NEAREST NEIGHBOUR PEER 3.\n".encode(FORMAT))



def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # When a new connection occurs..
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # Start a new thread to handle a new client 
        thread.start() 
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()