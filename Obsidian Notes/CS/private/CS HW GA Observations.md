# Observations
#### Samuel Cobb - 11/9/2021

## Tournament Selection
 - Slower that truncation in general
 - A little more inconsistent at getting a optimal answer 
 - Higher density of better scoring Genes (second place and third place have higher counts)
 - Max generation rarely met
 - Gets to a much higher generation that truncation
 - Works better than truncation with larger gene pools

<br>

## Roulette Wheel Selection
 - Fastest out of the 3 selection algorithms so far
 - Almost always gets to max generation
 - Converges faster with smaller gene pools ( <100 )
 - Answers are less than optimal by quite a lot
 - Really large variation in the top genes (only 1 of each of the top 10)
 - Inconsistent when it comes to final results (no matter how many generations)

<br>

## Stochastic Selection
 - Seems to be faster than tournament but slower that roulette 
 - Gets to max generation in most counts (other than 1 or 2 instances)
 - Pretty large variety in top genes (good, means more variation in children)
 - Gets good results, not perfect but better than roulette significantly.
 - Consistently ends up with similar/same top results
 - Top paths are all similar (only a few values switched)


<br>

## Partially Mapped Crossover
 - Slowest of the 3 crossover types
 - Reduced the amount of repetitive genes in all selection types (even TR)
 - Increased variation in the paths
 - Got average better results (increase variation == increased results???)
 - In the case of roulette selection, increased time taken to reach terminating condition significantly
 - Little variation between top gene fitness; withing range of around 200


<br>

## Order Crossover
 - Fastest of the crossover methods
 - Large variation in fitness values of best genes (~400 max)
 - Minimized fitness value well
 - Variation in oaths minimal but more noticeable than that in CX
 - Took longer to find best gene; at least 10 generations for a the best result. Implies significant variation
 - Reduces repetitive behavior; less repetition of genes in truncation for example.

<br>

## Cycle Crossover
 - Slightly faster than PMX.
 - Difference in paths minimal
 - Seemed to increase count better genes (could just be coincidence)
 - Decreased variation in the top genes; difference best and worst gene reduced
 - Significantly worse fitness performance than either of the other 2 methods
 - Can't seem to get anything better than the best value in the initial pool