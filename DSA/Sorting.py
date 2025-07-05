def countSort(arr):
    global ele
    fm = [0]*10
    for ele in arr:
        fm[ele] += 1
    output = []
    for digit in range(10):
        count = fm[digit]
        output.extend([digit]*count)
    return output

a = [9,0,2,1,2,3,5,3,1,7,1]
print(countSort(a))