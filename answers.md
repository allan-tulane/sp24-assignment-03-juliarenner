# CMPS 2200 Assignment 3
## Answers

**Name:** Julia Renner


Place all written answers from `assignment-03.md` here for easier grading.

- 1(a):

- A greedy algorithm that produces as few coins as possible that sum to N must first choose the largest value of 2^k (coin value) that is not greater than N. Then, the algorithm should continue subtracting this value from N until N equals zero. 

- 1(b):

- The largest coin possible is being used for the subtraction which means that there could be no way for a more optimal solution to exist because the least coins possible could be used in this greedy case.

- 1(c):

- The Work of my algorithm is O(logn)
- The Span of my algorithm is O(logn)

- 2(a):

- If the Fortuito currency uses coins with values 1, 3, and 4, the greedy algorithm would likely choose a 4 dollar coin and two one dollar coins if it were to be making change for 6 Fortuitan coins. This is obviously not the most optimal solution, which would be to simply select two of the 3 dollar coins. In this case, the greedy algorithm fails to use the fewest coins.

- 2(b):

- This problem has an optimal substructure property because it finds the optimal solutions to the sub-problems less than N amounts in order to solve the optimal amount for N.

- 2(c):

- We could use dynamic programming for this problem by writing a recurisve algorithm that iterates over itself, storing results from subproblems and thereby preventing uneeded repetition. This would be using top-down memoization. Work = O(N*k), Span = O(N).
