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

# Вывод словаря
print("Словарь стран и их столиц:")
for country, capital in countries_capitals.items():
    print(f"{country}: {capital}")

print(f"\nВсего стран в словаре: {len(countries_capitals)}")
