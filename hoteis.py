import os
hotel = []
nota = []
valor = []


def carregar_dados():
  if not os.path.isfile("hoteis.csv"):
    return
  
  with open("hoteis.csv", "r") as arq:
    linhas = arq.readlines()

    for linha in linhas:
      partes = linha.split(";")
      hotel.append(partes[0])
      nota.append(int(partes[1]))
      valor.append(int(partes[2]))    



def salva_dados():
  with open("hoteis.csv", "w") as arq:
    
  
    for (hoteis, notas, valores) in zip(hotel, nota, valor):
      arq.write(f"{hoteis};{notas};{valores}\n")



def titulo(texto, sublinhado="-"):
  print()
  print(texto)
  print(sublinhado*40)




def cadastrar():
  titulo("Incluir hotel")
  hoteis = input("Nome do Hotel: ") 
  notas = int(input("nota(1-5): "))
  valores = int(input("Valor diaria em R$: "))

  hotel.append(hoteis)
  nota.append(notas)
  valor.append(valores)  
  print("Hotel Cadastrado.")
  



def listar():
  titulo("Lista de Hoteis Cadastrados")
  print("Nº Nome do Hotel........  1Nota Valor.....")
  for x, (hoteis, notas, valores) in enumerate(zip(hotel, nota, valor), start=1):
    print(f"{x:2} {hoteis:20}  {notas:3}  {valores}")
  



def pesquisar():
  titulo("Pesquisa por Nota(☆)")

  pesq = int(input("☆: "))

  print("Nº Nome do Hotel........ Nota  Valor.....")
  
  for x, (hoteis,notas, valores) in enumerate(zip(hotel, nota, valor), start=1):
    if pesq == notas:
      print(f"{x:2} {hoteis:20}  {notas:3}  {valores}")



def deletar():
  listar() 

  titulo("Exclusão de Hoteis")
  num = int(input("Nº do Hotel a Deletar: "))

  if num <= 0 or num > len(hotel):
    print("Número inválido")
    return
  
  hotel.pop(num-1)
  nota.pop(num-1)
  valor.pop(num-1)
  print("Exclusão realizada com sucesso!")
  



def totalizar():
  titulo("Total de  ☆")

  num = len(hotel)

  soma = sum(nota)


  print(f"Nº Hotéis Cadastrados: {num}")


  print(f"Total  ☆: {soma:9}")



def descontar():
  titulo("Aplicação de Descontos")

  num = int(input("Quantos '%' de desconto deseja aplicar?"))

  desc = num /100

  for c in range(len(valor)):
    valor[c] = valor[c] - (valor[c] * desc)

  listar()



carregar_dados()

while True:
  titulo("Cadastro de instrumentos musicais", "=")
  print("1. Incluir hotel")
  print("2. Listar hotéis")
  print("3. Pesquisar por nota(☆) dos hotéis (1-5)")
  print("4. Excluir hotel")
  print("5. Pesquisa com totalização")
  print("6. Conceder Desconto (%)")
  print("7. Finalizar")
  opcao = int(input("Opção: "))  
  if opcao == 1:
    cadastrar()
  elif opcao == 2:
    listar()
  elif opcao == 3:
    pesquisar()
  elif opcao == 4:
    deletar()
  elif opcao == 5:
    totalizar()
  elif opcao == 6 :
    descontar()
  else:
   
    salva_dados()
    break