from state import State

class Transition:
    def __init__(self, name:str, origin:State, goal:State):
        self.name = name
        self.origin = origin
        self.goal = goal

    def get_name(self):
        return self.name


    def get_origin(self):
        return self.origin


    def set_origin(self, origin:State):
        self.origin = origin


    def get_goal(self):
        return self.goal


    def set_goal(self, goal:State):
        self.goal = goal


    def to_string(self):
        return f'{self.origin.get_name()} {self.name} > {self.goal.get_name()}'