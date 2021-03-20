from Transition import Transition

class Automaton:
    def __init__(self, name:str, transitions:Transition):
        self.name = name
        self.transitions = transitions