import obj_adicionais
import os
import obj_inimigo
import obj_personagem
import acoes
import random
import obj_inventario
def cls():
  os.system('clear')

def GerarInimigo1(inimigoselecionado=0,objplayer=0):
    randomizar=random.randint(1,11)
    if inimigoselecionado!=0:
      if inimigoselecionado=="Zumbi":
        randomizar=1
      if inimigoselecionado=="Goblin":
        randomizar=3
      if inimigoselecionado=="Lobo Atroz":
        randomizar=5
      if inimigoselecionado=="Minotauro Esquelético":
        randomizar=6
      if inimigoselecionado=="Carniçal":
        randomizar=7
      if inimigoselecionado=="Esqueleto":
        randomizar=8
      if inimigoselecionado=="Bruxa":
        randomizar=9
      if inimigoselecionado=="Espectro":
        randomizar=10
      if inimigoselecionado=="Troll":
        randomizar=11
      if inimigoselecionado=="Espada Viva":
        print("A espada começava a tremer, glifos e runas brilhavam em roxo emanando de seu cabo, e então, ela começava a voar e se balançar por aí, Atacando você! É uma Espada Viva!")
        input("ENTER")
        randomizar=0
        return("Espada Viva",5,5,0,0,4,0,1,0,0,0.5,"Ataque Espada","Defesa Espada",0,0,False,"")
      if inimigoselecionado=="Armadura Viva":
        print("De repente, uma armadura que estava no canto da sala começava a se mover, marchando em sua direção, como se estivesse possuída! É uma Armadura Viva!")
        randomizar=0
        return("Armadura Viva",10,10,5,5,3,0,3,1,0,2,"Ataque Espada","Surto De Ação",0,0,0,0)
      if inimigoselecionado=="Mímico":
        randomizar=0
        return("Mímico",8,8,0,0,3,0,1,3,0,1,"Mordida",0,0,0,0,0)
    if randomizar==1 or randomizar==2:
      print("Gemidos de Dor ecoavam pela mata escura, até que lá de dentro sai um homem arrastado, com roupas maltrapilhas, ele andava de lado, pela sua experiência, sabia não se tratar de homem, mas sim de morto. Um Zumbi!")
      return("Zumbi",8,8,2,2,3,0,2,0,True,0.5,"Arranhar","Mordida",0,0,0,0)
    if randomizar==3 or randomizar==4:
      print("Risadas e gorfadas podiam ser ouvidas, de surpresa, uma criatura pequena e verde com uma faca na mão corre em sua direção sem nem você saber de onde foi que ela saiu!")
      return("Goblin",5,5,2,2,3,0,1,0,True,1,"Facada","Fúria Do Nanico",0,0,0,0)
    if randomizar==5:
      print("Você ouvia uivos ao longe na floresta, o vento soprava carregando o som da morte que se aproximava, você podia ouvir o som de patas correndo, até que elas te alcançavam, estava diante de ti, o predador, O Lobo Atroz!")
      print("                              __")
      print("                            .d$$b")
      print("                          .' TO$;\ ")
      print("                         /  : TP._;")
      print("                        / _.;  :Tb|")
      print("                       /   /   ;j$j")
      print("                   _.-""       d$$$$")
      print("                 .' ..       d$$$$;")
      print("                /  /P'      d$$$$P. |\ ")
      print("               /   ""       d$$$P |\^'l")
      print("             .'           `T$P^'''''  :")
      print("         ._.'      _.'                ;")
      print("      `-.-"".-'-' ._.       _.-"    '.-'"")
      print('    `.-" __  .              .-""')
      print("   -(.g$$$$$$$b.              .'")
      print('     ""^^T$$$P^)            .(:')
      print('''       _/  -"  /.'         /:/;''')
      print("    ._.'-'`-'  ')/         /;/;")
      print(' `-.-"..--""   " /         /  ;')
      print('.-" ..--""        -''          :')
      print('..--""--.-"         (\     .-()')
      return ("Lobo Atroz",10,10,2,2,5,0,2,0,True,2,"Mordida","Surto De Ação","Transformar Lobisomem",0,0,0)
    if randomizar==6:
      print("Você podia sentir um frio sepulcral percorrer sua espinha conforme ele se aproximava...Você podia ver uma silhueta de um cavalo na floresta, até que percebe que tudo que o mesmo toca se esvai a vida, morrendo e murchando flores e árvores... Ele se vira pra você, revelando a luz de sua verdadeira natureza, um Minotauro Esquelético!")
      return("Minotauro Esquelético",15,15,1,1,8,0,4,1,True,3,"Ataque Espada","Frenesi",0,0,0,0)
    if randomizar==7:
      print("Você podia sentir um cheiro pútrido de morte na atmosfera da floresta, se aproximando da origem do cheiro, você podia ver uma pessoa de mais ou menos um metro e meio de altura, pálida, com veias saltadas pelo corpo inteiro, debruçada sobre um cadáver, observando melhor, você podia ver que este cadáver estava sendo devorado por essa pessoa! Se trata de um Carniçal!")
      return("Carniçal",15,15,3,3,5,0,0,0,True,3,"Mordida","Surto De Ação","Sangue-Suga",0,0,0)
    if randomizar==8:
      print("Você ouvia estalares, sons de algo duro se batendo, de repente, o som ficava mais próximo, você começava a ouvir o som de ossos se batendo, até que um Esqueleto salta sobre você empunhando uma cimitarra!")
      print("             .7")
      print("           .'/")
      print("          / /")
      print("         / /")
      print("        / /")
      print("       / /")
      print("      / /")
      print("     / /")
      print("  __|/")
      print(",-\__)")
      print("|f-''Y\|")
      print("\()7L/")
      print(" cgD                            __ _")
      print(" |\(                          .'  Y '>,")
      print("  \ \                        / _   _   )")
      print("   )))                       )(_) (_)(|}")
      print("    )\)                      {  4A   } /")
      print("     \)\                      (uLuJJ/)l")
      print("      (\)                     |3    p)/")
      print("       (\)___ __________      /nnm_n//")
      print("       c7___-__,__-)\,__)(""."  '\_>-<_/D'"'")
      print("       c7___-__,__-)\,__)(""."  '\_>-<_/D'"'")
      print("                       <<"'-._>__-,G_.___)\   \7)'"")
      print("                        ("'-.__.| ("<.__.-" I   \ )')
      return("Esqueleto",11,11,4,4,6,0,0,1,True,2,"Ataque Espada","Defesa Espada",0,0,0,0)
    if randomizar==9:
      print("Você ouvia risadas bizarras, seguindo-as, deparava-se com uma criança chorando de costas, ao tentar tocar-la, você notava o frio em seu corpo. Virando-a pelo ombro para ver seu rosto, você nota que ela não tem rosto. Suas suspeitas foram confirmadas, essa criança se trata de uma ilusão. O pseudo-corpo cai sem vida no chão, se esfarelando em milhares de grãos de poeira mágica, conforme você ouvia uma risada sádica típica de bruxas ao longe, você saca sua Espada e prepara-se para o combate, conforme o Inimigo se aproximava.")
      print("Bruxa:--Hihihi! Você caiu direitinho! Tinha que ver a sua cara! Bem que o Senhor Zarovich disse que você era um gatinho assustado!")
      return("Bruxa",20,20,10,10,4,3,1,2,True,4,"Transformação: Bruxa","Bola De Fogo",0,0,0,0)
     #lista de movimentos real, esses ai sao temporarios pq eu ainda n progrei os seguintes: "Transformação: Bruxa","Raio De Bruxa","Vida Falsa","Drenar Alma"
    if randomizar==10:
      print("Você ouvia o som de correntes se arrastando, vultos cruzavam sua linha de visão enquanto você caminhava, o vento ficava cada vez mais forte, você podia ouvir o som dos galhos das árvores se balançando, a Atmosfera fica mais densa, uma estranha névoa toma conta do lugar, a esse ponto, sua espada já estava sacada, você sabia bem o que estava por vir. Um Espectro aparecia!")
      print(" .-.")
      print("(o o) boo!")
      print("| O \     ")
      print(" \   \     ")
      print("  `~~~'")
      return("Espectro",14,14,3,3,3,4,0,-1,True,2.5,"Drenar Alma","Arranhar",0,0,True,"Perfurante Cortante Concussivo")
    if randomizar==11:
      print("Passos Estrondosos eram ouvidos ao longe, ao se aproximar, você sentia a terra tremer, uma criatura com braços largos devorava um Cervo, você podia ver sua boca ensanguentada cospir as tripas do cervo, enquanto arranca um dos ossos do animal para lutar contra você! Você encontrou um Troll!")
      return("Troll",20,20,5,5,3,4,5,0,0,3.5,"Arranhar","Mordida",0,0,False,"")
    #nome,hpmax,hp,mp,mpmax,ataqueF,ataqueM,defesa,defesaM,0,dificuldade,move1,move2,move3,move4,ataquesmagicos,imunidades
    
