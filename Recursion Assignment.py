# 1. Assignment - Geometric Sum
def gp(a,r,k):
    if k==1:
        return a
    smop = gp(a,r,k-1)
    return f'{smop},{a*r**(k-1)}'
def gpSum(a):
    if len(a)==0:
        return 0
    smop = gpSum(a[1:])
    return int(a[0]) + int(smop)

# a = list(gp(1,2,5).split(','))
# print(a)
# print(gpSum(a))
# -------------------------------------------------------------------------------
# 2. Assignment - Check Palindrome
def palindrome(a,si,ei):
    if si>=ei:
        return'true'
    if a[si] == a[ei]:
        return palindrome(a,si+1,ei-1)
    else:
        return 'false'
# a = 'areera'
# print(palindrome(a,0,len(a)-1))
# -------------------------------------------------------------------------------
# 3. Assignment - Sum of Digits
def sumD(n):
    if n==0:
        return 0
    r = n%10
    a = int(n/10)
    smop = sumD(a)
    return r+smop

# print(sumD(155))
# -------------------------------------------------------------------------------
# 4. Assignment - Multiplication
def mul(m,n):
    if n==0:
        return 0
    smop = mul(m,n-1)
    return m+smop

# print(mul(3,15))
# -------------------------------------------------------------------------------
# 5. Assignment - Count zeros
def countZero(n):
    if n==0:
        return 0
    smop  = countZero(n//10)
    if n%10==0:
        return 1 + smop
    return smop
# print(countZero(10010))
# -------------------------------------------------------------------------------
# 6. Assignment - String to integer
def str_int(a):
    if len(a)==1:
        return ord(a[0])-ord('0')
    y = str_int(a[1:])
    x= ord(a[0])-ord('0')
    x=x*(10**(len(a)-1))+y
    return x
# print(str_int('1252'))
# -------------------------------------------------------------------------------
# 7. Assignment - Pairs by star
def starPair(str):
    if len(str) == 0 or len(str)==1:
        return str
    smallop = starPair(str[1:])
    if str[0] == str[1]:
        return  str[0]+'*'+ smallop
    else:
        return str[0] + smallop

# print(starPair('hello'))
# -------------------------------------------------------------------------------
# 7. Assignment - check AB

def checkStr(a):
    if len(a)==0:
        return True
    if a[0]=='a':
        if a[1]=='a' or a[1]=='b':
            return checkStr(a[2:])
        if a[1]==None:
            return True
        else:
            return False
    elif a[0]=='b':
        if a[1]=='b' and a[2]==None:
            return checkStr(a[2:])
        elif a[1]=='b' and a[2]=='a':
            return True
        else:
            return False


# a =input()
# if a[0]=='a':
#     if checkStr(a[1:]):
#         print('true')
#     else:
#         print('false')
# else:
#     print('false')
# -------------------------------------------------------------------------------
# 7. Assignment - Stair-case
def staircase(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    if n ==3:
        return 4
    smop = staircase(n-1)
    smop2 = staircase(n-2)
    smop3 = staircase(n-3)
    return smop+smop2+smop3

print(staircase(4))

