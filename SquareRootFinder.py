
#   I wrote this code to help me with math homework
#   because my calculator gave decimals when I needed
#   simplified square roots. It is a combination/modification
#   of two other programs I had previously written as experiments:
#   a quadratic formula calculator and a prime number checker.




while True:
    num = int(input("Enter an integer to take the square root of: "))
    coef = 1
    while True:
        if num < 0:
            print("Domain Error")
            break
        if num > 3:
            end = num
            n = int(4)
            while True:       
                fac = int(2)
                while True:
                    if n > fac and n%fac != 0:
                        fac += 1
                        continue
                    if n%fac == 0 and n != fac:
                        break
                    elif fac == n:
                        if (num >= (n**2)) and (num%(n**2) == 0):
                            num = num/(n**2)
                            coef = coef*n
                        break
                if n < end:
                    n += 1
                    continue
                elif n == end:
                    break
        if num >= 4 and (num%4) == 0:
            num = num/4
            coef = coef*2
            continue
        if num >= 9 and (num%9) == 0:
            num = num/9
            coef = coef*3
            continue       
        else:
            coeff = str(int(coef))
            root = str(int(num))
            if (num == 1) or (num == 0):
                print(coeff)
            elif (coef > 1) and (num > 1):
                print(coeff + " root " + root)
            if (num != 1) or (coef == 1):
                print(coef*num**0.5)
            elif (coef == 1):
                print(num**0.5)
        break
                   
         
