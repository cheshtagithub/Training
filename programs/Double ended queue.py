#            ​ Double ended Queue:
class DoubleEndedQueue:
    def __init__(self):
        self.queue = []
    
    def enqueueAtEnd(self):
        x = int(input("Enter the value to enqueue in queue: "))
        self.queue.append(x)
        print(x, " enqueued into queue")
    
    def enqueueAtFront(self):
        x = int(input("Enter the value to enqueue in queue: "))
        self.queue.insert(0, x)
        print(x, " enqueued into queue")
        
    def dequeueAtFront(self):
        if not self.queue:
            print("The queue is empty")
        else:
            print("Dequeued element", self.queue.pop(0))
    
    def dequeueAtEnd(self):
        if not self.queue:
            print("The queue is empty")
        else:
            print("Dequeued element ",self.queue.pop())
    def front(self):
        if not self.queue:
            print("The queue is empty")
        else:
            print("Front element is", self.queue[0])
            
    def display(self):
        if not self.queue:
            print("queue is empty")
        else:
            print("The queue is", list(self.queue))

s = DoubleEndedQueue()
while True:
    print("---Queue menu---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Display")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        option = (input("If want to add element from front enter A else want to add element from end enter B: "))
        if option == 'A':
            s.enqueueAtFront()
        else:
            s.enqueueAtEnd()
    elif choice == 2:
        option = (input("If want to remove element from front enter A else want to remove element from end enter B: "))
        if option == 'A':
            s.dequeueAtFront()
        else:
            s.dequeueAtEnd()
    elif choice == 3:
        s.front()
    elif choice == 4:
        s.display()
    elif choice == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")

'''
Output:
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 1
If want to add element from front enter A else want to add element from end enter B: A
Enter the value to enqueue in queue: 4
4  enqueued into queue
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 1
If want to add element from front enter A else want to add element from end enter B: A
Enter the value to enqueue in queue: 1
1  enqueued into queue
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 1
If want to add element from front enter A else want to add element from end enter B: A
Enter the value to enqueue in queue: 6
6  enqueued into queue
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 1
If want to add element from front enter A else want to add element from end enter B: B
Enter the value to enqueue in queue: 9
9  enqueued into queue
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 4
The queue is [6, 1, 4, 9]
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 2
If want to remove element from front enter A else want to remove element from end enter B: B
Dequeued element  9
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 4
The queue is [6, 1, 4]
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 5
Exiting program
'''
