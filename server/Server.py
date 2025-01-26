from _thread import *
import sys
from player import Patient
import pickle
import random
import socket
from constants import *
import json

# server = "10.122.247.13"
server = "localhost"
port = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server, port))
except socket.error as e:
    print(str(e))

server_socket.listen()
print("Waiting for a connection, Server Started")

# List of players - dynamically growing as players connect
PATIENT_DATA = dict()
MAX_PATIENTS = 5  # You want to support at least 5 players

def threaded_client(conn, data):
    # # Send the initial position of the current player
    # conn.send(pickle.dumps(PATIENT_DATA[patient]))
    patient = data['name']
    while True:
        try:
            # # Receive data from the client and update player
            PATIENT_DATA[patient] = data

            if not data:
                print(f"Player {patient} disconnected")
                break

            # Send the updated data of all players to the current player
            reply = {k:v for k,v in PATIENT_DATA.items() if not(k == patient)}
            reply_data = json.dumps(reply).encode('utf-8')
            if len(reply) > 0:
                conn.sendall(reply_data)
            else:
                conn.sendall(json.dumps({"EMPTY": 1}).encode('utf-8'))
            # conn.sendall(pickle.dumps(reply))

        except Exception as e:
            print(f"Error in thread for player {patient}: {e}")
            break

    print(f"Lost connection with player {patient}")
    conn.close()


current_patient = 0

try:
    while True:
        client_socket, client_address = server_socket.accept()
        
        data = client_socket.recv(4096).decode('utf-8')
        print("Received from client: ", data)
        data = json.loads(data)

        if current_patient < MAX_PATIENTS:
            start_new_thread(threaded_client, (client_socket, data))
            current_patient += 1

        # # Only allow up to max_players to connect
        # if currentPlayer < MAX_PATIENTS:
        #     # Create a new player with a random position and random color
        #     # x, y = random_position()
        #     # color = random_color()

        #     # p = Patient("Bob", PLAYER_WIDTH, PLAYER_HEIGHT, [0,0], XLIM, YLIM)
        #     # p0_spritesheet = '/Users/Ritchie/Desktop/U4 Winter/mchacks/McHacks-12/server/graphics/16PixelSlime/BlueSlime/BlueSlimeWalking-Sheet.png'
        #     # n_frames = 4
        #     # p.init_sprite(p0_spritesheet, n_frames, SPRITE_RATE, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SCALE)
        #     # PATIENT_DATA.append(p)

        #     start_new_thread(threaded_client, (conn, currentPlayer))
        #     currentPlayer += 1
        # else:
        #     print("Max players reached. Closing connection.")
        #     conn.sendall(b"Server is full")
        #     conn.close()

except KeyboardInterrupt:
    print("Server interrupted by user")
finally:
    server_socket.close()
