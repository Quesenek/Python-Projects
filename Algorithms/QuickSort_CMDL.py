def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        
        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)

        print("Arr: %s,     low: %s,      pi-1: %s,      pi+1: %s,        high: %s" % (arr, low, pi-1, pi+1, high))

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

arr = [10, 7, 8, 9, 1, 5, 2, 6, 3, 4]
n = len(arr)
quickSort(arr, 0, n-1)

print("Sorted Array is:")

for i in range(n):
    print("%d" % arr[i])