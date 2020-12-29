class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SLinkedList:
    def __init__(self):
        self.head = ListNode(None)
        self.size = 0

    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def selectNode(self, idx):
        if idx >= self.size:
            print("Index Error")
        if idx == 0:
            return self.head
        else:
            target = self.head
            for cnt in range(idx):
                target = target.next
            return target

    def appendleft(self, value):
        if self.is_empty():
            self.head = ListNode(value)
        else:
            self.head = ListNode(value, self.head)
        self.size += 1

    def append(self, value):
        if self.is_empty():
            self.head = ListNode(value)
            self.size += 1
        else:
            target = self.head
            while target.next != None:
                target = target.next
            newtail = ListNode(value)
            target.next = newtail
            self.size += 1

    def insert(self, value, idx):
        if self.is_empty():
            self.head = ListNode(value)
            self.size += 1
        elif idx == 0:
            self.head = ListNode(value, self.head)
            self.size += 1
        else:
            target = self.selectNode(idx - 1)
            if target == None:
                return
            newNode = ListNode(value)
            tmp = target.next
            target.next = newNode
            newNode.next = tmp
            self.size += 1

    def delete(self, idx):
        if self.is_empty():
            print("Empty Linked List Error")
            return
        elif idx >= self.size:
            print("Index Error")
            return
        elif idx == 0:
            target = self.head
            self.head = target.next
            del target
            self.size -= 1
        else:
            target = self.selectNode(idx - 1)
            deltarget = target.next
            target.next = target.next.next
            del deltarget
            self.size -= 1

    def printlist(self):
        target = self.head
        while target:
            if target.next != None:
                print(target.val, "-> ", end="")
                target = target.next
            else:
                print(target.val)
                target = target.next


if __name__ == "__main__":
    mylist = SLinkedList()
    mylist.append("A")
    mylist.printlist()
    mylist.append("B")
    mylist.printlist()
    mylist.append("C")
    mylist.printlist()
    mylist.insert("D", 1)
    mylist.printlist()
    mylist.appendleft("E")
    mylist.printlist()
    print(mylist.listSize())
    mylist.delete(0)
    mylist.printlist()
    mylist.delete(3)
    mylist.printlist()
    mylist.delete(0)
    mylist.printlist()
    mylist.appendleft("A")
    mylist.printlist()
