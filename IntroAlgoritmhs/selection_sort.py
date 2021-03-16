# Choose between arrays and linked lists:
# If you have a few reads and a lot of inserts preffer Linked Lists
# If you have a few inserts and a lot of reads preffer arrays (Be able to explain why)

# Arrays are more used cuz they offer random access (index_at(77)) lists only one by one
    # sequential access

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))