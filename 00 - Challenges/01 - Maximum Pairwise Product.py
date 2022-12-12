
howMany = input()
numbers = input()
numStrArray = numbers.split(" ")
nums = []

def getMax():
    global nums
    arraySize = int(howMany)
    biggest = [-1, 0]
    for i in range(0, arraySize):
        if nums[i] > biggest[0]:
            biggest = [nums[i], i]
    nums[biggest[1]] = -1
    return biggest[0]


if __name__ == "__main__":
    for i in numStrArray:
        nums.append(int(i))
    noOne = getMax()
    noTwo = getMax()
    # print(noOne)
    # print(noTwo)
    timesed = noOne * noTwo
    print(str(timesed))
