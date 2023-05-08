# Introduction
The following was a project I completed for a Computer Networks module at university. Below is a detailed report on the project, but you can skip to the end for instructions on how to demo the project. [Link to instructions](#instructions)

# Aim
The aim of this project was to develop a decentralised, distributed file transfer network capable of allowing nodes to access files from the broader internet by requesting them from their local peers. Inspired by IPFS, this simple model was designed with a specific use case in mind: Taiwan.

# Use Case 
Taiwan’s internet access is very vulnerable, as the island nation relies on a small number of underwater fibre-optic lines to connect it with the internet. In the increasingly likely scenario that Taiwan is engaged in conflict by China, analysts predict that China would likely target Taiwan’s cable landing stations, forcing Taiwan to spend it’s time restoring communication with the rest of the world rather than coordinating a defence strategy. 

In 2006 a number of Taiwan’s cables were cut as a result of an earthquake, and just this year Japanese repair operations on the Trans-Pacific express were halted by Chinese military drills, so the aforementioned worst case scenario is certainly not out of the question.

Low-orbit satellites (provided by Starlink) have been successfully used in Ukraine throughout their conflict with Russia to provide network access despite damaged or destroyed network infrastructure. Taiwan has a different problem, however, as it is not individual areas that may be cut off from the rest of the national network but instead the entire country that may be cut off from the rest of the world. 

Although Taiwan’s space agency has announced plans to develop low-Earth orbit satellite communications for the country, this will likely take years. While traditional geostationary satellite technology can maintain some level of internet access for the most pressing communication requirements, it is not likely to be able to provide sufficient internet speeds to a sufficient portion of the population. Since the national network may still remain connected internally, it was my proposition that a decentralised, distributed data fabric be used to extend this intermittent satellite connection to the entire network. 

# Functional Description
At a high-level, my model operates on a consistent request-response basis. This means that the client will, at every stage, decide which peer to connect to and will switch to a different peer if they wish depending on information given to them by the current peer. At a later stage of 
design, this redirecting would not be visible to the user. However, for demonstration purposes, connecting with peers will be a manual process. 



 The order of operations is as follows:
1)	User chooses a peer to connect to, a default option is available.
2)	User requests the file they want
3)	The peer responds in one of 3 ways:
  a.	The peer has the file and provides the contents of the file.
  b.	The peer does not have the file, but knows which other peers can provide the file.  It passes this information to the user.
  c.	The peer does not have the file and does not know where it is located. It recommends that the user try its nearest peer.
4)	The user either has the file they want, or must disconnect from the current peer and connect to a new one based on the advice given from the last peer.

# Algorithm

While my network is a peer-to-peer network, each peer will have a client and server script to run depending on its activities.

#### SERVER SIDE

* Server binds to a socket/address and listens.
* When a client attempts to connect, the server starts a new thread and runs the handle_client() subroutine.
* While the client is connected, the server waits to receive a message.
*	As long as the message received is not a disconnect message, the server assumes it is a file name.
*	The server checks the file name against its database of files and then against its database of file locations, updating the relevant Boolean variables as required.
*	The server sends back a message to the client, either with the content of the requested file, the peer which has the file, or a FILE NOT FOUND message along with the address of its closest peer.
*	The server will loop infinitely, listening for incoming clients and starting new threads to handle each connection.

#### CLIENT SIDE 

*	The following runs in an infinite loop:
*	The client creates a socket to receive data to.
*	(While in my ideal network each peer will know the addresses of a certain number of other peers and will be passed the addresses of peers not in its immediate network, in my demonstration model the client knows the addresses of all the peers on the network and will simply be passed information about which ones to connect to as it interacts with various peers.)
*	The client asks for the user to input the peer it wishes to connect to.
*	The client connects to this peer.
*	Loop:
*	The client asks the user to input a message for the server.
*	The send(msg) subroutine is called.
*	The header and subsequently the message are both encoded and sent to the server.
*	The client waits to receive a message from the server and prints this for the user.
*	The loop repeats until the until the user types DISCONNECT

# Implementation details

My model was implemented using socket programming in Python. This involved using the socket library built-in to the python programming language. The use of this library was minimal to my design, functions called were limited to socket binding, connecting client to peer and vice versa, and sending messages. All HTTP-style messaging and header configuration was done explicitly for this use case.

To model my distributed hash table as well as the locating, requesting, and receiving of files, I used the titles and contents of 12 poems as my key-value pairs. This means that the user requests a poem using its title and, if the peer has the file, it will return the contents of the poem via the command line. This decision was made so that my model was accessible for testing, and so that it was immediately obvious whether the network was functioning correctly or not. In a real-life application, these pairs would be replaced with actual files and corresponding hashes. 

While my video demo showcased my distributed network transferring files between 4 devices, my implementation is set up by default to run locally. This means that all 6 peers running the server script will be located at ports 5050-5055 on a single device, and the peer running the client script will be located on the same device. This can be easily changed by altering the database of peer addresses, as was done for my demo.

# Instructions
### Required downloads
**Python:** ensure you have the most recent version of python downloaded. This can be downloaded from the following link https://www.python.org/downloads/.

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
