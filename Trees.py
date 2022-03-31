from PlantClass import MainClass

class Trees1(MainClass):
    def __init__(self, coordinates, garden):
        super().__init__(garden)
        self.parameters = {
            "type_id": 3,
            "name": "tree",
            "symbol_on_map": "T",
            "age": 0,
            "coordinates": coordinates,
            "max_age": 100,
            "life_points": 300,
            "points_to_grow_up": 14,
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
        self.parameters["start_points"] += 4
        if self.parameters["start_points"] >= self.parameters["points_to_grow_up"] and self.parameters["life_points"] > 170:
            self.parameters["start_points"] = 0
            return self

    def opportunity_to_live(self):
        if self.parameters["life_points"] <= 0:
            return self
        else:
            return None

