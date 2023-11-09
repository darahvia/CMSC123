import datetime
import ArrayQueue

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self, receiptNumber, foodItems):
        self.receiptNumber = receiptNumber
        self.foodItems = foodItems
        self.orderTime = datetime.datetime.now()

    def displayOrder(self):
        print("Order for Receipt number: ", self.receiptNumber)
        for item in self.foodItems:
            itemContents = "Item: " + item.name + "\nPrice: $" + str(item.price) + "\nQuantity: " + str(item.quantity)
            print(itemContents)

        print("Order time: ", self.orderTime)

class FastFoodChain:
    def __init__(self):
       self.orderQueue =  ArrayQueue.ArrayQueue() # Using a list 

    def takeOrder(self):
        foodItems = []
        while True:
            name = input("Enter food item name (or type 'done' to finish): ")
            if name.lower() == 'done':
                break
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            item = FoodItem(name, price, quantity)
            receiptNumber = input("Enter Receipt/Customer Number: ")
            foodItems.append(item)
        order = Order(receiptNumber, foodItems)
        self.orderQueue.enqueue(order)  # push the order to the end of the list
        print("Order added.")

    def displayCurrentOrder(self):  # Display the last order in the stack
        self.tempOrder = ArrayQueue.ArrayQueue()
        if not self.orderQueue.isEmpty():
            while self.orderQueue.getSize() > 1:
                self.tempOrder.enqueue(self.orderQueue.dequeue().getValue())
            currentOrder = self.orderQueue.front().getValue()
            self.orderQueue, self.tempOrder = self.tempOrder, self.orderQueue
            currentOrder.displayOrder()


        else:
            print("Queue empty.")
            


    def removeFinishedOrder(self):
        if not self.orderQueue.isEmpty():
            removeOrder = input("Would you like to remove the recent order? (yes/no): ")
            if removeOrder.lower() == 'yes':
                removedElement = self.orderQueue.dequeue().getValue()
                removedOrder = removedElement
                removedOrder.displayOrder()
                print("Recent order removed")
            else:
                print("Order not removed.")
        else:
            print("No orders to remove")


# Main program
fast_food_chain = FastFoodChain()

while True:
    print("\n===== Fast Food Chain Ordering System =====")
    print("1. Accept Order")
    print("2. Display Current Order")
    print("3. Remove Finished Order")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        fast_food_chain.takeOrder()
    elif choice == '2':
        fast_food_chain.displayCurrentOrder()
    elif choice == '3':
        fast_food_chain.removeFinishedOrder()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
