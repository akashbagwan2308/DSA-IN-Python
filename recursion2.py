def replace(str,a,b):
    if len(str)==0 :
        return str
    smallop = replace(str[1:],a,b)
    if str[0]==a:
        return b+smallop
    else:
        return str[0]+smallop

#-------------------------------------

def replacePi(str):
    if len(str)==0 or len(str)==1:
        return str
    if str[0]=='p' and str[1]=='i':
        smop = replacePi(str[2:])
        return '3.14'+smop
    else:
        smop = replacePi(str[1:])
        return str[0]+smop
#------------------------------------
def binarySearch(a,x,si,ei):
    if si>ei:
        return -1
    mid = (si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]>x:
        return binarySearch(a,x,si,mid-1)
    else:
        return binarySearch(a,x,mid+1,ei)
#------------------------------------
# merge sort
def merge(a1,a2,a):
    i= 0
    j=0
    k= 0
    while i<len(a1) and j< len(a2):
        if a1[i]<a2[j]:
            a[k]=a1[i]
            k+=1
            i+=1
        else:
            a[k]=a2[j]
            k+=1
            j+=1
    while i<len(a1):
        a[k] = a1[i]
        k += 1
        i += 1
    while j<len(a2):
        a[k] = a2[j]
        k += 1
        j += 1
    return a
def mergesort(a):
    if len(a)==0 or len(a)==1:
        return
    mid = len(a)//2
    a1 = a[:mid]
    a2 = a[mid:]
    mergesort(a1)
    mergesort(a2)
    return merge(a1,a2,a)
#---------------------------------------
# quick sort

def partition(a,si,ei):
    pivot = a[si]
    # find no of element smaller then pivot
    c = 0
    for i in range(si, ei + 1):
        if a[i] < pivot:
            c += 1
    a[si+c],a[si]=a[si],a[si+c]
    pivotIndex = si+c
    i = si
    j = ei
    while i<j:
        if a[i]<pivot:
            i+=1
        elif a[j]>=pivot:
            j-=1
        else:
            a[i],a[j]=a[j],a[i]
    return pivotIndex
def quickSort(a,si,ei):
    if si>=ei:
        return
    pivotIndex = partition(a,si,ei)
    quickSort(a,si,pivotIndex-1)
    quickSort(a,pivotIndex+1,ei)
    return a
#------------------------------------------------

def tower(n,a,b,c):
    if n==1:
        print('move 1st dick from ', a,'to', c)
        return
    tower(n-1,a,c,b)
    print(f'move {n}th disk from {a} to {c}')
    tower(n-1,b,a,c)


if __name__ == '__main__':
    # print(replace('dxacbcsaasx','x','b'))
    # print(replacePi('pipipispispi'))
    # print(binarySearch([1,3,5,7,9,11,13,15,16,17],15,0,9))
    # print(mergesort([15,1,8,9,7,61,4,6,3,7,5]))
    # a=[15,1,8,9,7,61,4,6,3,7,5]
    # print(quickSort(a,0,len(a)-1))
    tower(2,'s','h','d')