class CircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.data = [-1] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        else:
            if self.tail == -1:
                self.head = self.tail = 0
            else:
                self.tail = (self.tail + 1) % self.max_size
            self.data[self.tail] = value
            self.size += 1
            print (self.head, self.tail)
            return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        else:
            self.head = (self.head + 1) % self.max_size
            self.size -= 1     
            if self.size == 0:
                self.tail = self.head = -1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.data[self.head]
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.data[self.tail]
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False