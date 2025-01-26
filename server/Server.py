from _thread import *
import sys
from Player import Player
import pickle
import random
import socket

server = "10.122.247.13"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen()
print("Waiting for a connection, Server Started")

# List of players - dynamically growing as players connect
players = []
max_players = 5  # You want to support at least 5 players

# Helper function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Helper function to generate a random position near the center
def random_position():
    center_x = 250  # Center of the screen width
    center_y = 250  # Center of the screen height
    max_distance = 100  # Max distance from the center
    x = random.randint(center_x - max_distance, center_x + max_distance)
    y = random.randint(center_y - max_distance, center_y + max_distance)
    return (x, y)

def threaded_client(conn, player):
    # Send the initial position of the current player
    conn.send(pickle.dumps(players[player]))

    while True:
        try:
            # Receive data from the client and update player
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print(f"Player {player} disconnected")
                break

            # Send the updated positions of all players to the current player
            reply = [players[i] for i in range(len(players)) if i != player]

            print(f"Received from player {player}: {data}")
            print(f"Sending to player {player}: {reply}")

            # Send the reply back to the client
            conn.sendall(pickle.dumps(reply))

        except Exception as e:
            print(f"Error in thread for player {player}: {e}")
            break

    print(f"Lost connection with player {player}")
    conn.close()


currentPlayer = 0

try:
    while True:
        conn, addr = s.accept()
        print("Connected to: ", addr)

        # Only allow up to max_players to connect
        if currentPlayer < max_players:
            # Create a new player with a random position and random color
            x, y = random_position()
            color = random_color()
            players.append(Player(x, y, 50, 50, color))  # Starting position and random color for new player
            start_new_thread(threaded_client, (conn, currentPlayer))
            currentPlayer += 1
        else:
            print("Max players reached. Closing connection.")
            conn.sendall(b"Server is full")
            conn.close()

except KeyboardInterrupt:
    print("Server interrupted by user")
finally:
    s.close()
