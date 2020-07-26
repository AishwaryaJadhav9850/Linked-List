# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:52:32 2020

@author: SUPERNOVA2813

Creation
Display - llist.display() 
Insert node at the end - llist.insertAtEnd()
Insert node at the beginning - llist.insertAtBeginning()
Insert after node - llist.insertAfterNode()
Delete a node - llist.deleteNode()
Delete last node - llist.deleteLastNode()
Delete first node - llist.deleteFirstNode()
Reverse - llist.reverse()

"""


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtEnd(self):
        i=int(input("Enter the data to insert node at the end:"))
        if(self.head==None):
            self.head=Node(i)
            self.head.next=None
        else:
            n1=self.head
            while(n1.next!=None):
                n1=n1.next
            n2=Node(i)
            n1.next=n2
            n2.next=None
            
    def insertAtBeginning(self):
        i=int(input("Enter the data to insert node at the beginning:"))
        if(self.head==None):
            self.head=Node(i)
            self.head.next=None
        else:
            n1=Node(i)
            n1.next=self.head
            self.head=n1
            
    def insertAfterNode(self):
        if(self.head==None):
            print("List is empty!")
            return
        i=int(input("Enter the node after which to insert data:"))
                 
        n1=self.head
        while(n1.data!=i and n1.next!=None):
            n1=n1.next
        if(n1.data==i):
            j=int(input("Enter the data for the node:"))
            n2=Node(j)
            n2.next=n1.next
            n1.next=n2
        else:
            print("Data not found to insert node after.")
    
    
    def deleteLastNode(self):
        if(self.head==None):
            print("List is empty!")
            return
        n1=self.head;
        while(n1.next!=None): 
            prev=n1
            n1=n1.next
        prev.next=None
        del n1
        
            
    def deleteFirstNode(self):
        if(self.head==None):
            print("List is empty!")
            return
        n1=self.head
        self.head=self.head.next
        del n1
        
        
    def deleteNode(self):
        if(self.head==None):
            print("List is empty!")
            return
        i=int(input("Enter the node to delete:"))
        n1=self.head
        while(n1.data!=i and n1.next!=None):
            prev=n1
            n1=n1.next
        if(n1.data==i):
            prev.next=n1.next
            del n1
        else:
            print("Data not found to delete")
            return    
            
    def display(self):
        if(self.head==None):
            print("List is empty!")
            return
        else:
            print("\n");
            n1=self.head
            while(n1!=None):
                print(n1.data,end = "--> ")
                n1=n1.next  
                
    def reverse(self):
        if(self.head==None):
            print("List is empty!")
            return
        n1=self.head
        if(n1.next==None):
            return
        if(n1.next.next==None):
            n1=n1.next
            n1.next=self.head
            self.head.next=None
            self.head=n1
        else:
            curr=n1.next.next
            prev=n1
            n1=n1.next
            while(curr.next!=None):
                n1.next=prev
                prev=n1
                n1=curr
                curr=curr.next
            if(curr.next==None):
                n1.next=prev
                curr.next=n1
                self.head.next=None
                self.head=curr


llist=LinkedList()
ch=0
while(ch!=9): 
    print("\n")
    print("1.Insert at the beginning")     
    print("2.Insert at the end")  
    print("3.Insert after a specific node") 
    print("4.Delete first node") 
    print("5.Delete last node")
    print("6.Delete specific node")
    print("7.Reverse list")
    print("8.Display")
    print("9.EXIT")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        llist.insertAtBeginning()
        llist.display()
    elif ch==2:
        llist.insertAtEnd() 
        llist.display()
    elif ch==3:
        llist.insertAfterNode()
        llist.display()
    elif ch==4:
        llist.deleteFirstNode()
        llist.display()
    elif ch==5:
        llist.deleteLastNode()
        llist.display()
    elif ch==6:
        llist.deleteNode()
        llist.display()
    elif ch==7:
        llist.reverse()
        llist.display()
    elif ch==8:
        llist.display()
    elif ch==9:
        break;
    else:
        print("Unknown input. Kindly enter correct choice!")
        



 