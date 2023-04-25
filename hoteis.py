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
      valor.append(float(partes[2][0:-1]))    



def salva_dados():
  with open("hoteis.csv", "w") as arq:
    
  
    for (hoteis, notas, valores) in zip(hotel, nota, valor):
      arq.write(f"{hoteis};{notas};{valores}\n")



def titulo(texto, sublinhado="-"):
  print()
  print(texto)
  print(sublinhado*40)