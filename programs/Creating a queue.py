#            ​ Creating a queue

from collections import deque
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self):
        x = int(input("Enter the value to enqueue in queue: "))
        self.queue.append(x)
        print(x, " enqueued into queue")
        
    def dequeue(self):
        if not self.queue:
            print("The queue is empty")
        else:
            print("Dequeued element", self.queue.pop(0))
    
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

s = Queue()
while True:
    print("---Queue menu---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Display")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        s.enqueue()
    elif choice == 2:
        s.dequeue()
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
Enter the value to enqueue in queue: 1
1  enqueued into queue
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 1
Enter the value to enqueue in queue: 2
2  enqueued into queue
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 1
Enter the value to enqueue in queue: 3
3  enqueued into queue
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 4
The queue is [1, 2, 3]
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 3
Front element is 1
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 2
Dequeued element 1
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 4
The queue is [2, 3]
---Queue menu---
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Exit
Enter your choice: 5
Exiting program
'''
