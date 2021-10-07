
from obj_inimigo import *
from obj_personagem import *
from obj_grimorio import *
from obj_inventario import *
from acoes import *
import CasaHorrores
from Tabuleiro import *
from funcoesrpg import *
from obj_livrodegolpes import *

Player=objpersonagem("",0,0,0,0,0,0,0,0,0,0,0,False,0,0,0,0,300,1,0,False,1100,objgrimorio(True,False,False,False,False,True,True,True,False,False),objlivrodegolpes(False,False,False,True,True,True,True,True),objinventario(3,1,"Sobre-Tudo","Espada Curta","Cajado"),0,0,0,0,0,0,0,0,0,0,0,0)

pointbuy(Player)
descansar(Player)
GerenciarInventario(Player)

Dungeon_Crawling(Player)
#CasaHorrores.casadamorte(Player)

#combate_random_melhorado(Player,1,"Troll")

#(self,nome,HP,MP,HPMax,MPMax,FOR,DES,CON,INT,SAB,CAR,DanoArma,ataquesmagicos,Defesa,DefesaMagica,imunidades,expplayer,explevelup,levelplayer,DanoFoco,armaelementalativa,dinheiro,grimorio,livrogolpes,mochila,tipoarmadura=0,tipoarma=0,tipoanel=0,tipoescudo=0,movimento1=0,movimento2=0,movimento3=0,movimento4=0,movimento5=0,movimento6=0,movimento7=0,movimento8=0,armaelementaltipodano=""):