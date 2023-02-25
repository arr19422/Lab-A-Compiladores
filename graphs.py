import graphviz

def to_graphviz(nfa):
    """Generate DOT language code for the NFA."""
    dot = graphviz.Digraph()

    for state in nfa.states:
        dot.node(str(id(state)), label=state.label or "", shape="circle", style="bold" if state.accepting else "")

        for symbol, transitions in state.transitions.items():
            for dest_state in transitions:
                dot.edge(str(id(state)), str(id(dest_state)), label=symbol if symbol is not None else "ε")

    return dot.source

def render_graphviz(dot_source):
    """Render the NFA as an image using Graphviz."""
    dot = graphviz.Source(dot_source)
    dot.format = "png"
    return dot.render()