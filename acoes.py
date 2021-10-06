import obj_personagem
import obj_inimigo
import random
import obj_adicionais
import funcoesrpg

def Fugir(usuario,alvo1,alvo2=0,alvo3=0,alvo4=0):
  if alvo1.podefugir==False or alvo2.podefugir==False or alvo3.podefugir==False or alvo4.podefugir==False:
    print("Você não pode fugir deste combate!")
  else:
    rand=random.randint(1,20)
    rand+=int((usuario.DES**1/2)+(usuario.CON**1/3)/1.5)
    if rand>10:
      print(usuario.nome,"Escapava com Sucesso.")
      if alvo1!=0:
        alvo1.dificuldade=0
        alvo1.HP=0
      if alvo2!=0:
        alvo2.dificuldade=0
        alvo2.HP=0
      if alvo3!=0:
        alvo3.dificuldade=0
        alvo3.HP=0
      if alvo4!=0:
        alvo4.dificuldade=0
        alvo4.HP=0
      alvo1.alavanca,alvo2.alavanca,alvo3.alavanca,alvo4.alavanca=True,True,True,True
    else:
      print(usuario.nome,"Não conseguia Escapar.")
#glossário de golpes:

def Arranhar(usuario,alvo):
  a=type(usuario)
  b=type(alvo)
  a,b=str(a),str(b)
  imune=funcoesrpg.ConferirImunidade(alvo,"Cortante")
  if b=="<class 'obj_inimigo.objinimigo'>":
    if imune==True:
      print("O Alvo é Imune a Ataques físicos!")
  elif b=="<class 'obj_personagem.objpersonagem'>":
    if imune==True:
      print("O Alvo é Imune a Ataques físicos!")
  if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_inimigo.objinimigo'>":
    dano=int(((usuario.FOR/2)+usuario.DES+2)-alvo.defesa)
    if dano>0:
      print("O Arranhão causou",dano,"pontos de dano a",alvo.nome,"!")
      alvo.HP=alvo.HP-dano
      obj_inimigo.verificarHP(alvo)
    else:
      print("O Arranhão não causou danos!")
  if a=="<class 'obj_inimigo.objinimigo'>" and b=="<class 'obj_personagem.objpersonagem'>":
      dano=int((usuario.ataquefisico+2)-alvo.Defesa)
      if dano>0:
        print("O Arranhão causou",dano,"pontos de dano a",alvo.nome,"!")
        alvo.HP=alvo.HP-dano
        if b=="<class 'obj_personagem.objpersonagem'>":
          obj_personagem.verificarHP(alvo)
        if b==b=="<class 'obj_inimigo.objinimigo'>":
          obj_inimigo.verificarHP(alvo)
      else:
        print("O Arranhão não causou danos!")
  if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_personagem.objpersonagem'>":
      dano=int(usuario.FOR+usuario.DES+2)-alvo.Defesa
      if dano>0:
        print("O Arranhão causou",dano,"pontos de dano a",alvo.nome,"!")
        alvo.HP=alvo.HP-dano
        if b=="<class 'obj_personagem.objpersonagem'>":
          obj_personagem.verificarHP(alvo)
        if b=="<class 'obj_inimigo.objinimigo'>":
          obj_inimigo.verificarHP(alvo)
      else:
        print("O Arranhão não causou danos!")

def Mordida(usuario,alvo):
  imune=False
  damageflag=True
  a=type(usuario)
  b=type(alvo)
  a,b=str(a),str(b)
  imune=funcoesrpg.ConferirImunidade(alvo,"Perfurante")
  if b=="<class 'obj_inimigo.objinimigo'>":
    if imune==True:
      print(alvo.nome,"é Imune a Ataques físicos!") 
      damageflag=False
  elif b=="<class 'obj_personagem.objpersonagem'>":
    if imune==True:
      print(alvo.nome,"é Imune a Ataques físicos!")
      damageflag=False
  if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_inimigo.objinimigo'>":
    dano=int((usuario.FOR+(usuario.DES/2)+4)-alvo.defesa)
  if a=="<class 'obj_inimigo.objinimigo'>" and b=="<class 'obj_personagem.objpersonagem'>":
    dano=int((usuario.ataquefisico+3)-alvo.Defesa)
  if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_personagem.objpersonagem'>":
    dano=int((usuario.FOR+(usuario.DES/2)+4)-alvo.Defesa)
  rand=random.randint(1,3)
  if dano>0:
    if damageflag==True:
      print(alvo.nome,"era mordido em cheio pelo ",usuario.nome," perdendo",dano,"pontos de HP.")
      alvo.HP=alvo.HP-dano
    if b=="<class 'obj_personagem.objpersonagem'>":
      obj_personagem.verificarHP(alvo)
    if b=="<class 'obj_inimigo.objinimigo'>":
      obj_inimigo.verificarHP(alvo)
  else:
    if imune!=True:
      print("O Ataque não causava danos, pois a defesa de",alvo.nome,"o Protegera!")
  if dano>0 and rand==3 and (usuario.nome=="Zumbi" or usuario.nome=="Carniçal"):
    print(alvo.nome,"sentia a ferida da Mordida queimar, fazendo você se sentir tonto.")
    mploss=random.randint(3,5)
    if b=="<class 'obj_personagem.objpersonagem'>":
      alvo.MP=alvo.MP-mploss
    if b=="<class 'obj_inimigo.objinimigo'>":
      alvo.MP=alvo.MP-mploss
    obj_personagem.verificarMP(alvo)
    print(alvo.nome,"se sente mais cansado, perdendo",mploss,"pontos de Mana.")
  
