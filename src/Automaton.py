from Transition import Transition

class Automaton:
    def __init__(self, name:str, states:list, language:list, transitions:list, initials:list, finals:list):
        self.name = name
        self.states = states
        self.language = language
        self.transitions = transitions
        self.initials = initials
        self.finals = finals