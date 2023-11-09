import ArrayStack

def main():
    
    storage = ArrayStack.ArrayStack()
    userInput = input("Enter a string: ")

    for character in userInput:
        storage.push(character)

    reversedText = ''
    while not storage.isEmpty():
        reversedText =  reversedText + storage.pop().getValue()

    if userInput == reversedText:
        print("The input string is a palindrome.")
    else:
        print("The input string is not a palindrome.")

if __name__ == "__main__":
    main()