def Facada(usuario,alvo):
  imune=False
  a=type(usuario)
  b=type(alvo)
  a,b=str(a),str(b)
  randomizar=random.randint(1,2)
  if b=="<class 'obj_inimigo.objinimigo'>":
    if imune==True:
      print("O Alvo é Imune a Ataques físicos!")
  elif b=="<class 'obj_personagem.objpersonagem'>":
    if imune==True:
      print("O Alvo é Imune a Ataques físicos!")
  if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_inimigo.objinimigo'>":
    dano=int(((usuario.DES*1.4)+usuario.DanoArma)-alvo.defesa)
  if a=="<class 'obj_inimigo.objinimigo'>" and b=="<class 'obj_personagem.objpersonagem'>":
    dano=int(int(((usuario.ataquefisico*1.2)+3)-alvo.Defesa))
  if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_personagem.objpersonagem'>":
    dano=int(((usuario.DES*1.4)+usuario.DanoArma)-alvo.Defesa)
  if randomizar==2 and b=="<class 'obj_personagem.objpersonagem'>":
    dano=dano+alvo.Defesa
  if randomizar==2 and b=="<class 'obj_inimigo.objinimigo'>":
    dano=dano+alvo.defesa
  if dano>0:
    print("A Facada causou",dano,"pontos de dano a",alvo.nome)
    alvo.HP=alvo.HP-dano
    if b=="<class 'obj_personagem.objpersonagem'>":
      obj_personagem.verificarHP(alvo)
    if b=="<class 'obj_inimigo.objinimigo'>":
      obj_inimigo.verificarHP(alvo)
  if dano<=0 and imune==False:
    print("A Facada não causa dano. A Defesa o protege.")
  randomizar=random.randint(1,5)
  if (randomizar==1 or randomizar==2)and dano>0:
    print("A facada acertava o braço de",alvo.nome,",pegando seu músculo que usa para desviar/aparar golpes. A defesa de",alvo.nome,"está prejudicada em 1 ponto.")
    if b=="<class 'obj_personagem.objpersonagem'>":
      alvo.Defesa=alvo.Defesa-1 #para recuperar defesa, descanse.
    if b=="<class 'obj_inimigo.objinimigo'>":
      alvo.defesa=alvo.defesa-1

def Ataque_Espada(usuario,alvo):
  danoextra=0
  imune=False
  a=type(usuario)
  b=type(alvo)
  a,b=str(a),str(b)
  flag=False
  crit=False
  dano=0
  randomizar=random.randint(1,10)
  if a=="<class 'obj_personagem.objpersonagem'>":
    if usuario.armaelementalativa==True:
      imune=funcoesrpg.ConferirImunidade(alvo,usuario.armaelementaltipodano)
  else:
    imune=funcoesrpg.ConferirImunidade(alvo,"Cortante")
  if b=="<class 'obj_inimigo.objinimigo'>":
    if imune:
      print("O Alvo é Imune a Ataques físicos!")
      flag=True
  elif b=="<class 'obj_personagem.objpersonagem'>":
    if imune:
      if usuario.armaelementaltipodano!="":
        imune=funcoesrpg.ConferirImunidade(alvo,usuario.armaelementaltipodano)
      if imune==True:
        print("O Alvo é Imune aos Ataques de",usuario.nome,"!")
        flag=True
  if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_inimigo.objinimigo'>":
    dano=int((usuario.DanoArma+(usuario.FOR/2)+(usuario.DES/2))-alvo.defesa)
    if usuario.armaelementalativa==True:
      if usuario.armaelementaltipodano=="Fogo" and alvo.nome=="Troll":
        alvo.regenerar=False
      danoextra=int((usuario.INT/2.3+usuario.SAB/3.2)-alvo.defesamagica/4)
      if danoextra>0:
        dano+=danoextra
  if a=="<class 'obj_inimigo.objinimigo'>" and b=="<class 'obj_personagem.objpersonagem'>":
    dano=int((usuario.ataquefisico+2)-alvo.Defesa)
  if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_personagem.objpersonagem'>":
    dano=int((usuario.DanoArma+(usuario.FOR/2)+(usuario.DES/2))-alvo.Defesa)
  if randomizar==10:
    dano=int(dano*1.5)
    crit=True
  if dano<=0 and flag==False:
    if a=="<class 'obj_adicionais.EspadaVoadora'>":
      dano=int(usuario.dano)
      print("A espada voadora Atacava o alvo em suas frestas de armadura!, causando",dano,"pontos de dano!")
      alvo.HP=int(alvo.HP-usuario.dano)
      obj_inimigo.verificarHP(alvo)
    else:
      print("A Defesa do Inimigo protege ele de seu ataque!")
  if dano>0 and flag==False and crit==False:
    alvo.HP=alvo.HP-dano
    print("O ataque de espada de",usuario.nome,"causou",dano,"pontos de dano ao",alvo.nome)
    if b=="<class 'obj_personagem.objpersonagem'>":
      obj_personagem.verificarHP(alvo)
    if b=="<class 'obj_inimigo.objinimigo'>":
      obj_inimigo.verificarHP(alvo)
  elif dano>0 and flag==False and crit==True:
    alvo.HP=alvo.HP-dano
    print("O ataque de espada causou",dano,"pontos de dano ao",alvo.nome,"em um golpe crítico!")
    if b=="<class 'obj_personagem.objpersonagem'>":
      obj_personagem.verificarHP(alvo)
    if b=="<class 'obj_inimigo.objinimigo'>":
      obj_inimigo.verificarHP(alvo)
    
