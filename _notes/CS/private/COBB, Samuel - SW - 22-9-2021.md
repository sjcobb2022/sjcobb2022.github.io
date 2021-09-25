1. Outline the need for higher-level programming languages 
	- Higher level programming languages allows the code to be easier to read, write, and maintain. Additionally, they allow the development of cross-platform applications, since higher level languages are generally platform independent. It would take too long to write common programs in machine code.


2. Differentiate machine code from higher-level programming languages. 

Machine code is designed to be read by computers, and therefore is comprised of binary. In opposition, higher level languages are designed to be read by humans, which allows for greater amounts of abstraction. Machine code can be directly understood by a computer and requires no translation, wheras higher level programming languages need to be translated into machine code to be understood by a computer system. 

3. Create a psuedocode for the following: 
	- Bubble Sort 

```java

Array a

i = length a

sorted = false

//properties: always moves the largest value to its position
//will swap values if that is the case

loop while i > 0 AND sorted is false 
	sorted = true
	
	loop for j < i where j starts at 1
		
		if the value of a[j-1] > a[j]
			
			TEMP = a[j-1]
			
			a[j-1] = a[j]
			
			a[j] = TEMP
			
			sorted = false
	
		end if
	
	end loop
	
	i--
end loop

OUT a 


	

```

 - Selection Sort 

```java

Array a

N = length of a

loop for i=0; i < N; i++ 

	//max index is current index until proven otherwise

	MIN_INDEX = i
	
	loop for j=i+1; j < N; j++
		
		//check if the the values above current index are smaller
		
		if array[j] < array[MIN_INDEX]
		
			MIN_INDEX = j
			
		endif
		
	end loop
	
	if MIN_INDEX not the same as i
	
		//switch the values
		
		TEMP = a[i]
		
		a[i] = a[MIN_INDEX]
		
		a[MIN_INDEX] = TEMP
		
	end if
	
end loop




```

4. Differentiate a sequential search from a binary search. 

For a binary search, all elements in some set of data must be ordered for a value to be found, whereas sequential searches do not require data to be in order. Binary searches are generally faster than sequential searches, as they have a time complexity of O(log n), meaning that they search through log n elements in order to find the precise value. Sequential searches however search through each value in order to find the 

5. Convert the following:
	- 11001010 from binary to octal 
		-  312

	- 11001010 from binary to hexadecimal
		-  CA

	- 11001010 from octal to binary
		- 001001000000001000001000

	- 11001010 from hexadecimal to binary
		- 00010001000000000001000000010000

	- ABEF from hexadecimal to binary
		- 1010101111101111


