import random
class objinimigo:
  def __init__(self,nome=0,HPMax=0,HP=0,MPMax=0,MP=0,ataquefisico=0,ataquemagico=0,defesa=0,defesamagica=0,inimigovivo=0,dificuldade=0,movimento1=0,movimento2=0,movimento3=0,movimento4=0,ataquesmagicos=False,imunidades=0,podefugir=True,alavanca=False,regenerar=False):
    self.nome=nome
    self.HPMax=HPMax
    self.HP=HP
    self.MPMax=MPMax
    self.MP=MP
    self.ataquefisico=ataquefisico
    self.ataquemagico=ataquemagico
    self.defesa=defesa
    self.defesamagica=defesamagica
    self.inimigovivo=inimigovivo
    self.dificuldade=dificuldade
    self.movimento1=movimento1
    self.movimento2=movimento2
    self.movimento3=movimento3
    self.movimento4=movimento4
    self.ataquesmagicos=ataquesmagicos
    self.imunidades=str(imunidades)
    self.podefugir=podefugir
    self.alavanca=alavanca
    self.regenerar=regenerar #serve pra ver se fugiram ou não desse inimigo, pra calcular xp direito.
  
def verificarHP(inimigo):
  if inimigo.HP>inimigo.HPMax:
    inimigo.HP=inimigo.HPMax
  if inimigo.HP<1:
    inimigo.HP=0
    if inimigo.nome!=0:
      print(f"{inimigo.nome} Foi morto.")

def verificarMP(inimigo):
  if inimigo.MP>inimigo.MPMax:
    inimigo.MP=inimigo.MPMax
  if inimigo.MP<1:
    inimigo.MP=0