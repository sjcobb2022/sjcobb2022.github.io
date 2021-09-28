<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>
**Pre-University Department**

  
1.  A car park has two barriers. One barrier is at the entrance, where tickets are issued, and on barrier is at the exit, where paid tickets are checked when cars leave. A display at the entrance, showing the current availability of spaces in the car park, is updated as tickets are issued and checked.
    

	The actions of issuing, paying and checking a ticket operate on the collection of objects, TICKETS, that is organized as a linked list. Each object holds the following information:

	Nr: ticket number (a progressive unique identifier)

	Date: date of issue

	Arrival: time of issue (in 24-hour format)

	PaidOn: Date of payment

	PaidAt: time of payment (in 24-hour format)

	1.  Describe how a linked list is a suitable data structure for the given scenario. [2]
		- A linked list is a suitable format for this type of data, since it is reliant on time and the order of cars that come in. In this way, all cars that go through a barrier entrance will be ordered in the way in which they came in, which may lead to an easier way to search through data.


When a car arrives and the car park is not full, a ticket is issued, the entrance barrier is raised and the display is updated.

Payment of a ticket at a machine updates both the ticket and its object representation held in the linked list. The car must exit the car park within 10 minutes.

At the exit barrier the ticket is checked, and this makes the barrier rise and updates the display.
  
2.  For the given scenario, identify:
    
	1.  One example of two processes that could occur concurrently. [1]
		1.  raising both barriers since they are independent of one another
    
	2.  One example of two processes that could **not** occur concurrently. [1]
		1.  A ticket being checked cannot happen at the same time as a barrier opening since the ticked must be checked first before the barrier can open. 

	3.  State the conditions that needs to be checked on the ticket when a car leave the car park. [1]
		1.  The current time is less than 10 minutes from the time of payment
		2.  CurrentTime - PaidAt <= 10
    

A car arrives at the entrance barrier while another car is at the exit barrier.

4.  Explain the order in which the operations for raising the barriers and updating the display should be performed, to ensure a correct and efficient management of the car park. [3]
	- Exit barrier
		- Ticket is checked -> raise barrier for exit -> increment display
	- Entrance Barrier
		-   Give ticket -> decrement display -> raise barrier

Upon payment, the PaidOn and PaidAt fields are populated in the corresponding object, without removing it from the linked list.

5.  Outline one implication of this choice of design in terms of efficiency. [2]
	 -	If a value is not deleted, the linked list will eventually get too large and a device may run out of memory. Also to find a specific node in a linked list, it would take longer to traverse the linked list as there are more and more items.
 
The car park rules enforce a short-stay policy. Staying in the car park for up to 2 hours is allowed, and is subject to two possible fees. Stayin in the car park for durations longer than two hours is subject to three possible fines, in addition to the original fee, up to a maximum price for each day. Tickets are paid in Euros (EUR).

The possible fees and fine are stored in a two-dimensional (2D) array, RULES.

![](https://lh5.googleusercontent.com/E4eidVX7gznD8CMPjk7AtVGtOo2sxdALt6DRD7AMYnx5OB3Zeotb6RYHJ33zOXhxSpGEzYyDcd7pIp4wRYyqIt6-RfBNCeCvbJMwxJgwVS0zzEnmj2M6Cujbz8DQ2j_TYbdDJoA=s0)

For example:
-   Staying in the car park for 40 minutes cost 3.00 EUR
-   Staying in the car park for 3 hours costs 3.00 + 15.00 = 18.00 EUR
-   Any stay in the car park that exceeds 4 hours cost 30.00 EUR

6.  Construct the steps of an algorithm that calculates the amount that a ticket is to be charged. [5]


```java

TICKET

COST = 0

DURATION = TICKET.Date - TICKET.PaidOn

if DURATION > 4 hours then
	COST = RULES[1][2]

else if DURATION > 2 hours but DURATION < 4 hours
	COST = RULES[0][1] + RULES[1][1]

else if DURATION > 30 minutes and DURATION < 2 hours
	COST = RULES[0][1]

else if DURATION <= 30
	COST = RULES[0][0]

end if

OUT COST
	

```


2.  Identify the components of a node in a doubly linked list. [3]
     - A node in a doubly linked list has 3 main features, its data, the previous address and the next address.
     - The data in a doubly linked list contains the actual data that is meant to be stored.
     - The previous address stores the memory address of the previous item of data, this allows for the previous value to be found.
     - The next address stores the value of the next item in the linked list.
     - Previous addresses and next addresses are stored to allow data to be spread across memory mre freely that static data strictures.

3.  Describe the features of a dynamic data structure. [2]
	-   A dynamic data structure is a type of data that allows for data to be spread over memory and removes the need for consecutive data.
	-   Dynamic data structures also allow the flexibility to scale data in any way needed, allowing data to be changed in size at will.
	-   They 

4.  Create an algorithm that deletes a node from a double linked list based on a user-specified data. [5]

```java

LINKED_LIST;

curr_node = LINKED_LIST.HEAD

input X; //user inputed value to create

loop while True:
	if curr_node.next().data == X && curr_node.next().data != null
		curr_node = curr_node.next()
		break
	endif
endloop


if current_node.next().data == null
	OUT "there is not data that has that value"
else
	curr_node.prev().next() = curr_node.next().address
	curr_node.next().prev() = curr_node.prev().address
	
	clear memeory from curr_node or something or something like delete curr_node

endif


```