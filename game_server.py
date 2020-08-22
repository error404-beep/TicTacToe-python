# https://www.youtube.com/watch?v=3QiPPX-KeSc

import socket
import threading

import game_client

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'


# SOCK_STREAM uses TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_clinet(conn, addr):
    print(f'NEW CONNECTION {addr} connected')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f'{addr} {msg}')
            conn.send('Msg recieved'.encode(FORMAT))
    conn.close()


def start():
    server.listen(2)
    print(f'SERVER IS LISTENING ON {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clinet, args=(conn, addr))
        thread.start()
        print(f'ACTIVE CONNECTONS {threading.activeCount() - 1}')


    