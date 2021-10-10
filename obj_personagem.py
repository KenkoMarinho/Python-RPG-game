import obj_livrodegolpes
import obj_grimorio
import obj_inventario
from funcoesrpg import *
    
class objpersonagem:
  def __init__(self,nome,HP,MP,HPMax,MPMax,FOR,DES,CON,INT,SAB,CAR,DanoArma,ataquesmagicos,Defesa,DefesaMagica,imunidades,expplayer,explevelup,levelplayer,DanoFoco,armaelementalativa,dinheiro,grimorio,livrogolpes,mochila,tipoarmadura=0,tipoarma=0,tipoanel=0,tipoescudo=0,movimento1=0,movimento2=0,movimento3=0,movimento4=0,movimento5=0,movimento6=0,movimento7=0,movimento8=0,armaelementaltipodano=""):
    self.nome=str(nome)
    self.HP=float(HP)
    self.MP=float(MP)
    self.HPMax=float(HPMax)
    self.MPMax=float(MPMax)
    self.FOR=int(FOR)
    self.DES=int(DES)
    self.CON=int(CON)
    self.INT=int(INT)
    self.SAB=int(SAB)
    self.CAR=int(CAR)
    self.tipoarma=str(tipoarma)
    self.DanoArma=int(DanoArma)
    self.tipoarmadura=str(tipoarmadura)
    self.ataquesmagicos=bool(ataquesmagicos)
    self.Defesa=int(Defesa)
    self.DefesaMagica=int(DefesaMagica)
    self.imunidades=str(imunidades)
    self.expplayer=int(expplayer)
    self.explevelup=int(explevelup)
    self.levelplayer=int(levelplayer)
    self.DanoFoco=int(DanoFoco)
    self.armaelementalativa=bool(armaelementalativa)
    self.dinheiro=int(dinheiro)
    self.mochila=mochila
    self.movimento1=movimento1   #magias
    self.movimento2=movimento2   #magias
    self.movimento3=movimento3   #magias
    self.movimento4=movimento4   #magias
    self.movimento5=movimento5   #ataques
    self.movimento6=movimento6   #ataques
    self.movimento7=movimento7   #ataques
    self.movimento8=movimento8   #ataques
    self.grimorio=grimorio
    self.livrogolpes=livrogolpes
    self.armaelementaltipodano=armaelementaltipodano
    self.tipoanel=tipoanel
    self.tipoescudo=tipoescudo

def resetarHpMaxMpMax(objeto):
    objeto.HP=9+objeto.CON
    objeto.HPMax=objeto.HP
    objeto.MP=int(5+(objeto.INT/2))
    objeto.MPMax=objeto.MP

def verificarHP(personagem):
    if personagem.HP>personagem.HPMax:
      personagem.HP=personagem.HPMax
    if personagem.HP<1:
      personagem.HP=0
      input(f'{personagem.nome} morreu!')

def verificarMP(personagem):
    if personagem.MP>personagem.MPMax:
      personagem.MP=personagem.MPMax
    if personagem.MP<1:
      personagem.MP=0

def descansar(personagem):
    cls()
    resetarHpMaxMpMax(personagem)
    obj_livrodegolpes.preparacaogolpes(personagem,personagem.livrogolpes)
    cls()
    obj_grimorio.preparacaomagias(personagem,personagem.grimorio)
    cls()
    descansando=bool(True)
    resetarValores(personagem)
    print("Você descansava, e recuperava-se de seus ferimentos.")
    personagem.MP=personagem.MPMax
    personagem.HP=personagem.HPMax
    print("Seu HP é: ",personagem.HP)
    print("Seu MP é: ",personagem.MP)
    print("EXP Atual: ",personagem.expplayer)
    print("EXP para Level Up: ",personagem.explevelup)
    while personagem.expplayer>=personagem.explevelup:
      print("Você alcançou o EXP necessário para Subir de Nível, deseja Realizar o LevelUp agora?")
      decisao=input("1-Sim 2-Não: ")
      while decisao!='1' and decisao!='2':
        decisao=input('1-Sim 2-Não')
      cls()
      if decisao=='1':
          personagem.expplayer=personagem.expplayer-personagem.explevelup
          personagem.explevelup=personagem.explevelup+500
          personagem.levelplayer=personagem.levelplayer+1
          print("Level atual: ",personagem.levelplayer)
          print("Você Aumentou seu Nível! Qual atributo deseja incrementar?")
          Teclado=input("FOR,DES,CON,INT,SAB,CAR ")
          if Teclado=="FOR":
            personagem.FOR=personagem.FOR+1
            print("Você aumentava seu atributo de Força!")
          if Teclado=="DES":
            personagem.DES=personagem.DES+1
            print("Você aumentava seu atributo de Destreza!")
          if Teclado=="CON":
            personagem.CON=personagem.CON+1
            print("Você aumentava seu atributo de Constituição!")
          if Teclado=="INT":
            personagem.INT=personagem.INT+1
            print("Você aumentava seu atributo de Inteligência!")
          if Teclado=="SAB":
            personagem.SAB=personagem.SAB+1
            print("Você aumentava seu atributo de Sabedoria!")
          if Teclado=="CAR":
            personagem.CAR=personagem.CAR+1
            print("Você aumentava seu atributo de Carisma!")
          input("ENTER")
          cls()
          print("Seus Atributos Atuais são:")
          print("FOR: ",personagem.FOR)
          print("DES: ",personagem.DES)
          print("CON: ",personagem.CON)
          print("INT: ",personagem.INT)
          print("SAB: ",personagem.SAB)
          print("CAR: ",personagem.CAR)
          print("Você Finaliza seu descanso.")
      if decisao=='2':
          print("Você Finaliza seu descanso.")
    input("ENTER")
    cls()
  
