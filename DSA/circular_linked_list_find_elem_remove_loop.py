class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Circular_linked_list:
    def __init__(self):
        self.head = None


    def add_element(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        
        temp_node = self.head
        while (temp_node.next != self.head):
            temp_node = temp_node.next

        temp_node.next = new_node
        new_node.next = self.head



    def print_list(self):
        temp = self.head
        print(temp.data)
        
        while(temp.next != self.head):
            temp = temp.next
            print(temp.data)


    #print for singly linked list, for test
    #def print_list_singly(self):
    #    temp = self.head
    #    while(temp):
    #        print(temp.data)
    #        temp = temp.next


    def remove_loop(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if (fast_ptr == slow_ptr):
                fast_ptr = self.head
                while (fast_ptr.next != slow_ptr.next):
                    fast_ptr = fast_ptr.next
                    slow_ptr = slow_ptr.next
                slow_ptr.next = None      


    def search_element(self, data):
        temp = self.head
        found = False

        while(temp.next != self.head):
            temp = temp.next
            if(temp.data == data):
                found = True
             
        if(found == True):
            print(f"Element {data} is found")
        else:
            print(f"Element {data} is not found")

        return found

    

def main():
    node_val_list = [5, -7, 3, 2, 1, -8, 9, 17, -6, 4, 11]

    circular_linked_list = Circular_linked_list()

    for i in node_val_list:
        circular_linked_list.add_element(i)

    circular_linked_list.print_list()
    circular_linked_list.search_element(17)
    circular_linked_list.search_element(12)
    circular_linked_list.remove_loop()

    #after removing loop print singly linked list
    #circular_linked_list.print_list_singly()


if __name__=="__main__":
    main()


        