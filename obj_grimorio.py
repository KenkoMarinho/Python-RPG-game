from funcoesrpg import cls

class objgrimorio:
  def __init__(self,boladefogo=False,transformacaobruxa=False,raiodebruxa=False,vidafalsa=False,drenaralma=False,dancadaslaminas=False,transformacarlobisomem=False,armaelemental=False,misseismagicos=False,raioflamejante=False):
    self.boladefogo=boladefogo
    self.transformacaobruxa=transformacaobruxa
    self.raiodebruxa=raiodebruxa
    self.vidafalsa=vidafalsa
    self.drenaralma=drenaralma
    self.dancadaslaminas=dancadaslaminas
    self.transformacarlobisomem=transformacarlobisomem
    self.armaelemental=armaelemental
    self.misseismagicos=misseismagicos
    self.raioflamejante=raioflamejante

def preparacaomagias(player,grimorioplayer):
  Teclado=(input("Você deseja modificar suas magias preparadas? 1-Sim  2-Não"))
  while Teclado!='1' and Teclado!='2':
    Teclado=(input("Você deseja modificar suas magias preparadas? 1-Sim  2-Não"))
  cls()
  if Teclado=='1':
    if grimorioplayer.boladefogo==True or grimorioplayer.transformacaobruxa==True or grimorioplayer.raiodebruxa==True or grimorioplayer.vidafalsa==True or grimorioplayer.drenaralma==True or grimorioplayer.dancadaslaminas==True or grimorioplayer.transformacarlobisomem==True or grimorioplayer.armaelemental==True or grimorioplayer.misseismagicos==True or grimorioplayer.raioflamejante==True:
      print("Magias Disponíveis:")
      contador=0
      print("======================")
      if grimorioplayer.boladefogo==True:
        print("Bola De Fogo")
        contador+=1
      if grimorioplayer.transformacaobruxa==True:
        print("Transformação: Bruxa")
        contador+=1
      if grimorioplayer.raiodebruxa==True:
        print("Raio De Bruxa")
        contador+=1
      if grimorioplayer.vidafalsa==True:
        print("Vida Falsa")
        contador+=1
      if grimorioplayer.drenaralma==True:
        print("Drenar Alma")
        contador+=1
      if grimorioplayer.dancadaslaminas==True:
        print("Dança Das Lâminas")
        contador+=1
      if grimorioplayer.transformacarlobisomem==True:
        print("Transformar Lobisomem")
        contador+=1
      if grimorioplayer.armaelemental==True:
        print("Arma Elemental")
        contador+=1
      if grimorioplayer.misseismagicos==True:
        print("Misseis Mágicos")
        contador+=1
      if grimorioplayer.raioflamejante==True:
        print("Raio Flamejante")
        contador+=1
      print("======================")
      if contador>=1:
        Teclado=input("Digite o nome da primeira das quatro magias que você pode preparar:")
        while Teclado!="Bola De Fogo" and Teclado!="Transformação: Bruxa" and Teclado!="Raio De Bruxa" and Teclado!="Vida Falsa" and Teclado!="Drenar Alma" and Teclado!="Dança Das Lâminas" and Teclado!="Transformar Lobisomem" and Teclado!="Arma Elemental" and Teclado!="Misseis Mágicos" and Teclado!="Raio Flamejante":
          Teclado=input("Digite o nome da primeira das quatro magias que você pode preparar:")
        player.movimento1=Teclado
      if contador>=2:
        Teclado=input("Digite o nome da segunda das quatro magias que você pode preparar:")
        while Teclado!="Bola De Fogo" and Teclado!="Transformação: Bruxa" and Teclado!="Raio De Bruxa" and Teclado!="Vida Falsa" and Teclado!="Drenar Alma" and Teclado!="Dança Das Lâminas" and Teclado!="Transformar Lobisomem" and Teclado!="Arma Elemental" and Teclado!="Misseis Mágicos" and Teclado!="Raio Flamejante":
          Teclado=input("Digite o nome da segunda das quatro magias que você pode preparar:")
        player.movimento2=Teclado
      if contador>=3:
        Teclado=input("Digite o nome da terceira das quatro magias que você pode preparar:")
        while Teclado!="Bola De Fogo" and Teclado!="Transformação: Bruxa" and Teclado!="Raio De Bruxa" and Teclado!="Vida Falsa" and Teclado!="Drenar Alma" and Teclado!="Dança Das Lâminas" and Teclado!="Transformar Lobisomem" and Teclado!="Arma Elemental" and Teclado!="Misseis Mágicos" and Teclado!="Raio Flamejante":
          Teclado=input("Digite o nome da terceira das quatro magias que você pode preparar:")
        player.movimento3=Teclado
      if contador>=4:
        Teclado=input("Digite o nome da quarta das quatro magias que você pode preparar:")
        while Teclado!="Bola De Fogo" and Teclado!="Transformação: Bruxa" and Teclado!="Raio De Bruxa" and Teclado!="Vida Falsa" and Teclado!="Drenar Alma" and Teclado!="Dança Das Lâminas" and Teclado!="Transformar Lobisomem" and Teclado!="Arma Elemental" and Teclado!="Misseis Mágicos" and Teclado!="Raio Flamejante":
          Teclado=input("Digite o nome da quarta das quatro magias que você pode preparar:")
        player.movimento4=Teclado
    else:
      print("Você não conhece nenhuma magia!")
  print("Fim da Preparação.")
  if player.movimento1==player.movimento2:
    player.movimento2=0
  if player.movimento1==player.movimento3:
    player.movimento3=0
  if player.movimento1==player.movimento4:
    player.movimento4=0
  if player.movimento2==player.movimento3:
    player.movimento3=0
  if player.movimento2==player.movimento4:
    player.movimento4=0
  if player.movimento3==player.movimento4:
    player.movimento4=0

  if player.movimento1==0 and player.movimento5!=0:
    player.movimento1=player.movimento5
    player.movimento5=0
  else:
    if player.movimento1==0 and player.movimento6!=0:
      player.movimento1=player.movimento6
      player.movimento6=0
    else:
      if player.movimento1==0 and player.movimento7!=0:
        player.movimento1=player.movimento7
        player.movimento7=0
      else:
        if player.movimento1==0 and player.movimento8!=0:
          player.movimento1=player.movimento8
          player.movimento8=0
  if player.movimento2==0 and player.movimento5!=0:
    player.movimento2=player.movimento5
    player.movimento5=0
  else:
    if player.movimento2==0 and player.movimento6!=0:
      player.movimento2=player.movimento6
      player.movimento6=0
    else:
      if player.movimento2==0 and player.movimento7!=0:
        player.movimento2=player.movimento7
        player.movimento7=0
      else:
        if player.movimento2==0 and player.movimento8!=0:
          player.movimento2=player.movimento8
          player.movimento8=0
  if player.movimento3==0 and player.movimento5!=0:
    player.movimento3=player.movimento5
    player.movimento5=0
  else:
    if player.movimento3==0 and player.movimento6!=0:
      player.movimento3=player.movimento6
      player.movimento6=0
    else:
      if player.movimento3==0 and player.movimento7!=0:
        player.movimento3=player.movimento7
        player.movimento7=0
      else:
        if player.movimento3==0 and player.movimento8!=0:
          player.movimento3=player.movimento8
          player.movimento8=0
  if player.movimento4==0 and player.movimento5!=0:
    player.movimento4=player.movimento5
    player.movimento5=0
  else:
    if player.movimento4==0 and player.movimento6!=0:
      player.movimento4=player.movimento6
      player.movimento6=0
    else:
      if player.movimento4==0 and player.movimento7!=0:
        player.movimento4=player.movimento7
        player.movimento7=0
      else:
        if player.movimento4==0 and player.movimento8!=0:
          player.movimento4=player.movimento8
          player.movimento8=0
  