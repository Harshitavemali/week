stack = []


def push(element):
    stack.append(element)
    print(f"{element} pushed onto the stack")


def pop():
    if not stack:
        print("Stack is empty, nothing to pop")
    else:
        element = stack.pop()
        print(f"{element} popped from the stack")
        return element


def display():
    print("Current stack:")
    print(stack)


def quit():
    print("Quitting the operations")
    exit()


def main():
    while True:
        print("Select operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Quit")


        choice = input("Enter choice (1/2/3/4): ")


        if choice == '1':
            element = input("Enter element to push: ")
            push(element)
        elif choice == '2':
            pop()
        elif choice == '3':
            display()
        elif choice == '4':
            quit()
        else:
            print("Invalid choice, please select a valid operation")


main()
