cod1, num1, valor1 = map(float, input().split())
cod2, num2, valor2 = map(float, input().split())

valortotal1 = num1 * valor1
valortotal2 = num2 * valor2
valorfinal = valortotal1 + valortotal2

print('VALOR A PAGAR: R$', f"{valorfinal: .2f}")