def GerarInimigo(inimigoselecionado=0,objplayer=0):
  a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q=GerarInimigo1(inimigoselecionado,objplayer)
  return obj_inimigo.objinimigo(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q)

def ConferirImunidade(inimigo,tipodano):
  a=str(type(inimigo))
  tipodano=str(tipodano)
  if a=="<class 'obj_inimigo.objinimigo'>":
    if tipodano in inimigo.imunidades:
      return True
    else:
      return False
  if a=="<class 'obj_personagem.objpersonagem'>":
    if tipodano in inimigo.imunidades:
      return True
    else:
      return False

def PedirAcao(usuario,flag=False):
  textoinputlinha1="Insira o número do movimento que deseja utilizar" 
  textoinput="Comandos Adicionais: 'AbrirMochila','Fugir'."
  if flag==True:
    textoinputlinha1=0
    textoinput="Insira o número do movimento que deseja utilizar."
  if usuario.movimento8==0 and usuario.movimento7==0 and usuario.movimento6==0 and usuario.movimento5==0 and usuario.movimento4==0 and usuario.movimento3==0 and usuario.movimento2==0:
    if flag==False:
      print("1-",usuario.movimento1)
    if textoinputlinha1!=0:
      print(textoinputlinha1)
    selecao=(input(textoinput))
    while selecao!="1" and selecao!='AbrirMochila' and selecao!='Fugir':
      selecao=(input(textoinput))
  elif usuario.movimento8==0 and usuario.movimento7==0 and usuario.movimento6==0 and usuario.movimento5==0 and usuario.movimento4==0 and usuario.movimento3==0:
    if flag==False:
      print("1-",usuario.movimento1)
      print("2-",usuario.movimento2)
    if textoinputlinha1!=0:
      print(textoinputlinha1)
    selecao=(input(textoinput))
    while selecao!="1" and selecao!="2" and selecao!='AbrirMochila' and selecao!='Fugir':
      if textoinputlinha1!=0:
        print(textoinputlinha1)
      selecao=(input(textoinput))
  elif usuario.movimento8==0 and usuario.movimento7==0 and usuario.movimento6==0 and usuario.movimento5==0 and usuario.movimento4==0:
    if flag==False:
      print("1-",usuario.movimento1)
      print("2-",usuario.movimento2)
      print("3-",usuario.movimento3)
    if textoinputlinha1!=0:
      print(textoinputlinha1)
    selecao=input(input(textoinput))
    while selecao!="1" and selecao!="2" and selecao!="3" and selecao!='AbrirMochila' and selecao!='Fugir':
      if textoinputlinha1!=0:
        print(textoinputlinha1)
      selecao=(input(textoinput))
  elif usuario.movimento8==0 and usuario.movimento7==0 and usuario.movimento6==0 and usuario.movimento5==0:
    if flag==False:
      print("1-",usuario.movimento1)
      print("2-",usuario.movimento2)
      print("3-",usuario.movimento3)
      print("4-",usuario.movimento4)
    if textoinputlinha1!=0:
      print(textoinputlinha1)
    selecao=(input(textoinput))
    while selecao!="1" and selecao!="2" and selecao!="3" and selecao!="4" and selecao!='AbrirMochila' and selecao!='Fugir':
      if textoinputlinha1!=0:
        print(textoinputlinha1)
      selecao=(input(textoinput))
  elif usuario.movimento8==0 and usuario.movimento7==0 and usuario.movimento6==0:
    if flag==False:
      print("1-",usuario.movimento1)
      print("2-",usuario.movimento2)
      print("3-",usuario.movimento3)
      print("4-",usuario.movimento4)
      print("5-",usuario.movimento5)
    if textoinputlinha1!=0:
      print(textoinputlinha1)
    selecao=input(textoinput)
    while selecao!="1" and selecao!="2" and selecao!="3" and selecao!="4" and selecao!="5" and selecao!='AbrirMochila' and selecao!='Fugir':
      if textoinputlinha1!=0:
        print(textoinputlinha1)
      selecao=(input(textoinput))
  elif usuario.movimento8==0 and usuario.movimento7==0:
    if flag==False:
      print("1-",usuario.movimento1)
      print("2-",usuario.movimento2)
      print("3-",usuario.movimento3)
      print("4-",usuario.movimento4)
      print("5-",usuario.movimento5)
      print("6-",usuario.movimento6)
    if textoinputlinha1!=0:
      print(textoinputlinha1)
    selecao=(input(textoinput))
    while selecao!="1" and selecao!="2" and selecao!="3" and selecao!="4" and selecao!="5" and selecao!="6" and selecao!='AbrirMochila' and selecao!='Fugir':
      if textoinputlinha1!=0:
        print(textoinputlinha1)
      selecao=(input(textoinput))
  elif usuario.movimento8==0:
    if flag==False:
      print("1-",usuario.movimento1)
      print("2-",usuario.movimento2)
      print("3-",usuario.movimento3)
      print("4-",usuario.movimento4)
      print("5-",usuario.movimento5)
      print("6-",usuario.movimento6)
      print("7-",usuario.movimento7)
    if textoinputlinha1!=0:
      print(textoinputlinha1)
    selecao=(input(textoinput))
    while selecao!="1" and selecao!="2" and selecao!="3" and selecao!="4" and selecao!="5" and selecao!="6" and selecao!="7" and selecao!='AbrirMochila' and selecao!='Fugir':
      if textoinputlinha1!=0:
        print(textoinputlinha1)
      selecao=(input(textoinput))
  else:
    if flag==False:
      print("1-",usuario.movimento1)
      print("2-",usuario.movimento2)
      print("3-",usuario.movimento3)
      print("4-",usuario.movimento4)
      print("5-",usuario.movimento5)
      print("6-",usuario.movimento6)
      print("7-",usuario.movimento7)
      print("8-",usuario.movimento8)
    if textoinputlinha1!=0:
      print(textoinputlinha1)
    selecao=(input(textoinput))
    while selecao!="1" and selecao!="2" and selecao!="3" and selecao!="4" and selecao!="5" and selecao!="6" and selecao!="7" and selecao!="8" and selecao!='AbrirMochila' and selecao!='Fugir':
      if textoinputlinha1!=0:
        print(textoinputlinha1)
      selecao=(input(textoinput))
  if selecao=='1':
    return usuario.movimento1
  if selecao=='2':
    return usuario.movimento2
  if selecao=='3':
    return usuario.movimento3
  if selecao=='4':
    return usuario.movimento4
  if selecao=='5':
    return usuario.movimento5
  if selecao=='6':
    return usuario.movimento6
  if selecao=='7':
    return usuario.movimento7
  if selecao=='8':
    return usuario.movimento8
  if selecao=='AbrirMochila':
    return 'AbrirMochila'
  if selecao=="Fugir":
    return "Fugir"
  
