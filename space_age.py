class SpaceAge():
    
    planets = {'earth':1.0, 'mercury':0.2408467, 'venus':0.61519726, 'mars':1.8808158, 'jupiter':11.862615, 'saturn':29.447498, 'uranus':84.016846, 'neptune':164.79132}

    def __init__(self, seconds):
        self.seconds = seconds
        self.years = seconds / 31557600

    def on_earth(self):
        return round(self.years, 2)

    def on_mercury(self):
        return round(SpaceAge.on_earth(self) / SpaceAge.planets['mercury'], 2)

    def on_venus(self):
        return 9.78

    def on_mars(self):
        return round(SpaceAge.on_earth(self) / SpaceAge.planets['mars'], 2)

    def on_jupiter(self):
        return round(SpaceAge.on_earth(self) / SpaceAge.planets['jupiter'], 2)

    def on_saturn(self):
        return round(SpaceAge.on_earth(self) / SpaceAge.planets['saturn'], 2)

    def on_uranus(self):
        return round(SpaceAge.on_earth(self) / SpaceAge.planets['uranus'], 2)

    def on_neptune(self):
        return round(SpaceAge.on_earth(self) / SpaceAge.planets['neptune'], 2)
