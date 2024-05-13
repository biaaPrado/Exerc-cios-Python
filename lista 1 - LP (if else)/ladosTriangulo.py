a = int(input('Digite o lado A: '))
b = int(input('Digite o lado B: '))
c = int(input('Digite o lado C: '))

if ((b-c) < a < b + c and
   (a-c) < b < a + c and
   (a-b) < c < a + b):
    print(a, b, c,': podem formar um triângulo')
else:
    print(a, b, c, ': não podem formar um triângulo')