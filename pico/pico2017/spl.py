benedick = 0
beatrice = 0
donpedro = 0
donjohn = 0
achilles = 0
cleopatra = 0
benedicks = []
beatrices = []
donpedros = []
donjohns = []
achilless = []
cleopatras = []


#beatrice/donjohn
donjohn = 0
#exitdonjohn/enterdonpedro
donpedro = 0
#exitdonpedro/enterachilles
achilles = 1*2**5
#exitachilles/entercleopatra
cleopatra = 1*2**7-achilles#96
#exitcleopatra/enterbenedick
benedick = 0

inputs = [32,116,97-64,48,76+32,112,88+32,51,83+32,116,72+32,103,73+32,78,82+32,51,77+32,77,85+32,83,68+32,105,45+32,64,83,116,41+32]
copy = inputs[::]
#act2
while 1:
    
    benedick = inputs.pop()
    benedicks.append(benedick)
    
    beatrice += 1
    if(benedick == 2**5):
        break
beatrice += 1
benedick = benedicks.pop()#get rid of the 32

#act3
#
while 1:
    benedick = benedicks.pop() - achilles
    beatrice = beatrice - 1#assuming flirt-gill=negative
    #exitbeatrice/enterdonjohn
    donjohn = benedick
    #exitdonjohn/enterdonpedro
    benedick = donpedro+benedick
    benedick = benedick % cleopatra
    #exitbenedick/enterdonjohn
    donpedro = donjohn
    #exitall
    #enterbeatrice/enterbenedick
    benedick = benedick+achilles
    print chr(benedick),
    if len(benedicks)==0:
        break



        



