class MergeSort:
    def mergeSort(self,arr1,arr2):
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


    def MidMergeSort(self,arr):
        #Base case
        if len(arr) == 1:
            return arr
        mid = len(arr)//2
        arr1 = arr[:mid]
        arr2 = arr[mid:]

        #Recursive
        arr1 = self.MidMergeSort(arr1)
        arr2 = self.MidMergeSort(arr2)

        return self.mergeSort(arr1,arr2)

s = MergeSort()
a = [0,10,2,5,3,1,0]
print(s.MidMergeSort(a))