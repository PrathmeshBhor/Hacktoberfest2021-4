def swapList(newList):
    size = len(newList)
     
    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    print("some new changes has been proposed")
    print("some new changes has been proposed")
    print("some new changes has been proposed")
    print("some new changes has been proposed")
    print("this is me the sachin chaudhary")
    print("result: ")
    return newList
     
# Driver code
newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))
