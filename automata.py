class Automata:
    def __init__(self, exp):
        self.id = exp
        self.states = []

class State:
    def __init__(self, num, num2):
        self.id = num
        self.id2 = num2
        self.transitions = []
        self.accept = False
    pass

class Node:
    def __init__(self, type, value, first):
        self.type = type
        self.value = value
        self.first = first

    def __repr__(self):
        return f"{self.type} with value {self.value} and first {self.first}"