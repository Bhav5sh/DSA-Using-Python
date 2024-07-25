def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-1)
def sumNodd(n):
    if n==1:
        return 1
    return 2*n-1+sumNodd(n-1)
def sumNeven(n):
    if n==1:
        return 2
    return 2*n+sumNeven(n-1)
def factN(n):
    if n==0:
        return 1
    return n*factN(n-1)
def sumNsquare(n):
    if n==1:
        return 1
    return n*n+sumNsquare(n-1)


print('sum is =',sumNsquare(5))