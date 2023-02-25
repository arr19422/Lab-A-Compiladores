# Automata class
class Automata:
    def __init__(self, q, expression, alphabet, q0, f, transitions):
        self.q = q
        self.expression = expression
        self.alphabet = alphabet
        self.q0 = q0
        self.f=f
        self.transitions = transitions