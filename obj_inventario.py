from funcoesrpg import *
import obj_personagem
import os

class objinventario:
  def __init__(self,pocoeshp=0,pocoesmp=0,slot1=0,slot2=0,slot3=0,slot4=0,slot5=0,slot6=0,slot7=0,slot8=0,slot9=0,slot10=0):
    self.pocoeshp=pocoeshp
    self.pocoesmp=pocoesmp
    self.slot1=slot1
    self.slot2=slot2
    self.slot3=slot3
    self.slot4=slot4
    self.slot5=slot5
    self.slot6=slot6
    self.slot7=slot7
    self.slot8=slot8
    self.slot9=slot9
    self.slot10=slot10

#def AdicionarItem(objeto):
#def GerenciarInventario(objeto):
#def RemoverItem(objeto):
#def VerificarMaxPocoesHpMp(objeto):
#def UsarItem(objeto):
def GerenciarInventario(player):
  confirmacao="0"
  flagskip=False
  confirmar=False
  objeto=player.mochila
  flagfechar=False
  cont=0
  item1=0
  item2=0
  item3=0
  item4=0
  item5=0
  item6=0
  item7=0
  item8=0
  item9=0
  item10=0
  os.system('clear')
  print("===========ESTATÍSTICAS===========")
  print("Nome:",player.nome)
  print("HP:",player.HP,"/",player.HPMax)
  print("MP:",player.MP,"/",player.MPMax)
  print("FOR:",player.FOR," DES:",player.DES," CON:",player.CON)
  print("INT:",player.INT," SAB:",player.SAB," CAR:",player.CAR)
  if str(player.tipoarma)!='0' or str(player.tipoescudo)!='0' or str(player.tipoarmadura)!='0' or str(player.tipoanel)!='0':
    print("===========EQUIPAMENTOS===========")
  switch=False
  switch2=False
  switch3=False
  if str(player.tipoarma)!='0':
    print("Arma Equipada:",player.tipoarma)
    print("Dano:",player.DanoArma)
    if player.DanoFoco>0:
      print("Dano Foco:",player.DanoFoco)
    switch3=True
  if str(player.tipoescudo)!='0':
    if switch3==True:
      print("")
    print("Segunda Mão:",player.tipoescudo)
    switch=True
  if str(player.tipoarmadura)!='0':
    if switch==True or switch3==True:
      print("")
    print("Armadura/Vestimenta:",player.tipoarmadura)
    print("Defesa:",player.Defesa)
    print("Defesa Mágica:",player.DefesaMagica)
    switch2=True
  if str(player.tipoanel)!='0':
    if switch2==True or switch3==True or switch==True:
      print("")
    print("Anel Ligado:",player.tipoanel)
  print("============INVENTÁRIO============")
  print("Poções HP:",objeto.pocoeshp,"/ 10")
  print("Poções MP:",objeto.pocoesmp,"/ 10")
  if objeto.slot1!=0:
    cont+=1
    print(cont,"-",objeto.slot1)
    item1=objeto.slot1
  if objeto.slot2!=0:
    cont+=1
    print(cont,"-",objeto.slot2)
    if item1==0:
      item1=objeto.slot2
    elif item2==0:
      item2=objeto.slot2
  if objeto.slot3!=0:
    cont+=1
    print(cont,"-",objeto.slot3)
    if item1==0:
      item1=objeto.slot3
    elif item2==0:
      item2=objeto.slot3
    elif item3==0:
      item3=objeto.slot3
  if objeto.slot4!=0:
    cont+=1
    print(cont,"-",objeto.slot4)
    if item1==0:
      item1=objeto.slot4
    elif item2==0:
      item2=objeto.slot4
    elif item3==0:
      item3=objeto.slot4
    elif item4==0:
      item4=objeto.slot4
  if objeto.slot5!=0:
    cont+=1
    print(cont,"-",objeto.slot5)
    if item1==0:
      item1=objeto.slot5
    elif item2==0:
      item2=objeto.slot5
    elif item3==0:
      item3=objeto.slot5
    elif item4==0:
      item4=objeto.slot5
    elif item5==0:
      item5=objeto.slot5
  if objeto.slot6!=0:
    cont+=1
    print(cont,"-",objeto.slot6)
    if item1==0:
      item1=objeto.slot6
    elif item2==0:
      item2=objeto.slot6
    elif item3==0:
      item3=objeto.slot6
    elif item4==0:
      item4=objeto.slot6
    elif item5==0:
      item5=objeto.slot6
    elif item6==0:
      item6=objeto.slot6
  if objeto.slot7!=0:
    cont+=1
    print(cont,"-",objeto.slot7)
    if item1==0:
      item1=objeto.slot7
    elif item2==0:
      item2=objeto.slot7
    elif item3==0:
      item3=objeto.slot7
    elif item4==0:
      item4=objeto.slot7
    elif item5==0:
      item5=objeto.slot7
    elif item6==0:
      item6=objeto.slot7
    elif item7==0:
      item7=objeto.slot7
  if objeto.slot8!=0:
    cont+=1
    print(cont,"-",objeto.slot8)
    if item1==0:
      item1=objeto.slot8
    elif item2==0:
      item2=objeto.slot8
    elif item3==0:
      item3=objeto.slot8
    elif item4==0:
      item4=objeto.slot8
    elif item5==0:
      item5=objeto.slot8
    elif item6==0:
      item6=objeto.slot8
    elif item7==0:
      item7=objeto.slot8
    elif item8==0:
      item8=objeto.slot8
  if objeto.slot9!=0:
    cont+=1
    print(cont,"-",objeto.slot9)
    if item1==0:
      item1=objeto.slot9
    elif item2==0:
      item2=objeto.slot9
    elif item3==0:
      item3=objeto.slot9
    elif item4==0:
      item4=objeto.slot9
    elif item5==0:
      item5=objeto.slot9
    elif item6==0:
      item6=objeto.slot9
    elif item7==0:
      item7=objeto.slot9
    elif item8==0:
      item8=objeto.slot9
    elif item9==0:
      item9=objeto.slot9
  if objeto.slot10!=0:
    cont+=1
    print(cont,"-",objeto.slot10)
    if item1==0:
      item1=objeto.slot10
    elif item2==0:
      item2=objeto.slot10
    elif item3==0:
      item3=objeto.slot10
    elif item4==0:
      item4=objeto.slot10
    elif item5==0:
      item5=objeto.slot10
    elif item6==0:
      item6=objeto.slot10
    elif item7==0:
      item7=objeto.slot10
    elif item8==0:
      item8=objeto.slot10
    elif item9==0:
      item9=objeto.slot10
    elif item10==0:
      item10=objeto.slot10
  print("==================================")
  print("Digite o Número do Item selecionado")
  print("Se quiser Desequipar um item, digite 'Desequipar'")
  print("ou digite HP para Poção de Cura e MP para Poção de Mana")
  teclado=input("ou aperte ENTER para fechar o inventário.")
  while teclado!="HP" and teclado!="MP" and teclado!='1' and  teclado!='2' and  teclado!='3'and  teclado!='4' and  teclado!='5' and  teclado!='6' and  teclado!='7' and  teclado!='8' and  teclado!='9' and  teclado!='10' and teclado!="" and teclado!='Desequipar':
    print("Digite o Número do Item selecionado")
    print("ou digite HP para Poção de Cura e MP para Poção de Mana")
    teclado=input("ou aperte ENTER para fechar o inventário.")
  if teclado=="Desequipar":
    selecionar=input('1-Desequipar Arma, 2-Desequipar Armadura,3-Desequipar Escudo 4-Desequipar Anel')
    while selecionar!='1' and selecionar!='3' and selecionar!='2' and selecionar!='4':
      selecionar=input('1-Desequipar Arma, 2-Desequipar Armadura,3-Desequipar Escudo 4-Desequipar Anel')
    flagskip=True
    if selecionar=='1':
      player.tipoarma=0
    if selecionar=='2':
      player.tipoarmadura=0
    if selecionar=='3':
      player.tipoescudo=0
    if selecionar=='4':
      player.tipoanel=0
  if teclado=="HP":
    itemselecionado="pocaohp"
  if teclado=="MP":
    itemselecionado="pocaomp"
  if teclado=='1':
    itemselecionado=item1
  if teclado=='2':
    itemselecionado=item2
  if teclado=='3':
    itemselecionado=item3
  if teclado=='4':
    itemselecionado=item4
  if teclado=='5':
    itemselecionado=item5
  if teclado=='6':
    itemselecionado=item6
  if teclado=='7':
    itemselecionado=item7
  if teclado=='8':
    itemselecionado=item8
  if teclado=='9':
    itemselecionado=item9
  if teclado=='10':
    itemselecionado=item10
  if teclado=="":
    flagfechar=True
  if flagfechar==False:
    if flagskip==False:
      teclado2=input("O que você deseja fazer com esse item? 1-Jogar Fora, 2-Usar")
      while teclado2!='1' and teclado2!='2':
        teclado2=input("O que você deseja fazer com esse item? 1-Jogar Fora, 2-Usar")
      if teclado2=="1":
        jogarfora=True
    else:
      teclado2='1'
 #preguiça de arrumar identação de 200 linhas velho
    if 5==5:
      consumo=False
      jogarfora=False
      usar=False
      if teclado2=='2':
        consumo=True
        usar=True
      if teclado2=='1':
        jogarfora=True
      if itemselecionado=="pocaohp":
        if objeto.pocoeshp>0:
          if consumo==True:
            print("Você bebia uma poção de HP!")
            player.HP=player.HP+int(player.HPMax/3)
            if player.HP>player.HPMax:
              player.HP=player.HPMax
            print("HP:",player.HP,"/",player.HPMax)
          if jogarfora==True:
            print("Você jogava uma poção de HP fora.")
          objeto.pocoeshp=objeto.pocoeshp-1
        else:
          if jogarfora==True:
            print("Você não tem poções pra jogar fora!")
          elif consumo==True:
            print("Você não tem poções para consumir!")
      elif itemselecionado=="pocaomp":
        if objeto.pocoesmp>0:
          if consumo==True:
            print("Você bebia uma poção de MP!")
            player.MP=player.MP+int(player.MPMax/3)
            if player.MP>player.MPMax:
              player.MP=player.MPMax
            print("MP:",player.MP,"/",player.MPMax)
          if jogarfora==True:
            print("Você jogava uma poção de MP fora.")
          objeto.pocoesmp=objeto.pocoesmp-1
        else:
          if consumo==True:
            print("Você não tem poções para consumir!")
          if jogarfora==True:
            print("Você não tem poções para jogar fora!")
      #armas físicas equipar
      elif (itemselecionado=="Espada Curta" or itemselecionado=="Adaga" or itemselecionado=="Espada Longa" or itemselecionado=="Arco" or itemselecionado=="Rapieira" or itemselecionado=="Besta" or itemselecionado=="Adagas Gêmeas") and usar==True:
        player.tipoarma=itemselecionado
        if itemselecionado[len(itemselecionado)-1]=="a":
          print(player.nome,"equipava uma",itemselecionado)
          #jogarfora=True
          #confirmar=True
        else:
          print(player.nome,"equipava um",itemselecionado)
          #jogarfora=True
          #confirmar=True
      #focos mágicos equipar
      elif (itemselecionado=="Varinha De Teixo" or itemselecionado=="Varinha De Visco" or itemselecionado=="Cajado" or itemselecionado=="Bolsa De Runas" or itemselecionado=="Espada Dos Magos" or itemselecionado=="Cajado Sagrado") and usar==True:
        if itemselecionado!="Cajado Sagrado" or itemselecionado!="Cajado":
          player.tipoarma=itemselecionado
        else:
          player.tipoarma=itemselecionado
          player.tipoescudo=itemselecionado
        if itemselecionado[len(itemselecionado)-1]=="a":
          print(player.nome,"equipava uma",itemselecionado)
          #jogarfora=True
          #confirmar=True
        else:
          print(player.nome,"equipava um",itemselecionado)
          #jogarfora=True
          #confirmar=True
      #armaduras equipar
      elif (itemselecionado=="Armadura De Couro" or itemselecionado=="Cota De Malha" or itemselecionado=="Camisão De Malha" or itemselecionado=="Sobre-Tudo" or itemselecionado=="Robes Desgastadas") and usar==True:
        player.tipoarmadura=itemselecionado
        if itemselecionado[len(itemselecionado)-1]=="a":
          print(player.nome,"equipava uma",itemselecionado)
          #jogarfora=True
          #confirmar=True
        else:
          print(player.nome,"equipava um",itemselecionado)
          #jogarfora=True
          #confirmar=True
      #anéis equipar
      elif (itemselecionado=="Anel De Conjurador" or itemselecionado=="Anel De Bola De Fogo")and usar==True:
        player.tipoanel=itemselecionado
        if itemselecionado=="Anel De Conjurador":
          player.DanoFoco+=int(((player.INT*7+player.SAB*3)/10)/12)
        if itemselecionado=="Anel De Bola De Fogo":
          player.movimento1="Bola De Fogo"
        if itemselecionado[len(itemselecionado)-1]=="a":
          print(player.nome,"equipava uma",itemselecionado)
          #jogarfora=True
          #confirmar=True
        else:
          print(player.nome,"equipava um",itemselecionado)
          #jogarfora=True
          #confirmar=True
      #escudos/armas de duas mãos equipar
      elif itemselecionado==(itemselecionado=="Adagas Gêmeas" or itemselecionado=="Espada Larga" or itemselecionado=="Espada Larga" or itemselecionado=="Cajado" or itemselecionado=="Cajado Sagrado") and usar==True:
        player.tipoescudo=itemselecionado
        if itemselecionado=="Cajado" or itemselecionado=="Cajado Sagrado" or itemselecionado=="Espada Larga":
          player.tipoarma=itemselecionado
          player.tipoescudo=itemselecionado
        if itemselecionado[len(itemselecionado)-1]=="a":
          print(player.nome,"equipava uma",itemselecionado)
          #jogarfora=True
          #confirmar=True
        else:
          print(player.nome,"equipava um",itemselecionado)
          #jogarfora=True
          #confirmar=True
      if jogarfora==True:
        if confirmar==False:
          confirmacao=input("Tem Certeza? <1-Sim 2-Não>")
          while confirmacao!='1' and confirmacao!='2':
            confirmacao=input("Tem Certeza? <1-Sim 2-Não>")
        if confirmar==True:
          confirmacao='1'
        if confirmacao=='1':
          if (((itemselecionado==str(player.tipoarma))or(itemselecionado==str(player.tipoarmadura))or(itemselecionado==str(player.tipoescudo))or(itemselecionado==str(player.tipoanel))) and jogarfora==True and confirmacao=='1'):
            if itemselecionado in str(objeto.slot1):
              objeto.slot1=0
            elif itemselecionado in str(objeto.slot2):
              objeto.slot1=0
            elif itemselecionado in str(objeto.slot3):
              objeto.slot1=0
            elif itemselecionado in str(objeto.slot4):
              objeto.slot1=0
            elif itemselecionado in str(objeto.slot5):
              objeto.slot1=0
            elif itemselecionado in str(objeto.slot6):
              objeto.slot1=0
            elif itemselecionado in str(objeto.slot7):
              objeto.slot1=0
            elif itemselecionado in str(objeto.slot8):
              objeto.slot1=0
            elif itemselecionado in str(objeto.slot9):
              objeto.slot1=0
            elif itemselecionado in str(objeto.slot10):
              objeto.slot1=0

          if itemselecionado in str(objeto.slot1):
            if itemselecionado==str(item1):
              objeto.slot1=0
            elif item1 in str(objeto.slot2):
              objeto.slot2=0
            elif item1 in str(objeto.slot3):
              objeto.slot3=0
            elif item1 in str(objeto.slot4):
              objeto.slot4=0
            elif item1 in str(objeto.slot5):
              objeto.slot5=0
            elif item1 in str(objeto.slot6):
              objeto.slot6=0
            elif item1 in str(objeto.slot7):
              objeto.slot7=0
            elif item1 in str(objeto.slot8):
              objeto.slot8=0
            elif item1 in str(objeto.slot9):
              objeto.slot9=0
            elif item1 in str(objeto.slot10):
              objeto.slot10=0
            item1=0
          if itemselecionado==item2:
            if item2 in str(objeto.slot1):
              objeto.slot1=0
            elif item2 in str(objeto.slot2):
              objeto.slot2=0
            elif item2 in str(objeto.slot3):
              objeto.slot3=0
            elif item2 in str(objeto.slot4):
              objeto.slot4=0
            elif item2 in str(objeto.slot5):
              objeto.slot5=0
            elif item2 in str(objeto.slot6):
              objeto.slot6=0
            elif item2 in str(objeto.slot7):
              objeto.slot7=0
            elif item2 in str(objeto.slot8):
              objeto.slot8=0
            elif item2 in str(objeto.slot9):
              objeto.slot9=0
            elif item2 in str(objeto.slot10):
              objeto.slot10=0
            item2=0
          if itemselecionado==item3:
            if item3 in str(objeto.slot1):
              objeto.slot1=0
            elif item3 in str(objeto.slot2):
              objeto.slot2=0
            elif item3 in str(objeto.slot3):
              objeto.slot3=0
            elif item3 in str(objeto.slot4):
              objeto.slot4=0
            elif item3 in str(objeto.slot5):
              objeto.slot5=0
            elif item3 in str(objeto.slot6):
              objeto.slot6=0
            elif item3 in str(objeto.slot7):
              objeto.slot7=0
            elif item3 in str(objeto.slot8):
              objeto.slot8=0
            elif item3 in str(objeto.slot9):
              objeto.slot9=0
            elif item3 in str(objeto.slot10):
              objeto.slot10=0
            item3=0
          if itemselecionado==str(item4):
            if item4 in str(objeto.slot1):
              objeto.slot1=0
            elif item4 in str(objeto.slot2):
              objeto.slot2=0
            elif item4 in str(objeto.slot3):
              objeto.slot3=0
            elif item4 in str(objeto.slot4):
              objeto.slot4=0
            elif item4 in str(objeto.slot5):
              objeto.slot5=0
            elif item4 in str(objeto.slot6):
              objeto.slot6=0
            elif item4 in str(objeto.slot7):
              objeto.slot7=0
            elif item4 in str(objeto.slot8):
              objeto.slot8=0
            elif item4 in str(objeto.slot9):
              objeto.slot9=0
            elif item4 in str(objeto.slot10):
              objeto.slot10=0
            item4=0
          if itemselecionado==item5:
            if item5 in str(objeto.slot1):
              objeto.slot1=0
            elif item5 in str(objeto.slot2):
              objeto.slot2=0
            elif item5 in str(objeto.slot3):
              objeto.slot3=0
            elif item5 in str(objeto.slot4):
              objeto.slot4=0
            elif item5 in str(objeto.slot5):
              objeto.slot5=0
            elif item5 in str(objeto.slot6):
              objeto.slot6=0
            elif item5 in str(objeto.slot7):
              objeto.slot7=0
            elif item5 in str(objeto.slot8):
              objeto.slot8=0
            elif item5 in str(objeto.slot9):
              objeto.slot9=0
            elif item5 in str(objeto.slot10):
              objeto.slot10=0
            item5=0
          if itemselecionado==item6:
            if item6 in str(objeto.slot1):
              objeto.slot1=0
            elif item6 in str(objeto.slot2):
              objeto.slot2=0
            elif item6 in str(objeto.slot3):
              objeto.slot3=0
            elif item6 in str(objeto.slot4):
              objeto.slot4=0
            elif item6 in str(objeto.slot5):
              objeto.slot5=0
            elif item6 in str(objeto.slot6):
              objeto.slot6=0
            elif item6 in str(objeto.slot7):
              objeto.slot7=0
            elif item6 in str(objeto.slot8):
              objeto.slot8=0
            elif item6 in str(objeto.slot9):
              objeto.slot9=0
            elif item6 in str(objeto.slot10):
              objeto.slot10=0
            item6=0
          if itemselecionado==item7:
            if item7 in str(objeto.slot1):
              objeto.slot1=0
            elif item7 in str(objeto.slot2):
              objeto.slot2=0
            elif item7 in str(objeto.slot3):
              objeto.slot3=0
            elif item7 in str(objeto.slot4):
              objeto.slot4=0
            elif item7 in str(objeto.slot5):
              objeto.slot5=0
            elif item7 in str(objeto.slot6):
              objeto.slot6=0
            elif item7 in str(objeto.slot7):
              objeto.slot7=0
            elif item7 in str(objeto.slot8):
              objeto.slot8=0
            elif item7 in str(objeto.slot9):
              objeto.slot9=0
            elif item7 in str(objeto.slot10):
              objeto.slot10=0
            item7=0
          if itemselecionado==item8:
            if item8 in str(objeto.slot1):
              objeto.slot1=0
            elif item8 in str(objeto.slot2):
              objeto.slot2=0
            elif item8 in str(objeto.slot3):
              objeto.slot3=0
            elif item8 in str(objeto.slot4):
              objeto.slot4=0
            elif item8 in str(objeto.slot5):
              objeto.slot5=0
            elif item8 in str(objeto.slot6):
              objeto.slot6=0
            elif item8 in str(objeto.slot7):
              objeto.slot7=0
            elif item8 in str(objeto.slot8):
              objeto.slot8=0
            elif item8 in str(objeto.slot9):
              objeto.slot9=0
            elif item8 in str(objeto.slot10):
              objeto.slot10=0
            item8=0
          if itemselecionado==item9:
            if item9 in str(objeto.slot1):
              objeto.slot1=0
            elif item9 in str(objeto.slot2):
              objeto.slot2=0
            elif item9 in str(objeto.slot3):
              objeto.slot3=0
            elif item9 in str(objeto.slot4):
              objeto.slot4=0
            elif item9 in str(objeto.slot5):
              objeto.slot5=0
            elif item9 in str(objeto.slot6):
              objeto.slot6=0
            elif item9 in str(objeto.slot7):
              objeto.slot7=0
            elif item9 in str(objeto.slot8):
              objeto.slot8=0
            elif item9 in str(objeto.slot9):
              objeto.slot9=0
            elif item9 in str(objeto.slot10):
              objeto.slot10=0
            item9=0
          if itemselecionado==item10:
            if item10 in str(objeto.slot1):
              objeto.slot1=0
            elif item10 in str(objeto.slot2):
              objeto.slot2=0
            elif item10 in str(objeto.slot3):
              objeto.slot3=0
            elif item10 in str(objeto.slot4):
              objeto.slot4=0
            elif item10 in str(objeto.slot5):
              objeto.slot5=0
            elif item10 in str(objeto.slot6):
              objeto.slot6=0
            elif item10 in str(objeto.slot7):
              objeto.slot7=0
            elif item10 in str(objeto.slot8):
              objeto.slot8=0
            elif item10 in str(objeto.slot9):
              objeto.slot9=0
            elif item10 in str(objeto.slot10):
              objeto.slot10=0
            item10=0
  obj_personagem.resetarValores(player)
  if flagfechar==True:
    print("Você fechava a Mochila.")
    input("ENTER")
    os.system('clear')
  else:
    if conferirbagarma(player,objeto)==False:
      player.tipoarma=0
      Desequipararma(player)
    if conferirbagarmadura(player,objeto)==False:
      player.tipoarmadura=0
      Desequipararmadura(player)
    if conferirbagescudo(player,objeto)==False:
      player.tipoescudo=0
      Desequiparescudo(player)
    if conferirbaganel(player,objeto)==False:
      player.tipoanel=0
      Desequiparanel(player)
    input("ENTER")
    os.system('clear')
    GerenciarInventario(player)
  
  if conferirbagarma==False:
    player.tipoarma=0
    Desequipararma(player)
  if conferirbagarmadura==False:
    player.tipoarmadura=0
    Desequipararmadura(player)
  if conferirbagescudo==False:
    player.tipoescudo=0
    Desequiparescudo(player)
  if conferirbaganel==False:
    player.tipoanel=0
    Desequiparanel(player)
  player.mochila=objeto
  


