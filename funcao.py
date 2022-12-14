def soma(inicio, fim):
  lista_par = []
  valor1 = int(inicio)
  valor2 = int(fim+1)

  for indice in range(valor1, valor2):
    if indice%2==0:
      lista_par.append(indice)
  print(f'Números pares: {lista_par}')
  somar = sum(lista_par)
  print(f'Soma do intervalor: {somar}')
  return somar
  
def subtracao(numero1, numero2):
  valor3 = int(numero1)
  valor4 = int(numero2)

  if valor3 > valor4:
    subtrair = valor3 - valor4
    print(f'Diferença: {subtrair}')
  else:
    subtrair = valor4 - valor3
    print(f'Diferença: {subtrair}')
    return subtrair

while True:
  primeiro = int(input('Digite o primeiro número: '))
  segundo = int(input('Digite o segundo número: '))

  realizar_soma = soma(primeiro, segundo)
  realizar_subtracao = subtracao(primeiro, segundo)

  saida = input('Deseja continuar [S/n]? ')
  if saida == 'N':
    break