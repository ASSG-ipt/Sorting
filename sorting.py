import random

def swap(alist, leftIndex, rightIndex):
    temp = alist[leftIndex]
    alist[leftIndex] = alist[rightIndex]
    alist[rightIndex] = temp
    return alist

def makeList(length):
    answer = []
    for i in range (length):
        answer.append(random.randint(0,length)
    return answer

    
