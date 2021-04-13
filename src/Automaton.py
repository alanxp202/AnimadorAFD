from transition import Transition

class Automaton:
    def __init__(self,name:str, word:list, transitions:list):
        self.name = name
        self.word = word
        self.transitions = transitions
        self.initials = []
        self.finals = []
        self.start_initials()
        self.start_finals()


    def get_name(self):
        return self.name


    def start_initials(self):

        for transition in self.transitions:
            if transition.get_origin().is_initial() and transition.get_origin() not in self.initials:
                self.initials.append(transition.get_origin())

            if transition.get_goal().is_initial() and transition.get_goal() not in self.initials:
                self.initials.append(transition.get_goal())


    def start_finals(self):

        for transition in self.transitions:
            if transition.get_origin().is_final() and transition.get_origin() not in self.finals:
                self.finals.append(transition.get_origin())

            if transition.get_goal().is_final() and transition.get_goal() not in self.finals:
                self.finals.append(transition.get_goal())


    def reach(self, word):

        reach = []
        for i in self.transitions:
            if i.get_origin() in self.initials and i.get_name() == word[0]:
                reach.append(i.get_goal().get_name())
        
        return reach

    def walk(self):
        
        reach(self, word)
