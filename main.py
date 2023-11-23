import random
numero_atual = random.randint(1, 100)
print(f"o numero atual é {numero_atual}.")
proximo_numero = random.randint(1, 100)
escolha = input("o proximo numero sera maior ou menor?")
print(f"o proximo numero e {proximo_numero}.")
if escolha == "maior" and proximo_numero > numero_atual:
  print('voce acertou!')
elif escolha == "menor" and proximo_numero < numero_atual:
    print('voce acertou!')
if escolha != "menor" and proximo_numero < numero_atual:
  print('voce errou!')
elif escolha != "maior" and proximo_numero > numero_atual:
    print('voce errou')