def longest_common_subsequence(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values of size [m+1]*[n+1]
    L = [[None]*(n+1) for i in range(m+1)] 
    
    # the table is built bottom up, using the recurive definition thats shown in the elseif and else clause and the base case is shown in the if clause.      
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    print(f"The longest common subsequence is of length {L[m][n]}")


# Testing 
longest_common_subsequence("AGGTAB", "GXTXAYB")