def conferirbagarma(player,objeto):
  if not((player.tipoarma==objeto.slot1)or(player.tipoarma==objeto.slot2)or(player.tipoarma==objeto.slot3)or(player.tipoarma==objeto.slot4)or(player.tipoarma==objeto.slot5)or(player.tipoarma==objeto.slot6)or(player.tipoarma==objeto.slot7)or(player.tipoarma==objeto.slot8)or(player.tipoarma==objeto.slot9)or(player.tipoarma==objeto.slot10)):
    return False
  else:
    return True
  
def conferirbagarmadura(player,objeto):
  if not((player.tipoarmadura==objeto.slot1)or(player.tipoarmadura==objeto.slot2)or(player.tipoarmadura==objeto.slot3)or(player.tipoarmadura==objeto.slot4)or(player.tipoarmadura==objeto.slot5)or(player.tipoarmadura==objeto.slot6)or(player.tipoarmadura==objeto.slot7)or(player.tipoarmadura==objeto.slot8)or(player.tipoarmadura==objeto.slot9)or(player.tipoarmadura==objeto.slot10)):
    return False
  else:
    return True

def conferirbagescudo(player,objeto):
  if not((player.tipoescudo==objeto.slot1)or(player.tipoescudo==objeto.slot2)or(player.tipoescudo==objeto.slot3)or(player.tipoescudo==objeto.slot4)or(player.tipoescudo==objeto.slot5)or(player.tipoescudo==objeto.slot6)or(player.tipoescudo==objeto.slot7)or(player.tipoescudo==objeto.slot8)or(player.tipoescudo==objeto.slot9)or(player.tipoescudo==objeto.slot10)):
    return False
  else:
    return True

