# PMI : Principle of Mathematical Induction Hypothesis
# import sys
# sys.setrecursionlimit(1000)
def fact(n):
    if n ==0:
        return 1
    smallOutput = fact(n-1)
    return n * smallOutput
def sum(n):
    if n ==0:
        return 0
    smallOutput = sum(n-1)
    return smallOutput + n
#-------------------------------------------
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n)
    return
def print_n_to_1(n):
    if n==0:
        return
    print(n)
    print_n_to_1(n-1)
# -------------------------------------------
def fib(n):
    if n==1 or n== 2:
        return 1
    fib_n_1 = fib(n-1)
    fib_n_2 = fib(n-2)
    output = fib_n_1+fib_n_2
    return output
# -------------------------------------------
def isSorted(a):
    l = len(a)
    if l == 0 or l ==1:
        return True
    if a[0]>a[1]:
        return False
    smallerList = a[1:]
    isSmallerListSorted = isSorted(smallerList)
    if isSmallerListSorted:
        return True
    else:
        return False

def isSorted1(a,si):
    l= len(a)
    if si == l-1 or si == l:
        return True
    if a[si]>a[si+1]:
        return False
    isSmallerPartSorted = isSorted1(a,si+1)
    return isSmallerPartSorted
# -------------------------------------------
def sumArray(a):
    if len(a)==0:
        return 0
    restSum = sumArray(a[1:])
    return a[0] + restSum
def checkNum(a,x):
    if len(a)!=0:
        if x==a[0]:
            return True
        else:
            return checkNum(a[1:],x)
    return False
# -------------------------------------------
def Index(a,x):
    l = len(a)
    if l==0:
        return -1
    if x == a[0]:
        return 0
    smop = Index(a[1:],x)
    if smop == -1:
        return -1
    else:
        return smop +1

def Index1(a,x,si):
    l = len(a)
    if si == l:
        return -1
    if x == a[si]:
        return si
    smop = Index1(a,x,si+1)
    if smop == -1:
        return -1
    else:
        return smop
# -------------------------------------------
def indexLast(a,x):
    l = len(a)
    if l==0:
        return -1
    if x==a[l-1]:
        return l-1
    smop = indexLast(a[:-1],x)
    if smop == -1:
        return -1
    else:
        return smop
def indexLast1(a,x):
    l = len(a)
    if l == 0:
        return -1
    smop = indexLast1(a[1:], x)
    if smop != -1:
        return smop +1
    else:
        if x == a[0]:
            return 0
        else:
            return -1
def indexLastB(a,x,si):
    l = len(a)
    if si == l:
        return -1
    smop = indexLastB(a,x,si+1)
    if smop != -1:
        return smop
    else:
        if x == a[si]:
            return si
        else:
            return -1


#-------------------------------------------
if __name__ == '__main__':
    # n = int(input('give the value '))
    # print_1_to_n(n)
    # print_n_to_1(n)
    # print(fact(n))
    # print(sum(n))
    # print(fib(n))
    # a = [1,2,3,4,5,6,7,80,9]
    # print(isSorted(a))
    # print(sumArray(a))
    # print(checkNum(a,5))
    # print(isSorted1(a,0))
    a = [ 1,2,5,3,6,8,5,4,5,89,5,4]
    # print(Index(a,5))
    # print(Index1(a,5,0))
    print(indexLast(a,5))
    print(indexLast1(a,5))
    print(indexLastB(a,5,0))