def RealizarAcao(usuario,acao,alvo1=0,alvo2=0,alvo3=0,alvo4=0,player=0):
  if acao=="AbrirMochila":
    cls()
    obj_inventario.GerenciarInventario(usuario)
  if acao=="Facada":
    acoes.Facada(usuario,alvo1)
  if acao=="Arranhar":
    acoes.Arranhar(usuario,alvo1)
  if acao=="Ataque Espada":
    acoes.Ataque_Espada(usuario,alvo1)
  if acao=="Mordida":
    acoes.Mordida(usuario,alvo1)
  if acao=="Fúria Do Nanico":
    acoes.Furia_Do_Nanico(usuario,alvo1)
  if acao=="Bola De Fogo":
    acoes.Bola_De_Fogo(usuario,alvo1,alvo2,alvo3,alvo4)
  if acao=="Surto De Ação":
    acoes.Surto_De_Acao(usuario,alvo1,alvo2,alvo3,alvo4)
  if acao=="Dança Das Lâminas":
    a,b,c,d,e=acoes.Danca_Das_Laminas(usuario,alvo1)
    return a,b,c,d,e
  if acao=="Defesa Espada":
    acoes.Defesa_Espada(usuario)
  if acao=="Frenesi":
    acoes.Frenesi(usuario,alvo1,alvo2,alvo3,alvo4)
  if acao=="Sangue-Suga":
    acoes.Sangue_Suga(usuario,alvo1)
  if acao=="Transformação: Bruxa":
    acoes.Transformacao_Bruxa(usuario,player)
  if acao=="Transformar Lobisomem":
    acoes.Transformar_Lobisomem(usuario,alvo1)
  if acao=="Golpe Espiral":
    acoes.Golpe_Espiral(usuario,alvo1,alvo2,alvo3,alvo4)
  if acao=="Arma Elemental":
    acoes.ArmaElemental(usuario)
  if acao=="Fugir":
    acoes.Fugir(usuario,alvo1,alvo2,alvo3,alvo4)

