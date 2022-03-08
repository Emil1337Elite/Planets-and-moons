
class Planet:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.moons = []

    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size
    
    def get_moons(self):
        return self.moons
    
    def add_moons(self, moons):
        self.moons.append(moons)

    def print_moons(self):
        print(self.name)
        for moon in self.moons:
            print(moon.get_name())

class Moons:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.orbits = None

    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size

    def add_orbit(self, orbit):
        self.orbit = orbit
        
    def get_orbit(self):
        return self.orbits