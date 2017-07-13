# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):
    hleft = hright = 0
    if root.left is not None:
        hleft = 1 + height(root.left)
    if root.right is not None:
        hright = 1 + height(root.right)

    return max(hleft, hright)