def PedirAlvo(usuario,alvo1=0,alvo2=0,alvo3=0,alvo4=0):
  texto="Digite o número do seu alvo:"
  a1,a2,a3,a4=False,False,False,False
  if alvo2==0 and alvo3==0 and alvo4==0:
    #print("Inimigos: 1-",alvo1.nome)
    a1=True
  elif alvo3==0 and alvo4==0:
    #print("Inimigos: 1-",alvo1.nome," 2-",alvo2.nome)
    a1,a2=True,True
  elif alvo4==0:
    #print("Inimigos: 1-",alvo1.nome," 2-",alvo2.nome," 3-",alvo3.nome)
    a1,a2,a3=True,True,True
  else:
    #print("Inimigos: 1-",alvo1.nome," 2-",alvo2.nome," 3-",alvo3.nome," 4-",alvo4.nome)
    a1,a2,a3,a4=True,True,True,True
  if usuario.nome=="Espada Voadora":
    texto="Digite o número do alvo da espada voadora:"
  target=(input(texto))
  if target!="1" and target!="2" and target!="3" and target!="4":
    target="1"
  while ((target=="1" and a1==False)or(target=="2" and a2==False)or(target=="3" and a3==False)or(target=="4" and a4==False)):
    target=(input("Digite o número do seu alvo:"))   
  if (alvo4==0 or alvo4.nome==0 or alvo4.nome=="0")and target=='4':
    target='1'
  if (alvo3==0 or alvo3.nome==0 or alvo3.nome=="0") and target=='3':
    target='1'
  if (alvo2==0 or alvo2.nome==0 or alvo2.nome=="0") and target=='2':
    target='1'
  if target=='1':
    return alvo1
  if target=='2':
    return alvo2
  if target=='3':
    return alvo3
  if target=='4':
    return alvo4

