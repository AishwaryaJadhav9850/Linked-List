# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 19:11:35 2020


@author: SUPERNOVA2813
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class CircularLinkedList:
    def __init__(self):
         self.last=None

    def insertLast(self):
        i=int(input("Enter data to insert node at the end:"))
        if(self.last==None):
            self.last=Node(i)
            self.last.next=self.last
        else:
            n1=Node(i)
            n1.next=self.last.next
            self.last.next=n1
            self.last=n1
    
    def insertFirst(self):
        i=int(input("Enter data to insert node at the begining:"))
        if(self.last==None):            
            self.last=Node(i)
            self.last.next=self.last
        else:            
            n1=Node(i)
            n1.next=self.last.next
            self.last.next=n1
            
        
    def display(self):
        if(self.last==None):
            print("Empty List!")
            return
        else:
            print("\n")
            n1=self.last.next
            while(n1!=self.last):
                print(n1.data, end="->")
                n1=n1.next
            print(n1.data)    
                
            
    def deleteLastNode(self):
        if(self.last==None):
            print("Empty List!")
            return
        elif(self.last.next==self.last):
            self.last=None
            return
        else:
            n1=self.last.next
            while(n1.next!=self.last):
                n1=n1.next
            n1.next=self.last.next
            del self.last
            self.last=n1
            
    def deleteNode(self):
         if(self.last==None):
            print("Empty List!")
            return
         else:
            i=int(input("Enter the data to delete from the list:"))
            n1=self.last.next
            if(n1.data==i and n1==self.last):
                self.last=None
                return
                
            if(n1.data==i):
                self.last.next=n1.next
                del n1
                return
            
            while(n1.data!=i and n1!=self.last):
                prev=n1
                n1=n1.next
            if(n1==self.last and n1.data==i):
                prev.next=n1.next
                del n1
                self.last=prev
                return
            if(n1==self.last):
                print("Data not found!")
                return
            elif(n1.data==i):
                prev.next=n1.next
                del n1
                
           
                

clist=CircularLinkedList()
ch=0
while(True):
    print("\n")
    print("1.Insert at the beginning")
    print("2.Insert at the end")
    print("3.Delete last node")
    print("4.Delete node")
    print("5.Display")
    print("6.EXIT")
    ch=int(input("Enter your choice:"))
    if ch==1:
        clist.insertFirst()
        clist.display()
    elif ch==2:
        clist.insertLast()
        clist.display()
    elif ch==3:
        clist.deleteLastNode()
        clist.display()
    elif ch==4:
        clist.deleteNode()
        clist.display()
    elif ch==5:
        clist.display()
    elif ch==6:
        break;
    else:
        print("Please re-enter correct choice!")
        
