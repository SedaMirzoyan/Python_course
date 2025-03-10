class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None


    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        
        temp_node = self.head
        while (temp_node.next):
            temp_node = temp_node.next

        temp_node.next = new_node



    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next



    def detect_loop(self):
        has_cycle = False
        fast_ptr = self.head
        slow_ptr = self.head

        while(fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if(slow_ptr == fast_ptr):
                has_cycle = True

        return has_cycle
    
    
    def find_middle(self):
        len_list = 0
        temp = self.head
        while(temp):
            temp = temp.next
            len_list += 1

        mid = int(len_list/2)

        ind = 0
        temp = self.head
        while(temp and ind < mid):
            temp = temp.next
            ind += 1
            elem = temp.data
        
        return elem



def main():
    linked_list = Linked_list()
    linked_list.add_at_beginning(5)
    linked_list.add_at_end(-7)
    linked_list.add_at_beginning(3)
    linked_list.add_at_end(2)
    linked_list.add_at_beginning(1)
    linked_list.add_at_end(-8)
    linked_list.add_at_end(9)


    linked_list.print_list()
    print(linked_list.detect_loop())
    print("Linked list's middle element is", linked_list.find_middle())



if __name__=="__main__":
    main()


        