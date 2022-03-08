from resources import  Planet, Moons

def main():
    tellus = Planet("Tellus", 510100000)
    mars = Planet("Mars", 144800000)
    jupiter = Planet("Jupiter", 61420000000)
    luna = Moons("Luna", 38000000)
    phobos = Moons("Phobos", 1548)
    deimos = Moons("Deimos", 495)
    ganymede = Moons("Ganymede", 87200000)
    callisto = Moons("Callisto", 73005000)

    luna.add_orbit(tellus)
    deimos.add_orbit(mars)
    phobos.add_orbit(mars)
    ganymede.add_orbit(jupiter)
    callisto.add_orbit(jupiter)

    tellus.add_moons(luna)
    mars.add_moons(deimos)
    mars.add_moons(phobos)
    jupiter.add_moons(ganymede)
    jupiter.add_moons(callisto)

    tellus.print_moons()
    mars.print_moons()
    jupiter.print_moons()

if __name__ == "__main__":
    main()