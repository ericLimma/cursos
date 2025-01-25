n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
s = n1 + n2
m = n1 - n2
v = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
p = n1 ** n2


print('A soma entre os números é: {};\n'
      'A subtraçãob entre os números é: {};\n'
      'A multiplicação entre os números é: {};\n'
      'A divisão entre os números é: {};\n'
      'A divisão inteira entre os números é: {};\n'
      'O resto da divisão entre os números é {};\n'
      'A potência é: {}.' .format(s, m, v, d, di, r, p))
