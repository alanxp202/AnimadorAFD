from State import State

class Transition:
    def __init__(self, name:str, origin:State, goal:State):
        self.name = name
        self.origin = origin
        self.goal = goal