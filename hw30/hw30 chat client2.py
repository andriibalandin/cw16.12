import socket
import threading

host = "localhost"
port = 12345


def message_receive(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(message)
        except Exception as e:
            print("З'єднання розірвано", e)
            break


def launch():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except:
        print("Не вдалося підключитися")
        return
    threading.Thread(target=message_receive, args=(client,), daemon=True).start()
    while True:
        message = input()
        try:
            client.send(message.encode())
            if message == "exit":
                break
        except:
            print("Помилка надсилання повідомлення.")
            break
    client.close()


launch()
