a, b, c = map(float, input().split())

triangulo = (a * c)/2
circulo = 3.14159 * (c * c)
trap = (a + b) * (c/2)
quad = b * b
ret = a * b

print('TRIANGULO: ', f"{triangulo: .3f}")
print('CIRCULO: ', f"{circulo: .3f}")
print('TRAPEZIO: ', f"{trap: .3f}")
print('QUADRADO: ', f"{quad: .3f}")
print('RETANGULO: ', f"{ret: .3f}")