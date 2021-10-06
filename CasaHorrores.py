import random
import obj_inventario
from time import sleep
from obj_personagem import *
from funcoesrpg import *

class objcasahorrores:
  def __init__(self,mapeadasalaCM1=0,mapeadasalaCM2=0,mapeadasalaCM3=0,mapeadasalaCM4=0,mapeadasalaCM5=0,mapeadasalaCM6=0):
    self.mapeadasalaCM1="?"
    self.mapeadasalaCM2="?"
    self.mapeadasalaCM3="?"
    self.mapeadasalaCM4="?"
    self.mapeadasalaCM5="?"
    self.mapeadasalaCM6="?"

  def printarmapa(self):
    print("O----------O-----O")
    print("|    ",self.mapeadasalaCM3,"   |     |")
    print("O---O-u----O     |")
    print("    |      |     |")
    print("    |  ",self.mapeadasalaCM2," u ",self.mapeadasalaCM4," O----O")
    print("    |      |     u     |")
    print("    |u---OuO-----O ",self.mapeadasalaCM6," |")
    print("O---O    |       u     |")
    print("|   ",self.mapeadasalaCM1,"  |  ",self.mapeadasalaCM5,"  |     |")  
    print("O---u----O-------O-----O")

import os
def cls():
  os.system('clear')
  
