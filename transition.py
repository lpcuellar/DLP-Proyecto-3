class Transition:
    def __init__(self, start = None, transition = None, end = None):
        self.start = start
        self.transition = transition
        self.end = end
    
    def set_start(self, start):
        self.start = start
    
    def set_end(self, end):
        self.end = end