class TheWeather:
    parameters = {
        "counter_for_plants": 0,
        "counter_for_pests": 0,
    }

    def __init__(self, world=None):
        if world is not None:
            self.world = world

    def get_counters(self):
