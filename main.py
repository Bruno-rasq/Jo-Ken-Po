from time import sleep
from random import randint
from tabulate import tabulate
import os


opcoes = ['pedra', 'papel', 'tesoura']

#pontos
jogador = 0
computador = 0
partidas = []


def escolha_jogador():
  jogador = int(input(f"""
  [0] - Pedra
  [1] - Papel
  [2] - Tesoura
  """))
  return opcoes[jogador]


def escolha_maquina():
  computador = randint(0, 2)
  return opcoes[computador]


def vencedor_partida(jogador, maquina):
  if jogador == maquina:
        return "empate"
  elif (jogador == "pedra" and maquina == "tesoura") or \
         (jogador == "papel" and maquina == "pedra") or \
         (jogador == "tesoura" and maquina == "papel"):
        return "jogador"
  else:
        return "maquina"
    

def jokenpo():
  print("JO")
  sleep(1)
  print("KEN")
  sleep(1)
  print("PÔ!")
  sleep(1)


def clear():
  os.system('clear')


def exibir_tabela(jogadas):
    print(tabulate(jogadas, headers=["Jogador", "Máquina", "Vencedor"], tablefmt="grid"))


def partida():
  player = escolha_jogador()
  maquina = escolha_maquina()
  vencedor = vencedor_partida(player, maquina)
  
  clear()
  jokenpo()
  partidas.append([player, maquina, vencedor])
  exibir_tabela(partidas)
  
  return vencedor
  

def pontuacao(vencedor):
  global jogador
  global computador

  if vencedor == "jogador":
      jogador += 1
  elif vencedor == "maquina":
      computador += 1
  else:
      pass


def fim_de_jogo(jogador, maquina):
  if jogador == 3 or maquina == 3:
    return True
  return False


def game():
  global jogador
  global computador
  fim = False
  
  while not fim:
    vencedor = partida()
    pontuacao(vencedor)
    fim = fim_de_jogo(jogador, computador)
  

game()