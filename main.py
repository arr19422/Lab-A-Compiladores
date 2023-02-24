#Diego de Jesús Arredondo Turcios
#19422
#Laboratorio A

from funcs import check_expression_balanced, convertOE, expandEx, infixToPostfix


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
        
        # Crear el AFN con el algoritmo de Thompson y graficarlo
elif option == '2':
    pass
else:
    print('Opción incorrecta, inténtelo de nuevo')
    