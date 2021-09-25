1) 
a) 

````java


Collection Weather

int COUNT

loop while Weather.hasNext()
	COUNT++
	Weather.next()
end loop

OUTPUT COUNT
````


b) 

````java

Collection Weather;

String[] DAYS = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};

int COUNT;
float MAX = 0;
int POSITION = 0;

loop while Weather.hasNext()

	float CURR = Weather.next();
	if CURR > MAX 
		POSITION = COUNT;
		MAX = CURR;
	endif 
	
	COUNT++;
	
end loop

OUTPUT DAYS[floor(POSITION / 24)];

````


2) 

| A   | B   | C   | OUT |
| --- | --- | --- | --- |
| 1   | 1   | 1   | 0   |
| 1   | 1   | 0   | 1   |
| 1   | 0   | 1   | 1   |
| 1   | 0   | 0   | 1   |
| 0   | 1   | 1   | 0   |
| 0   | 1   | 0   | 1   |
| 0   | 0   | 1   | 0   |
| 0   | 0   | 0   | 0   | 


