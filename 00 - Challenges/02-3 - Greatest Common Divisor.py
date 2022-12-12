


if __name__ == "__main__":
    div = -1
    nos = input()
    nos = nos.split(" ")
    if int(nos[0]) <  int(nos[1]):
        noArray = [int(nos[0]),  int(nos[1])]
    else:
        noArray = [int(nos[1]),  int(nos[0])]

    top = int(nos[1])
    bottom = int(nos[0])

    arr = []
    while True:
        oldB = bottom
        arr.append(bottom)
        if bottom == 0: break
        bottom = top % bottom
        top = oldB
        
    print(arr[len(arr)-2])