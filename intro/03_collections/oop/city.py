class City:
    """Класс, описывающий город"""

    def __init__(self, name="", region="", country="", population=0, postal_code="", phone_code=""):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def input_data(self):
        """Метод для ввода данных пользователем с клавиатуры"""
        self.name = input("Введите название города: ")
        self.region = input("Введите название региона: ")
        self.country = input("Введите название страны: ")
        try:
            self.population = int(input("Введите количество жителей: "))
        except ValueError:
            print("Ошибка: Население должно быть целым числом.")
            self.population = 0
        self.postal_code = input("Введите почтовый индекс города: ")
        self.phone_code = input("Введите телефонный код города: ")

    def display_data(self):
        """Метод для вывода данных на экран"""
        print("-" * 30)
        print(f"Информация о городе: {self.name}")
        print(f"Регион: {self.region}")
        print(f"Страна: {self.country}")
        print(f"Жителей: {self.population}")
        print(f"Почтовый индекс: {self.postal_code}")
        print(f"Телефонный код: {self.phone_code}")
        print("-" * 30)

    # Методы доступа к отдельным полям (геттеры и сеттеры)
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_region(self):
        return self.region

    def set_region(self, region):
        self.region = region

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_population(self):
        return self.population

    def set_population(self, population):
        self.population = population

    def get_postal_code(self):
        return self.postal_code

    def set_postal_code(self, postal_code):
        self.postal_code = postal_code

    def get_phone_code(self):
        return self.phone_code

    def set_phone_code(self, phone_code):
        self.phone_code = phone_code
