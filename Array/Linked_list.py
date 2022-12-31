class Node:
    def __init__(self,data,next_node=None):
        self.data=data
        self.next_node=next_node

class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            return print('Linked is empty')
        iterator=self.head
        list_str=[]
        while iterator:
            #list_str+=str(iterator.data)+ '-->'
            list_str.append(iterator.data)
            iterator=iterator.next_node
        print(list_str)

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self, data):
        # print('start')
        # print(self.head)
        if self.head is None:
            self.head = Node(data, None)
            #print('I am returning myself')
            return
        iterator = self.head
        #print(iterator)
        while iterator.next_node != None:
            # print('while')
            iterator = iterator.next_node
            # print(iterator)
        # print(iterator.next_node)
        iterator.next_node = Node(data, None)
        # print(iterator.next_node)
        # print(iterator)
        # print('end')
    def insert_at_index(self,data,idx):
        if idx<0 or idx> self.count_length():
            raise Exception('Invalid Index')
        if idx==0:
            self.insert_at_begining(data)
            return
        count=0
        iterator=self.head
        while iterator.next_node:
            if count==idx-1:
                node=Node(data,iterator.next_node)
                iterator.next_node=node
                break
            iterator=iterator.next_node
            count+=1
    def count_length(self):
        count=0
        iterator=self.head
        while iterator.next_node != None:
            count+=1
            iterator=iterator.next_node
        return count+1

    def remove_at_index(self,idx):
        if idx<0 or idx> self.count_length():
            raise Exception('Invalid Index')
        iterator=self.head
        count=0
        if idx==0:
            self.head=iterator.next_node
            return
        while iterator.next_node:
            if count==idx-1:
                iterator.next_node=iterator.next_node.next_node
                return
            iterator=iterator.next_node
            count+=1


    def search(self, data):
        if self.head == None:
            return False
        iterator = self.head
        while iterator:
            if iterator.data == data:
                return True
            else:
                iterator = iterator.next_node
        return False

    def detect_loop(self):
        if self.head==None:
            return False
        tortoise=self.head
        hare=self.head
        while tortoise and hare and hare.next_node:
            tortoise=tortoise.next_node
            hare=hare.next_node.next_node
            if tortoise==hare:
                return True
        return False


list_1 = LinkedList()
list_1.insert_at_begining(45)
list_1.insert_at_end(46)
list_1.insert_at_end(50)
list_1.insert_at_end(34)
list_1.insert_at_index(6,2)
# print(list_1.count_length())
list_1.insert_at_end(78)
list_1.insert_at_end(90)
# print(list_1.count_length())
# list_1.print()
# list_1.insert_at_index(5,3)
# list_1.print()
# list_1.remove_at_index(3)
# list_1.print()
# list_1.insert_at_index(4,2)
# list_1.print()
# list_1.remove_at_index(0)
# list_1.print()

#list_1.head.next_node.next_node.next_node.next_node=list_1.head

result=list_1.detect_loop()
print(result)
    
    