def Furia_Do_Nanico(usuario,alvo):
  a=type(usuario) #MONSTER ONLY SKILL
  b=type(alvo)
  a,b=str(a),str(b)
  flag=False
  if usuario.MP<2:
    if a=="<class 'obj_inimigo.objinimigo'>":
      funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvo)
    else:
      print("A Habilidade de",usuario.nome," falhou por falta de Mana!")
  else:
    usuario.MP=usuario.MP-2
    obj_personagem.verificarMP(usuario)
    if b=="<class 'obj_inimigo.objinimigo'>":
      if funcoesrpg.ConferirImunidade(alvo,"Perfurante"):
        print("O Alvo é Imune a Ataques físicos!")
        flag=True
    elif b=="<class 'obj_personagem.objpersonagem'>":
      if funcoesrpg.ConferirImunidade(alvo,"Perfurante"):
        print("O Alvo é Imune a Ataques físicos!")
        flag=True
    if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_inimigo.objinimigo'>":
      dano=int(((usuario.FOR*0.8+usuario.DES*1.2)+usuario.DanoArma)-alvo.defesa+5)
    if a=="<class 'obj_inimigo.objinimigo'>" and b=="<class 'obj_personagem.objpersonagem'>":
      dano=int((usuario.ataquefisico+7)-alvo.Defesa)
    if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_personagem.objpersonagem'>":
      dano=int(((usuario.FOR*0.8+usuario.DES*1.2)+usuario.DanoArma)-alvo.Defesa+5)
    if dano<=0 and flag==False:
      print(alvo.nome,"conseguia repelir a investida!")
    if dano>0 and flag==False:
      print(usuario.nome,"Causou",dano,"pontos de dano em um frenesi de raiva!")
      alvo.HP=alvo.HP-dano
      if b=="<class 'obj_personagem.objpersonagem'>":
        obj_personagem.verificarHP(alvo)
      if b=="<class 'obj_inimigo.objinimigo'>":
        obj_inimigo.verificarHP(alvo)
    if a=="<class 'obj_inimigo.objinimigo'>":
      print("ATK de:",usuario.nome,"aumentado em",int((usuario.ataquefisico/10)+1))
    if a=="<class 'obj_personagem.objpersonagem'>":
      print("ATK de:",usuario.nome,"aumentado em",int(((usuario.DES+usuario.FOR)/12)+2))

