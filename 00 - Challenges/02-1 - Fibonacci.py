
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    fibArray = [0, 1]
    for i in range(2, n+1):
        putThis = fibArray[i-2] + fibArray[i-1]
        fibArray.append(putThis)
    return fibArray[len(fibArray)-1]

if __name__ == "__main__":
     howMany = input()
     howMany = int(howMany)
     print(int(fib(howMany)))