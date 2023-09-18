class Pizzeria:
    def __init__(self, dough, sauce, toppings):
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def prepare(self):
        print("Готовим пиццу...")
    def bake(self):
        print("Выпекаем пиццу...")
    def cut(self):
        print("Разрезаем пиццу...")
    def package(self):
        print("Упаковываем пиццу...")

class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_total(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.price
        return total


class Terminal:
    def __init__(self):
        self.menu = {
            1: Pizzeria("Пеперони тесто", "Пеперони соус", ["пеперони"]),
            2: Pizzeria("Барбекью тесто", "Барбекью соус", ["бекон", "лук", "ананас"]),
            3: Pizzeria("ДарыМоря тесто", "ДарыМоря соус", ["креветка", "кальмары", "моллюски"])
        }

    def display_menu(self):
        print("MENU:")
        for index, pizza in self.menu.items():
            print(f"{index}. {pizza.dough} {pizza.sauce} {pizza.toppings}")

    def create_order(self):
        order = Order()
        while True:
            self.display_menu()
            selected_pizza = int(input("Выберите пиццу из меню (введите число): "))
            order.add_pizza(self.menu[selected_pizza])

            more_pizzas = input("Хотите добавить еще пиццы в свой заказ? (да/нет): ")
            if more_pizzas.lower() != "да":
                break

        print("Заказ подтвержден!")
        total = order.calculate_total()
        print(f"Общая сумма: {total} USD")

        payment = float(input("Введите сумму платежа: "))
        if payment >= total:
            print("Оплата получена. Спасибо!")
            order.process()
        else:
            print("Недостаточная оплата. Заказ отменен.")


terminal = Terminal()
terminal.create_order()









import random

print("Добро пожаловать в игру камень, ножницы, бумага!")
def main():
    player_score = 0
    computer_score = 0

    # Цикл для 3 рануда
    for round in range(3):
        # Выбор пользователя
        player_choice = input("Выберите: камень (1), ножницы (2) или бумагу (3): ")
        player_choice = int(player_choice)

        # Выбор компьютера
        computer_choice = random.randint(1, 3)

        # Определение победителя
        if player_choice == 1 and computer_choice == 2:
            player_score += 1
        elif player_choice == 2 and computer_choice == 3:
            player_score += 1
        elif player_choice == 3 and computer_choice == 1:
            player_score += 1
        else:
            computer_score += 1

    # Вывод результатов
    print("Итоги игры:")
    print(f"Игрок: {player_score}")
    print(f"Компьютер: {computer_score}")

    # Определение победителя
    if player_score > computer_score:
        print("Победил игрок!")
    elif player_score < computer_score:
        print("Победил компьютер!")
    else:
        print("Ничья!")


if __name__ == "__main__":
    main()











import random


def main():
    # Инициализация переменных
    words = ["python", "java", "javascript", "html", "css"]
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0

    # Игра
    while wrong_guesses < 6:
        # Вывод загаданного слова с пробелами вместо неизвестных букв
        print(" ".join(["_" if letter not in guessed_letters else letter for letter in word]))

        # Получение буквы от игрока
        guess = input("Введите букву: ")

        # Проверка буквы
        if guess in word:
            guessed_letters.append(guess)

            # Проверка, выиграл ли игрок
            if all([letter in guessed_letters for letter in word]):
                print("Вы выиграли!")
                return
        else:
            wrong_guesses += 1

        # Вывод количества оставшихся попыток
        print("Осталось попыток:", 6 - wrong_guesses)

    # Вывод проигрыша
    print("Вы проиграли!")
    print("Загаданное слово:", word)


if __name__ == "__main__":
    main()







import random


def main():
    # Инициализация переменных
    number = random.randint(1, 100)
    guesses = 0

    # Игра
    while True:
        # Получение числа от игрока
        guess = input("Введите число от 1 до 100: ")
        guess = int(guess)

        # Проверка числа
        if guess < number:
            print("Загаданное число больше.")
        elif guess > number:
            print("Загаданное число меньше.")
        else:
            print("Вы угадали! Загаданное число было", number)
            break

        guesses += 1

    # Вывод количества попыток
    print("Вы угадали за", guesses, "попыток.")


if __name__ == "__main__":
    main()



















import random


def main():
    # Инициализация переменных
    questions = [
        {"question": "Сколько кубков лиги чемпионов у Реал Мадрида?", "answer": "14"},
        {"question": "В каком году был основан Реал Мадрид?", "answer": "1902"},
        {"question": "Как называется домашний стадион Реала Мадрида?", "answer": "Сантиагу Бернабеу"},
        {"question": "В основном какой лиге играет Реал Мадрид?", "answer": "Ла Лига"},
        {"question": "Сколько золотых мячей у Криштиану Роналду?", "answer": "5"},
    ]
    score = 0

    # Игра
    for question in questions:
        # Вывод вопроса
        print(question["question"])

        # Получение ответа от игрока
        answer = input("Ваш ответ: ")

        # Проверка ответа
        if answer == question["answer"]:
            print("Правильно!")
            score += 1
        else:
            print("Неправильно! Правильный ответ:", question["answer"])

    # Вывод итогов
    print("Ваш результат:", score, "правильных ответов.")


if __name__ == "__main__":
    main()



















