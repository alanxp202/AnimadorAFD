from state import State


class Transition:
    def __init__(self, name:str, origin:State, goal:State):
        self.name = name
        self.origin = origin
        self.goal = goal

    def to_string(self):
        
        return f'{self.origin} -{self.name}-> {self.goal}'