def casadamorte(player):
  nacozinha=False
  nasala=False
  adagadisponivel=True
  casahorrores=objcasahorrores()
  dungeoncrawling=bool(True)
  quartolocal=1
  mimicovivo=True
  entrando=True
  espectrothornvivo=True
  bruxaviva=True
  lootdisponivel=True
  adagadisponivel=True
  goblinsvivos=True
  espadavivaviva=True
  while dungeoncrawling==True:
    if quartolocal==1: #entrada
      if entrando==True:
        print("Essa é a Entrada da casa, você pode ver sapatos apodrecidos ao lado da porta, um casaco empoeirado, assim que você dá o primeiro passo pra dentro da casa, as portas se fecham com força e subitamente atrás de você. Você podia ver uma porta a sua frente.")
        acoes='"Examinar Área" "Abrir Porta" "Mapear" "Olhar Mochila"'
        print("Possiveis Ações: ",acoes)
        print("=======================")
        Teclado=input("O que você Faz?")
        while Teclado!="Examinar Área"and Teclado!="Abrir Porta"and Teclado!="Mapear"and Teclado!="Olhar Mochila":
          Teclado=input("O que você Faz?")
        cls()
        if Teclado=="Mapear":
          cls()
          casahorrores.mapeadasalaCM1="1"
          casahorrores.printarmapa()
        if Teclado=="Examinar Área":
          if adagadisponivel==True:
            print("Você examinava a sala, dentro dos sapatos você só encontrava poeira, ao examinar o casaco empoeirado, você acabava por se cortar com uma pequena adaga enferrujada que estava no Bolso do casaco. ")
            player.HP=player.HP-1
            print("Você encontrou 1 Adaga Enferrujada.")
            obj_inventario.AdicionarItem(player,"Adaga")
            adagadisponivel=False
          else:
            print("Você já explorou esse cômodo.")
        if Teclado=="Abrir Porta":
          print("Você abria a porta, passando para o próximo quarto.")
          nasala=True
          cls()
          quartolocal=2
          entrando=False
        if Teclado=="Olhar Mochila":
          cls()
          obj_inventario.GerenciarInventario(player)
      else:
        sair=input("Deseja ir embora?< 1-Sim 2-Não>")
        while sair!="1" and sair!="2":
          print("Você ia embora da casa.")
          dungeoncrawling=False

    if quartolocal==2: #sala de estar
      cls()
      if nasala:
        if espadavivaviva==True:
          print("Assim que você entra no quarto, a porta se fecha com força atrás de você, assustado, você caminhava pelo quarto empoeirado, tudo parecia abandonado aqui, este local parecia ser uma Sala De Estar ou algo assim...!")
          print('Acoes: "Examinar Área" "Mapear" "Olhar Mochila" "Abrir Porta Para Cozinha" "Abrir Porta Para Quarto Dos Pais"')
        else:
          print("A sala de estar está tão vazia quanto você a deixou.")
          print('Acoes: "Examinar Área" "Mapear" "Olhar Mochila" "Abrir Porta Para Cozinha" "Abrir Porta Para Quarto Dos Pais"')
        print("=======================")
        Teclado=input('O Que Você Faz?')
        while Teclado!="Examinar Área" and Teclado!="Mapear" and Teclado!="Olhar Mochila" and Teclado!="Abrir Porta Para Cozinha" and Teclado!="Abrir Porta Para Quarto Dos Pais":
          Teclado=input("O Que Você Faz?")
        if Teclado=="Examinar Área":
          if espadavivaviva==True:
            print("Acima de uma Lareira você podia observar uma Espada, ela tinha um moinho entalhado em seu cabo e o nome 'Durst' gravado em sua Lâmina.")
            decisao=input("1-Recolher a Espada  2-Deixar-la")
            while decisao!="1" and decisao!='2':
              decisao=input("1-Recolher a Espada  2-Deixar-la")
            if decisao=='1':
              combate_random_melhorado(player,1,"Espada Viva")
              if player.HP>0:
                espadavivaviva=False
        else:
          print("Não há nada de interessante nesse quarto a ser Examinado.")
        if Teclado=="Mapear":
          cls()
          casahorrores.mapeadasalaCM2="2"
          casahorrores.printarmapa()
          input("ENTER")
        if Teclado=="Olhar Mochila":
          obj_inventario.GerenciarInventario(player)
        if Teclado=="Abrir Porta Para Cozinha":
          cls()
          if goblinsvivos==True:
            print("Você se aproximava da Porta da cozinha, quando se aproximava, podia ouvir o som de algo batendo panelas lá dentro")
            decisao=input("Ainda deseja entrar? 1-Sim 2-Não")
            while decisao!='1' and decisao!='2':
              decisao=input("Ainda deseja entrar? 1-Sim 2-Não")
            if decisao=="1":
              print("Você então se preparava para invadir, e entrava com tudo na cozinha!")
              input("ENTER")
            else:
              print("Você retornava para o Centro do quarto.")
          else:
            print("Você entrava na cozinha.")
            input("ENTER")
          cls()
          if decisao=='1':
            nacozinha=True
            nasala=False
            quartolocal=3
            decisao="0"
        if Teclado=="Abrir Porta Para Quarto Dos Pais":
          cls()
          print("Você abria a porta para o quarto dos pais, a porta estava trancada, mas anos e anos de putrefação tornaram bem fácil arrombar uma porta de madeira apodrecida. Você a atravessava em seguida.")
          input("ENTER")
          cls()
          quartolocal=4

    if quartolocal==3: #cozinha
      cls()
      decisao='0'
      nacozinha=True
      nasala=False
      if nacozinha:
        if goblinsvivos==True:
          print("Assim que você entrava na cozinha, podia ver dois Goblins mechendo no lixo, ao perceber sua presença, eles saíam lá de dentro, e com uma panela na cabeça, e um facão enferrujado na mão, eles partiam para cima de você!")
          input("ENTER")
        else:
          print("Você entrava na cozinha suja novamente. Não há nada o que se fazer aqui.")
          input("ENTER")
        if goblinsvivos==True:
          combate_random_melhorado(player,2,"Goblin","Goblin")
          goblinsvivos=False
          if player.HP>0:
            input("ENTER")
            cls()
            print("Após derrotar os goblins, você observava a cozinha")
          print("Uma mesa de jantar com quatro cadeiras no canto do quarto, um forno a lenha requintado, e vários conjuntos de talheres e pratarias, ou enferrujados, ou cobertos por fungos ou sangue. Você também podia ver dois esqueletos tamanho infantil estirados ao canto do quarto, examinando eles, você acha um livro")
          ler=input("Ler o livro? 1-Sim 2-Não")
          while ler!="1" and ler!="2":
            ler=input("Ler o livro? 1-Sim 2-Não")
          if ler=='1':
            cls()
            print("Diário de Anna Durst")
            input("ENTER")
            cls()
            print("Página 1:")
            print("22 De Outubro do ano da colheita")
            print("Papai brincou de bonecas comigo hoje, ele nunca faz esse tipo de coisa, que bom que tenho ele e a mamãe por perto! Queria que meu irmão Thorn também brincasse, mas ele vive dizendo que é coisa de menina...")
            input("ENTER")
            cls()
            print("Página 2:")
            print("27 De Outubro do ano da colheita")
            print("Hoje algo horrível aconteceu, papai estava brincando de médico com a empregada, quando mamãe viu os dois começaram a discutir e a outra mulher fugiu correndo")
            input("ENTER")
            cls()
            print("Página 3:")
            print("2 de Novembro do ano da colheita")
            print("Papai sumiu. Já faz dias que não vejo ele, mamãe disse que ele foi embora. Meu irmão Thorn parece não se importar.")
            input("ENTER")
            cls()
            print("Página 4:")
            print("3 de Novembro do ano da colheita")
            print("Encontrei uma faca ensanguentada do lado de fora da casa, escondida atrás de alguns arbustos.")
            cls()
            print("Página 5:")
            print("5 de Novembro do ano da colheita")
            print("Mamãe está cada dia mais depressiva, ela se trancou no quarto dela e passa o dia inteiro murmurando maldições contra a nossa antiga empregada, Sinto falta do papai...")
            input("ENTER")
            cls()
            print("Página 6:")
            print("6 de Novembro do ano da colheita")
            print("Já me decidi. Vou perguntar a mamãe sobre essa faca... É minha decisão final.")
            input("ENTER")
            cls()
            print("Então... Você se perdia em pensamentos.")
            print("A mãe deve ter ficado louca, assassinado o marido, e usado algum tipo de magia para amaldiçoar a empregada... Sinto muito por vocês, pequenos.")
            print("Em seguida, você depositava novamente o livro onde encontrou, sobre o cadáver da criança")
          print("Você se levantava calmamente, ainda que levemente perturbado pelo que viu aqui. Ainda que já estivesse naturalizado a ver cadáveres, o sentimento sempre lhe faz lembrar dos rostos do passado.")
        print("Ações possíveis: 'Voltar Para A Sala' 'Mapear'")
        print("====================")
        selecao=input("O que você faz?")
        while selecao!="Voltar Para A Sala" and selecao!="Mapear":
          selecao=input("O que você faz?")
        if selecao=="Mapear":
          casahorrores.mapeadasalaCM3="3"
          casahorrores.printarmapa()
          input("ENTER")
          cls()
        if selecao=="Voltar Para A Sala":
          nasala=True
          nacozinha=False
          quartolocal=2
  
    if quartolocal==4: #quarto dos pais
      cls()
      acoes="'Voltar Para A Sala''Abrir Próxima Porta' 'Abrir Mochila'"
      if bruxaviva==True:
        cls()
        print("Você entrava no quarto dos pais. Assim que o fazia, ouvia uma gargalhada maligna o quarto se enchia de sombras, uma mulher velha, de cabelos desgrenhados, grisalhos, com um vestido preto resgado e com metade do rosto coberto por fungos e verrugas, ela olhava pra você e então perguntava")
        print("Madame Durst : --HiHiHi! O que veio buscar em meu covil, aventureiro?")
        input("ENTER")
        print(player.nome,": --Eu vim buscar o seu amuleto. Sinto lhe dizer, mas alguém me pagou pra vir buscar.")
        print("Madame Durst : --Foi aquela mulher, né?! Aquela que botou as garras em meu marido, a fim de tomar de mim essa herança! Foi ela quem me transformou no que eu sou! Sinto lhe desapontar, mas não deixarei você ter-lo!")
        print(player.nome,"Desembainhava suas armas e se preparava para o combate!")
        input("ENTER")
        cls()
        combate_random_melhorado(player,1,"Bruxa")
        if player.HP>0:
          bruxaviva=False
          cls()
          print("O Cadáver da bruxa cobria o quarto, seu sangue negro escorria pelo móvel, você podia ver ela agonizando e morrendo aos poucos, enquanto começa a delirar, falando sobre o 'bebê' dela, e sobre como sente falta dos filhos. Você impiedosamente finalizava ela, e pegava o amuleto que veio buscar.")
      else:
        print("O quarto está tão macabro quanto você o deixou da ultima vez que esteve nele.")
      print("Possíveis Ações: ",acoes)
      acao=input("O que você faz?")
      while acao!="Abrir Mochila" and acao!='Voltar Para A Sala' and acao!='Abrir Próxima Porta':
        acao=input("O que você faz?")
      if acao=="Abrir Mochila":
        obj_inventario.GerenciarInventario(player)
      if acao=="Voltar Para A Sala":
        quartolocal=2
      if acao=="Abrir Próxima Porta":
        quartolocal=5
    if quartolocal==5:
      if espectrothornvivo==True:
        cls()
        print("Esse é o quarto de empregadas, você pode ver um Espectro tristonho no canto da sala, e ao lado dele, uma foto de um garoto, exatamente igual ao Espectro, você assume que aquele era o Fantasma de uma das crianças que vivia na casa.")
        decisao=input("Libertar sua alma? <1-Sim 2-Não>")
        cls()
        while decisao!="1" and decisao!="2":
          decisao=input("Libertar sua alma? <1-Sim 2-Não>")
        if decisao=='1':
          combate_random_melhorado(player,1,"Espectro")
          print("Ao fim do combate, Thorn desaparecia no ar...")
          espectrothornvivo=False
        else:
          print("Você deixava o garoto ali.")
      else:
        if espectrothornvivo==True:
          print("O quarto de empregadas continua assombrado pelo choro de Thorn, que prantava pelos cantos na sala, tão indefeso quanto qualquer garotinho estaria.")
          matar=input("Deseja Pôr fim ao sofrimento de Thorn? <1-Sim 2-Não>")
          while matar!='1' and matar!='2':
            matar=input("Deseja Pôr fim ao sofrimento de Thorn? <1-Sim 2-Não>")
          if matar=='1':
            combate_random_melhorado(player,1,"Espectro")
            print("Ao fim do combate, Thorn desaparecia no ar...")
            espectrothornvivo=False
        else:
          print("O quarto de empregadas continua tão vazio quanto você o deixou. Com os restos das cinzas de Thorn no canto da sala")
      print("Ações possíveis:'Voltar Para O Quarto Dos Pais' 'Prosseguir Para O Último Quarto'  'Mapear' 'Abrir Mochila'")
      print("=======================")
      teclado=input("O que você faz?")
      while teclado!="Prosseguir Para O Último Quarto" and teclado!='Voltar Para O Quarto Dos Pais' and teclado!="Mapear" and Teclado!="Abrir Mochila":
        teclado=input("O que você faz?")
      if teclado=="Prosseguir Para O Último Quarto":
        print("Você abria a última porta")
        input("ENTER")
        cls()
        quartolocal=6
      if teclado=="Voltar Para O Quarto Dos Pais":
        quartolocal=4
      if teclado=="Abrir Mochila":
        obj_inventario.GerenciarInventario(player)
      if teclado=="Mapear":
        casahorrores.mapeadasalaCM5="5"
        casahorrores.printarmapa()

    if quartolocal==6:
      print("Você via que esse quarto era um tipo de depósito, onde a família guardava suas riquezas, as caixas de jóias já foram saqueadas")
      if player.SAB>2 and lootdisponivel==True:
        print("Andando pelo quarto, você notava um estranho ranger nas tábuas do chão, levantando-as, você notava um tesouro escondido,1 poção de vida, 1 poção de mana, e 1 Rapieira com o nome Durst cravado.")
        lootdisponivel=False
        player.mochila.pocoeshp+=1
        player.mochila.pocoesmp+=1
        obj_inventario.AdicionarItem(player,"Rapieira")
      print("Você podia ver um baú aberto")
      print("Possíveis ações: 'Abrir Mochila' , 'Voltar Para Quarto Da Empregada', 'Investigar Baú' 'Mapear'")
      print("===============")
      selecao=input("O que você faz?")
      while selecao!='Abrir Mochila'and selecao!='Voltar Para Quarto Da Empregada'and selecao!= 'Investigar Baú' and selecao!='Mapear':
        selecao=input("O que você faz?")
      if selecao=="Mapear":
        casahorrores.mapeadasalaCM6="6"
        casahorrores.printarmapa()
        input("ENTER")
        cls()
      if selecao=="Abrir Mochila":
        obj_inventario.GerenciarInventario(player)
      if selecao=="Voltar Para Quarto Da Empregada":
        quartolocal=5
      if selecao=="Investigar Baú":
        if mimicovivo==True:
          print("Você se aproximava do baú, ao abrir ele, a tampa do baú fecha-se sozinha sobre seu braço! Você felizmente consegue evitar a tempo, e se afastar do Mímico, que se levanta, e sobre duas pernas se prepara para lhe combater!")
          input("ENTER")
          combate_random_melhorado(player,1,"Mímico")
          cls()
          mimicovivo=False
        else:
          print("Você já saqueou esse baú.")
  while player.HP>0:
    input("YOU HAVE DIED")
      