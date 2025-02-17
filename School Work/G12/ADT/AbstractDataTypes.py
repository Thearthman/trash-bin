import random


class LStack:
    def __init__(self, element_count):
        self.null_pointer = -1
        self.element_count = element_count
        self.stack = [None for _ in range(self.element_count)]
        self.top_pointer = self.null_pointer

    def push(self, _input):
        if self.top_pointer < self.element_count:
            self.top_pointer += 1
            self.stack[self.top_pointer] = _input
        else:
            print("Exceeding the max element count")
            raise OverflowError

    def pop(self):
        if self.top_pointer != self.null_pointer:
            self.top_pointer -= 1
            return self.stack[self.top_pointer + 1]
        else:
            print("No Elements")
            raise ValueError

    def peek(self):
        if self.top_pointer > -1:
            return self.stack[self.top_pointer]

    def preview(self):
        for i in range(self.element_count):
            if self.top_pointer == -1 and i == 0:
                print("null_pointer => <top_pointer>")
            print(format(self.stack[i]), end=" ")
            if i == self.top_pointer:
                print("<top_pointer>", end=" ")
            print()


class LQueue:
    def __init__(self, element_count):
        self.null_pointer = -1
        self.element_count = element_count
        self.stack = [None for _ in range(self.element_count)]
        self.front_pointer = self.null_pointer
        self.end_pointer = self.null_pointer
        self.length = 0

    def queue(self, _input):
        if self.length < self.element_count:
            if self.front_pointer == -1:
                self.front_pointer = 0
                self.end_pointer = 0
            else:
                self.end_pointer += 1
            self.stack[self.end_pointer % self.element_count] = _input
            self.length += 1
        else:
            print("Max elements reached")
            raise OverflowError

    def dequeue(self):
        if self.length > 0:
            self.length -= 1
            self.end_pointer -= 1
            return self.stack[(self.end_pointer + 1) % self.element_count]
        else:
            print("No elements in queue")
            raise ValueError

    def preview(self):
        print("----------------------------")
        for _ in range(self.element_count):
            print(self.stack[_])
        print("----------------------------")

class LinkedList():
    def __init__(self,element_count):
        self.element_count = element_count
        self.array = [None for _ in range(self.element_count)],[_ + 1 for _ in range(self.element_count)]
        self.null_pointer = -1
        self.start_pointer = self.null_pointer
        self.free_pointer = 0

    def insert(self,_item):
        # Assign item
        if self.start_pointer == self.null_pointer:
            self.array[0][self.free_pointer] = _item
            self.array[1][self.free_pointer] = self.null_pointer
            self.start_pointer = self.free_pointer
            self.free_pointer = self.array[1][self.free_pointer]
        else:
            self.array[0][self.free_pointer]
            self.array[0][self.free_pointer] = _item
            self.array[1][self.free_pointer] = self.null_pointer
        pass

    def lastItem(self):
        # 
        return lastItem,lastItemPosition






# element_count = random.randint(10, 20)
# myQueue = LQueue(element_count)
# rand1 = random.randint(0, 10)
# for i in range(element_count):
    # myQueue.queue(random.randint(4, 10))
# myQueue.preview()
# for i in range(rand1):
    # print(myQueue.dequeue())
# myQueue.preview()
# for i in range(rand1):
    # myQueue.queue(random.randint(4, 10))
# myQueue.preview()
# for i in range(rand1):
    # print(myQueue.dequeue())
# myQueue.preview()
# myStack = LStack(element)
# for i in range(element):
#     if 0 < random.randint(0, 2):
#         rand = random.randint(5, 15)
#         print("> Stack input:", rand)
#         myStack.push(rand)
#     else:
#         print("> Stack output:", myStack.pop())
#     myStack.preview()
#     print("----------------")
