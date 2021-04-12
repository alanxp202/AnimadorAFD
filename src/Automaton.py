from transition import Transition

class Automaton:
    def __init__(self, word:list, transitions:list, initials:list, finals:list):
        self.word = word
        self.transitions = transitions
        self.initials = initials
        self.finals = finals

    def start_trasitions(self):
        
        transicoes =[]

        for info in self.transitions:
            sep = info.split(' ')
            t = Transition(sep[1], sep[0], sep[3])
            print(t.to_string())

            transicoes.append(t)

    def to_string(self):
        
        return f'Palavra: {self.word}, Transições: {self.transitions}, Estados iniciais: {self.initials}, Estados finais: {self.finals}'