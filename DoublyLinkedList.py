# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:00:03 2020


1. insertFirst
2. insertAfterNode
3. insertLast
4. deleteFirst
5. delete Node
6. display
7. reverseDisplay

@author: SUPERNOVA2813
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.last=None
        
    def insertFirst(self):
        i=int(input("Enter the data to insert node in the beginning:"))
        if(self.head==None):
            self.head=Node(i)
            self.last=self.head
            return                    
        else:
            n1=Node(i)
            n1.next=self.head
            self.head.prev=n1
            self.head=n1

    def insertAfterNode(self):
        if(self.head==None):
            print("List is empty!")
            return
        i=int(input("Enter the node to insert node after"))
        n1=self.head 
        while(n1.data!=i and n1!=self.last):
            n1=n1.next
        if(n1.data==i and n1==self.head and n1==self.last):
            j=int(input("Enter the data to insert:"))
            node=Node(j)
            n1.next=node
            node.prev=n1
            self.last=node
            return
        elif(n1.data==i and n1!=self.last):
            j=int(input("Enter the data to insert:"))
            node=Node(j)
            node.next=n1.next
            n1.next.prev=node
            n1.next=node
            node.prev=n1
            return
        elif(n1.data==i and n1==self.last):
            j=int(input("Enter the data to insert:"))
            node=Node(j)
            node.prev=n1
            n1.next=node
            self.last=node
            return
        elif(n1.data!=i and n1==self.last):
            print("Node not found to insert data!")
    
    
    def insertLast(self):
        i=int(input("Enter the data to insert node at the end:"))
        if(self.head==None):
            self.head=Node(i)
            self.last=self.head
            return                    
        else:
            n1=Node(i)
            self.last.next=n1
            n1.prev=self.last
            self.last=n1
            
    def display(self):
        if(self.head==None):
            print("List is Empty!")
            return
        n1=self.head
        print("\n")
        while(n1!=self.last):
            print(n1.data,end="-->")
            n1=n1.next     
        print(n1.data)

    def deleteFirst(self):
        if(self.head==None):
            print("List is Empty!")
            return
        if(self.head==self.last):
            self.head=None
            self.last=None
            return
        if(self.head.next==self.last):
            del self.head
            self.head=self.last
            self.head.prev=None
            self.head.next=None
            return
        else:
            n1=self.head.next
            n1.prev=None
            del self.head
            self.head=n1
            
    def deleteNode(self):
        if(self.head==None):
            print("List is Empty!")
            return
        i=int(input("Enter the node to delete:-"))
        if(self.head==self.last and self.head.data==i):
            del self.head
            del self.last
            self.head=self.last=None
            return
        
        elif(self.head.next==self.last and self.head.data==i):  
            del self.head
            self.last.prev=None
            self.last.next=None
            self.head=self.last
            return
        elif(self.head.next==self.last and self.last.data==i):
            self.head.next=None
            self.head.prev=None
            self.last=self.head
            return
        elif(self.head==self.last or self.head.next==self.last):
            print("Data not found to delete")
            return    
        else:
            n1=self.head
            while(n1.data!=i):
                n1=n1.next
            if(n1.data==i and n1==self.head):               
                self.head=self.head.next
                self.head.prev=None
                del n1
                return
            elif(n1.data==i and n1==self.last):
                self.last=self.last.prev
                self.last.next=None
                del n1
                return 
            elif(n1.data==i):
                n1.prev.next=n1.next
                n1.next.prev=n1.prev
                del n1
                return
            else:
                print("Data not found to delete")
                return
                
            
    def reverseDisplay(self):
        if(self.head==None):
            print("List is Empty!")
            return
        n1=self.last
        print("\n")
        while(n1!=self.head):
            print(n1.data,end="-->")
            n1=n1.prev     
        print(n1.data)



d=DoublyLinkedList()
while(1):
    print("\n")
    print("1.Insert in the beginning")
    print("2.Insert in the end")
    print("3.Insert after node")
    print("4.Delete first node")
    print("5.Delete specific node")
    print("6.Display")
    print("7.Display Reverse")
    print("8.EXIT")
    ch=int(input("Please enter your choice:-"))
    if ch==1:
        d.insertFirst()
        d.display()
    elif ch==2:
        d.insertLast()
        d.display()
    elif ch==3:
        d.insertAfterNode()
        d.display()
    elif ch==4:
        d.deleteFirst()
        d.display()
    elif ch==5:
        d.deleteNode()
        d.display()
    elif ch==6:
        d.display()
    elif ch==7:
        d.reverseDisplay()
    elif ch==8:
        break
    else:
        print("Please enter correct choice!")
