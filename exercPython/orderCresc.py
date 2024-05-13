num1 = input('Digite um valor para A: ')
num2 = input('Digite um valor para B: ')
num3 = input('Digite um valor para C: ')

if num1 > num2 > num3:
    print(num3, num2, num1)
elif num1 > num3 > num2:
    print(num2, num3, num1)
elif num2 > num1 > num3:
    print(num3, num1, num2)
elif num2 > num3 > num1:
    print(num1, num3, num2)
elif num3 > num2 > num1:
    print(num1, num2, num3)
elif num3 > num1 > num2:
    print(num2, num1, num3)