def Bola_De_Fogo(usuario,alvo1,alvo2=0,alvo3=0,alvo4=0):
  if alvo1==0:
    alvo1=obj_inimigo.objinimigo()
  if alvo2==0:
    alvo2=obj_inimigo.objinimigo()
  if alvo3==0:
    alvo3=obj_inimigo.objinimigo()
  if alvo4==0:
    alvo4=obj_inimigo.objinimigo()
  a=type(usuario)
  b=type(alvo1)
  c=type(alvo2)
  d=type(alvo3)
  e=type(alvo4)
  alvo1imune=funcoesrpg.ConferirImunidade(alvo1,"Fogo")
  alvo2imune=funcoesrpg.ConferirImunidade(alvo2,"Fogo")
  alvo3imune=funcoesrpg.ConferirImunidade(alvo3,"Fogo")
  alvo4imune=funcoesrpg.ConferirImunidade(alvo4,"Fogo")
  if usuario.MP<5:
    if a=="<class 'obj_inimigo.objinimigo'>":
      funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvo1)
    else:
      if b=="<class 'obj_personagem.objpersonagem'>":
        print("O Feitiço de",usuario.nome,"falhava por falta de mana!")
      else:
        funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvo1)
  else:
    usuario.MP=usuario.MP-5
    obj_personagem.verificarMP(usuario)
    print(usuario.nome,"Conjurava uma bola de fogo!")
    if alvo1.nome=="Troll":
      alvo1.regenerar=False
    if alvo2.nome=="Troll":
      alvo2.regenerar=False
    if alvo3.nome=="Troll":
      alvo3.regenerar=False
    if alvo4.nome=="Troll":
      alvo4.regenerar=False
    a,b,c,d,e=str(a),str(b),str(c),str(d),str(e)
    if a=="<class 'obj_personagem.objpersonagem'>":
      dano=int((((usuario.INT+usuario.SAB)/1.5)+usuario.DanoFoco)+5)
    if a=="<class 'obj_inimigo.objinimigo'>":
      dano=(usuario.ataquemagico)+5
    if alvo4.nome!=0:
      if e=="<class 'obj_personagem.objpersonagem'>":
        if dano-alvo4.DefesaMagica>0:
          alvo4.HP=alvo4.HP-(dano-alvo4.DefesaMagica)
          if alvo4imune==False:
            print(f"{alvo4.nome} recebeu {dano-alvo4.DefesaMagica} pontos de dano da Bola de fogo")
          else:
            print(alvo4.nome,"É imune a ataques de fogo!")
          obj_personagem.verificarHP(alvo4)
      if e=="<class 'obj_inimigo.objinimigo'>":
        if dano-alvo4.defesamagica>0:
          if alvo4imune==False:
            alvo4.HP=alvo4.HP-(dano-alvo4.defesamagica)
            print(f"{alvo4.nome} recebeu {dano-alvo4.defesamagica} pontos de dano da Bola de fogo")
            obj_inimigo.verificarHP(alvo4)
          else:
            print(alvo4.nome,"É imune a ataques de fogo!")
    if alvo3.nome!=0:
      if d=="<class 'obj_personagem.objpersonagem'>":
        if dano-alvo3.DefesaMagica>0:
          if alvo3imune==False:
            alvo3.HP=alvo3.HP-(dano-alvo3.DefesaMagica)
            print(f"{alvo3.nome} recebeu {dano-alvo3.DefesaMagica} pontos de dano da Bola de fogo")
            obj_personagem.verificarHP(alvo3)
          else:
            print(alvo3.nome,"é imune a ataques de fogo!")
      if d=="<class 'obj_inimigo.objinimigo'>":
        if dano-alvo3.defesamagica>0:
          if alvo3imune==False:
            alvo3.HP=alvo3.HP-(dano-alvo3.defesamagica)
            print(f"{alvo3.nome} recebeu {dano-alvo3.defesamagica} pontos de dano da Bola de fogo")
            obj_inimigo.verificarHP(alvo3)
          else:
            print(alvo3.nome,"é imune a ataques de fogo!")
    if alvo2.nome!=0:
      if c=="<class 'obj_personagem.objpersonagem'>":
        if dano-alvo2.DefesaMagica>0:
          if alvo2imune==False:
            alvo2.HP=alvo2.HP-(dano-alvo2.DefesaMagica)
            print(f"{alvo2.nome} recebeu {dano-alvo2.DefesaMagica} pontos de dano da Bola de fogo")
            obj_personagem.verificarHP(alvo2)
          else:
            print(alvo2.nome,"é imune a ataques de fogo!")
      if c=="<class 'obj_inimigo.objinimigo'>":
        if dano-alvo2.defesamagica>0:
          if alvo2imune==False:
            alvo2.HP=alvo2.HP-(dano-alvo2.defesamagica)
            print(f"{alvo2.nome} recebeu {dano-alvo2.defesamagica} pontos de dano da Bola de fogo")
            obj_inimigo.verificarHP(alvo2)
          else:
            print(alvo2.nome,"é imune a ataques de fogo!")
    if alvo1.nome!=0:
      if b=="<class 'obj_personagem.objpersonagem'>":
        if dano-alvo1.DefesaMagica>0:
          if alvo1imune==False:
            alvo1.HP=alvo1.HP-(dano-alvo1.DefesaMagica)
            print(f"{alvo1.nome} recebeu {dano-alvo1.DefesaMagica} pontos de dano da Bola de fogo")
            obj_personagem.verificarHP(alvo1)
          else:
            print(alvo1.nome,"é imune a ataques de fogo!")
      if b=="<class 'obj_inimigo.objinimigo'>":
        if dano-alvo1.defesamagica>0:
          if alvo1imune==False:
            alvo1.HP=alvo1.HP-(dano-alvo1.defesamagica)
            print(f"{alvo1.nome} recebeu {dano-alvo1.defesamagica} pontos de dano da Bola de fogo")
            obj_inimigo.verificarHP(alvo1)
          else:
            print(alvo1.nome,"é imune a ataques de fogo!")

def Surto_De_Acao(usuario,Inimigo1=0,Inimigo2=0,Inimigo3=0,Inimigo4=0,flag=False,player=0):
  a=str(type(usuario))
  if usuario.MP>1 or flag==True:
    if a=="<class 'obj_personagem.objpersonagem'>":
      print(usuario.nome,"ativa seu surto de ação!")
    custo=(usuario.MP/3)
    usuario.MP=int(usuario.MP-custo)
    obj_personagem.verificarMP(usuario)
    if a=="<class 'obj_personagem.objpersonagem'>":
      print("Defina sua Ação Duplicada!")
    if a=="<class 'obj_personagem.objpersonagem'>":
      acao=funcoesrpg.PedirAcao(usuario,True)
      if acao!="Bola De Fogo" and acao!="Dança Das Lâminas" and "Frenesi":
        alvo=funcoesrpg.PedirAlvo(usuario,Inimigo1,Inimigo2,Inimigo3,Inimigo4)
        funcoesrpg.RealizarAcao(usuario,acao,alvo)
        funcoesrpg.RealizarAcao(usuario,acao,alvo)
      else:
        print("Essa Habilidade não suporta essa magia!")
        usuario.MP=int(usuario.MP+custo)
        Surto_De_Acao(usuario,Inimigo1,Inimigo2,Inimigo3,Inimigo4)
    else:
      alvo=player
      if usuario.movimento1=="Frenesi":
        usuario.movimento1=0
      if usuario.movimento2=="Frenesi":
        usuario.movimento2=0
      if usuario.movimento3=="Frenesi":
        usuario.movimento3=0
      if usuario.movimento4=="Frenesi":
        usuario.movimento4=0
      funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvo)
      funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvo)
  else:
    if a=="<class 'obj_personagem.objpersonagem'>":
      print("O Surto de ação falha devido a falta de Mana!")
    else:
      alvo=player
      funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvo)

