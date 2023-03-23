import socket

HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESSES = {"1": (SERVER, 5050), "2": (SERVER, 5051), "3": (SERVER, 5052), "4": (SERVER, 5053), "5": (SERVER, 5054), "6": (SERVER, 5055)}


while True :
    option = input("Enter the peer you would like to connect to, or type nothing to connect to your closest peer: ")
    # If the user types nothing, connect to peer 1
    if option == "" : option = "1"
    # Catch incorrect input
    while True:
        if option.isdigit():
            if(int(option) > 0 and int(option) < 7): break 
        print("\nERROR: please type a number between 1 and 6.\n")
        option = input("Enter the peer you would like to connect to, or type nothing to connect to your closest peer: ")

    # Creates client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connects to the server.
    client.connect(ADDRESSES[option])

    
    def send(msg):
        # Encodes message
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        # Sends a header to the server containing the length of the following message
        client.send(send_length)
        # Sends the message
        client.send(message)
        # Prints the response from the server
        print(client.recv(2048).decode(FORMAT))

    msg = input("Enter the title of the file you require, or type 'DISCONNECT' to disconnect from this peer:\n")
    while(msg != "DISCONNECT"):
        send(msg)
        msg = input("Enter the title of the file you require, or type 'DISCONNECT' to disconnect from this peer:\n")
    send(DISCONNECT_MESSAGE)
    print("Disconnected from server\n")
