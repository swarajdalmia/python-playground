
# Dynamic Programming 

Dynamic Programming, solves a problem by breaking them into subproblems and solving the subproblems. Such a relationship can be captured using a Bellman Equation. It is applicable for problems that have operlapping subproblems and an optimal substructure property. 
 
The simplest subproblems are naive\base cases and larger subproblems are solved incrementally using the earlier solved subproblems. The approach is applicable when one is trying to optimise something gives constraints and cannot be applied to solve all probelms. All problem that can be solved by this approach have an [optimal substructure](https://en.wikipedia.org/wiki/Optimal_substructure). Some probelms that have optimal substructure but don't have operlapping subproblems, can be solved using a greedy approach.   

The *Knapsack probelem* is one of the quientessential problems that can be solved using this approach. The knapsack problem is solved by builing up a table. Each row of the table is filled considering the elements of that row and the optimal solution uptill then, which is contained in the previous row. The granularity of the subproblems is the size of the smallest item. At each level, the optimal knapsack can't be composed on more than 2 subknapsacks. However, each of the subknack sacs might themselves contain two sub knacksacs. the most optimal soluition doesn't need to fill the knapsack completely. 

The *longest common subsequence* is another common problems thats solved using this approach.  A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.The formula for filling up the table is different in this case. The value for each element is dependent on the element on the top-left, left and top. The "git diff" command uses a DP approach similar to solving the longest common subsequence.

Other examples : (these problems have overlapping subproblems) Fibonacci sequence, Dijkstra's shortest path algorithm. 

The fibonacci numbers if generated through only recursion will have exponential complexity however, if solved using dynamic programming will have a linear complexity. 


### Tabulation vs Memoization 
In tablulation, a complete table is built up to solve all the subproblems, finally reaching the ooptimal solution right at the end. Memoization refers to the technique of caching and reusing previously computed results. Memorization is typically top-down. We start with the largest problem, while tabulation is always bottom up. 

If the original problem requires all subproblems to be solved, tabulation usually outperformes memoization by a constant factor. This is because tabulation has no overhead for recursion and can use a preallocated array rather than, say, a hash map. So memory is effiiently used and since it is done iteratively less stack space is used. Furthermore, the regular pattern of the table accesses may be used to reduce time or space requirements.

If only some of the subproblems need to be solved for the original problem to be solved, then memoization is preferrable since the subproblems are solved lazily, i.e. precisely the computations that are needed are carried out.[REF](https://programming.guide/dynamic-programming-vs-memoization-vs-tabulation.html)   


### Solving Heuristic
There is no one formula for solving a problem using DP. 

### Independence of sub-probelms
The DP approach can only be used when each of the subproblems are discrete and independent of the others. If some subproblem is depedent on another, then the default DP approach can not be used. 


### Problems 

#### Longest Increasing Subsequence: 
Example : The longest LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is {10, 22, 33, 50, 60, 80} and it consists of 6 elements.
 
Solution : The start of the sequence is 10. Now, one could have been given the string start that starts from 22. Therefore the recurrence relation is such.
Let n\_LIS[i] be the length of the LIS starting from i and one that includes i. Now:

n\_LIS[i] = 1 + max( n\_LIS[j]) such that i\<j\<n and arr[i] < arr[j]
if no such j exists 
n\_LIS[i[ = 1

The time cimplexity is n^2, however there exists an algorithm that does it in nlog(n)

#### Edit Distance 
Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’. If the 3 operations of insert, remove, replace cost the same. 


if str1[i-1] == str2[j-1]: 
    dp[i][j] = dp[i-1][j-1]

else: 
    dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                       dp[i-1][j],        # Remove 
                       dp[i-1][j-1])      # Replace

The time,space complexity if O(n\*m). The space complexity can be reduced, since we require only the elements 
fromt he above row. therefore the space complexity can be reduced to O(m). 

#### Partition 
Partition a set into two subsets such that the difference of subset sums is minimum. 

...

Link to [common problems](https://www.geeksforgeeks.org/top-20-dynamic-programming-interview-questions/) and a larger [list](https://www.geeksforgeeks.org/dynamic-programming/) of problems. 



