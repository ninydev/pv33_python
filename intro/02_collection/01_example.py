# Приклад 01: особливості роботи Python з колекціями

numbers = [7, 2, 9, 4, 2, 8, 1, 5]

# 1) Обхід колекції через for
# Тут ми просто проходимо по кожному елементу списку
print("Обхід через for:")
for n in numbers:
    print(n)

# 2) Обхід "засобами колекції" — list comprehension
# Це зручний спосіб створити новий список на основі старого
print("\nКвадрати чисел через list comprehension:")
squares = [n * n for n in numbers]
print(squares)

# 3) Пошук елемента
# Перевіряємо, чи є число в списку
print("\nПошук елемента:")
target = 4
if target in numbers:
    print(f"Число {target} знайдено")
else:
    print(f"Число {target} не знайдено")

# 4) Пошук першого парного числа
# Зручно використовувати генератор і next()
print("\nПошук першого парного числа:")
first_even = next((n for n in numbers if n % 2 == 0), None)
print(first_even)

# 5) Сортування
# sorted() повертає новий список, а не змінює оригінал
print("\nСортування:")
sorted_numbers = sorted(numbers)
print("Оригінал:", numbers)
print("Відсортований:", sorted_numbers)

# Сортування у зворотному порядку
sorted_desc = sorted(numbers, reverse=True)
print("За спаданням:", sorted_desc)

# 6) Слайси (slices)
# Слайс дозволяє брати частину списку
print("\nСлайси:")
print("Перші 3 елементи:", numbers[:3])
print("З 3-го до 5-го:", numbers[2:5])
print("Кожен другий елемент:", numbers[::2])
print("У зворотному порядку:", numbers[::-1])

# 7) Приклад зі словником
# Для словників часто працюють через keys(), values(), items()
print("\nРобота зі словником:")
user = {"name": "Olena", "age": 25, "city": "Kyiv"}

print("Ключі:")
for key in user.keys():
    print(key)

print("Значення:")
for value in user.values():
    print(value)

print("Пари ключ-значення:")
for key, value in user.items():
    print(f"{key} = {value}")

# 8) Приклад з множиною
# Set зберігає лише унікальні значення
print("\nМножина:")
unique_numbers = set(numbers)
print(unique_numbers)

# Швидка перевірка наявності елемента в множині
print(2 in unique_numbers)