def resetarValores(personagem):
    personagem.DanoArma=int(((personagem.FOR+personagem.DES/2)*3)/8)#dano unnarmed

    personagem.MPMax=int(5+(personagem.INT/2))
    personagem.HPMax=9+personagem.CON
    #if personagem.HP==0:
      #personagem.HP=personagem.HPMax
    verificarHP(personagem)
    #criterios de balanceamento do sistema de armas:
    #armas com escalamento BOM devem ter DANO BASE BAIXO, e a soma da média dos atributos pedidos deve ser dividida por 4, armas com escalamento MÉDIO devem ter o resultado da média de seus atributos divididos por 5. armas com escalamento RUIM devem ter dano base alto e ter a média de seus atributos dividida por 8.
    if personagem.tipoarma=="Adaga": #Scaling Médio
      personagem.DanoArma=1+int((personagem.DES)/5)
    if personagem.tipoarma=="Espada Curta": #Scaling Médio
      personagem.DanoArma=3+int(((personagem.DES*4+personagem.FOR*3)/7)/5)
    if personagem.tipoarma=="Arco": #Scaling Médio
      personagem.DanoArma=4+int(personagem.DES/5)
    if personagem.tipoarma=="Besta": #Scaling Ruim
      personagem.DanoArma=7+int((personagem.DES+personagem.FOR/2)/8)
    if personagem.tipoarma=="Rapieira": #Scaling Bom
      personagem.DanoArma=1+int(((personagem.DES/5+personagem.FOR/2)/7)/4)
    if personagem.tipoarma=="Espada Longa": #Scaling Bom
      personagem.DanoArma=3+int(((personagem.DES*3+personagem.FOR*4+personagem.CON*1)/8)/4)
    #criterios de balanceamento do sistema de focos arcanos:
    #Mesmas regras das armas, exceto que não existe dano base, logo, todos os scalings tem qualidade RUIM.
    if personagem.tipoarma=="Varinha De Teixo" or personagem.tipoarma=="Varinha De Visco" or personagem.tipoarma=="Bolsa De Runas" or personagem.tipoarma=="Espada Dos Magos":
      if personagem.tipoarma=="Varinha de Teixo":
        personagem.DanoFoco=int(((personagem.SAB*3+personagem.INT)/4)/8)
      if personagem.tipoarma=="Varinha De Visco":
        personagem.DanoFoco=int(((personagem.INT*3+personagem.SAB)/4)/8)
      if personagem.tipoarma=="Bolsa De Runas":
        personagem.DanoFoco=int(((personagem.INT+personagem.SAB+personagem.DES)/3)/8)
      if personagem.tipoarma=="Espada Dos Magos":
        personagem.DanoFoco=int(((personagem.INT+personagem.FOR)/2)/8)
      
    #criterios de balanceamento do sistema de anéis: todos os aneis só tem efeitos que se ativam quando são equipados, logo, não cabe pôr-los em "resetarValores".

    #criterios de balanceamento do sistema de Escudos:
    #Escudos também podem ser Armas de Duas mãos.
    #Armas de Duas Mãos tem 1.4x o Scaling do que teriam se fossem Armas de Uma mão.
    if personagem.tipoescudo=="Adagas Gêmeas" or personagem.tipoescudo=="Cajado" or personagem.tipoescudo=="Cajado Sagrado":
      if personagem.tipoescudo=="Espada Larga": #Scaling Ruim
        personagem.DanoArma=9+int((((personagem.FOR*7+personagem.DES*1+personagem.CON*2)/10)/8)*1.4)
      if personagem.tipoescudo=="Cajado Sagrado":
        personagem.DanoFoco=int((((personagem.SAB*3+personagem.INT)/4)/8)*1.4)
      if personagem.tipoescudo=="Cajado":
        personagem.DanoFoco=int((((personagem.INT*3+personagem.SAB+personagem.CON+personagem.FOR)/6)/8)*1.4)
    #criterios de balanceamento do sistema de armaduras:armaduras leves tem a média de atributos dividida por 10 no final, armaduras medias sao divididas por 9, e pesadas por 8, o contrario acontece quando se fala de Defesa Mágica.
    if personagem.tipoarmadura=="Armadura De Couro" or personagem.tipoarmadura=="Cota De Malha" or personagem.tipoarmadura=="Camisão De Malha" or personagem.tipoarmadura=="Sobre-Tudo" or personagem.tipoarmadura=="Robes Desgastadas":
      #armaduras leves:
      if personagem.tipoarmadura=="Armadura de Couro" or "Sobre-Tudo" or "Robes Desgastadas":
        personagem.Defesa=1+int(((personagem.DES*8+personagem.CON*2+personagem.FOR)/11)/10)
        personagem.DefesaMagica=3+int(((personagem.INT+personagem.SAB*2)/3)/8)
      #armaduras medias:
      if personagem.tipoarmadura=="Camisão de Malha":
        personagem.Defesa=2+int((personagem.DES*5+personagem.CON*5+personagem.FOR*2)/12)/9
        personagem.DefesaMagica=2+int(((personagem.INT*2+personagem.SAB)/3)/9)
      #armaduras pesadas:
      if personagem.tipoarmadura=="Cota de Malha":
        personagem.Defesa=4+int((personagem.DES*5+personagem.CON*5+personagem.FOR*2)/12)/8
        personagem.DefesaMagica=0+int(((personagem.INT*2+personagem.SAB)/3)/10)

