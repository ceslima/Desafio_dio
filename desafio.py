def classificar_heroi(nome, xp):
  """Classifica o nível de um herói com base na sua experiência.
  """
  if xp < 1000:
    nivel = "Ferro"
  elif xp <= 2000:
    nivel = "Bronze"
  elif xp <= 5000:
    nivel = "Prata"
  elif xp <= 7000:
    nivel = "Ouro"
  elif xp <= 8000:
    nivel = "Platina"
  elif xp <= 9000:
    nivel = "Ascendente"
  elif xp <= 10000:
    nivel = "Imortal"
  else:
    nivel = "Radiante"

  return f"O Herói de nome {nome} está no nível de {nivel}"


# Exemplo de uso
nome_heroi = input("Digite o nome do herói: ")
xp_heroi = int(input("Digite a quantidade de XP do herói: "))

mensagem = classificar_heroi(nome_heroi, xp_heroi)
print(mensagem)