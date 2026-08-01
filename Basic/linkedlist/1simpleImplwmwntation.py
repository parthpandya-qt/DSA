class Node:
    def __init__(self,k):
        self.key=k
        self.next=None
temp1=Node(10)
temp2=Node(20)
temp3=Node(30)
temp1.next=temp2
temp2.next=temp3
head=temp1

class linked_list:
    def __init__(self,head):
        self.head = None
    def insertEnd(self,data):
        insert_node = Node(data)
        if self.head == None:
            self.head = insert_node
            return self.head
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = insert_node
    def display(self,head):
        if self.head == None:
            return None
        else:
            curr = head
            while curr!=None:
                print(curr.data,end="->")
                curr=curr.next
    def insertFront(self,data):
        insertNode = Node(data)
        if self.head == None:
            self.head = insertNode
            return self.head
        else:
            insertNode.next=self.head
            self.head = insertNode
            return insertNode
    def insertAtposition(self,head,data,pos):
        insertNode = Node(data)
        curr = head
        for _ in range(pos-2):
            curr = curr.next
        insertNode.next = curr.next
        curr.next = insertNode
    def search(self,head,data):
        curr = head
        while curr != None:
            if curr.data == data:
                return True
            curr = curr.next
        return False
    def deleteFirst(self,head):
        if head == None:
            return None
        else:
            next = head.next
            head.next =None
            head = next
    def deleteLast(self,head):
        if head == None:
            return None
        else:
            curr = head
            while curr.next.next!=None:
                curr = curr.next
            curr.next = None
            return head
    def deletewithPointergiven(self,ptr):
        temp = ptr.next
        ptr.key = temp.key
        ptr.next = temp.next
    def deleteSpecificPosition(self,head,pos):
        curr = head
        for i in range(pos-2):
            curr = curr.next 
            if curr == None:
                return None
        curr.next = curr.next.next
    def sortedInsert(self,head,data):
        temp = Node(data)
        if head.key>temp.key:
            temp.next = head
            head = temp
            return head
        else:
            curr = head
            while curr.next!=None:
                if curr.next.key<temp.key:
                    curr=curr.next
                else:
                    break
            temp.next = curr.next
            curr.next = temp
    def middleLinkedList(self,head):
        slow = self.head
        fast = self.head
        while fast!=None and fast.next.next!=None:
            slow=slow.next
            fast = fast.next.next
        print(slow.key)
            

            