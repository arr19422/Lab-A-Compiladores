# Transitions for thompson algorithm
class Transition:
    def __init__(self, start, transition, end):
        self.start = start
        self.transition = transition
        self.end = end
    
    def start(self, start):
        self.start = start

    def end(self, end):
        self.end = end