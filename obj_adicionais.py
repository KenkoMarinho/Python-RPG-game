import funcoesrpg
import random
import acoes
class EspadaVoadora:
    def __init__(self,nome,dano,mestre,movimento1="Ataque Espada",movimento2="Defesa Espada"):
        self.nome=nome
        self.dano=dano
        self.mestre=mestre
        self.movimento1=movimento1
        self.movimento2=movimento2
class Armazenar:
  def __init__(self,armazenarplayer=0):
    self.armazenarplayer=armazenarplayer

def CriarEspadaVoadora(mestre,inimigo):
  a,b=str(type(mestre)),str(type(inimigo))
  mestre=mestre
  inimigo=inimigo
  if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_inimigo.objinimigo'>":
    dano=(mestre.INT+mestre.DanoFoco)/5
  if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_personagem.objpersonagem'>":
    dano=(mestre.INT+mestre.DanoFoco)/5
  if a=="<class 'obj_inimigo.objinimigo'>" and b=="<class 'obj_personagem.objpersonagem'>":
    dano=mestre.ataquemagico/5
  return "Espada Voadora",dano,mestre,"Ataque Espada","Defesa Espada"

def randomizar_executar_acao_espada(EspadaVoadora,Inimigo1,Inimigo2,Inimigo3,Inimigo4):
    print("1-Atacar, 2-Proteger")
    rand=input("Deseja que a Espada Ataque ou te proteja?")
    while rand!="1" and rand!="2":
      rand=input("Deseja que a Espada Ataque ou te proteja?")
    rand=int(rand)
    if EspadaVoadora!=0:
      if rand==1:
          alvo=funcoesrpg.PedirAlvo(EspadaVoadora,Inimigo1,Inimigo2,Inimigo3,Inimigo4)
          acoes.Ataque_Espada(EspadaVoadora,alvo)
      else:
          acoes.Defesa_Espada(EspadaVoadora)
    
