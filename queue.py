front_of_queue_pointer = 0
end_of_queue_pointer = -1
queue = ["","","","","","",""] # pretending to be a fixed sized queue
animals = ["tiger", "zebra", "koala", "rhinoceros", "flamingo", "hippopotamus", "python", "eagle", "shark", "sloth"]

def print_queue():
    """
    Prints the current state of the queue
    :return:
    """
    for i in range(len(queue)):
        if i == front_of_queue_pointer and i == end_of_queue_pointer:
            print("front & end queue pointers -> ",end="")
        elif i == front_of_queue_pointer:
            print("front queue pointer        -> ", end="")
        elif i == end_of_queue_pointer:
            print("end queue pointer          -> ", end="")
        else:
            print(" "*30,end="")

        print(i,"|",queue[i])

def enqueue(item):
    """
    This adds an item to the queue
    :param item: The item you want to add
    :return:
    """
    global end_of_queue_pointer
    if end_of_queue_pointer == 6:
        print("Queue is full")
    else:
        end_of_queue_pointer += 1
        print("Moving end of queue pointer +1")
        print("Inserting",item)
        queue[end_of_queue_pointer]=item

def dequeue():
    """
        This removes the item from the queue and gives it back to you.
        :return: the item at front of queue
        """
    global end_of_queue_pointer
    if end_of_queue_pointer < 0:
        print("queue is empty")
    else:
        print("removing item:",queue[0])
        item_from_queue = queue[0]
        for i in range(0,end_of_queue_pointer+1):
            queue[i] = queue[i+1]
            print("moving item",i+1,queue[i])
        end_of_queue_pointer -=1
        print("end_of_queue_pointer -1")
        return item_from_queue

print("Welcome to your very own queue")
print("You can use print_queue(), enqueue(item) and dequeue() to use the queue. The list is pretending to be a fixed sized array although its not fussy about data types.")
print("You can even ask for help using e.g. help(print_queue)")
