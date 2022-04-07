import matplotlib.pyplot as plt


# Linear Function

def LinearSearch(number,list):
    complexity = 0
    for i in list:
        complexity += 1
        if i == number:
            return complexity

# BinarySearchFunction   

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

def main():

    #Applying these functions above to a sorted list , searching for the last element

    # X-axis and Y-axis 

    Xline = []
    YLinearS = []
    YBinaryS = []

    #Making some test lists and applying functions , storing the result of complexity in Y-axis and len(teslist) in X-axis

    for N in range(1,201):
        Counter = 0
        TestList = []

        for i in range(0,N+1):
            TestList.append(i)
        
        #This is a random number that is taken 
        number = TestList[-1]

            
        Complexity = LinearSearch(number , TestList)
        YLinearS.append(Complexity)

        Complexity2 = BinarySearch(number, TestList)
        YBinaryS.append(Complexity2)


    print(YLinearS)
    print(YBinaryS)


    plt.plot(range(1,201),YLinearS,label="LinearSearch_NoSort")
    plt.plot(range(1,201),YBinaryS,label="BinarySearch_NoSort")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

    
#So , in the case that the list is sorted , it's better to use Binary Search than Linear Search
 
