class Node:
    def __init__(self,value=None,left=None,right=None):
        self.val=value
        self.left=left
        self.right=right

class BST:
    def __init__(self):
        self.root=None

    def insertion(self,data):
        n=Node(data)
        if self.root==None:
            self.root=n
        else:
            final=[]
            def find_loc(current,value):
                if not current:
                    return True
                if current.val > value and find_loc(current.left,value):
                    final.append(current)
                    return True                
                if current.val < value and find_loc(current.right,value):
                    final.append(current)
                    return True
                else:
                    raise AttributeError('Dublicate number not be insert')
                
            find_loc(self.root,data)
            loc=final[0]
            if loc.val > data:
                loc.left=n
            else:
                loc.right=n
    def preorder_traversing(self):
        preorder=[]
        def preorder_traverse(current):
            if current:
                preorder.append(current.val)
                preorder_traverse(current.left)
                preorder_traverse(current.right)
        preorder_traverse(self.root)
        return preorder
        
    def inorder_traversing(self):
        inorder=[]
        def inorder_traverse(current):
            if current:
                inorder_traverse(current.left)
                inorder.append(current.val)
                inorder_traverse(current.right)
            
        inorder_traverse(self.root)
        return inorder
    def postorder_traversing(self):
        postorder=[]
        def postorder_traverse(current):
            if current:
                postorder_traverse(current.left)
                postorder_traverse(current.right)
                postorder.append(current.val)
        postorder_traverse(self.root)
        return postorder
    def search(self,data):
        def searching(current,data):
            if not current or current.val==data:
                return current
            if data < current.val:
                return searching(current.left,data)
            else:
                return searching(current.right,data)
    #     if current.left==None or current.right==None:


bst=BST()
bst.insertion(5)
bst.insertion(1)
bst.insertion(8)
bst.insertion(2)
bst.insertion(34)
bst.insertion(12)
bst.insertion(15)
bst.insertion(16)
bst.insertion(134)
bst.insertion(151)
# print('preorder element=',bst.preorder_traversing())
# print('inorder element=',bst.inorder_traversing())
# print('postorder element=',bst.postorder_traversing())
a=input("enter a number for check, it is present or not in bst")
print(f'is {a} in bst??',bst.search(a))