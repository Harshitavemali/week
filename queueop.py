from collections import deque


queue = deque()


def enqueue(element):
    queue.append(element)
    print(f"{element} enqueued into the queue")


def dequeue():
    if not queue:
        print("Queue is empty, nothing to dequeue")
    else:
        element = queue.popleft()
        print(f"{element} dequeued from the queue")
        return element


def display():
    print("Current queue:")
    print(list(queue))


def quit():
    print("Quitting the operations")
    exit()


def main():
    while True:
        print("Select operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Quit")


        choice = input("Enter choice (1/2/3/4): ")


        if choice == '1':
            element = input("Enter element to enqueue: ")
            enqueue(element)
        elif choice == '2':
            dequeue()
        elif choice == '3':
            display()
        elif choice == '4':
            quit()
        else:
            print("Invalid choice, please select a valid operation")


main()