def conferirbaganel(player,objeto):
  if not((player.tipoanel==objeto.slot1)or(player.tipoanel==objeto.slot2)or(player.tipoanel==objeto.slot3)or(player.tipoanel==objeto.slot4)or(player.tipoanel==objeto.slot5)or(player.tipoanel==objeto.slot6)or(player.tipoanel==objeto.slot7)or(player.tipoanel==objeto.slot8)or(player.tipoanel==objeto.slot9)or(player.tipoanel==objeto.slot10)):
    return False
  else:
    return True

def Desequipararma(player):
  player.DanoArma=0
def Desequipararmadura(player):
  player.Defesa=0
  player.DefesaMagica=0
def Desequiparescudo(player):
  player.escudo=0
def Desequiparanel(player):
  if player.tipoanel=="Anel De Bola De Fogo":
    player.movimento1=0
    player.tipoanel=0
  if player.tipoanel=="Anel Do Conjurador":
    player.DanoFoco-=int(((player.INT*7+player.SAB*3)/10)/12)

def AdicionarItem(player,item):
  if player.mochila.slot1==0 or player.mochila.slot1=='0':
    player.mochila.slot1=item
  elif player.mochila.slot2==0 or player.mochila.slot1=='0':
    player.mochila.slot2=item
  elif player.mochila.slot3==0 or player.mochila.slot1=='0':
    player.mochila.slot3=item
  elif player.mochila.slot4==0 or player.mochila.slot1=='0':
    player.mochila.slot4=item
  elif player.mochila.slot5==0 or player.mochila.slot1=='0':
    player.mochila.slot5=item
  elif player.mochila.slot6==0 or player.mochila.slot1=='0':
    player.mochila.slot6=item
  elif player.mochila.slot7==0 or player.mochila.slot1=='0':
    player.mochila.slot7=item
  elif player.mochila.slot8==0 or player.mochila.slot1=='0':
    player.mochila.slot8=item
  elif player.mochila.slot9==0 or player.mochila.slot1=='0':
    player.mochila.slot9=item
  elif player.mochila.slot10==0 or player.mochila.slot1=='0':
    player.mochila.slot10=item
  else:
    print("Você não tem espaços na sua mochila! Deseja jogar algo fora?")
    escolha=input("<1-Sim 2-Não>")
    while escolha!='1' and escolha!="2":
      escolha=input("<1-Sim 2-Não>")
    if escolha=='1':
      print("1-",player.mochila.slot1)
      print("2-",player.mochila.slot2)
      print("3-",player.mochila.slot3)
      print("4-",player.mochila.slot4)
      print("5-",player.mochila.slot5)
      print("6-",player.mochila.slot6)
      print("7-",player.mochila.slot7)
      print("8-",player.mochila.slot8)
      print("9-",player.mochila.slot9)
      print("10-",player.mochila.slot10)
      escolha=input("Digite o Número do item que deseja remover")
      while escolha!='1' and escolha!='2' and escolha!='3' and escolha!='4' and escolha!='5' and escolha!='6' and escolha!='7' and escolha!='8' and escolha!='9' and escolha!='10':
        escolha=input("Digite o Número do item que deseja remover")
      if escolha=='1':
        player.mochila.slot1=0
        AdicionarItem(player,item)
      if escolha=='2':
        player.mochila.slot1=0
        AdicionarItem(player,item)
      if escolha=='3':
        player.mochila.slot1=0
        AdicionarItem(player,item)
      if escolha=='4':
        player.mochila.slot1=0
        AdicionarItem(player,item)
      if escolha=='5':
        player.mochila.slot1=0
        AdicionarItem(player,item)
      if escolha=='6':
        player.mochila.slot1=0
        AdicionarItem(player,item)
      if escolha=='7':
        player.mochila.slot1=0
        AdicionarItem(player,item)
      if escolha=='8':
        player.mochila.slot1=0
        AdicionarItem(player,item)
      if escolha=='9':
        player.mochila.slot1=0
        AdicionarItem(player,item)
      if escolha=='10':
        player.mochila.slot1=0
        AdicionarItem(player,item)
