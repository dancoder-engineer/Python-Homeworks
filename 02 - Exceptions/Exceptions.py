from bs4 import BeautifulSoup

def part1():
  for i in ['a', 2,'c']:
    try:
      print(i**2)
    except TypeError:
      print("Input not an int.")

def part2():
    try:
      x = 5  
      y = 0
      z = x/y
    except ZeroDivisionError:
      print("Can't divide by 0. Now the universe is gonna explode, and it's all your fault!")

def part3():
    while True:
      try:
          base = input("Please input the number to square: ")
          base = int(base)
      except ValueError:
          print("Please input a number!")
      else:
        print("The square of your number is " + str(base ** 2))
        break
      
#part3()
