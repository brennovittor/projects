n = int(input('Digite um número: '))

print("=-"*15)
print(f"TABUADA DO {n}")
print("=-"*15)
for i in range(1, 11):
  print(f' {n} X {i} = {n * i}')