def randomizar_executar_acao_inimigo(Inimigo,player):
  randmax=4
  if Inimigo.movimento4==0:
    randmax=randmax-1
  if Inimigo.movimento3==0:
    randmax=randmax-1
  if Inimigo.movimento2==0:
    randmax=randmax-1
  randomizer=random.randint(1,randmax)
  if randomizer==4:
    acao=Inimigo.movimento4
  if randomizer==3:
    acao=Inimigo.movimento3
  if randomizer==2:
    acao=Inimigo.movimento2
  if randomizer==1:
    acao=Inimigo.movimento1
  if acao=="Arranhar":
    acoes.Arranhar(Inimigo,player)
  if acao=="Mordida":
    acoes.Mordida(Inimigo,player)
  if acao=="Facada":
    acoes.Facada(Inimigo,player)
  if acao=="Ataque Espada":
    acoes.Ataque_Espada(Inimigo,player)
  if acao=="Fúria Do Nanico":
    acoes.Furia_Do_Nanico(Inimigo,player)
  if acao=="Bola De Fogo":
    acoes.Bola_De_Fogo(Inimigo,player)
  if acao=="Surto De Ação":
    acoes.Surto_De_Acao(Inimigo,0,0,0,0,False,player)
  if acao=="Frenesi":
    acoes.Frenesi(Inimigo,0,0,0,0,player)
  if acao=="Sangue-Suga":
    acoes.Sangue_Suga(Inimigo,player)
  if acao=="Transformar Lobisomem":
    acoes.Transformar_Lobisomem(Inimigo,player)
  if acao=="Transformação: Bruxa":
    acoes.Transformacao_Bruxa(Inimigo,player)

