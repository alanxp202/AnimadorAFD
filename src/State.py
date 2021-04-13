class State:
    def __init__(self, name:str, is_initial:bool, is_final:bool):
        self.name = name
        self.is_initial = is_initial
        self.is_final = is_final


    def get_name(self):
        return self.name