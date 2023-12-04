def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    front += 1
    return queue[front]

queue = [0] * 3
front = -1
rear = -1

rear += 1
queue[rear] = 1
enqueue(2)
enqueue(3)

print(queue)
print(dequeue())
print(dequeue())
print(dequeue())