def combate_random_melhorado(player,qntinimigos=0,inimigo1=0,inimigo2=0,inimigo3=0,inimigo4=0):
  obj_personagem.resetarValores(player)
  ArmazenarPlayer=retonarplayer(player)
  Inimigo1=obj_inimigo.objinimigo()
  Inimigo2=obj_inimigo.objinimigo()
  Inimigo3=obj_inimigo.objinimigo()
  Inimigo4=obj_inimigo.objinimigo()
  EspadaVoadora=obj_adicionais.EspadaVoadora("",0,0,0,0)
  if qntinimigos==0:
    qntinimigos=random.randint(1,4)
  if qntinimigos>0:
    Inimigo1=GerarInimigo(inimigo1)
  if qntinimigos>1:
    Inimigo2=GerarInimigo(inimigo2)
  if qntinimigos>2:
    Inimigo3=GerarInimigo(inimigo3)
  if qntinimigos>3:
    Inimigo4=GerarInimigo(inimigo4)
  cls()
  if qntinimigos==1:
    Inimigo1=GerarInimigo(inimigo1)
  else:
    print("Você foi emboscado por Inimigos!")
  while Inimigo1.HP>0 or Inimigo2.HP>0 or Inimigo3.HP>0 or Inimigo4.HP>4:
    cls()
    obj_personagem.verificarHP(player)
    print("===========================")
    print("HP:",int(player.HP),"/",int(player.HPMax))
    print("MP:",int(player.MP),"/",int(player.MPMax))
    print("===========================")
    if qntinimigos==1:
      print(f"Inimigos: 1-{Inimigo1.nome}(HP:{Inimigo1.HP})")
    if qntinimigos==2:
      print(f"Inimigos: 1-{Inimigo1.nome}(HP:{Inimigo1.HP}) 2-{Inimigo2.nome}(HP:{Inimigo2.HP})")
    if qntinimigos==3:
      print(f"Inimigos: 1-{Inimigo1.nome}(HP:{Inimigo1.HP}) 2-{Inimigo2.nome}(HP:{Inimigo2.HP}) 3-{Inimigo3.nome}(HP:{Inimigo3.HP})")
    if qntinimigos==4:
      print(f"Inimigos: 1-{Inimigo1.nome}(HP:{Inimigo1.HP}) 2-{Inimigo2.nome}(HP:{Inimigo2.HP}) 3-{Inimigo3.nome}(HP:{Inimigo3.HP}) 4-{Inimigo4.nome}(HP:{Inimigo4.HP})")
    acao=PedirAcao(player)
    if acao=="Facada" or acao=="Fúria Do Nanico" or acao=="Ataque Espada" or acao=="Mordida" or acao=="Arranhar":
      alvo=PedirAlvo(player,Inimigo1,Inimigo2,Inimigo3,Inimigo4)
      RealizarAcao(player,acao,alvo)
    elif acao=="Dança Das Lâminas":
      alvo=PedirAlvo(player,Inimigo1,Inimigo2,Inimigo3,Inimigo4)
      a,b,c,d,e=(RealizarAcao(player,acao,alvo))
      EspadaVoadora=obj_adicionais.EspadaVoadora(a,b,c,d,e)
    else:
      RealizarAcao(player,acao,Inimigo1,Inimigo2,Inimigo3,Inimigo4,player)
    if EspadaVoadora.nome!="":
      obj_adicionais.randomizar_executar_acao_espada(EspadaVoadora,Inimigo1,Inimigo2,Inimigo3,Inimigo4)
    if Inimigo1.HP>0:
      randomizar_executar_acao_inimigo(Inimigo1,player)
    if Inimigo2.HP>0:
      randomizar_executar_acao_inimigo(Inimigo2,player)
    if Inimigo3.HP>0:
      randomizar_executar_acao_inimigo(Inimigo3,player)
    if Inimigo4.HP>0:
      randomizar_executar_acao_inimigo(Inimigo4,player)
    if (Inimigo1.nome=="Bruxa" or Inimigo1.nome=="Troll"):
      if Inimigo1.nome=="Bruxa" and Inimigo1.HP<Inimigo1.HPMax and Inimigo1.MP<Inimigo1.MPMax:
        print(Inimigo1.nome,"absorvia a energia do ambiente para se regenerar e recuperar sua magia!")
        if Inimigo1.HP>0:
          Inimigo1.HP=Inimigo1.HP+1
          Inimigo1.MP=Inimigo1.MP+1
      if Inimigo1.nome=="Troll" and Inimigo1.HP<Inimigo1.HPMax:
        if Inimigo1.regenerar==True:
          print("O Troll se regenerava ao fim do turno...")
          if Inimigo1.HP>0:
            Inimigo1.HP=Inimigo1.HP+2
            obj_inimigo.verificarHP(Inimigo1)
        else:
          Inimigo1.regenerar=True
    if (Inimigo2.nome=="Bruxa"or Inimigo2.nome=="Troll"):
      if Inimigo2.nome=="Bruxa" and Inimigo2.HP<Inimigo2.HPMax and Inimigo2.MP<Inimigo2.MPMax:
        print(Inimigo2.nome,"absorvia a energia do ambiente para se regenerar e recuperar sua magia!")
        if Inimigo2.HP>0:
          Inimigo2.HP=Inimigo2.HP+1
          Inimigo2.MP=Inimigo2.MP+1
      if Inimigo2.nome=="Troll" and Inimigo2.HP>Inimigo2.HPMax:
        if Inimigo2.regenerar==True:
            print("O Troll se regenerava ao fim do turno...")
            if Inimigo2.HP>0:
              Inimigo2.HP=Inimigo2.HP+2
              obj_inimigo.verificarHP(Inimigo2)
        else:
          Inimigo2.regenerar=True
    if (Inimigo3.nome=="Bruxa" or Inimigo3.nome=="Troll"):
      if Inimigo3.nome=="Bruxa" and (Inimigo3.HP<Inimigo3.HPMax and Inimigo3.MP<Inimigo3.MPMax):
        print(Inimigo3.nome,"absorvia a energia do ambiente para se regenerar e recuperar sua magia!")
        if Inimigo3.HP>0:
          Inimigo3.HP=Inimigo3.HP+1
          Inimigo3.MP=Inimigo3.MP+1
      if Inimigo3.nome=="Troll" and Inimigo3.HP<Inimigo3.HPMax:
        if Inimigo3.regenerar==True:
          print("O Troll se regenerava ao fim do turno...")
          if Inimigo3.HP>0:
            Inimigo3.HP=Inimigo3.HP+2
            obj_inimigo.verificarHP(Inimigo3)
        else:
          Inimigo3.regenerar=True
    if (Inimigo4.nome=="Bruxa" or Inimigo4.nome=="Troll"):
      if Inimigo4.nome=="Bruxa" and Inimigo4.HP<Inimigo4.HPMax and Inimigo4.MP<Inimigo4.MPMax:
        print(Inimigo4.nome,"absorvia a energia do ambiente para se regenerar e recuperar sua magia!")
        if Inimigo4.HP>0:
          Inimigo4.HP=Inimigo4.HP+1
          Inimigo4.MP=Inimigo4.MP+1
      if Inimigo4.nome=="Troll" and Inimigo4.HP<Inimigo4.HPMax:
        if Inimigo4.regenerar==True:
          print("O Troll se regenerava ao fim do turno...")
          if Inimigo4.HP>0:
            Inimigo4.HP=Inimigo4.HP+2
            obj_inimigo.verificarHP(Inimigo4)
        else:
          Inimigo4.regenerar=True
    input("ENTER")
    if player.HP==0:
      break
  if EspadaVoadora.nome!="":
    print("A espada voadora lentamente desaparecia no ar...")
  if player.HP>0:
    exprecebido=(Inimigo1.dificuldade+Inimigo2.dificuldade+Inimigo3.dificuldade+Inimigo4.dificuldade)*50
    print("Fim de Combate! Você recebeu",exprecebido,"pontos de EXP")
    player.expplayer=int(player.expplayer+exprecebido)
    print("EXP atual:",player.expplayer)
  playerhp=player.HP
  playermp=player.MP
  playerexp=player.expplayer
  
  ArmazenarPlayer.HP=player.HP
  ArmazenarPlayer.MP=player.MP
  ArmazenarPlayer.expplayer=player.expplayer
  player=retonarplayer(ArmazenarPlayer)


