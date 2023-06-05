# testFile.py
from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_Car():
    car0 = Car("A", "A", 2018, 18000)
    car1 = Car("A", "A", 2018, 18000)
    car2 = Car("B", "B", 2018, 50000)
    car3 = Car("C", "C", 2022, 40000)
    car4 = Car("C", "C", 2014, 25000)
    car5 = Car("C", "A", 2014, 25000)
    car6 = Car("D", "D", 2021, 25000)
    car7 = Car("D", "D", 2021, 10000)

    assert car1 < car2
    assert car3 > car2
    assert car4 < car3
    assert car6 > car7
    assert car0 == car1
