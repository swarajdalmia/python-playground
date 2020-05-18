
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

 

