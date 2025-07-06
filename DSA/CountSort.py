def count_sort(arr):
    if not arr:
        return []
    fm = [0] * (max(arr)+1)
    output=[]
    for ele in arr:
        fm[ele] += 1
    for digit in range(1,len(fm)):
        output.extend([digit]*fm[digit])
    return output

arr = [0,8,9,1,3,0,5,1]
print(count_sort(arr))
