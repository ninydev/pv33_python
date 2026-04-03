# Словарь: Страна -- Столица
countries_capitals = {
    "Ukraine": "Kiev",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "Japan": "Tokyo",
    "China": "Beijing",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "Egypt": "Cairo",
    "Australia": "Canberra",
    "South Africa": "Pretoria",
    "Argentina": "Buenos Aires",
    "Mexico": "Mexico City",
    "Turkey": "Ankara",
    "South Korea": "Seoul",
    "Thailand": "Bangkok"
}

# # Вывод словаря
# print("Словарь стран и их столиц:")
# for country, capital in countries_capitals.items():
#     print(f"{country}: {capital}")
#
# print(f"\nВсего стран в словаре: {len(countries_capitals)}")


# Нужно реализовать функциональность по добавлению, удалению, поиску и замене.

def add_country():
    country = input("Введите название страны: ")
    capital = input("Введите столицу страны: ")
    if country in countries_capitals:
        print(f"Страна {country} уже существует в словаре.")
    else:
        countries_capitals[country] = capital
        print(f"Страна {country} с столицей {capital} успешно добавлена в словарь.")


def remove_country():
    country = input("Введите название страны для удаления: ")
    if country in countries_capitals:
        del countries_capitals[country]
        print(f"Страна {country} успешно удалена из словаря.")
    else:
        print(f"Страна {country} не найдена в словаре.")


def replace_capital():
    old_capital = input("Введите название столицы для замены: ")
    new_capital = input("Введите новое название столицы: ")
    if old_capital in countries_capitals.values():
        for country, capital in countries_capitals.items():
            if capital == old_capital:
                countries_capitals[country] = new_capital
                print(f"Столица {old_capital} успешно заменена на {new_capital} для страны {country}.")
                return
    else:
        print(f"Столица {old_capital} не найдена в словаре.")


def search_country():
    capital = input("Введите название столицы для поиска страны: ")
    for country, capital in countries_capitals.items():
        if capital == capital:
            print(f"Страна {country} имеет столицу {capital}.")
            return
    print(f"Столица {capital} не найдена в словаре.")


def search_capital():
    country = input("Введите название страны для поиска столицы: ")
    for country, capital in countries_capitals.items():
        if country == country:
            print(f"Страна {country} имеет столицу {capital}.")
            return
    print(f"Страна {country} не найдена в словаре.")


def print_all_countries():
    print("\nСписок всех стран в словаре:")
    for country, capital in countries_capitals.items():
        print(f"{country}: {capital}")


def echo_menu():
    """
    Выводит меню для работы с словарем стран и столиц.
    """
    print("\nМеню:")
    print("1. Добавить страну и столицу")
    print("2. Удалить страну")
    print("3. Заменить столицу")
    print("4. Найти страну по столице")
    print("5. Найти столицу по стране")
    print("6. Показать все страны и столицы")
    print("7. Выйти")


def exit_app():
    print("Программа завершена.")
    exit()


def run_menu():
    echo_menu()
    k = int(input("Выберите действие: "))

    switcher = {
        1: add_country,
        2: remove_country,
        3: replace_capital,
        4: search_country,
        5: search_capital,
        6: print_all_countries,
        7: exit_app
    }

    func = switcher.get(k, lambda: "Invalid choice")
    func()


if __name__ == "__main__":
    run_menu()