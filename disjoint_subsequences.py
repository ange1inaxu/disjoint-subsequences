def disjoint_subsequences(X, Y):
    """Determine whether X appears as a sub-sequence of Y twice, where the two
    sub-sequences are disjoint. In addition to the usual alphanumeric
    characters, Y may contain instances of the special wild card character '*'
    that can match any other character.

    Args:
        X: a string
        Y: a string

    Returns:
        True if X appears as a sub-sequence of Y twice.
    """
    k, n = len(X), len(Y)
    
    # base cases
    if k==0:
        if n==0:
            return False
        return True
    
    # relate
    def helper(i1, i2, j):
        
        if j == n:
            return i1 == i2 == k
        
        if i1 < k and j < n and (X[i1] == Y[j] or Y[j] == "*"):
            return helper(i1+1, i2, j+1)
        
        if i2 < k and j < n and (X[i2] == Y[j] or Y[j] == "*"):
            return helper(i1, i2+1, j+1)
        
        return helper(i1, i2, j+1)
    
    return helper(0, 0, 0)
        
    