def encontro_aleatorio(player,qntinimigos=0,Inimigo1=0,Inimigo2=0,Inimigo3=0,Inimigo4=0):
  rand=random.randint(1,30)
  if rand>=1 and rand<=15 or qntinimigos==1:
    qntinimigos=1
    playerhp,playermp,playerexp=combate_random_melhorado(player,qntinimigos,Inimigo1)
  elif rand>=16 and rand<=23 or qntinimigos==2:
    qntinimigos=2
    playerhp,playermp,playerexp=combate_random_melhorado(player,qntinimigos,Inimigo1,Inimigo2)
  elif rand>=24 and rand<=27 or qntinimigos==3:
    qntinimigos=3
    playerhp,playermp,playerexp=combate_random_melhorado(player,qntinimigos,Inimigo1,Inimigo2,Inimigo3)
  elif rand>=28 and rand<=30 or qntinimigos==4:
    qntinimigos=4
    playerhp,playermp,playerexp=combate_random_melhorado(player,qntinimigos,Inimigo1,Inimigo2,Inimigo3,Inimigo4)


def retonarplayer(player):
  objeto=obj_personagem.objpersonagem(player.nome,player.HP,player.MP,player.HPMax,player.MPMax,player.FOR,player.DES,player.CON,player.INT,player.SAB,player.CAR,player.DanoArma,player.ataquesmagicos,player.Defesa,player.DefesaMagica,player.imunidades,player.expplayer,player.explevelup,player.levelplayer,player.DanoFoco,player.armaelementalativa,player.dinheiro,player.grimorio,player.livrogolpes,player.mochila,player.tipoarmadura,player.tipoarma,player.tipoanel,player.tipoescudo,player.movimento1,player.movimento2,player.movimento3,player.movimento4,player.movimento5,player.movimento6,player.movimento7,player.movimento8,player.armaelementaltipodano)
  return objeto

def Comercio(player,comerciante=0):
    if comerciante=0:
        comerciante="Padrão"
    #Tipos de Comerciante:
    if comerciante=="Padrão":
        mercadorias=RandomizarMercadorias("Padrão")
        while True:
            MostrarMercadorias(mercadorias)
            RealizarCompraOuFecharLoja(player,mercadorias)
    if comerciante=="Mercador Aventureiro":
        mercadorias=RandomizarMercadorias("Mercador Aventureiro")
        while True:
            MostrarMercadorias(mercadorias)
            RealizarCompraOuFecharLoja(player,mercadorias)
    if comerciante=="Mercador Mago":
        mercadorias=RandomizarMercadorias("Mercador Mago")
        while True:
            MostrarMercadorias(mercadorias)
            RealizarCompraOuFecharLoja(player,mercadorias)
    if comerciante=="Goblin Mercador":
        mercadorias=RandomizarMercadorias("Goblin Mercador")
        while True:
            MostrarMercadorias(mercadorias)
            RealizarCompraOuFecharLoja(player,mercadorias)
    if comerciante=="Pequeno Mascate":
        mercadorias=RandomizarMercadorias("Pequeno Mascate")
        while True:
            MostrarMercadorias(mercadorias)
            RealizarCompraOuFecharLoja(player,mercadorias)


