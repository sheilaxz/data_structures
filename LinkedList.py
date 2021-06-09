class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def InsertAtHead(self,  data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def InsertAtEnd(self, data):
        new_node = Node(data)
        if self.head:
            cur_node = self.head
            if cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            self.length += 1
        else:
            self.head = new_node
            self.length += 1

    def PrintList(self):
        cur_node = self.head
        while cur_node:
            print (cur_node.val)
            cur_node = cur_node.next

    def _get_idx_element(self, idx): # index starts from 0
        if self.head:
            cur_node = self.head
            i = 0
            while i <= idx:
                if i == idx:
                    return cur_node
                else:
                    if cur_node.next:
                        cur_node = cur_node.next
                        i += 1
                    else:
                        print("Invalid input: element does not exist.")
                        break
        else:
            print ("Invalid input: empty list.")

    def GetValue(self, idx):  # index starts from 0
        if self._get_idx_element(idx):
            val = self._get_idx_element(idx).val
            print (val)

    def Insert(self, data, idx):
        new_node = Node(data)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            if self._get_idx_element(idx - 1):
                prev_node = self._get_idx_element(idx - 1)
                new_node.next = prev_node.next
                prev_node.next = new_node
                self.length += 1

    def Delete(self, idx):
        if idx == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            if self._get_idx_element(idx - 1):
                prev_node = self._get_idx_element(idx - 1)
                idx_node = prev_node.next
                prev_node.next = idx_node.next
                self.length -= 1

