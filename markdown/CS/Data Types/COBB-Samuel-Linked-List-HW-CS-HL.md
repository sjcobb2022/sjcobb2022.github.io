```JAVA

NAMES;

new_node = Node("Charlie");

changed = false;

curr_node = NAMES.head;


//assuming that the forst node is null and therefore therfore the first next value is teh first index in arrat
//added second stopping condition to prevent unuecessary loops
loop while curr_node.next() && !changed:
	
	//check charactesr , if asccii greater than the other then will insert
	if curr_node.next().data > new_node.data
		
		new_node.next = curr_node.next()
		
		curr_node.next = new_node.address()
		
		changed = true
		
	endif
	
	curr_node = curr_node.next()

endloop


```

