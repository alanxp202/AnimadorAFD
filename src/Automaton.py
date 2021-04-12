from transition import Transition

class Automaton:
    def __init__(self, name:str, word:list, transitions:list, initials:list, finals:list):
        self.name = name
        self.word = word
        self.transitions = transitions
        self.initials = initials
        self.finals = finals