def Danca_Das_Laminas(usuario,alvo): #ONLYPLAYERSKILL
  a,b=str(type(usuario)),str(type(alvo))
  if usuario.MP>=4:
    if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_personagem.objpersonagem'>":
      dano=int((usuario.DES+usuario.INT+(usuario.FOR*(1/2)))+3-alvo.Defesa)
      return 0,0,0,0,0
    if a=="<class 'obj_inimigo.objinimigo'>" and b=="<class 'obj_personagem.objpersonagem'>":
      dano=int((usuario.ataquemagico+(usuario.ataquefisico*(2/5)))+1-alvo.Defesa)
      return 0,0,0,0,0
    if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_inimigo.objinimigo'>":
      dano=int((usuario.DES+usuario.INT+(usuario.FOR*1/2))+3-alvo.defesa)
    imune=funcoesrpg.ConferirImunidade(alvo,"Cortante")
    if a=="<class 'obj_personagem.objpersonagem'>":
      if usuario.armaelementaltipodano!="":
        imune=funcoesrpg.ConferirImunidade(alvo,usuario.armaelementaltipodano)
    if usuario.MP>4:
      usuario.MP=usuario.MP-4
      a,b,c,d,e=obj_adicionais.CriarEspadaVoadora(usuario,alvo)
      EspadaVoadora=obj_adicionais.EspadaVoadora(a,b,c,d,e)
      return a,b,c,d,e
    if imune==True:
      print("Você acerta seu ataque, e invoca uma espada voadora para lhe auxiliar, Mas o Inimigo é Imune a ataques cortantes!")
      usuario.MP=usuario.MP-4
      a,b,c,d,e=obj_adicionais.CriarEspadaVoadora(usuario,alvo)
      EspadaVoadora=obj_adicionais.EspadaVoadora(a,b,c,d,e)
      return a,b,c,d,e
    else:
      if dano>0:
        print("A dança das Lâminas lhe concede um aliado, que perfura em cheio as defesas de",alvo.nome,"causando",dano,"pontos de dano!")
        a,b,c,d,e=obj_adicionais.CriarEspadaVoadora(usuario,alvo)
        EspadaVoadora=obj_adicionais.EspadaVoadora(a,b,c,d,e)
        obj_inimigo.verificarHP(alvo)
        usuario.MP=usuario.MP-4
        alvo.HP=alvo.HP-dano
        return a,b,c,d,e
      else:
        print("A dança das Lâminas lhe concede uma espada aliada, mas ela não é capaz de perfurar as defesas do",alvo.nome)
        a,b,c,d,e=obj_adicionais.CriarEspadaVoadora(usuario,alvo)
        EspadaVoadora=obj_adicionais.EspadaVoadora(a,b,c,d,e)
        usuario.MP=usuario.MP-4
        return a,b,c,d,e
  else:
    if a=="<class 'obj_inimigo.objinimigo'>":
      funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvo)
      return 0,0,0,0,0
    else:
      print("A Dança das Lâminas falhava devido a falta de MP!")
      return 0,0,0,0,0
  

def Defesa_Espada(usuario):
  a=str(type(usuario))
  if a=="<class 'obj_adicionais.EspadaVoadora'>":
    if usuario.mestre.MP>2:
      usuario.mestre.MP=usuario.mestre.MP-2
      protegido=usuario.mestre
      bonus=int(usuario.dano**1/2)
      print("A espada voadora passava a te proteger, aumentando sua prontidão para aparar ataques!, Bônus de Defesa:",bonus)
    else:
      print("A Defesa falhou por falta de Mana!")
  else:
    if usuario.MP>2:
      usuario.MP=usuario.MP-2
      if a=="<class 'obj_personagem.objpersonagem'>":
        protegido=usuario
      if a=="<class 'obj_inimigo.objinimigo'>":
        protegido=usuario
      bonus=round(int(usuario.CON**1/2)-0.49)
      print("Você serrava sua espada, preparando-se para aparar ataques, aumentando sua Defesa física em",bonus,"pontos.")
    else:
      print("A Defesa falhou por falta de Mana!")

def Frenesi(usuario,alvo1=0,alvo2=0,alvo3=0,alvo4=0,alvofrenesiinimigo=0):
  a=str(type(usuario))
  if a=="<class 'obj_personagem.objpersonagem'>":
    if usuario.MP>=usuario.MPMax/2:
      usuario.MP=0
      print("Uma aura vermelha passava a se irradiar de",usuario.nome)
      usuario.FOR=int(usuario.FOR*1.5)
      usuario.CON=int(usuario.CON*1.5)
      obj_personagem.resetarValores(usuario)
      flag=True
      if usuario.movimento1=="Frenesi":
        usuario.movimento1=0
      if usuario.movimento2=="Frenesi":
        usuario.movimento2=0
      if usuario.movimento3=="Frenesi":
        usuario.movimento3=0
      if usuario.movimento4=="Frenesi":
        usuario.movimento4=0
      if usuario.movimento5=="Frenesi":
        usuario.movimento5=0
      if usuario.movimento6=="Frenesi":
        usuario.movimento6=0
      Surto_De_Acao(usuario,alvo1,alvo2,alvo3,alvo4,flag)
    else:
      print("O Frenesi falhava por falta de Mana!")
  else:
    if a=="<class 'obj_inimigo.objinimigo'>":
      if usuario.MP>0:
        print("Uma aura de calor começava a irradiar dos olhos do",usuario.nome,"era possível notar uma fúria emergindo do fundo de sua alma!")
        usuario.MP=0
        usuario.ataquefisico=int(usuario.ataquefisico*1.5)
        usuario.defesafisica=int(usuario.defesa*1.4)
        funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvofrenesiinimigo)
      else:
        funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvofrenesiinimigo)

