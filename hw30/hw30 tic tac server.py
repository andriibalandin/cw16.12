import socket
import threading

HOST = 'localhost'
PORT = 12345

clients = []
symbols = {}
board = [" "] * 9
current_turn = "X"
lock = threading.Lock()


def print_board():
    display = ""
    for i in range(9):
        if board[i] == " ":
            display += str(i + 1)
        else:
            display += board[i]
        if i % 3 != 2:
            display += " | "
        else:
            display += "\n"
            if i != 8:
                display += "---------\n"
    return display


def check_win():
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return True
    return False


def broadcast(message):
    global clients
    disconnected = []
    for client in clients:
        try:
            client.sendall(message.encode())
        except Exception as e:
            print("Помилка:", e)
            disconnected.append(client)
    for dc in disconnected:
        if dc in clients:
            clients.remove(dc)


def handle_client(client, symbol):
    global board, current_turn
    try:
        client.sendall(f"Ви граєте як {symbol}\n".encode())
    except:
        return
    while True:
        try:
            data = client.recv(1024)
            data = data.decode().strip()
            if data.lower() == "exit" or not data:
                print(f"Клієнт {symbol} відключився.")
                broadcast(f"Гравець {symbol} відключився. Гра завершена.\n")
                client.close()
                break
            with lock:
                if symbol != current_turn:
                    try:
                        client.sendall("Не ваш хід. Чекайте свого ходу.\n".encode())
                    except:
                        pass
                    continue
                try:
                    pos = int(data)
                except ValueError:
                    try:
                        client.sendall("Введіть число від 1 до 9 або 'finish'\n".encode())
                    except:
                        pass
                    continue

                if pos < 1 or pos > 9:
                    try:
                        client.sendall("Невірний номер клітинки. Введіть число від 1 до 9.\n".encode())
                    except:
                        pass
                    continue

                pos -= 1
                if board[pos] != " ":
                    try:
                        client.sendall("Ця клітинка вже зайнята. Спробуйте інший хід.\n".encode())
                    except:
                        pass
                    continue

                board[pos] = symbol
                board_str = print_board()
                broadcast(f"Гравець {symbol} зробив хід.\n{board_str}\n")

                if check_win():
                    broadcast(f"Гравець {symbol} переміг!\n")
                    board = [" "] * 9
                    current_turn = "X"
                    broadcast("Нова гра починається. Гравець X ходить першим.\n")
                    broadcast(print_board())
                    continue
                elif " " not in board:
                    broadcast("Нічия!\n")
                    board = [" "] * 9
                    current_turn = "X"
                    broadcast("Нова гра починається. Гравець X ходить першим.\n")
                    broadcast(print_board())
                    continue

                current_turn = "O" if current_turn == "X" else "X"
                broadcast(f"Черга гравця {current_turn}\n")
        except ConnectionResetError:
            print(f"Клієнт {symbol} розірвав з'єднання.")
            broadcast(f"Гравець {symbol} розірвав з'єднання. Гра завершена.\n")
            break
        except Exception as e:
            print(f"Помилка в клієнті {symbol}: {e}")
            break
    try:
        client.close()
    except:
        pass


def launch():
    global clients
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(2)
    print("Очікуємо двох гравців...")

    client1, addr1 = s.accept()
    print("Перший гравець підключився:", addr1)
    clients.append(client1)
    symbols[client1] = "X"
    client1.sendall("Ви ініціювали гру як X. Чекаємо другого гравця...\n".encode())

    client2, addr2 = s.accept()
    print("Другий гравець підключився:", addr2)
    clients.append(client2)
    symbols[client2] = "O"

    broadcast("Гра починається. Введіть 'exit' для виходу\n")
    broadcast(f"Черга гравця {current_turn}\n")
    broadcast(print_board())

    threading.Thread(target=handle_client, args=(client1, "X"), daemon=True).start()
    threading.Thread(target=handle_client, args=(client2, "O"), daemon=True).start()

    while True:
        pass
        s.close()

launch()
