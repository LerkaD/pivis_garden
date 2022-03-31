from Trees import Trees1
from Vegetables import Carrot
from PestsClass import Pests
import random
class World:
    class Cell:
        coordinates = tuple()
        all_in_cell = list()#не только растения
        list_for_print = list()

        def __init__(self, coordinates):
            self._coordinates = coordinates
            self.all_in_cell = list()
            self.list_for_print = list()

        def add_plant_on_cell(self, plant):
            if len(self.all_in_cell) < 4:
                self.all_in_cell.append(plant)
                self.list_for_print.append(plant.parameters["symbol_on_map"])
            else:
                return

        def print_cell(self):
            if len(self.list_for_print) != 0:
                return self.list_for_print
            else:
                return "*"

        def remove_smth_from_cell(self, smth):
            self.all_in_cell.remove(smth)
            self.list_for_print.remove(smth.parameters["symbol_on_map"])

    game_map = list()
    map_size = tuple()
    plants = list()
    step = 0
    harvest_of_vegetables = 0
    harvest_of_apples = 0
    died_from_pests = 0
    died_from_hungry = 0

    def __init__(self, map_size):
        self.count_of_pests = None
        self.map_size = map_size
        for i in range(0, map_size[0]):
            row = list()
            for j in range(0, map_size[1]):
                row.append(World.Cell([i, j]))
            self.game_map.append(row)

    def find_plant_position(self):
        x = random.randint(0, self.map_size[0] - 1)
        y = random.randint(0, self.map_size[1] - 1)
        position = (x, y)
        return position

    def add_pests_on_game_map(self):
        new_plant = Pests(self.find_plant_position(), self)
        self.plants.append(new_plant)
        x = int(new_plant.parameters["coordinates"][0])
        y = int(new_plant.parameters["coordinates"][1])
        self.game_map[x][y].add_plant_on_cell(new_plant)

    def add_plant_on_game_map(self):
        new_plant = Carrot(self.find_plant_position(), self)
        self.plants.append(new_plant)
        x = int(new_plant.parameters["coordinates"][0])
        y = int(new_plant.parameters["coordinates"][1])
        self.game_map[x][y].add_plant_on_cell(new_plant)

    def add_trees_on_game_map(self):
        new_plant = Trees1(self.find_plant_position(), self)
        self.plants.append(new_plant)
        x = int(new_plant.parameters["coordinates"][0])
        y = int(new_plant.parameters["coordinates"][1])
        self.game_map[x][y].add_plant_on_cell(new_plant)

    def step_print(self):
        for row in self.game_map:
            for Cell in row:
                print(Cell.print_cell())
            print("")

    def aging_in_map(self):
        for smth in self.plants:
            smth = smth.aging()
            if smth is not None:
                self.plants.remove(smth)
                smth.get_position()
                x = int(smth.parameters["coordinates"][0])
                y = int(smth.parameters["coordinates"][1])
                self.game_map[x][y].remove_smth_from_cell(smth)

    def plants_grow_up(self):
        for smth in self.plants:
            if smth.parameters["type_id"] == 1:
                smth = smth.grow_up()
                if smth is not None:
                    self.harvest_of_vegetables += 1
                    self.plants.remove(smth)
                    smth.get_position()
                    x = int(smth.parameters["coordinates"][0])
                    y = int(smth.parameters["coordinates"][1])
                    self.game_map[x][y].remove_smth_from_cell(smth)

    def trees_grow_up(self):
        for tree in self.plants:
            if tree.parameters["type_id"] == 3:
                tree = tree.grow_up()
                if tree is not None:
                    self.harvest_of_apples += 1

    def eat_plant_on_map(self):
        for pests in self.plants:
            if pests.parameters["type_id"] == 2:
                pests.get_position()
                for plant_for_eat in self.plants:
                    if plant_for_eat.parameters["type_id"] == 1:
                        plant_for_eat.get_position()
                        if int(plant_for_eat.parameters["coordinates"][0]) == int(pests.parameters["coordinates"][0]) and int(plant_for_eat.parameters["coordinates"][1]) == int(pests.parameters["coordinates"][1]):
                            plant_for_eat = pests.attack_plant(plant_for_eat)
                            if plant_for_eat is not None:
                                self.died_from_pests += 1
                                self.plants.remove(plant_for_eat)
                                self.game_map[int(plant_for_eat.parameters["coordinates"][0])][int(plant_for_eat.parameters["coordinates"][1])].remove_smth_from_cell(plant_for_eat)

    def damage_trees_on_map(self):
        for pests in self.plants:
            if pests.parameters["type_id"] == 3:
                pests.get_position()
                for plant_for_eat in self.plants:
                    if plant_for_eat.parameters["type_id"] == 1:
                        plant_for_eat.get_position()
                        if int(plant_for_eat.parameters["coordinates"][0]) == int(pests.parameters["coordinates"][0]) and int(plant_for_eat.parameters["coordinates"][1]) == int(pests.parameters["coordinates"][1]):
                            plant_for_eat = pests.attack_plant(plant_for_eat)
                            if plant_for_eat is not None:
                                self.died_from_pests += 1
                                self.plants.remove(plant_for_eat)
                                self.game_map[int(plant_for_eat.parameters["coordinates"][0])][int(plant_for_eat.parameters["coordinates"][1])].remove_smth_from_cell(plant_for_eat)

    def opportunity_to_live_on_map(self):
        for smth in self.plants:
            if smth.parameters["type_id"] == 2:
                smth = smth.opportunity_to_live()
                if smth is not None:
                    smth.get_position()
                    x = int(smth.parameters["coordinates"][0])
                    y = int(smth.parameters["coordinates"][1])
                    self.game_map[x][y].remove_smth_from_cell(smth)
                    self.plants.remove(smth)
                    self.died_from_hungry += 1

    def every_days_hungry(self):
        for pests in self.plants:
            if pests.parameters["type_id"] == 2:
                pests.parameters["hungry"] = True

    def life_cycle(self):
        self.plants_grow_up()
        self.trees_grow_up()
        self.eat_plant_on_map()
        self.aging_in_map()
        self.opportunity_to_live_on_map()
        self.every_days_hungry()
        print("pests->deid", self.died_from_pests)
        print("hungry->died", self.died_from_hungry)
        print("vegetables", self.harvest_of_vegetables)
        print("fruits", self.harvest_of_apples)






