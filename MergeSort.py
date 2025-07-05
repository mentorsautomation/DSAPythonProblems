def mergeSort(arr1,arr2):
    i = 0
    j = 0
    output = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            output.append(arr1[i])
            i+=1
        else:
            output.append(arr2[j])
            j+=1
    while i<len(arr1):
        output.append(arr1[i])
        i+=1
    while j<len(arr2):
        output.append(arr2[j])
        j+=1

    return output


arr1 = [0,0,1,2,7,9]
arr2 = [2,4,6,10]
print(mergeSort(arr1,arr2))
