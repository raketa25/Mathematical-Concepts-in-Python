class DecisionNode:
    # Class of nodes in the decision tree
    # It is a simple binary node with potentially two children: left and right
    # the left node is returned when the condition is true, and the right node is returned when the condition is false
    def __init__(self, name, condition, value=None):
        self.name = name
        self.condition = condition
        self.value = value
        self.left = None
        self.right = None
        
    def add_left_node(self, left):
        self.left = left
        
    def add_right_node(self, right):
        self.right = right

    def is_leaf(self):
        # a node without children is a leaf node
        return (not self.left) and (not self.right)
    
    def next_node(self, input_data):
        # this function returns the next node to go through based on the test results of the condition function
        cond = self.condition(input_data)
        if self.is_leaf():                      # if the node is a leaf, there are no children to go through.
            return None
        if cond:
            return self.left
        else:
            return self.right
        

# Now let's create a simple decision tree class

class DecisionTree:
    # A simple decision tree model which provides predictions based on the input data.
    # A prediction is the sum of leaves values, for leaves that have been activated by the input data.
    
    def __init__(self, root):
        self.root = root


    def predict(self, input_data):
        # this function traverses the tree based on the input data and returns the sum of the values of the activated leaves
        # current_node = self.root
        # prediction = 0
        child = root
        while child and not child.is_leaf():
                child = child.next_node(input_data)
        
        return child.value
 
# Let's create a simple decision tree and test it
# Define some conditions for the nodes

root = DecisionNode("root", lambda d: d["A"] > 2.0)

root_left = DecisionNode("root_left", lambda d: d["B"] > 10.0, None)
root_right = DecisionNode("root_right", None, 1)

left_left = DecisionNode("left_left", None, 2)
left_right = DecisionNode("left_right", None, 3)

root.add_left_node(root_left)
root.add_right_node(root_right)

root_left.add_left_node(left_left)
root_left.add_right_node(left_right)

# Create the decision tree
tree = DecisionTree(root)

# Test the decision tree with some input data
input_data_1 = {"A": 1, "B": 1}         # This should activate root -> root_left -> left_left
input_data_2 = {"A": 1, "B": 10}        # This should activate root -> root_left -> left_right
input_data_3 = {"A": 3, "B": 11}                # This should activate root -> root_right
input_data_4 = {"A": 3, "B": 9}                 # This should activate root -> root_right but not activate the leaf

print(tree.predict(input_data_1))  # Expected output: 1
print(tree.predict(input_data_2))  # Expected output: 1
print(tree.predict(input_data_3))  # Expected output: 2
print(tree.predict(input_data_4))  # Expected output: 3