import os
import random
from funcoesrpg import *
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

def GerarObstaculosNaturais(tabuleiro):
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

def ConferirEvento(tabuleiro,player):
    randomizar=random.randint(2,5) #vai ter um evento?
    if randomizar==1 or randomizar==2:
        randomizar=random.randint(1,20) #tipo de evento
        if randomizar==1:                           #evento de mercador
            EventoMercador(player)
        elif randomizar>=2 and randomizar<=16:      #evento de combate
            EventoCombate(player)
        elif randomizar>=17 and randomizar<=18:     #evento de viajante
            EventoViajante(player)
        elif randomizar==19:                        #evento de descanso
            EventoDescanso(player)
        elif randomizar==20:                        #evento de tesouro
            EventoTesouro(player)

def EventoMercador(player):            
    randomizar=random.randint(1,20)
    if randomizar>=1 and randomizar<=7:
        Comercio(player,"Padrão")
    elif randomizar>=8 and randomizar<=12:
        Comercio(player,"Mercador Aventureiro")
    elif randomizar>=13 and randomizar<=16:
        Comercio(player,"Mercador Mago")
    elif randomizar>=17 and randomizar<=19:
        Comercio(player,"Goblin Mercador")
    elif randomizar==20:
        Comercio(player,"Pequeno Mascate")

def EventoCombate(player):
    print("Você podia pressentir... Inimigos se aproximando... Conforme você seguia seu caminho.")
    input("ENTER")
    encontro_aleatorio(player)

def EventoViajante(player):
    print("AINDA A SER FEITO")
def EventoTesouro(player):
    print("AINDA A SER FEITO")   #FAZ ESSAS PORRAS AÍ NAMORAL TO CANSADÃO
def EventoDescanso(player):
    print("AINDA A SER FEITO")

def EntrarNaDungeon(tabuleiro):
  tabuleiro[random.randint(0,10)][random.randint(0,14)]="o"
  return tabuleiro

def gerar_saida(tabuleiro):
    x,y=random.randint(0,10),random.randint(0,14)
    tabuleiro[x][y]="."
    return x,y,tabuleiro

def conferir_saida(saidax,saiday,tabuleiro):
    xrobo,yrobo=LocalizarRobo(tabuleiro)
    if xrobo==saidax and yrobo==saiday:
        return "ACHOU A SAIDA"
    else:
        return "NAO ACHOU A SAIDA"

def Dungeon_Crawling(player): #dimensões: 11(A)x15(L), indices variam de 0 a 10 e de 0 a 14
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
    tabuleiro=GerarObstaculosNaturais(tabuleiro)
    tabuleiro=EntrarNaDungeon(tabuleiro)
    saidax,saiday,tabuleiro=gerar_saida(tabuleiro)

    while True:
        MostrarTabuleiro(tabuleiro)
        InputAutomatico(tabuleiro)
        sair=conferir_saida(saidax,saiday,tabuleiro)
        if sair=="ACHOU A SAIDA":
            input("Você encontrava a saída da dungeon")
            break
        ConferirEvento(tabuleiro,player)
        
    if player.HP==0:
        while True:
            input("VOCÊ MORREU")
    #inclui uma condição de parada aqui fazendo o favor? HP=0 ou se o player achar a saída