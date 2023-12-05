# Rough code; to be tidied up and improved

import math

def nCk(n,k):
    result = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return result

#output the list of odd integers leq n
def oddInts(n):
    _ = []
    for i in range(1,n+1):
        if i%2==1 and i<=n:
            _.append(i)
    return _


#F_n = [0;2,2,...,2], where there are n 2's in the continued fraction
def F_n(n):
    a_n,b_n = 0,0
    for x in oddInts(n):
        qty = nCk(n,x)*2**((x-1)/2)
        a_n+= qty
        b_n+= qty*(n+1)/(n+1-x)
    if n%2==0:
        b_n = b_n + 2**(n/2)
    a_n, b_n = int(a_n), int(b_n)
    F_n = "/".join([str(a_n),str(b_n)])
    return F_n
 
    
# A_n = 1+F_n. A_n is the rational approximation of sqrt2
def A_n(n,type="Fraction"):
    numbs = F_n(n).split("/")
    if int(numbs[0])>int(numbs[1]):
        a_n = numbs[1]
        b_n = numbs[0]
    elif int(numbs[0])<int(numbs[1]):      
        a_n = numbs[0]
        b_n = numbs[1]
    a_n = int(a_n)+int(b_n)
    if type.lower() =="decimal":
        A_n = a_n / int(b_n)
    elif type.lower() == "fraction":
        A_n = "/".join([str(a_n),str(b_n)])
    return A_n


#Let c_n, b_n \in \mathbb{N}. Suppose A_n = c_n \ b_n. Then the bound for |A_n-sqrt2| is 1/{b_n}^2
def errorBounds(n,type="Fraction"):
    numbs = A_n(n,"Fraction").split("/")
    if int(numbs[0])>int(numbs[1]):
        b_n = numbs[1]
    elif int(numbs[0])<int(numbs[1]):
        b_n = numbs[0]
    if type.lower() =="decimal":
        error = 1 / (int(b_n)**2)
    elif type.lower() == "fraction":
        error = "/".join([str(1),str(int(b_n)**2)])
    return error


for n in range(1,20):
    absError = abs(A_n(n,"Decimal")-math.sqrt(2))
    print(f'A_{n} = {A_n(n)} ≈ {A_n(n,"Decimal")}, errorBound ≈ {errorBounds(n,"Decimal")}, errorBound - absError ≈ {errorBounds(n,"Decimal")-absError}')
