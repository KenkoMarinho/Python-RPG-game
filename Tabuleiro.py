import os
import random
from funcoesrpg import *
import obj_inventario
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

def Controlador(tabuleiro,player):
    Teclado=input("Insira W/A/S/D ou digite 'Mochila' para abrir seu inventário.")
    Teclado=Teclado.upper()
    while Teclado!="W" and Teclado!="A" and Teclado!="S" and Teclado!="D" and Teclado!="MOCHILA":
        Teclado=input("Insira W/A/S/D ou digite 'Mochila' para abrir seu inventário.")
        Teclado=Teclado.upper()
    if Teclado=="W":
        MoverNorte(tabuleiro)
    if Teclado=="S":
        MoverSul(tabuleiro)
    if Teclado=="D":
        MoverLeste(tabuleiro)
    if Teclado=="A":
        MoverOeste(tabuleiro)
    if Teclado=="MOCHILA":
        obj_inventario.GerenciarInventario(player)

def GerarObstaculosNaturais(tabuleiro):
  for i in range (len(tabuleiro)):
    randomizar=random.randint(1,8)
    if randomizar==2:
      tabuleiro[i][0],tabuleiro[i][2],tabuleiro[i][3],tabuleiro[i][4],tabuleiro[i][7],tabuleiro[i][9]="#","#","#","#","#","#"
    if randomizar==3:
      tabuleiro[i][5],tabuleiro[i][6],tabuleiro[i][10],tabuleiro[i][14]="#","#","#","#"
    if randomizar==4:
      tabuleiro[i][2],tabuleiro[i][7],tabuleiro[i][8],tabuleiro[i][10],tabuleiro[i][13]="#","#","#","#","#"
    if randomizar==5:
      tabuleiro[i][1],tabuleiro[i][2],tabuleiro[i][9]="#","#","#"
    if randomizar==6:
      tabuleiro[i][4],tabuleiro[i][8],tabuleiro[i][13]="#","#","#"
    if randomizar==7:
      tabuleiro[i][2],tabuleiro[i][4],tabuleiro[i][10],tabuleiro[i][11]="#","#","#","#",
    if randomizar==8:
      tabuleiro[i][0],tabuleiro[i][7],tabuleiro[i][9],tabuleiro[i][13],tabuleiro[i][14]="#","#","#","#","#"
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

def EventoViajante(player):  #FAZ ESSAS PORRAS AÍ NAMORAL TO CANSADÃO
    print("AINDA A SER FEITO")

def EventoTesouro(player):
  rand=random.randint(1,3)  
  if rand<3: #Baú Benigno
    print("Seguindo seu caminho por ruínas, florestas, e masmorras, eventualmente você dava de cara")
    print("com um baú fechado, você podia perceber sua fechadura quebrada, pronto para ser aberto.")
    teclado=input("Deseja Abrir? Sim/Não")
    teclado=teclado.upper()
    while teclado!="SIM" and teclado!="NÃO":
      teclado=input("Deseja Abrir? Sim/Não")
      teclado=teclado.upper()
    if teclado=="SIM":
      recompensas=["Espada Larga","Espada Curta","Adagas Gêmeas","Cajado","Rapieira","Cajado Sagrado","Sobre-Tudo","Camisão de Malha","Cota de Malha","Armadura de Couro","Robes Desgastadas","Espada Dos Magos","Bolsa De Runas","Espada Longa","Varinha De Teixo","Varinha De Visco"]
      recompensasdinheiro=random.randint(5,40)
      indexrecompensa=random.randint(0,(len(recompensas)-1))
      recompensafinal=recompensas[indexrecompensa]
      print("Você abria o baú, e dentro dele você encontrava...")
      print(recompensasdinheiro,"Moedas de Ouro")
      print(recompensafinal)
      input("ENTER")
      player.dinheiro+=recompensasdinheiro
      obj_inventario.AdicionarItem(player,recompensafinal)
      cls()
  if rand==3: #Bau Mimico
    print("Seguindo seu caminho por ruínas, florestas, e masmorras, eventualmente você dava de cara")
    print("com um baú fechado, você podia perceber sua fechadura quebrada, pronto para ser aberto.")
    teclado=input("Deseja Abrir? Sim/Não")
    teclado=teclado.upper()
    while teclado!="SIM" and teclado!="NÃO":
      teclado=input("Deseja Abrir? Sim/Não")
      teclado=teclado.upper()
    if teclado=="SIM":
      print("Assim que você encostava na tranca do baú para abrir-lo, o mesmo se abria bruscamente, tentando")
      print("Devorar sua mão!, você conseguia rapidamente repelir o ataque, e saltar para trás, se preparando")
      print("para o combate.")
      input("ENTER")
      cls()
      combate_random_melhorado(player,1,"Mímico")
      if player.HP>0:
        print("Entre os destroços do baú, você encontrava alguns trocados.")
        moedas=random.randint(7,15)
        print("Você encontrou",moedas,"moedas de ouro.")
        player.dinheiro+=moedas

