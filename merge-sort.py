#merge sort algorithm is an O(n*log(n)) alg.
def merge_sort(arr,p,r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)

def merge(arr,p,q,r):
    n1 = q - p + 1
    n2 = r - q

    left_arr = [0] * (n1)
    right_arr = [0] * (n2)

    for i in range(0, n1):
        left_arr[i] = arr[p + i]
    for j in range(0, n2):
        right_arr[j] = arr[q + j + 1]
        
    i = 0
    j = 0
    k = p

    while i < n1 and j< n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i+=1
        else: 
            arr[k] = right_arr[j]
            j+=1
        k+=1
        
    while i < n1:
        arr[k] = left_arr[i]
        i+=1
        k+=1

    while j < n2:
        arr[k] = right_arr[j]
        j+=1
        k+=1

#generate a random list
arr = []
for i in range(10):
    import random
    arr.append(random.randint(0,99))

#print this list before sorting.
print(f'before: {arr}')

#print this list after sorting.
merge_sort(arr, 0, len(arr)-1)
print(f'after: {arr}')