def pointbuy(objeto):
    pontos=0
    if objeto.FOR==0 and objeto.DES==0 and objeto.CON==0 and objeto.INT==0 and objeto.SAB==0 and objeto.CAR==0:
      pontos=25
      pontosiniciais=pontos
    confirma=False
    if objeto.nome=="":
      objeto.nome=input("Digite o Nome do seu personagem: ")
      while confirma==False:
        aux=input("Tem certeza? 1-Sim 2-Não")
        if aux=='1':
          break
        else:
          objeto.nome=input("Digite o Nome do seu personagem")
    cls()
    print(f"Você tem {pontos} pontos de atributo para distribuir entre os seguintes atributos:")
    print("FOR")
    print("DES")
    print("CON")
    print("INT")
    print("SAB")
    print("CAR")
    #definir FOR
    aux_for=(input("Insira a quantidade de pontos que deseja alocar para FOR: "))
    while aux_for!='0' and aux_for!='1' and aux_for!='2' and aux_for!='3' and aux_for!='4' and aux_for!='5' and aux_for!='6' and aux_for!='7' and aux_for!='8' and aux_for!='9' and aux_for!='10' and aux_for!='11' and aux_for!='12' and aux_for!='13' and aux_for!='14' and aux_for!='15' and aux_for!='16' and aux_for!='17' and aux_for!='18' and aux_for!='19' and aux_for!='20':
      aux_for=(input("Insira a quantidade de pontos que deseja alocar para FOR: "))
    aux_for=int(aux_for)
    pontos=pontos-aux_for
    print(f"Você ainda tem {pontos} pontos")
    #definir DES
    aux_des=(input("Insira a quantidade de pontos que deseja alocar para DES: "))
    while aux_des!='0' and aux_des!='1' and aux_des!='2' and aux_des!='3' and aux_des!='4' and aux_des!='5' and aux_des!='6' and aux_des!='7' and aux_des!='8' and aux_des!='9' and aux_des!='10' and aux_des!='11' and aux_des!='12' and aux_des!='13' and aux_des!='14' and aux_des!='15' and aux_des!='16' and aux_des!='17' and aux_des!='18' and aux_des!='19' and aux_des!='20':
      aux_des=(input("Insira a quantidade de pontos que deseja alocar para DES: "))
    aux_des=int(aux_des)
    pontos=pontos-aux_des
    print(f"Você ainda tem {pontos} pontos")
    #definir CON
    aux_con=(input("Insira a quantidade de pontos que deseja alocar para CON: "))
    while aux_con!='0' and aux_con!='1' and aux_con!='2' and aux_con!='3' and aux_con!='4' and aux_con!='5' and aux_con!='6' and aux_con!='7' and aux_con!='8' and aux_con!='9' and aux_con!='10' and aux_con!='11' and aux_con!='12' and aux_con!='13' and aux_con!='14' and aux_con!='15' and aux_con!='16' and aux_con!='17' and aux_con!='18' and aux_con!='19' and aux_con!='20':
      aux_con=(input("Insira a quantidade de pontos que deseja alocar para CON: "))
    aux_con=int(aux_con)
    pontos=pontos-aux_con
    print(f"Você ainda tem {pontos} pontos")
    #definir INT
    aux_int=(input("Insira a quantidade de pontos que deseja alocar para INT: "))
    while aux_int!='0' and aux_int!='1' and aux_int!='2' and aux_int!='3' and aux_int!='4' and aux_int!='5' and aux_int!='6' and aux_int!='7' and aux_int!='8' and aux_int!='9' and aux_int!='10' and aux_int!='11' and aux_int!='12' and aux_int!='13' and aux_int!='14' and aux_int!='15' and aux_int!='16' and aux_int!='17' and aux_int!='18' and aux_int!='19' and aux_int!='20':
      aux_int=(input("Insira a quantidade de pontos que deseja alocar para INT: "))
    aux_int=int(aux_int)
    pontos=pontos-aux_int
    print(f"Você ainda tem {pontos} pontos")
    #definir SAB
    aux_sab=(input("Insira a quantidade de pontos que deseja alocar para SAB: "))
    while aux_sab!='0' and aux_sab!='1' and aux_sab!='2' and aux_sab!='3' and aux_sab!='4' and aux_sab!='5' and aux_sab!='6' and aux_sab!='7' and aux_sab!='8' and aux_sab!='9' and aux_sab!='10' and aux_sab!='11' and aux_sab!='12' and aux_sab!='13' and aux_sab!='14' and aux_sab!='15' and aux_sab!='16' and aux_sab!='17' and aux_sab!='18' and aux_sab!='19' and aux_sab!='20':
      aux_sab=(input("Insira a quantidade de pontos que deseja alocar para SAB: "))
    aux_sab=int(aux_sab)
    pontos=pontos-aux_sab
    print(f"Você ainda tem {pontos} pontos")
    #definir CAR
    aux_car=(input("Insira a quantidade de pontos que deseja alocar para CAR: "))
    while aux_car!='0' and aux_car!='1' and aux_car!='2' and aux_car!='3' and aux_car!='4' and aux_car!='5' and aux_car!='6' and aux_car!='7' and aux_car!='8' and aux_car!='9' and aux_car!='10' and aux_car!='11' and aux_car!='12' and aux_car!='13' and aux_car!='14' and aux_car!='15' and aux_car!='16' and aux_car!='17' and aux_car!='18' and aux_car!='19' and aux_car!='20':
      aux_car=(input("Insira a quantidade de pontos que deseja alocar para CAR: "))
    aux_car=int(aux_car)
    pontos=pontos-aux_car
    print(f"Você ainda tem {pontos} pontos")
    #valida a soma dos atbs e compara com a quantidade de pontos
    if (aux_for+aux_des+aux_con+aux_int+aux_sab+aux_car)!=pontosiniciais:
      print(f"A soma dos atributos não dá {pontosiniciais}! O processo será repetido.")
      pointbuy(objeto)
    #Pergunta se quer repetir
    repetir=input("Deseja distribuir os pontos novamente? 1-Sim 2-Não")
    while repetir !='1' and repetir !='2':
      repetir=input("Deseja distribuir os pontos novamente? 1-Sim 2-Não")
    if repetir=='1':
      cls()
      pointbuy(objeto)
    else:
      cls()
      print("Processo concluído!")
      objeto.FOR=aux_for
      objeto.DES=aux_des
      objeto.CON=aux_con
      objeto.INT=aux_int
      objeto.SAB=aux_sab
      objeto.CAR=aux_car
      resetarHpMaxMpMax(objeto)