def EventoDescanso(player):
    if random.randint(1,2)==1: #evento positivo
      randomizar=random.randint(1,3)
      if randomizar==1:
        print("Você encontrava uma bela árvore, debaixo da qual você conseguia descansar")
        Teclado=input("Você deseja descansar sob ela? Sim/Não")
        Teclado=Teclado.upper()
        while Teclado!="SIM" and Teclado!="NÃO":
          Teclado=input("Você deseja descansar sob ela? Sim/Não")
          Teclado=Teclado.upper()
        Teclado=Teclado.upper()
        if Teclado=="SIM":
          print("Você acabava por adormecer sob a arvore...")
          input("ENTER")
          cls()
          print("Você tinha um ótimo sonho, onde fadas e duendes lhe traziam comidas de todo o tipo")
          print("Você acordava, bem descansado e pronto para seguir viagem.")
          input("ENTER")
          cls()
          player.HP+=int(player.HP/6)
          player.MP+=int(player.MP/8)
          if player.HP>player.HPMax:
            player.HP=player.HPMax
          if player.MP>player.MPMax:
            player.MP=player.MPMax
      if randomizar==2:
        print("Depois de cruzar ruínas, masmorras e florestas, você dava de cara com em uma clareira")
        print("Chegava a um doce chalé reconfortante, você podia ver uma doce velhinha varrendo as folhas de frente da sua casa")
        print("Idosa: --Oh! saudações meu jovem, eu não esperava por visitas hoje...")
        print("A idosa vestia roupas camponesas dos pés a cabeça mantinha um doce e gentil olhar enquanto falava contigo.")
        print("Idosa:--Está perdido? Não tem onde dormir? Se quiser pode passar a noite aqui.")
        Teclado=input("Sim/Não")
        while Teclado.upper()!="SIM" and Teclado.upper!="NÃO":
          Teclado=input("Sim/Não")
        Teclado=Teclado.upper()
        cls()
        if Teclado=="SIM":
          print(f"{player.nome}--Obrigado, estou perdido há dias, exausto, vagando por essas terras infestadas de monstros")
          print("Era bom ver um rosto amigo pra variar, você se sentava ao lado da velha por horas na varanda.")
          if random.randint(1,4)==4 and player.grimorio.transformacaobruxa==False:
            print("A mulher revela, dentre várias histórias, uma de muito tempo atrás, quando ela conhecera uma bruxa boa")
            print("Uma bruxa que buscava fazer o bem, apesar de sua natureza horrenda")
            print("Ela lhe ensinara um feitiço, que permitia que a idosa assumisse a forma de bruxa quando estiver em perigo.")
            print("A idosa lhe mostrava um grimório dessa magia, e perguntava se você deseja ler.")
            print("Após ler o livro, você aprendia com sucesso a magia 'Transformação: Bruxa'")
            player.grimorio.transformacaobruxa=True
          else:
            print("Você caía no sono depois de conversar várias horas com a idosa, descansando no curral aos fundos da cabana")
            print("Você acordava no outro dia, bem melhor para seguir viagem.")
          player.HP+=int(player.HP/8)
          player.MP+=int(player.MP/7)
          if player.HP>player.HPMax:
            player.HP=player.HPMax
          if player.MP>player.MPMax:
            player.MP=player.MPMax
        else:
          print(f"{player.nome}--Não estou perdido. Vou seguir meu caminho agora. Adeus.")
          print("Com essas palavras você voltava para dentro do mato, se despedindo da idosa, que apenas o observava sumir entre a folheagem.")
      if randomizar==3:
        print("Após explorar as ruínas do local, você podia ver um cão latindo pra você, assim que o mesmo")
        print("captara sua atenção, ele corria para entre os prédios abandonados do local")
        Teclado=input("Seguir ele? Sim/Não")
        while Teclado.upper!=("SIM") and Teclado.upper()!="NÃO":
          Teclado=input("Seguir ele? Sim/Não")
        Teclado=Teclado.upper()
        cls()
        if Teclado=="SIM":
          print("Você conduzia o pobre cão por dentro das ruínas, ele o guiava até o porão de uma casa antiga")
          print("Você podia ver o piso do primeiro andar da casa (teto do porão) completamente arregaçado")
          print("Também via um homem entre os destroços, completamente ensanguentado.")
          print("Homem:--Malditos... Trolls...")
          print("Após dizer isso, o homem apagava completamente.")
          Teclado=input("Tratar suas feridas? Sim/Não")
          Teclado=Teclado.upper()
          while Teclado!="SIM" and Teclado!="NÃO":
            Teclado=input("Tratar suas feridas? Sim/Não")
            cls()
            Teclado=Teclado.upper()
          if Teclado=="SIM":
            print("Você tratava os ferimentos do homem...")
            if random.randint(3,4)<4:
              print("Você ouvia passos altos, aparentemente, o Troll de mais cedo retornou pra buscar seu jantar.")
              print("Subitamente o teto da cabana se rompe, e um Troll de três metros de altura aparece no porão.")
              print("Você desembainhava sua(o)",player.tipoarma,"para defender o homem")
              combate_random_melhorado(player,1,"Troll")
              flagtroll=True
            if player.HP>0:
              cls()
              print("Você heroicamente derrotava o Troll, salvando o pobre homem.")
              print("Após embainhar sua arma, Sentava-se ao lado do homem novamente")
              input("ENTER")
              cls()
              print("As horas se passavam, eventualmente as feridas do homem melhoravam, e ele acordava.")
              print("Ele se curva, lhe agradecendo por salvar sua vida. E então ele lhe entrega uma recompensa.")
              recompensa=50+random.randint(1,20)
              print("O homem lhe entregava",recompensa,"moedas de ouro e uma poção de HP.")
              player.mochila.pocoeshp+=1
              player.dinheiro+=recompensa
              print("Homem:--Desculpe... Sei que não é muito, mas é tudo que eu tenho...")
              print(f"{player.nome}--Já recebi recompensas piores de fazendeiros aos quais eu de fato prestei algum serviço.")
              print(f"{player.nome}--Não se preocupe com dinheiro, em vez disso, pense em como chegar em casa.")
              print("Então você se despedia do homem e do cão, e voltava a seguir sua viagem.")
              if random.randint(1,3)==3 and player.grimorio.transformacarlobisomem==False and flagtroll:
                print("Na saída dali, você tropeçava em um grimório.")
                print("'Transformação: Lobisomem'")
                print("Ao passo que você lia o grimório, e copiava seu feitiço, o mesmo se desmaterializava.")
                player.grimorio.transformacarlobisomem=True
                print(f"{player.nome}--Até que compensa fazer boas ações, pra variar.")
          else:
            print("Você virava as costas e ia embora, mesmo com o cão chorando pela vida de seu dono.")
        else:
          print("Você virava suas costas para o cão, e voltava a seguir seu caminho para fora das ruínas.")
    else: #evento negativo
      randomizar=random.randint(1,3)
      if randomizar==1:
        print("Você encontrava uma bela árvore, debaixo da qual você conseguia descansar")
        Teclado=input("Você deseja descansar sob ela? Sim/Não")
        Teclado=Teclado.upper()
        while Teclado!="SIM" and Teclado!="NÃO":
          Teclado=input("Você deseja descansar sob ela? Sim/Não")
          Teclado=Teclado.upper()
        if Teclado=="SIM":
          print("Você acabava por adormecer sob a arvore...")
          input("ENTER")
          cls()
          print("Você tinha um ótimo horrível, onde fadas e duendes lhe esfaqueavam de todos os lados")
          print("Você acordava, a floresta parecia mais morta ao seu redor.")
          print("Pelo jeito, os espíritos daqui não estão ao seu lado.")
          input("ENTER")
          cls()
          player.HP-=int(player.HP/8)
          player.MP-=int(player.MP/8)
          if player.HP<0:
            player.HP=1
          if player.MP<0:
            player.MP=1
      if randomizar==2:
        print("Depois de cruzar ruínas, masmorras e florestas, você dava de cara com em uma clareira")
        print("Chegava a um doce chalé reconfortante, você podia ver uma doce velhinha varrendo as folhas de frente da sua casa")
        print("Idosa: --Oh! saudações meu jovem, eu não esperava por visitas hoje...")
        print("A idosa vestia roupas camponesas dos pés a cabeça mantinha um doce e gentil olhar enquanto falava contigo.")
        print("Idosa:--Está perdido? Não tem onde dormir? Se quiser pode passar a noite aqui.")
        Teclado=input("Sim/Não")
        while Teclado.upper()!="SIM" and Teclado.upper!="NÃO":
          Teclado=input("Sim/Não")
        Teclado=Teclado.upper()
        cls()
        if Teclado=="SIM":
          print(f"{player.nome}--Obrigado, estou perdido há dias, exausto, vagando por essas terras infestadas de monstros")
          print("Você então descansava... Pelomenos até a hora em que você via luzes se ascendendo dentro da casa.")
          print("Você ouvia berros baixinho, vindo de dentro da casa...")
          print("E então você decide espiar, olhando pela janela, você podia ver a mesma idosa")
          print("Dessa vez, ela tinha um saco ao lado dela, e um caldeirão com água fervente a sua frente.")
          print("Você via ela tentar arrancar algo de dentro do saco, até perceber que ela estava puxando não era comida... Mas sim uma criança humana!")
          print("Ela percebe-te espiando-a pela janela, e se prepara para um combate contigo!")
          input("ENTER")
          cls()
          combate_random_melhorado(player,1,"Bruxa")
        else:
          print(f"{player.nome}--Não estou perdido. Vou seguir meu caminho agora. Adeus.")
          print("Com essas palavras você voltava para dentro do mato, se despedindo da idosa, que apenas o observava sumir entre a folheagem.")
      if randomizar==3:
        print("Após explorar as ruínas do local, você podia ver um cão latindo pra você, assim que o mesmo")
        print("captara sua atenção, ele corria para entre os prédios abandonados do local")
        Teclado=input("Seguir ele? Sim/Não")
        while Teclado.upper!=("SIM") and Teclado.upper()!="NÃO":
          Teclado=input("Seguir ele? Sim/Não")
        cls()
        Teclado=Teclado.upper()
        if Teclado=="SIM":
          print("Você acompanhava o pobre cão...")
          print("Ele estava sujo e sarnento, ele virava uma esquina nas ruínas, e assim que você o segue...")
          input("ENTER")
          cls()
          print("Você podia ver vários goblins saindo de janelas acima de você! Quatro deles lhe cercavam!")
          print("Você caiu em uma armadilha!")
          input("ENTER")
          combate_random_melhorado(player,4,"Goblin","Goblin","Goblin","Goblin",)
          if player.HP>0:
            cls()
            print("Você conseguia derrotar todos os inimigos, mas estava longe de ter paz, você começava")
            print("A tentar fugir pelos becos e ruelas, arrombava uma das portas de madeira apodrecida")
            print("das ruínas, você cruzava a casa, e assim que saía pela porta da frente, você era atacado")
            print("pelo mesmo cão que você estava a seguir, junto de mais três goblins.")
            input("ENTER")
            combate_random_melhorado(player,4,"Lobo Atroz","Goblin","Goblin","Goblin",)
            if player.HP>0:
              print("Você finalizava o cão selvagem, cravando sua espada em sua cabeça.")
              recompensa=random.randint(10,30)
              print("Você saqueava cada um dos goblins, e encontrava",recompensa,"moedas de ouro.")
              player.dinheiro+=recompensa
              if random.randint(1,2)==1:
                print("A maioria das adagas dos goblins estavam inutilizáveis, mas você achava uma decente entre elas.")
                obj_inventario.AdicionarItem(player,"Adaga")
              elif random.randint(1,4)==3:
                print("Dentre as armas dos goblins, você encontrava um par de Adagas Gêmeas.")
                obj_inventario.AdicionarItem(player,"Adagas Gêmeas")
              print(f"{player.nome}--Nunca mais eu ajudo cães de rua, anotado.")
        else:
          print("Você virava suas costas para o cão, e voltava a seguir seu caminho para fora das ruínas.")

def EntrarNaDungeon(tabuleiro):
  tabuleiro[random.randint(0,10)][random.randint(0,14)]="o"
  return tabuleiro

def gerar_saida(tabuleiro):
    x,y=random.randint(0,10),random.randint(0,14)
    tabuleiro[x][y]="n"
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
        if player.HP<0:
          while True:
            input("Você Morreu!")
        Controlador(tabuleiro,player)
        sair=conferir_saida(saidax,saiday,tabuleiro)
        if sair=="ACHOU A SAIDA":
            input("Você encontrava a saída da dungeon, um portal que lhe levava para o lado de fora!")
            break
        ConferirEvento(tabuleiro,player)