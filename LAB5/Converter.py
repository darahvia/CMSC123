import SLLStack

# Create an instance of SLLStack
stack = SLLStack.SLLStack()
postfix = SLLStack.SLLStack()

def isOperator(char):          #function to check if a character is an operator
    return char in "+-*/"


def precedence(operator):      #function to determine the precedence of operators
    if operator in "+-":
        return 1
    if operator in "*/":
        return 2
    return 0

def infixToPostfix(expression):
    stack = SLLStack.SLLStack()         #stack for operators
    postfix = SLLStack.SLLStack()       #stack for the converted postfix

    for char in expression:
        if char.isalnum():
            postfix.push(char)

        

        elif isOperator(char):
            while not stack.isEmpty() and isOperator(stack.top().getValue()) and (precedence(stack.top().getValue()) >= precedence(char)):      #pop operators from the operator stack and push them to the postfix stack if their precedence is higher or equal
                postfix.push(stack.pop().getValue())
            stack.push(char)

        elif char == '(':           #push the opening parenthesis
            stack.push(char)        
        
        elif char == ')':
            while not stack.isEmpty() and stack.top().getValue() != '(':    
                postfix.push(stack.pop().getValue())                        #push operators from the operator stack to postfix stack until open parenthesis
            if not stack.isEmpty() and stack.top().getValue() == '(':
                stack.pop()                                                 #pop the open parenthesis, not needed

    while not stack.isEmpty():
        postfix.push(stack.pop().getValue())        #push the remaining operators
    
    result = []                                     #just to print, does not matter
    while not postfix.isEmpty():
        result += postfix.pop().getValue()
    result = result[::-1]
    return ' '.join(result)


def postfixToInfix(expression):
    stack = SLLStack.SLLStack()

    for char in expression:
        if char.isalnum():
            stack.push(char)        #push every character or number

        elif isOperator(char):
            if stack.getSize() < 2:
                raise Exception
            operand2 = stack.pop().getValue()
            operand1 = stack.pop().getValue()
            stack.push(f'({operand1} {char} {operand2})')

    return stack.top().getValue() if stack else ""              #top of the stack contains final

# Main program
while True:
    userChoice = input("1: Infix to Postfix\n2: Postfix to Infix\nChoice: ")

    if userChoice == '1' or userChoice == '2':
        expression = input("Enter an expression: ")
        


        if userChoice == '1':
            postfix = infixToPostfix(expression)
            print(f'Postfix notation: {postfix}')

        elif userChoice == '2':
            try:
                infix = postfixToInfix(expression)
                print(f'Infix notation: {infix}')
            except:
                print("Invalid postfix expression.")

    else:
        print("Invalid choice. Please enter '1' or '2'.")
