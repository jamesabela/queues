import turtle
from random import choice
front_of_queue_pointer = 0
end_of_queue_pointer = -1
queue = ["","","","","","",""] # pretending to be a fixed sized queue
animals = ["tiger", "zebra", "koala", "rhinoceros", "flamingo", "hippopotamus", "python", "eagle", "shark", "sloth"]

def circle_print():
    """
    Prints the queue in turtle, making it much more visual.
    :return:
    """
    turtle.speed(0)
    turtle.clear()
    turtle.goto(0,0)
    turtle.penup()
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    for i in range(7):
        statement = str(i)+"|"+queue[i]
        if i == front_of_queue_pointer and i == end_of_queue_pointer:
            statement+="(fp&ep)"
        elif i == front_of_queue_pointer:
            statement+="(fp)"
        elif i == end_of_queue_pointer:
            statement+="(ep)"
        turtle.write(statement,font=('Arial', 14, 'normal'))
        turtle.right(360/7)
        turtle.forward(100)


def print_queue():
    """
    Prints the current state of the queue
    :return:
    """
    for i in range(7):
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
    This add an item to the queue
    :param item: The item you want to add
    :return:
    """
    global front_of_queue_pointer
    global end_of_queue_pointer

    if front_of_queue_pointer-1 == end_of_queue_pointer and end_of_queue_pointer!=-1:
        print("Queue is full")
    elif front_of_queue_pointer==0 and end_of_queue_pointer == 6:
        print("Queue is full")
    else:
        if end_of_queue_pointer < 6:
            end_of_queue_pointer += 1
            print("Moving end of queue pointer +1")
        else:
            end_of_queue_pointer = 0
            print("Moving end of queue pointer to 0")
        print("Inserting",item)
        queue[end_of_queue_pointer]=item

def dequeue():
    """
    This removes the item from the queue and gives it back to you.
    :return: the item at front of queue
    """
    global front_of_queue_pointer
    global end_of_queue_pointer
    if end_of_queue_pointer == front_of_queue_pointer:
        item_from_queue = queue[front_of_queue_pointer]
        queue[front_of_queue_pointer] = ""
        front_of_queue_pointer=0
        end_of_queue_pointer = -1
    elif end_of_queue_pointer == -1:
        print("Empty")

    else:
        item_from_queue = queue[front_of_queue_pointer]
        queue[front_of_queue_pointer] =""
        if front_of_queue_pointer == 6:
            front_of_queue_pointer =0
        else:
            front_of_queue_pointer+=1
        return item_from_queue

def add():
    """
    press a to add a random item to the queue. enqueue it
    :return:
    """
    enqueue(choice(animals))
    circle_print()

def subtract():
    """
    Press s to subtract a random item from the queue. dequeue it
    :return:
    """
    dequeue()
    circle_print()

print("Welcome to your very own queue")
print("You can use print_queue(), circle_print() enqueue(item) and dequeue() to use the circular queue. The list is pretending to be a fixed sized array although its not fussy about data types.")
print("You can even ask for help using e.g. help(print_queue)")
print("This queue enables you to press a to add and s to takeaway.")

turtle.listen()
turtle.onkey(add,"a")
turtle.onkey(subtract,"s")
circle_print()
turtle.done()
