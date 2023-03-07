expression = input('Type an expression: ')

parentheses = []
for char in expression:
    if char == '(':
        parentheses.append('(')
    elif char == ')':
        if len(parentheses) > 0:
            parentheses.pop()
        else:
            parentheses.append(')')
            break

if len(parentheses) == 0:
    print('The expression is valid')
else:
    print('The expression is not valid')
