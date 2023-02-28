from transition import *
from automata import *

# ref: https://github.com/niemaattarian/Thompsons-Construction-on-NFAs
# ref: https://github.com/OJP98/py-finite-automata

# Thomspson's algorithm for postfix expressions


def thomspson(postfix):
    stack = []
    counter = 0

    for c in postfix:
        if (c != '(') and (c != ')') and (c != '*') and (c != '|') and (c != '.'):
            # si el caracter a evaluar no es un operador, creamos un automata con un estado inicial y final
            state1 = str(counter)
            state2 = str(counter+1)
            states = [state1, state2]
            counter += 2
            transitions = [Transition(start=state1, transition=c, end=state2)]
            automata = Automata(q=states, expression=c, alphabet=[
                c], q0=state1, f=state2, transitions=transitions)
            stack.append(automata)
        else:

            if (c == '.'):
                # si el caracter a evaluar no es un operador ., que es concatenación, creamos un automata con un estado inicial y final

                element2 = stack.pop()
                element1 = stack.pop()
                new_transitions = []
                element2_transitions = []

                for transition in element2.transitions:
                    if transition.start == element2.q0:
                        new_transitions.append(Transition(
                            start=element1.f, transition=transition.transition, end=transition.end))
                    else:
                        element2_transitions.append(transition)

                old_transitions = element1.transitions + element2_transitions
                current_transitions = old_transitions + new_transitions

                old_states = element1.q + element2.q
                current_states = []

                for state in old_states:
                    if state != element2.q0:
                        current_states.append(state)

                current_expression = '(' + element1.expression + \
                    '.' + element2.expression + ')'
                current_alphabet = element1.alphabet + element2.alphabet

                automata = Automata(q=current_states, expression=current_expression, alphabet=current_alphabet,
                                    q0=element1.q0, f=element2.f, transitions=current_transitions)
                stack.append(automata)

            if (c == '|'):
                # si el caracter a evaluar no es un operador |, que es un or, creamos un automata con un estado inicial y final

                element2 = stack.pop()
                element1 = stack.pop()
                initial_state = str(counter)
                final_state = str(counter+1)
                counter += 2
                transition1 = Transition(
                    start=initial_state, transition='ε', end=element1.q0)
                transition2 = Transition(
                    start=initial_state, transition='ε', end=element2.q0)
                transition3 = Transition(
                    start=element1.f, transition='ε', end=final_state)
                transition4 = Transition(
                    start=element2.f, transition='ε', end=final_state)

                old_transitions = element1.transitions + element2.transitions
                new_transitions = [transition1,
                                   transition2, transition3, transition4]
                current_transitions = old_transitions + new_transitions

                old_states = element1.q + element2.q
                new_states = [initial_state, final_state]
                current_states = old_states + new_states

                current_expression = '(' + element1.expression + \
                    '|' + element2.expression + ')'
                current_alphabet = element1.alphabet + element2.alphabet
                automata = Automata(q=current_states, expression=current_expression, alphabet=current_alphabet,
                                    q0=initial_state, f=final_state, transitions=current_transitions)
                stack.append(automata)

            if (c == '*'):
                # si el caracter a evaluar no es un operador *, creamos un automata con un estado inicial y final
                element = stack.pop()
                initial_state = str(counter)
                final_state = str(counter+1)
                counter += 2
                transition1 = Transition(
                    start=initial_state, transition='ε', end=element.q0)
                transition2 = Transition(
                    start=element.f, transition='ε', end=final_state)
                transition3 = Transition(
                    start=initial_state, transition='ε', end=final_state)
                transition4 = Transition(
                    start=element.f, transition='ε', end=element.q0)

                old_transitions = element.transitions
                new_transitions = [transition1,
                                   transition2, transition3, transition4]
                current_transitions = old_transitions + new_transitions

                old_states = element.q
                new_states = [initial_state, final_state]
                current_states = old_states + new_states

                current_expression = '(' + element.expression + ')*'
                current_alphabet = element.alphabet

                automata = Automata(q=current_states, expression=current_expression, alphabet=current_alphabet,
                                    q0=initial_state, f=final_state, transitions=current_transitions)
                stack.append(automata)

    # Imprimir el automata
    last = stack.pop()
    for state in last.q:
        print(state + ', ')

    last.alphabet = unique(last.alphabet)
    for char in last.alphabet:
        print(char + ', ')

    for transition in last.transitions:
        print('('+transition.start+', '+transition.transition+', '+transition.end+'), ')
    return (last)

# Referencia de codigo https://www.geeksforgeeks.org/python-get-unique-values-list/


def unique(alphabet):
    # insertar la lista en el conjunto
    list_set = set(alphabet)
    # Convierte a lista la lista anterior
    unique_list = (list(list_set))
    return unique_list
