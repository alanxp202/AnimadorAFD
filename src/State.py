class State:
    def __init__(self, name:str, initial:bool, final:bool):
        self.name = name
        self.initial = initial
        self.final = final


    def get_name(self):
        return self.name


    def is_initial(self):
        return self.initial


    def is_final(self):
        return self.final