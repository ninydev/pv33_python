# Приклад 02: робота з множинами (set) у Python

# Множина — це колекція:
# - без дублікатів
# - без гарантованого порядку
# - дуже швидка для перевірки наявності елемента

# 1) Створення множини
# Дублікати автоматично прибираються
numbers = {1, 2, 3, 3, 4, 5, 5, 6}
print("Множина numbers:", numbers)

# 2) Створення множини з list
# Часто потрібно прибрати повтори зі списку
raw_list = [10, 20, 20, 30, 30, 30, 40]
unique_values = set(raw_list)
print("\nСписок з дублями:", raw_list)
print("Унікальні значення:", unique_values)

# 3) Додавання елементів
# add() додає один елемент
print("\nДодавання елементів:")
unique_values.add(50)
unique_values.add(20)  # не додасться повторно
print(unique_values)

# 4) Додавання кількох елементів
# update() додає одразу декілька значень
print("\nДодавання кількох елементів:")
unique_values.update([60, 70, 70, 80])
print(unique_values)

# 5) Видалення елементів
# remove() викликає помилку, якщо елементу немає
print("\nВидалення елементів:")
unique_values.remove(20)
print("Після remove(20):", unique_values)

# discard() безпечніший — не викликає помилку, якщо елемента немає
unique_values.discard(999)
print("Після discard(999):", unique_values)

# pop() видаляє довільний елемент
# Оскільки множина не впорядкована, неможливо передбачити який саме
popped_item = unique_values.pop()
print("Видалений елемент через pop():", popped_item)
print("Після pop():", unique_values)

# 6) Перевірка наявності елемента
# Це одна з найсильніших сторін множини
print("\nПеревірка наявності:")
print(30 in unique_values)
print(999 in unique_values)

# 7) Обхід множини через for
# Порядок обходу може бути будь-яким
print("\nОбхід множини через for:")
for item in unique_values:
    print(item)

# 8) Використання множини для видалення дублікатів зі списку
# Це дуже частий сценарій
names = ["anna", "ivan", "olena", "ivan", "anna", "petro"]
print("\nСписок імен:", names)
print("Унікальні імена:", set(names))

# 9) Операції над множинами
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\nМножина a:", a)
print("Множина b:", b)

# Об'єднання множин
# Можна через union() або |
print("Об'єднання:", a.union(b))
print("Об'єднання через |:", a | b)

# Перетин множин
# Елементи, які є в обох множинах
print("Перетин:", a.intersection(b))
print("Перетин через &:", a & b)

# Різниця множин
# Елементи, які є тільки в a
print("Різниця a - b:", a.difference(b))
print("Різниця через -:", a - b)

# Симетрична різниця
# Елементи, які є лише в одній з множин
print("Симетрична різниця:", a.symmetric_difference(b))
print("Симетрична різниця через ^:", a ^ b)

# 10) Перевірка підмножини та надмножини
print("\nПідмножина / надмножина:")
small = {2, 3}
big = {1, 2, 3, 4, 5}

print("small ⊆ big:", small.issubset(big))
print("big ⊇ small:", big.issuperset(small))

# 11) Оновлення множини іншою множиною
# update() змінює поточну множину
print("\nОновлення множини:")
c = {100, 200}
c.update({200, 300, 400})
print(c)

# 12) Frozen set — незмінна множина
# Використовується, коли потрібна множина, яку не можна змінити
print("\nFrozen set:")
immutable_set = frozenset([1, 2, 2, 3, 4])
print(immutable_set)

# 13) Практичний приклад: пошук спільних тегів
# Зручно для порівняння наборів даних
post_tags_1 = {"python", "collections", "set", "tutorial"}
post_tags_2 = {"python", "django", "set", "backend"}

common_tags = post_tags_1 & post_tags_2
print("\nСпільні теги:", common_tags)

# 14) Практичний приклад: пошук унікальних тегів
all_tags = post_tags_1 | post_tags_2
print("Усі теги без повторів:", all_tags)

# 15) Практичний приклад: теги, які є тільки в першому наборі
only_first = post_tags_1 - post_tags_2
print("Тільки в першому наборі:", only_first)

# 16) Практичний приклад: швидке очищення від повторів
# Наприклад, коли дані прийшли з форми або з файлу
emails = [
    "a@example.com",
    "b@example.com",
    "a@example.com",
    "c@example.com",
    "b@example.com",
]
unique_emails = list(set(emails))
print("\nEmail з дублями:", emails)
print("Email без дублювання:", unique_emails)

# Важливо:
# Якщо потрібен стабільний порядок після видалення дублікатів,
# краще використовувати спеціальні підходи, а не просто set()