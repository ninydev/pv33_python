# Список городов для первого множества (с повторами)
cities_list_1 = [
    "Tokyo", "Delhi", "Shanghai", "Sao Paulo", "Mexico City", "Kiev"
    "Cairo", "Mumbai", "Beijing", "Dhaka", "Osaka",
    "New York", "Karachi", "Buenos Aires", "Chongqing", "Istanbul",
    "Kolkata", "Manila", "Lagos", "Rio de Janeiro", "Tianjin",
    "Kinshasa", "Guangzhou", "Los Angeles", "Moscow", "Shenzhen",
    "Lahore", "Bangalore", "Paris", "Bogota", "Jakarta",
    "Tokyo", "Delhi", "Shanghai", "Moscow", "Paris"  # Повторы внутри списка
]

# Список городов для второго множества (с повторами)
cities_list_2 = [
    "Moscow", "Shenzhen", "Lahore", "Bangalore", "Paris",
    "Bogota", "Jakarta", "Chennai", "Lima", "Bangkok",
    "Seoul", "Nagoya", "Hyderabad", "London", "Tehran",
    "Chicago", "Chengdu", "Nanjing", "Wuhan", "Ho Chi Minh City",
    "Luanda", "Ahmedabad", "Kuala Lumpur", "Xi'an", "Hong Kong",
    "Dongguan", "Hangzhou", "Berlin", "Madrid", "Rome",
    "Moscow", "London", "Berlin", "Jakarta", "Seoul"  # Повторы внутри списка
]


set_1 = set(cities_list_1)
set_2 = set(cities_list_2)



# 1 ----------------------------------------
print("содержащее названия, которые есть в обоих множествах")
cities1 = set_1 & set_2
print(cities1, "\n")

# 2 ----------------------------------------
print("содержащее названия, которые есть в первом множестве, но нет во втором")
cities2 = set_1 - set_2
print(cities2, "\n")

#3 ----------------------------------------
print("содержащее названия, которые есть во втором множестве, но нет в первом")
cities3 = set_2 - set_1
print(cities3, "\n")

#4 ----------------------------------------
print("Необходимо создать третье множество, содержащее уникальные названия для каждого множества.")
unique_cities = set_1 ^ set_2
print(unique_cities, "\n")
print(cities2 | cities3, "\n")