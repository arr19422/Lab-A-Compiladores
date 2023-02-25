from state import State

class NFA:
    """A non-deterministic finite automaton."""

    def __init__(self, start_state=None, accept_state=None):
        self.start_state = start_state or State()
        self.accept_state = accept_state or State()
        self.states = set()
        self.add_states(self.start_state, self.accept_state)

    def add_states(self, *states):
        """Add one or more states to the NFA."""
        for state in states:
            if state not in self.states:
                self.states.add(state)

    def add_transition(self, from_state, to_state, symbol):
        """Add a transition between two states on a symbol."""
        from_state.transitions.setdefault(symbol, set()).add(to_state)
