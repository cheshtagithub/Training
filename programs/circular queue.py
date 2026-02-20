 #           ​ Circula queue:
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
        
    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = value
            print(value ,"is added in the queue at index", self.rear)
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            print(value ,"is added in the queue at index", self.rear)
            
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            print(self.queue[self.front] ,"is deleted from queue")
            self.front = self.rear = -1
        else:
            print(self.queue[self.front] ,"is deleted from queue")
            self.front = (self.front + 1) % self.size
            

n = int(input("Enter the size of circular queue: "))            
q = CircularQueue(n)

while True:
    print("1. Add to Circular queue \n2. Delete from circular queue \n3. Exit the program")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        data = int(input("Enter the data: "))
        q.enqueue(data)
    
    elif choice == 2:
        q.dequeue()
    
    elif choice == 3:
        print("Exiting program")
        break
    else:
        print("invalid choice")

"""
Output:
Enter the size of circular queue: 4
1. Add to Circular queue 
2. Delete from circular queue 
3. Exit the program
Enter the choice: 1
Enter the data: 1
1 is added in the queue at index 0
1. Add to Circular queue 
2. Delete from circular queue 
3. Exit the program
Enter the choice: 1
Enter the data: 2
2 is added in the queue at index 1
1. Add to Circular queue 
2. Delete from circular queue 
3. Exit the program
Enter the choice: 1
Enter the data: 3
3 is added in the queue at index 2
1. Add to Circular queue 
2. Delete from circular queue 
3. Exit the program
Enter the choice: 1
Enter the data: 4
4 is added in the queue at index 3
1. Add to Circular queue 
2. Delete from circular queue 
3. Exit the program
Enter the choice: 1
Enter the data: 5
Queue is full
1. Add to Circular queue 
2. Delete from circular queue 
3. Exit the program
Enter the choice: 2
1 is deleted from queue
1. Add to Circular queue 
2. Delete from circular queue 
3. Exit the program
Enter the choice: 1
Enter the data: 6
6 is added in the queue at index 0
1. Add to Circular queue 
2. Delete from circular queue 
3. Exit the program
Enter the choice: 3
Exiting program
"""
