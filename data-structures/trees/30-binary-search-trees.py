#Day 22 of 30 days of code.
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getMaxNodes(self,root):
        if root is None:
            return 0

        height = 1
        h_left = myTree.getMaxNodes(root.left)
        h_right = myTree.getMaxNodes(root.right)
        return max(h_left, h_right) + height

    def getHeight(self, root):
        return myTree.getMaxNodes(root) - 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)