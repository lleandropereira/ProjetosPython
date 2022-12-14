lista_nome=[]
lista_idade=[]
#lista_final=[]
valores=[]

for i_time in range(16):
  print(f'Time {i_time+1}')
  for i_jogador in range(23):
    nome = input('Nome do jogador: ')
    idade = int(input('Idade: '))
    lista_nome.append(nome)
    lista_idade.append(idade)
    
  if i_time == 0:
    soma_primeiro_time=sum(lista_idade)
  if i_time == 5:
    soma_quarto_time=sum(lista_idade)

media_primeiro_time=soma_primeiro_time/23
media_quarto_time=soma_quarto_time/23

#caso seja necessário armazenar os dados em apenas uma ÚNICA lista
#lista_final.append(lista_nome)
#lista_final.append(lista_idade)

print(f'A idade média dos jogadores do 1° time é: {media_primeiro_time}')
print(f'A idade média dos jogadores do 2° time é: {media_quarto_time}')