def Sangue_Suga(usuario,alvo):
  a,b=str(type(usuario)),str(type(alvo))
  imune=funcoesrpg.ConferirImunidade(alvo,"Necrótico")
  if usuario.MP>3:
    if a=="<class 'obj_inimigo.objinimigo'>" and b=="<class 'obj_personagem.objpersonagem'>":
      dano=int((usuario.ataquefisico)+3-((alvo.Defesa+alvo.DefesaMagica)/4))
    if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_personagem.objpersonagem'>":
      dano=int((usuario.FOR/2+usuario.DES/2)+3-((alvo.Defesa+alvo.DefesaMagica)/4))
    if a=="<class 'obj_personagem.objpersonagem'>" and b=="<class 'obj_inimigo.objinimigo'>":
      dano=int((usuario.FOR/2+usuario.DES/2)+3-(alvo.defesa/4+alvo.defesamagica/4))
    rand=random.randint(1,3)
    if dano>0 and imune==False:
      if int(dano/8)>0:
        print(alvo.nome,"sentia sua vida se esvaindo, perdendo",int(dano/8),"pontos de CON.")
      print(usuario.nome,"causa a",alvo.nome,dano,'pontos de dano com "Sangue-Suga", se curando em',int(dano/4),'pontos de HP.')
      alvo.HP=int(alvo.HP-dano)
      usuario.HP=int(usuario.HP+dano/4)
      if b=="<class 'obj_personagem.objpersonagem'>":
        if rand==3:
          alvo.CON=int(alvo.CON-dano/8)
          alvo.HPMax=9+alvo.CON
      if b=="<class 'obj_inimigo.objinimigo'>":
        if rand==3:
          alvo.HPMax=int(alvo.HPMax-dano/8)
    else:
      if imune==True:
        print(alvo.nome,"é imune a dano Necrótico.")
      else:
        print('A defesa de',alvo.nome,'o protege de "Sangue Suga"')
    if b=="<class 'obj_personagem.objpersonagem'>":
      obj_personagem.verificarHP(alvo)
    if b=="<class 'obj_inimigo.objinimigo'>":
      obj_inimigo.verificarHP(alvo)
    if a=="<class 'obj_inimigo.objinimigo'>":
      obj_inimigo.verificarHP(usuario)
    if a=="<class 'obj_personagem.objpersonagem'>":
      obj_personagem.verificarHP(usuario)
  else:
    if a=="<class 'obj_inimigo.objinimigo'>":
      funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvo)
    if a=="<class 'obj_personagem.objpersonagem'>":
      print('"Sangue-Suga" falha por falta de Mana!')
  
def Transformacao_Bruxa(usuario,player):
  a=str(type(usuario))
  if usuario.MP>=(usuario.MPMax/2):
    print(usuario.nome,"Começava a se transformar em uma criatura horrivel, de pele negra e coberta por óleo e sangue, ela gritava em agonia enquanto seu corpo crescia de tamanho, garras negras tomavam o lugar de suas unhas, até que finalmente tomava a forma de uma Bruxa da Noite!")
    if a=="<class 'obj_personagem.objpersonagem'>":
      usuario.FOR=int(usuario.FOR+(usuario.INT/4))
      usuario.DES=int(usuario.DES+(usuario.SAB/4))
      usuario.CON=int(usuario.CON+((usuario.INT/5)+(usuario.SAB/5)))
      usuario.INT=usuario.INT/4
      usuario.SAB=usuario.SAB/3
      usuario.MP=0
      usuario.HPMax=9+usuario.CON
      usuario.Defesa=int(usuario.Defesa+usuario.INT)
      usuario.DefesaMagica=int(usuario.DefesaMagica+usuario.SAB)
    if a=="<class 'obj_inimigo.objinimigo'>":
      usuario.HP=int(usuario.HP+usuario.ataquemagico/4)
      usuario.HPMax=int(usuario.HPMax+usuario.ataquemagico/3)
      usuario.defesa=usuario.defesa+int(usuario.ataquemagico/4)
      usuario.defesamagica=int(usuario.defesamagica-usuario.ataquemagico/4)
      usuario.ataquemagico=0
      usuario.MP=0
      usuario.movimento1="Arranhar"
      usuario.movimento2="Mordida"
  else:
    if a=="<class 'obj_personagem.objpersonagem'>":
      print("A Tranformação Falhava por falta de Mana!")
    if a=="<class 'obj_inimigo.objinimigo'>":
      funcoesrpg.randomizar_executar_acao_inimigo(usuario,player)

