# This program checks an input and tells you if it is a prime number


while True:

    num = int(input("Enter a number:"))
    if num < 0:
          print("Error")         
    i = 2

    while True:
    
        if num > i and num%i != 0:
              i += 1
              continue
        
        if num%i == 0 and num != i:
              print("Not a prime number")
              break
        
        elif i == num:
              print("Prime")
              break
