# Time Complexity
import time
def merge(a1,a2,a): 
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i]<a2[j]:
            a[k]=a1[i]
            k +=1
            i +=1
        else:
            a[k]=a2[j]
            k +=1
            j +=1
    while i< len(a1):
        a[k]= a1[i]
        k +=1
        i +=1
    while j<len(a2):
        a[k]=a2[j]
        k +=1
        j +=1

def  mergsort(a):
    if  len(a)==0 or len(a)==1:
        return
    mid = len(a)//2
    a1 = a[0:mid]
    a2 = a[mid:]

    mergsort(a1)
    mergsort(a2)
    merge(a1,a2,a)

def selectionSort(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1,len(a)):
            if a[min_idx]>a[j]:
                min_idx = j
        a[i],a[min_idx]= a[min_idx],a[i]

def create_rev_array(n):
    a = []
    for i in range(n,0,-1):
        a.append(i)
    return a

n = 10000
a = create_rev_array(n)
# timer start
start = time.time()
mergsort(a)
# timer stop
end = time.time()
print(a)
print(n,end-start)

n = 10000
a = create_rev_array(n)
# timer start
start = time.time()
selectionSort(a)
# timer stop
end = time.time()
print(a)
print(n,end-start)