def Transformar_Lobisomem(usuario,player):
  a=str(type(usuario))
  rand=random.randint(1,10)
  if a=="<class 'obj_inimigo.objinimigo'>":
    if rand==10:
      print("O Lobo começava a se contorcer, lentamente sua pele se rasgava, você ouvia ossos quebrando, lá de dentro, saía um Lobisomem, completamente ensanguentado!")
      usuario.nome="Lobisomem"
      usuario.imunidades="Perfurante Cortante Concussivo"
      usuario.HPMax=int(usuario.HPMax*1.8)
      usuario.HP=usuario.HPMax
      usuario.ataquefisico=int(usuario.ataquefisico*1.5)
      usuario.movimento1="Arranhar"
      usuario.movimento2="Mordida"
      usuario.movimento3="Surto De Ação"
      usuario.movimento4="Frenesi"
      usuario.dificuldade=3
      Arranhar(usuario,player)
    else:
      funcoesrpg.randomizar_executar_acao_inimigo(usuario,player)
  elif a=="<class 'obj_personagem.objpersonagem'>":
    print(usuario.nome,"Começava a se contorcer, lentamente sua pele se rasgava, ossos se quebravam, aos poucos sua caixa toráxica se expandia, pelos emergiam de sua pele, um focinho crescia em seu rosto, tomando a forma de um Lobisomem!")
    usuario.FOR+=int(usuario.FOR*1/3)
    usuario.CON+=int(usuario.CON*1/3)
    usuario.DES+=int(usuario.DES*1/6)
    usuario.INT-=int(usuario.INT*1/1.75)
    usuario.SAB-=int(usuario.SAB*1/4)
    usuario.CAR-=int(usuario.CAR*1/1.3)
    usuario.HPMax=usuario.CON+9
    usuario.HP+=int(usuario.HPMax*1/4)
    usuario.MP=int(usuario.MP/2.4)
    usuario.movimento5="Arranhar"
    usuario.movimento6="Mordida"
    usuario.movimento7="Surto De Ação"
    usuario.movimento8="Frenesi"
    obj_personagem.verificarHP(usuario)
    usuario.MP=0

