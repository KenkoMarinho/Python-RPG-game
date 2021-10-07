import os
def cls():
    os.system('clear')

class objlivrodegolpes:
  def __init__(self,arranhar=False,mordida=False,facada=False,ataqueespada=False,surtodeacao=False,defesaespada=False,frenesi=False,golpeespiral=False):
    self.arranhar=arranhar
    self.mordida=mordida
    self.facada=facada
    self.ataqueespada=ataqueespada
    self.surtodeacao=surtodeacao
    self.defesaespada=defesaespada
    self.frenesi=frenesi
    self.golpeespiral=golpeespiral

#modificar para adaptar o sistema de grimório ao sistema de golpes.
def preparacaogolpes(player,livrogolpesplayer):
  Teclado=(input("Você deseja modificar sua lista de golpes? 1-Sim  2-Não"))
  while Teclado!='1' and Teclado!='2':
    Teclado=(input("Você deseja modificar sua lista de golpes? 1-Sim  2-Não"))
  cls()
  if Teclado=='1':
    if livrogolpesplayer.arranhar==True or livrogolpesplayer.mordida==True or livrogolpesplayer.facada==True or livrogolpesplayer.ataqueespada==True or livrogolpesplayer.surtodeacao==True or livrogolpesplayer.defesaespada==True or livrogolpesplayer.frenesi==True or livrogolpesplayer.golpeespiral==True:
      print("Golpes Disponíveis:")
      contador=0
      print("======================")
      if livrogolpesplayer.arranhar==True:
        print("Arranhar")
        contador+=1
      if livrogolpesplayer.mordida==True:
        print("Mordida")
        contador+=1
      if livrogolpesplayer.facada==True:
        print("Facada")
        contador+=1
      if livrogolpesplayer.ataqueespada==True:
        print("Ataque Espada")
        contador+=1
      if livrogolpesplayer.surtodeacao==True:
        print("Surto De Ação")
        contador+=1
      if livrogolpesplayer.defesaespada==True:
        print("Defesa Espada")
        contador+=1
      if livrogolpesplayer.frenesi==True:
        print("Frenesi")
        contador+=1
      if livrogolpesplayer.golpeespiral==True:
        print("Golpe Espiral")
        contador+=1
      print("======================")
      if contador>=1:
        Teclado=input("Digite o nome do primeiro dos quatro golpes que você pode preparar:")
        while Teclado!="Arranhar" and Teclado!="Mordida" and Teclado!="Facada" and Teclado!="Ataque Espada" and Teclado!="Surto De Ação" and Teclado!="Defesa Espada" and Teclado!="Frenesi" and Teclado!="Golpe Espiral":
          Teclado=input("Digite o nome do primeiro dos quatro golpes que você pode preparar:")
        player.movimento5=Teclado
      if contador>=2:
        Teclado=input("Digite o nome do segundo dos quatro golpes que você pode preparar:")
        while Teclado!="Arranhar" and Teclado!="Mordida" and Teclado!="Facada" and Teclado!="Ataque Espada" and Teclado!="Surto De Ação" and Teclado!="Defesa Espada" and Teclado!="Frenesi" and Teclado!="Golpe Espiral":
          Teclado=input("Digite o nome do segundo dos quatro golpes que você pode preparar:")
        player.movimento6=Teclado
      if contador>=3:
        Teclado=input("Digite o nome do terceiro dos quatro golpes que você pode preparar:")
        while Teclado!="Arranhar" and Teclado!="Mordida" and Teclado!="Facada" and Teclado!="Ataque Espada" and Teclado!="Surto De Ação" and Teclado!="Defesa Espada" and Teclado!="Frenesi" and Teclado!="Golpe Espiral":
          Teclado=input("Digite o nome do terceiro dos quatro golpes que você pode preparar:")
        player.movimento7=Teclado
      if contador>=4:
        Teclado=input("Digite o nome do quarto dos quatro golpes que você pode preparar:")
        while Teclado!="Arranhar" and Teclado!="Mordida" and Teclado!="Facada" and Teclado!="Ataque Espada" and Teclado!="Surto De Ação" and Teclado!="Defesa Espada" and Teclado!="Frenesi" and Teclado!="Golpe Espiral":
          Teclado=input("Digite o nome do quarto dos quatro golpes que você pode preparar:")
        player.movimento8=Teclado
    else:
      print("Você não conhece nenhum golpe!")
  print("Fim da Preparação.")
  if player.movimento5==player.movimento6:
    player.movimento6=0
  if player.movimento5==player.movimento7:
    player.movimento7=0
  if player.movimento5==player.movimento8:
    player.movimento8=0
  if player.movimento6==player.movimento7:
    player.movimento7=0
  if player.movimento6==player.movimento8:
    player.movimento8=0
  if player.movimento7==player.movimento8:
    player.movimento8=0