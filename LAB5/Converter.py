import ArrayStack
stack = ArrayStack.ArrayStack()

# Function to check if a character is an operator
def isOperator(char):
    return char in "+-*/"

def precedence(operator):
    if operator in "+-":
        return 1
    if operator in "*/":
        return 2
    return 0

# Function to convert infix to postfix notation
def infixToPostfix(expression):
    stack = []
    postfix = []
    
    for char in expression:
        if char.isalpha():
            postfix.append(char)

        elif isOperator(char):
            while stack and isOperator(stack[-1]) and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
    
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)


# Function to convert postfix to infix notation
def postfixToInfix(expression): 
    stack = []
    
    for char in expression:
        if char.isalnum():
            stack.append(char)

        elif isOperator(char):
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(f'({operand1} {char} {operand2})')
    
    return stack[0]

# Main program
while True:
    userChoice = input("1: Infix to Postfix\n2: Postfix to Infix\nChoice: ")
    
    if userChoice == '1' or userChoice == '2':
        expression = input("Enter an expression: ")

        if userChoice == '1':
            postfix = infixToPostfix(expression)
            print(f'Postfix notation: {postfix}')

        elif userChoice == '2':
            infix = postfixToInfix(expression)
            print(f'Infix notation: {infix}')

    else:
        print("Invalid choice. Please enter '1', '2'.")

