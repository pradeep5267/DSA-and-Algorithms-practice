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

    def find_parent_and_current(self, data):
        parent_node = None
        current_node = self.root
        while True:
            if (current_node.data == data):
                return (parent_node, current_node)
            if (data < current_node.data):
                parent_node = current_node
                current_node = current_node.left_child
            if (data > current_node.data):
                parent_node = current_node
                current_node = current_node.right_child
            if (current_node is None or current_node.data is None):
                return None

    def delete_node_recursive(self, data, recursive_root, recursive_root_parent):
        '''
        ugly, but works  
        '''
        if recursive_root is None:
            return recursive_root
        
        if (data < recursive_root.data):
            print('less than')
            print(recursive_root.data)
            recursive_root = self.delete_node_recursive(data, recursive_root.left_child, recursive_root)
        elif (data > recursive_root.data):
            print('more than')
            recursive_root = self.delete_node_recursive(data, recursive_root.right_child, recursive_root)

        elif (recursive_root.data == data):
            print('match found')
            print(f'recursive_root.data = {recursive_root.data}, parent_node = {recursive_root_parent.data}')

            # assume the node has no left or right children
            if (recursive_root.left_child is None and recursive_root.right_child is None):
                print(f'node has no children')
                if (recursive_root_parent.left_child == recursive_root):
                    recursive_root_parent.left_child = None
                elif (recursive_root_parent.right_child == recursive_root):
                    recursive_root_parent.right_child = None
                return

            # assume only left child exists
            if (recursive_root.right_child is None):
                print(f'node has left child')
                tmp = recursive_root.left_child
                recursive_root_parent.left_child = tmp
                recursive_root = None
                return
            # assume only right child exists
            if (recursive_root.left_child is None):
                print(f'node has left child')
                tmp = recursive_root.right_child
                recursive_root_parent.right_child = tmp
                recursive_root = None
                return
    
            # assume right child/tree exists
            if (recursive_root.left_child is None):
                print(f'node has right child')
                right_min_node = self.min_value(recursive_root.right_child)
                recursive_root.data = right_min_node.data
                # right_min_node.data
                self.delete_node_recursive(right_min_node.data, right_min_node, right_min_node)
                # recursive_root = None
                return


    def print_inorder(self, recursive_root):
        '''
        left, root, right
        '''
        if recursive_root is None:
            return
        self.print_inorder(recursive_root.left_child)
        print(recursive_root.data)
        self.print_inorder(recursive_root.right_child)

    def print_preorder(self, recursive_root):
        '''
        root, left, right
        '''
        if recursive_root is None:
            return
        print(recursive_root.data)
        self.print_preorder(recursive_root.left_child)
        self.print_preorder(recursive_root.right_child)

    def print_postorder(self, recursive_root):
        '''
        left, right, root
        '''
        if recursive_root is None:
            return
        self.print_preorder(recursive_root.left_child)
        self.print_preorder(recursive_root.right_child)
        print(recursive_root.data)


    def print_level_order_queue(self, root):
        '''
        used a list as a queue
        '''
        root = None
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
    def min_value(self, recursive_root):
        current_node = self.root
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node


tree = BST() 
tree.insert(5) 
tree.insert(2) 
tree.insert(7) 
tree.insert(9) 
tree.insert(1)

# parent_node, child_node = tree.find_parent_and_current(2)
# print(f'parent is {parent_node.data}, child is {child_node.data}')
# # print(tree.root.data)
# tree.print_inorder(tree.root)
# print('***************')
# tree.delete_node_recursive(7, tree.root, tree.root)
# # print('level order using queue')
# tree.print_level_order_queue(tree.root)

### for printing
# tree.print_inorder(tree.root)
# tree.print_preorder(tree.root)
# tree.print_postorder(tree.root)
# tree.print_level_order_queue(tree.root)

### for finding min value
# tree.min_value()
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