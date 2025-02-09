import threading
import random


def min_from_list(list):
    print(f"Найменьше значення - {min(list)}")


def max_from_list(list):
    print(f"Найбільше значення - {max(list)}")


def check_list():
    user_list = input("Ведіть числа через пробіл: ").split()
    try:
        user_list = [float(i) for i in user_list]
        return user_list
    except ValueError:
        print("Некоректні числа")
        return None


def threads():
    user_list = check_list()
    if user_list is None:
        return
    thr1 = threading.Thread(target=min_from_list, args=(user_list,))
    thr2 = threading.Thread(target=max_from_list, args=(user_list,))

    thr1.start()
    thr1.join()
    thr2.start()
    thr2.join()


#threads()


# ex 2

def find_even(nums):
    evens = [i for i in nums if i % 2 == 0]
    print(f"Парні - {evens}")
    with open("even nums.txt", "w") as file:
        file.write(" ".join(map(str, evens)))
    pass


def find_odd(nums):
    odds = [i for i in nums if i % 2 != 0]
    print(f"Непарні - {odds}")
    with open("odd nums.txt", "w") as file:
        file.write(" ".join(map(str, odds)))
    pass


def make_list():
    filename = input("Введіть назву файла: ")
    with open(filename, "r") as file:
        nums_list = file.readline().split()
        try:
            nums_list = [int(i) for i in nums_list]
            return nums_list
        except ValueError:
            print("Некоректні числа у файлі")
            return None


def threads2():
    nums = make_list()
    if nums is None:
        return
    thr1 = threading.Thread(target=find_even, args=(nums,))
    thr2 = threading.Thread(target=find_odd, args=(nums,))

    thr1.start()
    thr1.join()
    thr2.start()
    thr2.join()


threads2()

# ex 3

def find_word():
    filename = input("Введіть назву файла: ")
    user_word = input("Введіть слово для пошуку: ")
    with open(filename, "r") as file:
        file_text = file.read()
        position = file_text.find(user_word)
        if position == -1:
            print(f"Слово '{user_word}' не знайдено у файлі.")
        else:
            print(f"Слово '{user_word}' знайдено на позиції {position}.")


def thread3():
    thr = threading.Thread(target=find_word)

    thr.start()
    thr.join()


#thread3()

# ex 4

fill_event = threading.Event()
shared_numbers = []


def create_list(quantity):
    global shared_numbers
    shared_numbers = [random.randint(1, 100) for i in range(quantity)]
    print(f"Список чисел : {shared_numbers}")
    fill_event.set()


def find_sum():
    fill_event.wait()
    nums_sum = sum(shared_numbers)
    print(f"Сума чисел з списку : {nums_sum}")


def find_mean():
    fill_event.wait()
    if shared_numbers:
        mean = sum(shared_numbers) / len(shared_numbers)
        print(f"Середнє аріфметичне чисел з списку : {mean}")
    else:
        print("Список порожній, неможливо обчислити середнє врифметичне.")


def threads4():
    quantity = 10

    thr_create = threading.Thread(target=create_list, args=(quantity,))
    thr_sum = threading.Thread(target=find_sum)
    thr_mean = threading.Thread(target=find_mean)

    thr_create.start()
    thr_sum.start()
    thr_mean.start()

    thr_create.join()
    thr_sum.join()
    thr_mean.join()


#threads4()
