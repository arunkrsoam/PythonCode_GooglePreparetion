class BinaryTreeNode(object):
    # Iniliase the node object
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to insert the node values
def insert_node(node, eleValue):
    if node == None:
        return BinaryTreeNode(eleValue)
    if eleValue < node.value:
        node.left = insert_node(node.left, eleValue)
    elif eleValue > node.value:
        node.right = insert_node(node.right, eleValue)
    return node


# Function to get the 2nd largest element
def nth_largest(root, c):
    if root == None or c[0] >= 2:
        return
    # Revvers order traversal
    # print(root.value)
    nth_largest(root.right, c)

    # Counter increase of nodes
    c[0] += 1

    # If c becomes nth then this is the 2nd largest element
    if c[0] == 2:
        print(c[0], "largest element is", root.value)
        return

    # Recur for left subtree
    # nth_largest(root.left, c)


# Main function for BST nth hight element
# BST
#          40
#        /    \
#     20       50
#   /   \     /   \
# 70     80  100   55
if __name__ == '__main__':
    root = None
    root = insert_node(root, 40)
    insert_node(root, 20)
    insert_node(root, 50)
    insert_node(root, 70)
    insert_node(root, 80)
    insert_node(root, 100)
    insert_node(root, 55)
    # Function to find the nth largest value
    c = [0]  # iniliase the counter of node as [0]
    # Call the function to get the nth largest element
    nth_largest(root, c)
