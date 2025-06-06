from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iphone 15 Pro", "+79111234567"),
    Smartphone("Samsung", "Galaxy S25", "+79219876543"),
    Smartphone("Sony", "Xperia 1 Mark V", "+79335557777"),
    Smartphone("Nubia", "Z70 Ultra", "+79889996677"),
    Smartphone("OnePlus", "11 Pro", "+79559998844")
]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model} - {smartphone.number}")
