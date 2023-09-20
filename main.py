class Pizzeria:
    #Класс пицерии
    def __init__(self, dough, sauce, toppings):
    #Конструктор класса
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
    def prepare(self):
        #Готовим пиццу
        print("Готовим пиццу...")
    def bake(self):
        #Выпекаем пиццу
        print("Выпекаем пиццу...")
    def cut(self):
        #Разрезаем пиццу
        print("Разрезаем пиццу...")
    def package(self):
        #Упаковываем пиццу
        print("Упаковываем пиццу...")

class Order:
    #Класс заказа
    def __init__(self):
        #Конструктор класса.
        self.pizzas = []

    def add_pizza(self, pizza):
        #Добавляет пиццу в заказ.
        self.pizzas.append(pizza)

    def calculate_total(self):
        #Рассчитывает общую стоимость заказа
        total = 0
        for pizza in self.pizzas:
            total += pizza.price
        return total


class Terminal:
    #Класс терминала
    def __init__(self):
        #Конструктор класса
        self.menu = {
            1: Pizzeria("Пеперони тесто", "Пеперони соус", ["пеперони"]),
            2: Pizzeria("Барбекью тесто", "Барбекью соус", ["бекон", "лук", "ананас"]),
            3: Pizzeria("ДарыМоря тесто", "ДарыМоря соус", ["креветка", "кальмары", "моллюски"])
        }

    def display_menu(self):
        #Выводит меню
        print("MENU:")
        for index, pizza in self.menu.items():
            print(f"{index}. {pizza.dough} {pizza.sauce} {pizza.toppings}")

    def create_order(self):
        #Создает заказ
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





























