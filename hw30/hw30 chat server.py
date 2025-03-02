import json
import socket
import threading

host = 'localhost'
port = 12345

clients = {}


def load_users():
    try:
        with open("chat_users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_users(users):
    with open("chat_users.json", "w") as file:
        json.dump(users, file)


registered_users = load_users()


def send_to_everyone(message, server_client=None):
    for client in list(clients.keys()):
        if client != server_client:
            try:
                client.send(message.encode())
            except:
                client.close()
                del clients[client]


def translation(client_socket):
    try:
        client_socket.send("Введіть логін: ".encode())
        username = client_socket.recv(1024).decode().strip()
        client_socket.send("Введіть пароль: ".encode())
        password = client_socket.recv(1024).decode().strip()
        if username in registered_users:
            if registered_users[username] != password:
                client_socket.send("Невірний пароль, відключення".encode())
                client_socket.close()
                return
        else:
            registered_users[username] = password
            save_users(registered_users)
            client_socket.send("Успішна регістрація".encode())
        client_socket.send("Ви приєдналися до чату. напишіть 'exit' для виходу".encode())
        clients[client_socket] = username
        print(f"{username} приєднався до чату")
        send_to_everyone(f"{username} приєднався до чату", client_socket)

        while True:
            message = client_socket.recv(1024).decode().strip()
            if not message or message == "exit":
                break
            print(f"{username}: {message}")
            send_to_everyone(f"{username}: {message}", client_socket)
    except Exception as e:
        print(f"Помилка {e}")
    finally:
        if client_socket in clients:
            print(f"{clients[client_socket]} вийшов")
            send_to_everyone(f"{clients[client_socket]} вийшов", )
            try:
                del clients[client_socket]
            except KeyError:
                pass
        client_socket.close()


def launch():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Сервер {host}:{port} працює")

    while True:
        client_socket, addr = server_socket.accept()
        threading.Thread(target=translation, args=(client_socket,), daemon=True).start()


launch()
