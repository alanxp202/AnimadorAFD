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


    def get_initials(self, start = ''):
        
        if start == '':
            for i in self.initials:
                return i
        else:
            for i in self.initials:
                if i.get_name() == start:
                    return i


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


    def get_reach(self, state_origin ,word):

        for t in self.transitions:
            if t.get_name() == word[0] and t.get_origin() == self.initials[0]:
                print(t.to_string())
                return t.get_goal()


