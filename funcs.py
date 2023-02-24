from graphviz import Digraph

# Clase para la creacion de los nodos del AFN
def check_expression_balanced(expression):
    # Balanceo de los parentesis en una expresion
    # Referencia de codigo: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
    def check(myStr):
        open_list = ["[", "{", "("]
        close_list = ["]", "}", ")"]
        stack = []
        for i in myStr:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(stack) > 0) and
                        (open_list[pos] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

    if check(expression):
        return True
    else:
        return False

#Convert regex to infix notation
def regex_to_infix(regex):
    # Convertir a infix
    infix = convertOE(regex)
    return infix

# Expandir la expresión
def convertOE(regex):
    new = []
    stack = []
    for char in regex:
        if char != "?" and char != "+":
            new.append(char)
            stack.append(char)
        # Si la expresion tiene un ? lo reemplaza por ( |ε)
        elif char == "?":
            x = stack.pop()
            new.pop()
            new.append(str("("+x+"|ε)"))
            stack = []
        # Si la expresion tiene un + lo reemplaza por el patron previo ( ( *))
        elif char == "+":
            x = stack.pop()
            if x == ")":
                y = stack.pop()
                operador = stack.pop()
                v = stack.pop()
                p = stack.pop()
                final = p + v + operador + y + x
                new.append(str(final+"*"))
            else:
                new.append(str("("+x+"*)"))
    return ''.join(new)

# Verifica la existencia de los simbolos, en donde si encuentra dos juntos, coloca un .
def expandEx(infix):
    r = ""
    counter = 0
    for character in infix:
        if character == "|":
            counter = 0
        elif character == "(":
            if counter == 1:
                r = r + "."
                counter = 0
        elif character == ")" or character == "*" or character == ".":  # Si es un operador, no se hace nada
            pass
        else:
            counter += 1
        if counter == 2:
            r = r + "." + character
            counter = 1
        else:
            r = r + character
    return r



# Pasa la expresion infix a postfix
def infixToPostfix(expandedInfix):
    print("Infix: ", expandedInfix)
    stack = []
    output = []
    operators = ['.', '|', '*', '(', ')']
    for char in expandedInfix:
        print("char: ", char)
        if char not in operators:
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence(char) <= precedence(stack[-1]):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return output
            
# Verifica la precedencia de los operadores
def precedence(char):
    if char == '*':
        return 3
    elif char == '.':
        return 2
    elif char == '|':
        return 1
    else:
        return -1
