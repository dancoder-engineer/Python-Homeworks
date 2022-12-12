def gcd(nos):
    top = int(nos[1])
    bottom = int(nos[0])

    arr = []
    while True:
        oldB = bottom
        arr.append(bottom)
        if bottom == 0: break
        bottom = top % bottom
        top = oldB
        
    return(arr[len(arr)-2])

def abs(num):
    if num < 0: return num * -1
    else: return num

def inputNum():
    arr = []
    inputted = input()
    inputted = inputted.split(" ")
    for i in inputted:
        arr.append(int(i))
    return arr

if __name__ == "__main__":
    nos = inputNum()
    answer = (abs(nos[0] * nos[1]))/gcd(nos)
    answer = int(answer)
    print(str(answer))