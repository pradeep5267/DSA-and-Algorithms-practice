#%%
class Node():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.right_child = right
        self.left_child = left

class BST():
    def __init__(self):
        self.root = None

    def insert(self, data):
        tmp_node = Node(data)
        if self.root is None:
            self.root = tmp_node
            current_node = self.root
        else:
            current_node = self.root
            parent_node = None

            while current_node is not None:
                parent_node = current_node
                if (tmp_node.data < current_node.data):
                    current_node = current_node.left_child
                    if current_node is None:
                        parent_node.left_child = tmp_node
                        return
                if (tmp_node.data >= current_node.data):
                    current_node = current_node.right_child
                    if current_node is None:
                        parent_node.right_child = tmp_node
                        return

    # !!! incomplete wrong logic !!! 
    def delete_node_recursive(self, data, recursive_root):
        '''
        INCOMPLETE !!!
        work in progress 
        '''
        if recursive_root is None:
            return recursive_root
        if self.root.data == data:
            return '0'
        
        if (data < recursive_root.data):
            print('less than')
            print(recursive_root.data)
            recursive_root = self.delete_node(data, recursive_root.left_child)
        elif (data > recursive_root.data):
            print('more than')
            recursive_root = self.delete_node(data, recursive_root.right_child)

        elif (recursive_root.data == data):
            print('match found')
            print(f'recursive_root.data = {recursive_root.data}')

            # assume the node has no left or right children
            if (recursive_root.left_child is None and recursive_root.right_child is None):
                self.recursive_root = None
    
            # assume right child exists
            if (recursive_root.left_child is None):
                tmp = recursive_root.right_child
                self.recursive_root.right_child = None
                self.recursive_root.data = tmp.data
         
            # assume left child exists
            if (recursive_root.right_child is None):
                tmp = recursive_root.left_child
                self.recursive_root.data = tmp.data
                self.recursive_root.left_child = None
    

    def delete_node(self, data):
        current_node = self.root
        parent_node = None
        if (data == current_node.data):
            return 'cant delete root node'
        while current_node.data is not None:
            parent_node = current_node
            if (data < current_node.data):
                current_node = current_node.left_child
            elif (data > current_node.data):
                current_node = current_node.right_child
            elif (data == current_node.data):
                parent_node = current_node

                # assume the node has no left or right children
                if (current_node.left_child is None and current_node.right_child is None):
                    current_node = None
                    # parent_node = None
                    return
        
                # assume right child exists
                if (current_node.left_child is None):
                    tmp_node = current_node.right_child
                    current_node = current_node.right_child
                    current_node = None
                    parent_node.data = tmp.data
                    return
                    
                # assume left child exists
                if (current_node.right_child is None):
                    current_node = current_node.left_child
                    current_node = None
                    parent_node.data = tmp.data
                    return


    def print_inorder(self, recursive_root):
        if recursive_root is None:
            return
        self.print_inorder(recursive_root.left_child)
        print(recursive_root.data)
        self.print_inorder(recursive_root.right_child)


    def print_level_order_queue(self):
        current_node = self.root
        queue = []
        queue.append(current_node)

        while (len(queue) > 0):
            current_node = queue[0]
            queue.pop(0)
            
            if current_node.left_child is not None:
                queue.append(current_node.left_child)
            if current_node.right_child is not None:
                queue.append(current_node.right_child)
            
            
            print(current_node.data)
            


    
    def min_value(self):
        current_node = self.root
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node.data




    
tree = BST() 
tree.insert(5) 
tree.insert(2) 
tree.insert(7) 
tree.insert(9) 
tree.insert(1)
# print(tree.root.data)
tree.print_inorder(tree.root)
# tree.delete_node(1)
# print(z)
print('level order using queue')
tree.print_level_order_queue()


# # tree.min_value()
# tree = BST() 
# tree.insert(5, tree.root) 
# tree.insert(2, tree.root) 
# tree.insert(7, tree.root) 
# tree.insert(9, tree.root) 
# tree.insert(1, tree.root)
# # print(tree.root.data)
# tree.print_inorder(tree.root)

# # tree.min_value()
#%%
#     n1 = Node("root node")  
#     n2 = Node("left child node") 
#     n3 = Node("right child node") 
#     n4 = Node("left grandchild node")

#     n1 = Node("root node")  
#     n2 = Node("left child node") 
#     n3 = Node("right child node") 
#     n4 = Node("left grandchild node")

#     n1.left_child = n2 
#     n1.right_child = n3 
#     n2.left_child = n4

#     n1._print()
#     #%%
# #%%
# i = 0
# while i<=5:
#     print(f'i = {i} entered while loop')
#     if (i<6):
#         print(f'i = {i} entered first if block')
#         i += 1
#         if (i<6):
#             print(f'i = {i} entered second if block')
            
#         else:
#             print(f'i = {i} entered first else block')
# print(f'i = {i} exited while block')

#%%
