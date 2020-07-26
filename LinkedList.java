/*
1.Creation - done
Insertion after node - list.insertAfterNode();
Insertion at the end - list.insertNode();
Insertion in the beginning - list.insertAtHead();
Deletion on last node - list.deleteLastNode();
Deletion of specific node - list.deleteNode();
Deletion of first node - list.deleteFirstNode();
Display list - list.display();
List Reverse - list.reverse();
Merge 2 linked list sorted
 */

import java.util.Scanner;

class Node
{
    int data;
    Node next;
    Node(int data)
    {
        this.data=data;
        this.next=null;
    }
}

public class LinkedList {
    static Scanner sc=new Scanner(System.in);
    static Node head=null;
    public static void main(String args[])
    {
        LinkedList list=new LinkedList();
        int ch=0;
        do
        {
            System.out.println("\n1.Insert at the beginning");
            System.out.println("2.Insert at the end");
            System.out.println("3.Insert after a specific node");
            System.out.println("4.Delete first node");
            System.out.println("5.Delete last node");
            System.out.println("6.Delete specific node");
            System.out.println("7.Reverse list");
            System.out.println("8.Display");
            System.out.println("9.EXIT");
            System.out.println("Enter your choice:");
            ch=sc.nextInt();
            switch(ch)
            {
                case 1:
                    list.insertAtHead();
                    list.display();
                    break;
                case 2:
                    list.insertNode();
                    list.display();
                    break;
                case 3:
                    list.insertAfterNode();
                    list.display();
                    break;
                case 4:
                    list.deleteFirstNode();
                    list.display();
                    break;
                case 5:
                    list.deleteLastNode();
                    list.display();
                    break;
                case 6:
                    list.deleteNode();
                    list.display();
                    break;
                case 7:
                    list.reverse();
                    list.display();
                    break;
                case 8:
                    list.display();
                    break;
                case 9:
                    break;

            }
        }while(ch!=9);

    }
    public void reverse()
    {
        System.out.println("Reverse");
        if(head==null)
        {
            System.out.println("List is Empty!");
            return;
        }
        Node temp=null,prev=null,curr=null;
        temp=head;
        prev=head;
        if(head.next.next!=null) {
            curr = head.next.next;
            temp=head.next;
        }
        else
        {
            temp=temp.next;
            temp.next=head;
            head.next=null;
            head=temp;
            return;
        }
        while(curr.next!=null)
        {

            temp.next=prev;

            prev=temp;
            temp=curr;
            curr=curr.next;

        }
        if(curr.next==null)
        {
            temp.next=prev;
            curr.next=temp;
            head.next=null;
            head=curr;
        }
    }


    public void deleteNode()
    {
        if(head==null)
        {
            System.out.println("List is Empty!");
            return;
        }
        System.out.println("Enter the node to delete");
        int i=sc.nextInt();
        Node temp=head;
        Node prev=null;
        while(temp.data!=i) {
            prev=temp;
            temp = temp.next;
        }
        if(prev==null)
        {
            head=temp.next;
            temp=null;
        }
        else
        {
            prev.next=temp.next;
            temp=null;
        }
    }
    public void deleteFirstNode()
    {

        if(head==null)
        {
            System.out.println("List is Empty!");
            return;
        }
        if(head.next==null)
            head=null;
        else
        {
            Node temp;
            temp=head;
            head=head.next;
            temp=null;
        }
    }
    public void deleteLastNode()
    {
        if(head==null)
        {
            System.out.println("List is Empty!");
            return;
        }
        Node temp=head,prev=null;
        while(temp.next!=null) {
            prev=temp;
            temp = temp.next;
        }
        if(prev==null)
            head=null;
        else
        {
            prev.next=null;
            temp=null;
        }
    }
    public void insertAtHead()
    {
        System.out.println("Enter data to insert at the beginning:");
        int i=sc.nextInt();
        if(head==null)
            head = new Node(i);
        else
        {
            Node n1=new Node(i);
            n1.next=head;
            head=n1;
        }

    }
    public void display()
    {

        if(head==null)
        {
            System.out.println("List is Empty!");
            return;
        }
        System.out.println("Display List:");
        Node temp;
        temp=head;
        do {
            System.out.print(temp.data+"-->");
            temp=temp.next;
        }while(temp!=null);
        System.out.println();
    }
    public void insertNode()
    {
        System.out.println("Enter the data to insert at the end:");
        int i=sc.nextInt();
        if(head==null)
            head = new Node(i);
        else
        {
            Node temp;
            temp=head;
            while(temp.next!=null)
                temp=temp.next;
            Node n1=new Node(i);
            temp.next=n1;
            n1.next=null;
        }
    }

    public void insertAfterNode()
    {
        System.out.println("Enter the node to insert data after it:");
        int i=sc.nextInt();
        System.out.println("Enter the data to insert:");
        int j=sc.nextInt();
        if(head==null)
        {
            System.out.println("List is Empty!");
            return;
        }
        Node temp;
        temp=head;
        while(temp.data!=i && temp.next!=null)
            temp=temp.next;
        if(temp.next==null && temp.data!=i)
        {
            System.out.println("Node not present!");
            return;
        }
        else
        {
            Node n1=new Node(j);
            n1.next=temp.next;
            temp.next=n1;
        }
    }
}
