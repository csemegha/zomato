class Node:
    def __init__(self,data):
        self.nextNode=None
        self.data=data
class singlylinkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            pointer=self.head
            while pointer.nextNode is not None:
                pointer=pointer.nextNode
            pointer.nextNode=Node(data)
    def delete(self,data):
        if self.head is None:
            return False
        if self.head.data==data:
            self.head=self.head.nextNode
            return True
        pointer=self.head
        while pointer.nextNode is not None:
            if pointer.nextNode.data==data:
                pointer.nextNode=pointer.nextNode.nextNode
                return True
            pointer=pointer.nextNode
        return False
    def traverse(self):
        pointer=self.head
        while pointer is not None:
            print(pointer.data,end=" ")
            if pointer.nextNode is not None:
                print("=>",end=" ")
            pointer=pointer.nextNode
        print()
if __name__=="__main__":
    mylist=singlylinkedlist()
    print("*"*50)
    print("singly linked list-holycoder.com")
    print("*"*50)
    while True:
        print("*"*50)
        el=int(input("1 to insert,2 for deletion,3 for traversing,4 to exit:"))
        if el==1:
            item=int(input("enter element to insert in linked list:"))
            mylist.insert(item)
            print("inseted")
        elif el==2:
            print("element not found"if not mylist.delete(item)else"deleted")
        elif el==3:
            mylist.traverse()
        elif el==4:
            break
    