def RandomizarMercadorias(comerciante):
    if comerciante=="Padrão":
        randomizar=random.randint(1,4)
        if randomizar==1:
            mercadorias=["Poção de HP","Poção De HP","Machado"]
        if randomizar==2:
            mercadorias=["Espada Curta","Picareta","Poção de HP"]
        if randomizar==3:
            mercadorias=["Poção de MP","Conjunto De Dados","Sobre-Tudo"]
        if randomizar==4:
            mercadorias=["Robes Desgastadas","Poção de MP","Cajado"]

    if comerciante=="Mercador Aventureiro":
        randomizar=random.randint(1,4)
        if randomizar==1:
            mercadorias=["Espada Larga","Cota De Malha","Varinha De Visco"]
        if randomizar==2:
            mercadorias=["Bolsa De Runas","Rapieira","Arco"]
        if randomizar==3:
            mercadorias=["Espada Longa","Espada Larga","Espada Curta"]
        if randomizar==4:
            mercadorias=["Besta","Adaga","Adagas Gêmeas"]

    if comerciante=="Mercador Mago":
        randomizar=random.randint(1,4)
        if randomizar==1:
            mercadorias=["Cajado","Sobre-Tudo","Varinha De Teixo"]
        if randomizar==2:
            mercadorias=["Robes Desgastadas","Bolsa De Runas","Varinha De Visco"]
        if randomizar==3:
            mercadorias=["Cajado Sagrado","Armadura De Couro","Varinha De Teixo"]
        if randomizar==4:
            mercadorias=["Varinha De Visco","Espada Dos Magos","Robes Desgastadas"]

    if comerciante=="Goblin Mercador":
        randomizar=random.randint(1,4)
        if randomizar==1:
            mercadorias=["Adaga","Pérola","Corda"]
        if randomizar==2:
            mercadorias=["Espada Curta","Diamante","Poção De HP"]
        if randomizar==3:
            mercadorias=["Adaga","Rapieira","Diamante"]
        if randomizar==4:
            mercadorias=["Adagas Gêmeas","Sobre-Tudo","Robes Desgastadas"]
#lista de itens:
#"Diamante","Rapieira","Armadura De Couro","Pérola","Espada Longa","Camisão De Malha","Diamante","Pérola","Espada Longa","Esmeralda","Barra De Ferro","Espada Dos Magos"
    if comerciante=="Pequeno Mascate":
        randomizar=random.randint(1,4)
        if randomizar==1:
            mercadorias=["Diamante","Rapieira","Armadura De Couro"]
        if randomizar==2:
            mercadorias=["Pérola","Espada Longa","Camisão De Malha"]
        if randomizar==3:
            mercadorias=["Diamante","Pérola","Espada Longa"]
        if randomizar==4:
            mercadorias=["Esmeralda","Barra De Ferro","Espada Dos Magos"]
    return mercadorias

def MostrarMercadorias(mercadorias,comerciante):
    if comerciante=="Padrão":
        print("O Logista então mostrava seus pertences...")
    if comerciante=="Mercador Aventureiro":
        print("O Aventureiro então mostrava-lhe sua mochila...")
    if comerciante=="Mercador Mago":
        print("O Mago então lhe mostrava o que levava consigo...")
    if comerciante=="Goblin Mercador":
        print("O Goblin saltitava de felicidade, excitado para vender seus produtos, lhe mostrava o que carregava.")
    if comerciante=="Pequeno Mascate":
        print("O Pequeno Mascate Observava silenciosamente você, que analisava suas mercadorias.")
    print("======MERCADORIAS======")
    if len(mercadorias)>=1:
        print("1-",mercadorias[0])
    if len(mercadorias)>=2:
        print("2-",mercadorias[1])
    if len(mercadorias)>=3:
        print("3-",mercadorias[2])
    print("=======================")

def RealizarCompraOuFecharLoja(player,mercadorias):
    teclado=input("Digite o Número da mercadoria selecionada, ou aperte ENTER para sair da loja.")
    while teclado!="" and teclado!=str(len(mercadorias)) and teclado!=str(len(mercadorias)-1) and teclado!=str(len(mercadorias-2)):
        teclado=input("Digite o Número da mercadoria selecionada, ou aperte ENTER para sair da loja.")
    if teclado=="1":
        mercadoriaselecionada=mercadorias[0]
    elif teclado=="2":
        mercadoriaselecionada=mercadorias[1]
    elif teclado=="3":
        mercadoriaselecionada=mercadorias[2]
    elif teclado!="":
        RealizarCompraOuFecharLoja(player,mercadorias)
    if mercadoriaselecionada=="Diamante":
        preco=500
    if mercadoriaselecionada=="":
    if mercadoriaselecionada=="":
    if mercadoriaselecionada=="":
    if mercadoriaselecionada=="":
    if mercadoriaselecionada=="":
    if mercadoriaselecionada=="":
    if mercadoriaselecionada=="":
    if mercadoriaselecionada=="": #Pelo amor d deus seta o preço desses itens comentados aí, vai.
    if mercadoriaselecionada=="":
    if mercadoriaselecionada=="":
    if mercadoriaselecionada=="":
    if mercadoriaselecionada=="":
    if mercadoriaselecionada=="":
#Diamante Rapieira Armadura De Couro Pérola Espada Longa
#Camisão De Malha Esmeralda Barra De Ferro Espada Dos Magos 
#Adagas Gêmeas Sobre-Tudo Robes Desgastadas Adaga Espada Curta 
#Corda Varinha De Visco Cajado Sagrado Varinha De Teixo Bolsa De Runas 
#Cajado Besta Espada Larga Arco Cota De Malha Poção De MP Conjunto De Dados Picareta Poção De HP, Machado


#arquivo com funções que servem para fazer Tudo no RPG que não envolva Cidades,Dungeons,Movimentos,História, Quests,ou Comércio

