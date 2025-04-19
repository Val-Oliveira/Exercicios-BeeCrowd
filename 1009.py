nome = input()
salario = float(input())
vendas = float(input())

bonus = (vendas * 0.15)
valorfinal = bonus + salario
print('TOTAL = R$', f"{valorfinal: .2f}")