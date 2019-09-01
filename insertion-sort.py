#insertion sort algorithm is an O(n^2) alg.
def selection_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        
        arr[j+1] = key

#generate a random list
arr = []
for i in range(10):
    import random
    arr.append(random.randint(0,99))

#print this list before sorting.
print(f'before: {arr}')

#print this list after sorting.
selection_sort(arr)
print(f'after: {arr}')
