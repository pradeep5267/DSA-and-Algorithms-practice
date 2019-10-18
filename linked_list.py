#%%
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList():
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0


    def _print(self):
        if self.head is None:
            print('None')
        else:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next

    def append(self, data):
        tmp_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = tmp_node

        if self.tail is None:
            self.tail = tmp_node
        else:
            tail_node = self.tail
            while tail_node.next:
                tail_node = tail_node.next
            tail_node.next = tmp_node

    def insert(self, position, data):
        insert_node = Node(data)
        counter = 0
        if self.head is None:
            self.head = insert_node 

        if position == 0:
            insert_node.next = self.head
            self.head = insert_node   

        current_node = self.head
        while current_node:
            if (counter == position-1):
                insert_node.next = current_node.next
                current_node.next = insert_node 
            current_node = current_node.next
            counter += 1
        self.size += 1
                
    def delete_node(self, position):
        if self.head is None:
            print('Invalid')
        else:
            counter = 0
            previous_node = self.head
            next_to_deleted_node = self.head
            while previous_node:
                if (counter == position - 1):
                    # both pointers now point to node which 
                    # is one position before delete node
                    next_to_deleted_node = previous_node

                    # the next_to_deleted_node points to the node to be 
                    # deleted 
                    next_to_deleted_node = next_to_deleted_node.next

                    # now the next is stored in tmp 
                    tmp_next = next_to_deleted_node.next

                    # previous node.next was pointing to the node to be deleted
                    # however it is now pointing to next of the deleted node ie 
                    # it points to the node which is after the deleted node
                    # and the next of the node to be deleted now points to None
                    previous_node.next = tmp_next
                    next_to_deleted_node.next = None
                    self.size -= 1
                previous_node = previous_node.next
                counter += 1

            












words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')
words.append('bacon')
words.append('chicken')
words.insert(0,'apple')
words.delete_node(2)
words._print()

#%%
