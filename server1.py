import socket
import threading
import time

HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
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
files = {"Nothing gold can stay":"Nature's first green is gold,\nHer hardest hue to hold. \nHer early leaf's a flower; \nBut only so an hour. \nThen leaf subsides to leaf. \nSo Eden sank to grief, \nSo dawn goes down to day. \nNothing gold can stay.", "Underface":"Underneath my outside face\nhere's a face that none can see.\nA little less smiley,\nA little less sure,\nBut a whole lot more like me"}
file_locations = {"Like the moon" : "4", "In a station of a metro" : "6", "Someday" : "4", "Secrets under trees" : "3", "A fallen leaf" : "2"} 

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
                conn.send(f"\nFILE UNKNOWN. TRY MY NEAREST NEIGHBOUR PEER 2.\n".encode(FORMAT))



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