def Golpe_Espiral(usuario,alvo1,alvo2=0,alvo3=0,alvo4=0):
  danoextra=0
  if alvo1==0:
    alvo1=obj_inimigo.objinimigo()
  if alvo2==0:
    alvo2=obj_inimigo.objinimigo()
  if alvo3==0:
    alvo3=obj_inimigo.objinimigo()
  if alvo4==0:
    alvo4=obj_inimigo.objinimigo()
  a=str(type(usuario))
  b=str(type(alvo1))
  c=str(type(alvo2))
  d=str(type(alvo3))
  e=str(type(alvo4))
  alvo1imune=funcoesrpg.ConferirImunidade(alvo1,"Cortante")
  alvo2imune=funcoesrpg.ConferirImunidade(alvo2,"Cortante")
  alvo3imune=funcoesrpg.ConferirImunidade(alvo3,"Cortante")
  alvo4imune=funcoesrpg.ConferirImunidade(alvo4,"Cortante")
  if a=="<class 'obj_personagem.objpersonagem'>":
    if usuario.armaelementalativa==True:
      alvo1imune=funcoesrpg.ConferirImunidade(alvo1,usuario.armaelementaltipodano)
      alvo2imune=funcoesrpg.ConferirImunidade(alvo2,usuario.armaelementaltipodano)
      alvo3imune=funcoesrpg.ConferirImunidade(alvo3,usuario.armaelementaltipodano)
      alvo4imune=funcoesrpg.ConferirImunidade(alvo4,usuario.armaelementaltipodano)
  if usuario.MP<2:
    if a=="<class 'obj_inimigo.objinimigo'>":
      funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvo1)
    else:
      funcoesrpg.randomizar_executar_acao_inimigo(usuario,alvo1)
  else:
    usuario.MP=usuario.MP-2
    obj_personagem.verificarMP(usuario)
    print(usuario.nome,"Realizava um Golpe Espiral!")
    a,b,c,d,e=str(a),str(b),str(c),str(d),str(e)
    if a=="<class 'obj_personagem.objpersonagem'>":
      dano=int((((usuario.FOR/1.8)+(usuario.DES/2.2))+usuario.DanoArma/1.6)+2)
      if usuario.armaelementalativa==True:
        dano+=int(usuario.INT/3.1+usuario.SAB/4.3)
    if a=="<class 'obj_inimigo.objinimigo'>":
      dano=(usuario.ataquefisico)+1
    if alvo4.nome!=0:
      if e=="<class 'obj_personagem.objpersonagem'>":
        if dano-alvo4.Defesa>0:
          if usuario.armaelementalativa==True:
            if usuario.armaelementaltipodano=="Fogo" and alvo4.nome=="Troll":
              alvo4.regenerar=False
          alvo4.HP=alvo4.HP-(dano-alvo4.Defesa)
          if alvo4imune==False:
            print(f"{alvo4.nome} recebeu {dano-alvo4.Defesa} pontos de dano de Golpe Espiral!")
          else:
            print(alvo4.nome,"É imune a ataques cortantes!")
          obj_personagem.verificarHP(alvo4)
      if e=="<class 'obj_inimigo.objinimigo'>":
        if dano-alvo4.defesa>0:
          if usuario.armaelementalativa==True:
            if usuario.armaelementaltipodano=="Fogo" and alvo4.nome=="Troll":
              alvo4.regenerar=False
          if alvo4imune==False:
            alvo4.HP=alvo4.HP-(dano-alvo4.defesa)
            print(f"{alvo4.nome} recebeu {dano-alvo4.defesa} pontos de dano de Golpe Espiral!")
            obj_inimigo.verificarHP(alvo4)
          else:
            print(alvo4.nome,"É imune a ataques cortantes!")
    if alvo3.nome!=0:
      if d=="<class 'obj_personagem.objpersonagem'>":
        if dano-alvo3.Defesa>0:
          if alvo3imune==False:
            alvo3.HP=alvo3.HP-(dano-alvo3.Defesa)
            print(f"{alvo3.nome} recebeu {dano-alvo3.Defesa} pontos de dano de Golpe Espiral!")
            obj_personagem.verificarHP(alvo3)
          else:
            print(alvo3.nome,"é imune a ataques cortantes!")
      if d=="<class 'obj_inimigo.objinimigo'>":
        if dano-alvo3.defesa>0:
          if usuario.armaelementalativa==True:
            if usuario.armaelementaltipodano=="Fogo" and alvo3.nome=="Troll":
              alvo3.regenerar=False
          if alvo3imune==False:
            alvo3.HP=alvo3.HP-(dano-alvo3.defesa)
            print(f"{alvo3.nome} recebeu {dano-alvo3.defesa} pontos de dano do Golpe Espiral!")
            obj_inimigo.verificarHP(alvo3)
          else:
            print(alvo3.nome,"é imune a ataques cortantes!")
    if alvo2.nome!=0:
      if c=="<class 'obj_personagem.objpersonagem'>":
        if dano-alvo2.Defesa>0:
          if alvo2imune==False:
            alvo2.HP=alvo2.HP-(dano-alvo2.Defesa)
            print(f"{alvo2.nome} recebeu {dano-alvo2.Defesa} pontos de dano de Golpe Espiral!")
            obj_personagem.verificarHP(alvo2)
          else:
            print(alvo2.nome,"é imune a ataques cortantes!")
      if c=="<class 'obj_inimigo.objinimigo'>":
        if dano-alvo2.defesa>0:
          if usuario.armaelementalativa==True:
            if usuario.armaelementaltipodano=="Fogo" and alvo2.nome=="Troll":
              alvo2.regenerar=False
          if alvo2imune==False:
            alvo2.HP=alvo2.HP-(dano-alvo2.defesa)
            print(f"{alvo2.nome} recebeu {dano-alvo2.defesa} pontos de dano de Golpe Espiral!")
            obj_inimigo.verificarHP(alvo2)
          else:
            print(alvo2.nome,"é imune a ataques cortantes!")
    if alvo1.nome!=0:
      if b=="<class 'obj_personagem.objpersonagem'>":
        if dano-alvo1.Defesa>0:
          if alvo1imune==False:
            alvo1.HP=alvo1.HP-(dano-alvo1.Defesa)
            print(f"{alvo1.nome} recebeu {dano-alvo1.Defesa} pontos de dano de Golpe Espiral!")
            obj_personagem.verificarHP(alvo1)
          else:
            print(alvo1.nome,"é imune a ataques cortantes!")
      if b=="<class 'obj_inimigo.objinimigo'>":
        if dano-alvo1.defesa>0:
          if usuario.armaelementalativa==True:
            if usuario.armaelementaltipodano=="Fogo" and alvo1.nome=="Troll":
              alvo1.regenerar=False
          if alvo1imune==False:
            alvo1.HP=alvo1.HP-(dano-alvo1.defesa)
            print(f"{alvo1.nome} recebeu {dano-alvo1.defesa} pontos de dano do Golpe Espiral!")
            obj_inimigo.verificarHP(alvo1)
          else:
            print(alvo1.nome,"é imune a ataques cortantes!")

def ArmaElemental(usuario):#PLAYERONLY SKILL
  if usuario.MP>=1:
    usuario.MP=usuario.MP-1
    elemento=(input("Selecione um Elemento: 1-Raio 2-Fogo 3-Gelo"))
    while elemento!='1' and elemento!='2' and elemento!='3':
      elemento=(input("Selecione um Elemento: 1-Raio 2-Fogo 3-Gelo"))
    elemento=int(elemento)
    if elemento==1:
      texto="Trovão"
      usuario.armaelementaltipodano="Trovejante"
    if elemento==2:
      texto="Fogo"
      usuario.armaelementaltipodano="Fogo"
    if elemento==3:
      texto="Gelo"
      usuario.armaelementaltipodano="Frio"
    print(usuario.nome,"embuia sua arma com os poderes do",texto)
    usuario.armaelementalativa=True
  else:
    print("A Magia falhava por falta de Mana!")


  


'''
def Transformacao_Homem_Corvo(usuario,player)
def Raio_De_Bruxa(usuario,alvo):
def Vida_Falsa(usuario):
def Drenar_Alma(usuario,alvo):
def MisseisMagicos(usuario,alvo1,alvo2=alvo1,alvo3=alvo2):
def RaioFlamejante(usuario,alvo1,alvo2=alvo1,alvo3=alvo2):
def BeberPocao(usuario):
def Fugir(usuario):,
'''
