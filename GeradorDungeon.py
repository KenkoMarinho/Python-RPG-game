import random

class dungeonrandom:
  def __init__(self,nquartos=0,tematica=0,boss=0,numeventos=0,evento1=0,evento2=0,evento3=0,evento4=0,evento5=0,quarto1=0,quarto2=0,quarto3=0,quarto4=0,quarto5=0,quarto6=0,acoes=0):
    self.nquartos=nquartos
    self.tematica=tematica
    self.boss=boss
    self.numeventos=numeventos
    self.evento1=evento1
    self.evento2=evento2
    self.evento3=evento3
    self.evento4=evento4
    self.evento5=evento5
    self.quarto1=quarto1
    self.quarto2=quarto2
    self.quarto3=quarto3
    self.quarto4=quarto4
    self.quarto5=quarto5
    self.quarto6=quarto6 
    self.acoes=acoes

def GerarTematica(tematica):
  if tematica!=0:
    rand=random.randint(1,5)
    if rand==1:
      tematica="Masmorra"
    if rand==2:
      tematica="Mata"
    if rand==3:
      tematica="Acampamento Inimigo"
    if rand==4:
      tematica="Caverna"
    if rand==5:
      tematica="Local Abandonado"

#TO DO:
'''
def GerarBoss(boss):
def GerarNumQuartos(nquartos):
def GerarEventos(evento1,evento2,evento3,evento4,evento5)

def ExplorarQuarto()
def ExecutarDungeon()
def MostarAcoes()
'''