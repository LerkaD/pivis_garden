from PlantClass import MainClass

class Carrot(MainClass):
    def __init__(self, coordinates, garden):
        super().__init__(garden)
        self.parameters = {
            "type_id": 1,
            "name": "carrot",
            "symbol_on_map": "C",
            "age": 0,
            "coordinates": coordinates,
            "max_age": 8,
            "life_points": 100,
            "points_to_grow_up": 12,
            "start_points": 0
        }

    def aging(self):
        self.parameters["age"] += 1
        if self.parameters["age"] >= self.parameters["max_age"]:
            return self
        else:
            return None

    def get_position(self):
        x = self.parameters["coordinates"][0]
        y = self.parameters["coordinates"][1]
        position = (x, y)
        return position

    def grow_up(self):
        self.parameters["start_points"] += 3
        if self.parameters["points_to_grow_up"] <= self.parameters["start_points"] and self.parameters["life_points"] > 5:
            return self
        else:
            return None

    def opportunity_to_live(self):
        if self.parameters["life_points"] <= 0:
            return self
        else:
            return None

