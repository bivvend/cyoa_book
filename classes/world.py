import race 
class World:
    '''
    Class for storing global information about the world
    '''
    def __init__(self, name, lore_text):
        self.name = name
        self.lore_text = lore_text
        self.races = {}

    def add_race(self, name, description, home_region):
        self.races[name] = race.Race(name, description, home_region)
