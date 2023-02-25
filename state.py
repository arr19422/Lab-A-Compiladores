class State:
    """A state in the NFA."""
    def __init__(self, label=None):
        self.label = label
        self.accepting = False
    