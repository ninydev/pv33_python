from garden_service import GardenService
from pitchfork import Pitchfork
from shovel import Shovel
from cultivator import Cultivator

def run_garden_job():
    # Демонструємо роботу з лопатою
    print("Сценарій 1: Класичне перекопування")
    shovel = Shovel()
    # Впроваджуємо лопату в сервіс
    service_with_shovel = GardenService(shovel)
    service_with_shovel.prepare_garden("Присадибна ділянка")

    # Демонструємо роботу з вилами
    print("Сценарій 2: Робота з пухким ґрунтом")
    pitchfork = Pitchfork()
    # Впроваджуємо вила в сервіс
    service_with_pitchfork = GardenService(pitchfork)
    service_with_pitchfork.prepare_garden("Клумба з квітами")

    # Демонструємо роботу з культиватором
    print("Сценарій 3: Автоматизація великої площі")
    cultivator = Cultivator()
    # Впроваджуємо культиватор в сервіс
    service_with_cultivator = GardenService(cultivator)
    service_with_cultivator.prepare_garden("Фермерське поле")

if __name__ == "__main__":
    run_garden_job()
