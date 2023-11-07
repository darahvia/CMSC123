import SLLStack

# Create an instance of SLLStack
stack = SLLStack.SLLStack()
postfix = SLLStack.SLLStack()

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
    stack = SLLStack.SLLStack()
    postfix = SLLStack.SLLStack()

    for char in expression:
        if char.isalpha():
            postfix.push(char)

        elif isOperator(char):
            while not stack.isEmpty() and isOperator(stack.top().getValue()) and (precedence(stack.top().getValue()) <= precedence(char)):
                postfix.push(stack.pop().getValue())
            stack.push(char)

        elif char == '(':
            stack.push(char)
        
        elif char == ')':
            while not stack.isEmpty() and stack.top().getValue() != '(':
                postfix.push(stack.pop().getValue())
            if not stack.isEmpty() and stack.top().getValue() == '(':
                stack.pop()

    while not stack.isEmpty():
        postfix.push(stack.pop().getValue())
    
    result = []
    while not postfix.isEmpty():
        result += postfix.pop().getValue()
    result = result[::-1]
    return ' '.join(result)


# Function to convert postfix to infix notation
def postfixToInfix(expression):
    stack = SLLStack.SLLStack()

    for char in expression:
        if char.isalnum():
            stack.push(char)

        elif isOperator(char):
            operand2 = stack.pop().getValue()
            operand1 = stack.pop().getValue()
            stack.push(f'({operand1} {char} {operand2}')

    return stack.top().getValue() if stack else ""

# Main program
while True:
    userChoice = input("1: Infix to Postfix\n2: Postfix to Infix\nChoice: ")

    if userChoice == '1' or userChoice == '2':
        expression = input("Enter an expression: ").strip()
        print(expression)

        if userChoice == '1':
            postfix = infixToPostfix(expression)
            print(f'Postfix notation: {postfix}')

        elif userChoice == '2':
            infix = postfixToInfix(expression)
            print(f'Infix notation: {infix}')

    else:
        print("Invalid choice. Please enter '1' or '2'.")
