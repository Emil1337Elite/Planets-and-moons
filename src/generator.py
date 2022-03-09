from resources import Planet, Moons
from random import choice, randint

planet_names = ["Cato Neimoidia", "Moraband", "Mustafar", "Reach", "Charum Hakkor", "Sanghelios"]
moon_name = ["Endor", "Nequiquam", "Illizar", "Ulamaza", "Kutmoria", "Lom", "Opturion", "Belsana"]

def create_planets():
    name = choice(planet_names)
    size = randint(5000,200000000)

    planet2=Planet(name,size)

    for i in range (randint(1,6)):
        name = choice(moon_name)
        size = randint(500,2300000)
        moon = Moons(name,size)
        planet2.moons.append(moon)

    return planet2 