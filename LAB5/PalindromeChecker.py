# class ArrayStack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items = [item] + self.items

#     def pop(self):
#         if not self.is_empty():
#             item = self.items[0]
#             self.items = self.items[1:]
#             return item

#     def is_empty(self):
#         return not self.items

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