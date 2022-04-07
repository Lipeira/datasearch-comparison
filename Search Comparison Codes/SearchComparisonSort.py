import matplotlib.pyplot as plt


# Linear Function - the list don't need to be sorted

def LinearSearch(number,list):
    complexity = 0
    for i in list:
        complexity += 1
        if i == number:
            return complexity

# BinarySearchFunction - works if list is sorted      

def BinarySearch(number,list):
    complexity = 0
    init = 0
    end = len(list) - 1
    while init <= end:
        complexity += 1
        mid = (init + end)//2
        if number > mid:
            init = mid + 1
        elif number < mid:
            end = mid -1
        else:
            return complexity
    return complexity

# Quicksort Functions to include in complexity comparison

def quicksort(lista,N,complexity = 0):
    complexity = qs(lista,0,N-1,complexity)
    return complexity

def qs(lista,esq,dir,complexity):
    complexity += 1
    if esq >= dir:
        return complexity
    complexity,p = particao(lista,esq,dir,complexity)
    
    complexity = qs(lista,esq,p-1,complexity)
    complexity = qs(lista,p+1,dir,complexity)    
    return complexity

def particao(lista,esq,dir,complexity):
    complexity += 1
    pivo = lista[esq]
    i = esq
    j = dir + 1
    while True:
        i += 1
        while lista[i] < pivo: 
            if i >= dir:
                break
            i += 1
        j -= 1
        while lista[j] > pivo:  #lista[j] < pivo
            if j <= esq:
                break
            j -= 1
        if i >= j:
            break
        trocar(lista,i,j)
    trocar(lista,esq,j)
    return complexity,j
        
def trocar(unsortedlist,i,min):    
    temp = unsortedlist[i]
    unsortedlist[i] = unsortedlist[min]
    unsortedlist[min] = temp


def main():

    #Applying these functions above to an unsorted list , searching for the last element

    # X-axis and Y-axis 

    Xline = []
    YLinearS = []
    YBinaryS = []

    #Making some test lists and applying functions , storing the result of complexity in Y-axis and len(teslist) in X-axis

    for N in range(1,201):
        Counter = 0
        TestList = []

        for i in range(N,-1,-1):
            TestList.append(i)
        
        #This is a random number that is taken 
        number = TestList[-1]

            
        Complexity = LinearSearch(number , TestList)
        YLinearS.append(Complexity)


    #The list needs to be sorted here , because binary search requires a sorted list to work
        complexitysort = quicksort(TestList,len(TestList))
        Complexity2 = BinarySearch(number, TestList)
        YBinaryS.append(Complexity2 + complexitysort)


    print(YLinearS)
    print(YBinaryS)


    plt.plot(range(1,201),YLinearS,label="LinearSearch_NoSort")
    plt.plot(range(1,201),YBinaryS,label="BinarySearch_WithSort")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

    
#So , in the case that the list is unsorted , it's better to use Linear search than binary search