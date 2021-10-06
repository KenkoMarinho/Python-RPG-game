import os
import random
# . espaço vazio, o robo, # pilastra

#funcoes
def cls():
  os.system('clear')

def MostrarTabuleiro(tabuleiro):
  print("O===============================O")
  for i in range (len(tabuleiro)):
    print("I",tabuleiro[i][0],tabuleiro[i][1],tabuleiro[i][2],tabuleiro[i][3],tabuleiro[i][4],tabuleiro[i][5],tabuleiro[i][6],tabuleiro[i][7],tabuleiro[i][8],tabuleiro[i][9],tabuleiro[i][10],tabuleiro[i][11],tabuleiro[i][12],tabuleiro[i][13],tabuleiro[i][14],"I")
  print("O===============================O")
def LocalizarRobo(tabuleiro):
  for i in range(len(tabuleiro)):
    if "o" in tabuleiro[i]:
      linha_robo=int(i)
    for x in range(len(tabuleiro[1])):
      if "o" in tabuleiro[i][x]:
        numero_elemento_robo=int(x)
  #print(f"O Robô é o elemento numero {numero_elemento_robo} da linha {linha_robo}")
  return linha_robo,numero_elemento_robo

def MoverNorte(tabuleiro):
  indice1robo,indice2robo=LocalizarRobo(tabuleiro)
  if indice1robo>=1:
    if not tabuleiro[indice1robo-1][indice2robo]=="#":
      tabuleiro[indice1robo][indice2robo]=","
      tabuleiro[indice1robo-1][indice2robo]="o"

def MoverSul(tabuleiro):
  indice1robo,indice2robo=LocalizarRobo(tabuleiro)
  if indice1robo<10:
    if not tabuleiro[indice1robo+1][indice2robo]=="#":
      tabuleiro[indice1robo][indice2robo]=","
      tabuleiro[indice1robo+1][indice2robo]="o"

def MoverLeste(tabuleiro):
  indice1robo,indice2robo=LocalizarRobo(tabuleiro)
  if indice2robo<14:
    if not tabuleiro[indice1robo][indice2robo+1]=="#":
      tabuleiro[indice1robo][indice2robo]=","
      tabuleiro[indice1robo][indice2robo+1]="o"

def MoverOeste(tabuleiro):
  indice1robo,indice2robo=LocalizarRobo(tabuleiro)
  if indice2robo>=1:
    if not tabuleiro[indice1robo][indice2robo-1]=="#":
      tabuleiro[indice1robo][indice2robo]=","
      tabuleiro[indice1robo][indice2robo-1]="o"

def Controlador(tabuleiro,x=0):
  if x==0:
    Teclado=input("Digite N para Norte, S para Sul, L para Leste e O para Oeste.")
    while Teclado!="N" and Teclado!="S" and Teclado!="L" and Teclado!="O":
      Teclado=input("Digite N para Norte, S para Sul, L para Leste e O para Oeste.")
  else:
    Teclado=x
    Teclado=Teclado.upper()
  if Teclado=="N":
    MoverNorte(tabuleiro)
  if Teclado=="S":
    MoverSul(tabuleiro)
  if Teclado=="L":
    MoverLeste(tabuleiro)
  if Teclado=="O":
    MoverOeste(tabuleiro)
  
  
def InputAutomatico(tabuleiro):#bagunça e gambiarra, boa sorte pra entender essa merda aí.
  comandos2=""
  comandos=input("Insira os comandos: Ex:W/A/S/D")
  while len(comandos)!=1 and not(("W" in comandos)or("A" in comandos)or("S" in comandos)or("D" in comandos)):
    comandos=input("Insira os comandos: Ex:W/A/S/D")
  for i in range (len(comandos)):
    if comandos[i]=="w" or comandos[i]=="W":
      comandos2+="N"
    if comandos[i]=="a" or comandos[i]=="A":
      comandos2+="O"
    if comandos[i]=="s" or comandos[i]=="S":
      comandos2+=""
    if comandos[i]=="d" or comandos[i]=="D":
      comandos2+="L"
  comandos+=comandos2
  cls()
  if len(comandos)>5:
    comandos=comandos[0:4]
  for i in comandos:
    Controlador(tabuleiro,i)

def GerarObstaculos(tabuleiro):
  for i in range (len(tabuleiro)):
    randomizar=random.randint(1,8)
    if randomizar==2:
      tabuleiro[i][0],tabuleiro[i][2],tabuleiro[i][3],tabuleiro[i][4],tabuleiro[i][6],tabuleiro[i][7],tabuleiro[i][8],tabuleiro[i][9],tabuleiro[i][14]="#","#","#","#","#","#","#","#","#"
    if randomizar==3:
      tabuleiro[i][5],tabuleiro[i][6],tabuleiro[i][10],tabuleiro[i][14]="#","#","#","#"
    if randomizar==4:
      tabuleiro[i][2],tabuleiro[i][7],tabuleiro[i][8],tabuleiro[i][10],tabuleiro[i][13]="#","#","#","#","#"
    if randomizar==5:
      tabuleiro[i][1],tabuleiro[i][2],tabuleiro[i][6],tabuleiro[i][8],tabuleiro[i][9]="#","#","#","#","#"
    if randomizar==6:
      tabuleiro[i][4],tabuleiro[i][8],tabuleiro[i][13]="#","#","#"
    if randomizar==7:
      tabuleiro[i][2],tabuleiro[i][3],tabuleiro[i][4],tabuleiro[i][10],tabuleiro[i][11]="#","#","#","#","#"
    if randomizar==8:
      tabuleiro[i][0],tabuleiro[i][1],tabuleiro[i][2],tabuleiro[i][3],tabuleiro[i][4],tabuleiro[i][5],tabuleiro[i][6],tabuleiro[i][7],tabuleiro[i][9],tabuleiro[i][10],tabuleiro[i][13],tabuleiro[i][14]="#","#","#","#","#","#","#","#","#","#","#","#"
  return tabuleiro

def EntrarNaDungeon(tabuleiro):
  tabuleiro[random.randint(0,10)][random.randint(0,14)]="o"
  return tabuleiro

def main():
  tabuleiro=[
  [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]]
  tabuleiro=GerarObstaculos(tabuleiro)
  tabuleiro=EntrarNaDungeon(tabuleiro)
  while True:
    MostrarTabuleiro(tabuleiro)
    InputAutomatico(tabuleiro)
main()