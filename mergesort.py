def mergeSort(list):
    size = len(list)
    if size <= 1:
        return
    middle = size / 2
    left = []
    right = []
    for i in range(size):
        if i < middle:
            left.append(list[i])
        else:
            right.append(list[i])
    print(left, right)

    mergeSort(left)
    mergeSort(right)
    merge(list, left, right)
    
def merge(list, left, right):
    leftSize = len(list) / 2
    rightSize = len(list) - leftSize
    i = 0
    l = 0
    r = 0
    while l < leftSize and r < rightSize:
        if left[l] < right[r]:
            list[i] = left[l]
            i+=1
            l+=1
        else:
            list[i] = right[r]
            i+=1
            r+=1
    while r < rightSize:
        list[i] = right[r]
        i+=1
        r+=1
    while l < leftSize:
        list[i] = left[l]
        i+=1
        l+=1
list = [8, 1, 7, 6, 5, 4, 3, 2]
mergeSort(list)
#print(list)

