# class Pizzeria:
#     def __init__(self, dough, sauce, toppings):
#         self.dough = dough
#         self.sauce = sauce
#         self.toppings = toppings
#
#     def prepare(self):
#         print("Готовим пиццу...")
#     def bake(self):
#         print("Выпекаем пиццу...")
#     def cut(self):
#         print("Разрезаем пиццу...")
#     def package(self):
#         print("Упаковываем пиццу...")
#
# class Order:
#     def __init__(self):
#         self.pizzas = []
#
#     def add_pizza(self, pizza):
#         self.pizzas.append(pizza)
#
#     def calculate_total(self):
#         total = 0
#         for pizza in self.pizzas:
#             total += pizza.price
#         return total
#
#
# class Terminal:
#     def __init__(self):
#         self.menu = {
#             1: Pizzeria("Пеперони тесто", "Пеперони соус", ["пеперони"]),
#             2: Pizzeria("Барбекью тесто", "Барбекью соус", ["бекон", "лук", "ананас"]),
#             3: Pizzeria("ДарыМоря тесто", "ДарыМоря соус", ["креветка", "кальмары", "моллюски"])
#         }
#
#     def display_menu(self):
#         print("MENU:")
#         for index, pizza in self.menu.items():
#             print(f"{index}. {pizza.dough} {pizza.sauce} {pizza.toppings}")
#
#     def create_order(self):
#         order = Order()
#         while True:
#             self.display_menu()
#             selected_pizza = int(input("Выберите пиццу из меню (введите число): "))
#             order.add_pizza(self.menu[selected_pizza])
#
#             more_pizzas = input("Хотите добавить еще пиццы в свой заказ? (да/нет): ")
#             if more_pizzas.lower() != "да":
#                 break
#
#         print("Заказ подтвержден!")
#         total = order.calculate_total()
#         print(f"Общая сумма: {total} USD")
#
#         payment = float(input("Введите сумму платежа: "))
#         if payment >= total:
#             print("Оплата получена. Спасибо!")
#             order.process()
#         else:
#             print("Недостаточная оплата. Заказ отменен.")
#
#
# terminal = Terminal()
# terminal.create_order()









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
