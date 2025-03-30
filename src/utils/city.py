class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def get_distance(self, city):
        return round(((self.x - city.x) ** 2 + (self.y - city.y) ** 2) ** 0.5)