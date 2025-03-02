import socket
import threading

HOST = 'localhost'
PORT = 12345


def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                print("З'єднання закрито сервером.")
                break
            print(msg)
        except Exception as e:
            print("Помилка прийому:", e)
            break


def launch():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except Exception as e:
        print("Не вдалося підключитися до сервера:", e)
        return

    threading.Thread(target=receive_messages, args=(s,), daemon=True).start()

    while True:
        try:
            message = input()
            if message.lower() == "exit":
                s.sendall(message.encode())
                break
            if message:
                s.sendall(message.encode())
        except Exception as e:
            print("Помилка відправлення даних:", e)
            break
    s.close()


launch()
