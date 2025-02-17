class BinaryTree:
    def __init__(self, element_count):
        self.null_pointer = -1
        self.element_count = element_count
        self.nodes = [None for _ in range(element_count)],\
            [_+1 for _ in range(element_count)],\
            [self.null_pointer for _ in range(element_count)]
        self.free_list = self.null_pointer
    def insert(self,element):
        for i in range(self.element_count):
            value = self.nodes[0][i]
            right = self.nodes[2][i]
            left = self.nodes[1][i]
            if value is None: value = -1
            if self.free_list == self.null_pointer:
                self.free_list = 1
                self.nodes[0][0]=element
            elif element > value and right == -1:
                self.nodes[0][self.free_list] = value
                self.nodes[2][i] = self.free_list
            elif element < value and left == -1:
                self.nodes[0][self.free_list] = value
                self.nodes[1][i] = self.free_list
        print(self.nodes)



        pass


test = BinaryTree(10)
test.insert(1)