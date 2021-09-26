# Case Study SW


## Define Computational intractability.

Intractable problems are problems in which there are not efficient algorithm to solve them. Computationally, this means that there are no efficient algorithms to solve a specific problem. 

## Define Heuristic

A Heuristic is a method used for solving some problem faster than classical methods. Additionally heuristics can be used to help to approximate values that would take too long with the default algorithms used in these subject areas. Heuristics may be considered a "shortcut" to an answer, by trading accuracy and precision for speed.

## Differentiate Genetic Algorithms and Simulated Annealing

The first major differences between genetic algorithms and simulated annealing is the way in which data is handled. In the case of Genetic Algorithms, a population of genes is created to optimize a solution. In the case of simulated annealing, a single value is generally mutated with reducing random variation probabilistically. A second difference between the two algorithms are their strengths in hill climbing. Genetic algorithms (due to their reliance on random breeding between parents), are poor at hill climbing, wheras simulated annealing has the ability to do this probabilistically.

## Choose one application where the usage of a Genetic Algorithm may be considered ethically questionable? Explain. Expound further on how it can arrive at an ethically questionable conclusion? Give suggestions as to how it can be avoided.

### Application: Construction of Facial composites of suspects. 

the usage of genetic algorithms in this use case may be considered ethically questionable due to a variety of factors. One main factor that may be considered is the data that the model was originally trained to use; if the data is biased in any way, whether it be through certain features or racially biased in term of skin tone other other factors, the genetic algorithm will produced results that are biased in a similar way. Another factor that may be considered may be the effect of confirmation bias of eye-witnesses; if images produces show an eye-witness something that they would want to see (in opposition to the truth), there may be a bias in favor of specific features that may be similar, but misleading. 

The issue with eye-witnesses is harder to negate, due to confirmation biases being harder to remove, but certain steps (such as showing a certain ratio of possible features etc.) could be a feasible method to negate this issue. Additioanlly, using large amounts of unbiased training data (equal amounts of certain features and skin tones etc.) could help a genetic algorithm adapt better and become less racially sensitive. By defining a ethical fitness lanscape, genetic algorithsm are able to beocme more ethical and less biased.