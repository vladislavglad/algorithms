#merge sort algorithm is an O(n*log(n)) alg.
def merge_sort(arr,p,r):
    if p < r:
        q = abs((p + (r)) / 2)
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)

def merge(arr,p,q,r):
    n1 = q - p + 1
    n2 = r - q

    left_arr = []
    right_arr = []

    for i in range(n1):
        left_arr.append(arr[p + i - 1])
    for j in range(n2):
        right_arr.append(arr[q + j])

    #sentinel values.
    left_arr[n1+1] = 100
    right_arr[n2+1] = 100

    i = 0
    j = 0
    k = p

    while k < r:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i+=1
            k+=1
        else: 
            arr = right_arr[j]
            j+=1
            k+=1   