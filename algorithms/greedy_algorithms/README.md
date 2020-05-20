# Greedy Algorithms

Often used for difficult problems(NP-Complete). A greedy strategy is a problem solving heuristic that can be used to arrive at approximate solutions, quickly.

At every decision branch one performs a locally optimal decision. This method often reaches to a good approimation of the global optima and sometimes even reaches it. However, it doesn't always work. 

**Greedy Knapsack**: The most expensive item that fits in the remaining bag space is picked up recursively.    

For NP-Complete problems greedy algorithms become necessary. 

**Set Cover Problem**: One needs to cover an entire set of elements using the smallest number of elements. Each element is a subset of the entire set. 
The grredy solution is : Pick the station that covers the most states that haven’t been covered yet irrespective of already covered states it covered. 

They are also called approximate algorithms and they are judged by how fast they are and how close to the actual solution they are. 

Popular problems solved using this approach : Job scheduling, shortest path problem, huffman encoding, k-centre's problem, coloring of graphs, minimum spanning tree problem, shortest superstring problem. 

 

