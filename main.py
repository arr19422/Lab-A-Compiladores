#Diego de Jesús Arredondo Turcios
#19422
#Laboratorio A

from funcs import check_expression_balanced, convertOE, expandEx, infixToPostfix
from thompson_algorithm import thomspson
from graphs import to_graphviz, render_graphviz


main_menu = '''
What would you like to do?
1 Create a DFN Graph
2 Exit out of the program
'''

option = input(main_menu)
flag = True

if option == '1':
    regex = input('Enter the regex: ')
    balanceRegex = check_expression_balanced(regex)
    
    if balanceRegex:
        # Convertir a infix
        infix = convertOE(regex)
        # Expandir la expresión
        expandedInfix = expandEx(infix)
        # Convertir a postfix
        postfix = infixToPostfix(expandedInfix)
        
        print('Infix: ', infix)
        print('Expanded Infix: ', expandedInfix)
        print('Postfix: ', postfix)
        
        nfa = thomspson(postfix)
        
        print('NFA: ', nfa.q0)
        print('NFA: ', nfa.f)
        
        dot_source = to_graphviz(nfa)
        filename = render_graphviz(dot_source)
        
elif option == '2':
    pass
else:
    print('Opción incorrecta, inténtelo de nuevo')
    