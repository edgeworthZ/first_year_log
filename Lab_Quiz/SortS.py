def SelectionSort(ls=[5,8,6,11,3,2,1,1,5]):
    for i in range(len(ls)):
        minP = i
        for j in range(i,len(ls)):
            if ls[j] < ls[minP]:
                minP = j
        ls[i],ls[minP] = ls[minP], ls[i]
    return ls
print(SelectionSort())
        
