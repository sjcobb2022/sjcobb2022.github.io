# Data Structures: Binary Trees SW

1. How to insert a new node into a binary search tree? `assumes that this is a leaf`
	 - traverse through the binary tree
	 - check if inserted value greater or less than data of current node
		 - if value greater than nodes data continue traversing on right
		 -  if value less than nodes data continue traversing on left
	 - if node is greater than value, and current left/right node is null
		 - set parent's left/right pointer to be new node

2. How to delete a leaf node in a binary search tree?
 - select leaf (may involve traversing until some key/data is found)
 - get leaf parent (if has backlogs then this should be easy but should be stored if have to traverse tree)
 - set parents pointer to null (doesn't have any children since it is a leaf node)
	 - may have to check values to make sure if it was the right or left node

3. How to delete a node in the middle of a binary search tree?  
 - select node (may involve traversing until some key/data is found)
 - if node has 1 child, simply set the parent node pointer to the only child
 - otherwise
	 - find inorder successor to node
	 - copy the contents of that value to parent node address and then delete current node

4. How to delete a node in a binary search tree if it were the root node?
 - can use same method as in question 3, in order succession seems a pretty good option
 - another method: 
	 - find deepest rightmost value of the node that is going to be deleted (root)
	 - replace the root with this data
	 - delete the previous deepest right-most node