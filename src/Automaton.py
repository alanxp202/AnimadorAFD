from transition import Transition

class Automaton:
    def __init__(self,name:str, word:list, transitions:list):
        self.name = name
        self.word = word
        self.transitions = transitions
        self.initials = []
        self.finals = []
        self.steps = []
        self.start_initials()
        self.start_finals()


    def get_name(self):
        return self.name


    def get_steps(self):
        return self.steps


    def get_transitions(self):
        return self.transitions


    def get_states(self):

        result = []
        for t in self.transitions:
            if t.get_origin() not in result:
                result.append(t.get_origin())
            if t.get_goal() not in result:
                result.append(t.get_goal())
        
        return result


    def get_initials(self, start = ''):
        
        if start == '':
            for i in self.initials:
                return i.get_origin()
        else:
            for i in self.initials:
                if i.get_origin().get_name() == start:
                    return i.get_origin()


    def get_initials_list(self):

        finals_list =[]
        for i in self.initials:
            finals_list.append(i.get_origin())

        return finals_list


    def get_finals(self, end = ''):
        
        if end == '':
            for f in self.finals:
                return f.get_goal()
        else:
            for f in self.finals:
                if f.get_goal().get_name() == end:
                    return f.get_goal()


    def get_finals_list(self):

        finals_list =[]
        for f in self.finals:
            finals_list.append(f.get_goal())

        return finals_list


    def start_initials(self):

        for transition in self.transitions:
            if transition.get_origin().is_initial() and transition.get_origin() not in self.initials:
                self.initials.append(transition)

            if transition.get_goal().is_initial() and transition.get_goal() not in self.initials:
                self.initials.append(transition)


    def start_finals(self):

        for transition in self.transitions:
            if transition.get_origin().is_final() and transition.get_origin() not in self.finals:
                self.finals.append(transition)

            if transition.get_goal().is_final() and transition.get_goal() not in self.finals:
                self.finals.append(transition)


    def get_reach(self, state ,word):
        
        for t in self.transitions:
            if t.get_origin()== state and t.get_name() == word[0]:
                self.steps.append (t)
                return t.get_goal()