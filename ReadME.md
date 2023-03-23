# Instructions
### Required downloads
**Python:**ensure you have the most recent version of python downloaded. This can be downloaded from the following link https://www.python.org/downloads/.

*That is all, everything is run from the command line. If you are on mac and macOS prompts you to install xCode dev tools when trying to run python scripts from the command line, you can instead run the scripts by right clicking on them in finder and selecting "open with Python Launcher"*.

### Setup instructions
You will need to open a total of 7 different terminal windows to fully test the code as it operates on 6 different servers. Although the demonstation video demoed file transfer between 4 nodes, the code is setup for testing on one device. Therefore, all 6 servers will run locally on ports 5050-5055 on your device.

##### Launching a server
1. Navigate to the directory containing the project code in your terminal (cd desktop, etc.).
2. Run the following command: "python3 server1.py" (If you have an older version of python, the command will simply be "python server1.py")
4. The server is now running. Nothing needs to be inputted by the user on the server side.
5. Repeat these steps in 5 more terminal windows, using file names "server2.py" - "server6.py".

##### Launching the client
1. Navigate to the directory containing the project code in your terminal (cd desktop, etc.).
2. Run the following command: "python3 client.py" (If you have an older version of python, the command will simply be "python client.py")
3. The client is now running. This only needs to be done once. All user inputs will be via this terminal window.

### Test instructions
- To connect to a peer, type a number between 1-6 when prompted to do so by the client script.
- When connected to a peer, you can request a file by typing the name of the file and pressing enter (ensure the first letter of the title is capitalised!).
- To disconnect from a peer, type "DISCONNECT" (all capitals).
##### Test cases
*You are free to request any file from the list in "queries.txt". A peer will either have a file, not have a file but know which peer does have it, or not have any information on the file and encourage the user to try the next peer. If you would like to test all 3 scenarios, the following steps can be taken:*

###### Test case 1

1. Type nothing in response to the first prompt from the client in order to connect to peer 1.
2. Request "Nothing gold can stay"
3. The peer will respond with the contents of the requested file.

###### Test case 2

1. Now, remaining connected to peer 1, request "Like the moon".
2. The peer will not have the file, but will know where the file is.
3. Type "DISCONNECT"
4. Enter the peer which was recommended by the previous peer (in this case it will be peer 4).
5. Request "Like the moon" again.
6. This peer will have the file.

###### Test case 3

1. Finally, remaining connected to peer 4, request "Camouflaged".
2. The peer will not have any information on the file and will prompt you to try the next nearest peer, peer 5.
3. Type "DISCONNECT"
4. Type 5 to connect to peer 5.
5. Request "Camouflaged".
6. The peer will not have the file, but will know where it's located.
7. Type "DISCONNECT"
8. Connect to the peer recommended by the previous peer (in this case peer 2).
9. Request "Camouflaged"
10. The peer will respond with the contents of the file.
