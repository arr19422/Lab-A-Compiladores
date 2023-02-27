import graphviz

def to_graphviz(nfa):
    """Generate DOT language code for the NFA."""
    dot = graphviz.Digraph()

    dot.node(str(id(nfa.q0)), label=nfa.q0 or "", shape="circle", style="bold" if nfa.q0 else "")
    dot.node(str(id(nfa.f)), label=nfa.f or "", shape="circle", style="bold" if nfa.f else "")

    for transition in nfa.transitions:
        dot.edge(str(transition.start), str(transition.end), label=str(transition.transition))
    return dot.source

def render_graphviz(dot_source):
    """Render the NFA as an image using Graphviz."""
    dot = graphviz.Source(dot_source)
    dot.format = "png"
    return dot.render()
