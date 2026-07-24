import random
import datetime
def lotofacil():
    num = []
    cont = 0
    sai = 0
    while cont < 25:
        cont = cont + 1
        num.append(cont)
    while sai < 10:
        sai = sai + 1
        num.remove(random.choice(num))
    #print(num)
    jog.write('\nLotofacil\n'+str(num)+'\n')
    return num

def lotomania():
    num = []
    cont = 0
    sai = 0
    while cont < 100:
        cont = cont + 1
        num.append(cont)
    while sai < 50:
        sai = sai + 1
        num.remove(random.choice(num))
    jog.write('\nLotomania\n'+str(num)+'\n')
    return num

def mega_sena():
    num = []
    cont = 0
    sai = 0
    while cont < 60:
        cont = cont + 1
        num.append(cont)
    while sai < 54:
        sai = sai + 1
        num.remove(random.choice(num))
    jog.write('\nMega Sena\n'+str(num)+'\n')
    return num

def dupla_sena():
    num = []
    cont = 0
    sai = 0
    while cont < 50:
        cont = cont + 1
        num.append(cont)
    while sai < 44:
        sai = sai + 1
        num.remove(random.choice(num))
    jog.write('\nDupla Sena\n'+str(num)+'\n')
    return num

def dia_de_sorte():
    num = []
    mes = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    cont = 0
    sai = 0
    while cont < 31:
        cont = cont + 1
        num.append(cont)
    while sai < 24:
        sai = sai + 1
        num.remove(random.choice(num))
    m = random.choice(mes)
    jog.write('\nDia de Sorte\n'+str(num)+' Mes: '+m+'\n')
    return num
    

def quina():
    num = []
    cont = 0
    sai = 0
    while cont < 80:
        cont = cont + 1
        num.append(cont)
    while sai < 75:
        sai = sai + 1
        num.remove(random.choice(num))
    jog.write('\nQuina\n'+str(num)+'\n')
    return num  


def swith(case):
    match case:
        case 1:
            x = 0
            while x < int(jogos['Lotofacil']):
                print(lotofacil())
                x = x + 1
            return '-------------------------------------------------------'
            
        case 2:
            x = 0
            while x < int(jogos['Lotomania']):
                print(lotomania())
                x = x + 1
            return '-------------------------------------------------------'
            
        case 3:
            x = 0
            while x < int(jogos['Mega Sena']):
                print(mega_sena())
                x = x + 1
            return '-------------------------------------------------------'
            
        case 4:
            x = 0
            while x < int(jogos['Dupla Sena']):
                print(dupla_sena())
                x = x + 1
            return '-------------------------------------------------------'
            
        case 5:
            x = 0
            while x < int(jogos['Dia de Sorte']):
                print(dia_de_sorte())
                x = x + 1
            return '-------------------------------------------------------'
            
        case 6:
            x = 0
            while x < int(jogos['Quina']):
                print(quina())
                x = x + 1
            return '-------------------------------------------------------'
            
        case 7:
            return 0


def faz_jogo():#preenche o dicionário com os jogos e as quantidades
    contador = 1#incrementa valores inteiros ao dicionário tab
    total = 0#calcula a soma dos valores dos jogos escolhidos
    valor = {'Lotofacil':3.5,'Lotomania':3,'Mega Sena':6,'Dupla Sena':3,'Dia de Sorte':2.5,'Quina':3}
    for key in valor:#adiciona valores tipo string ao dicionário jogos usando as chaves do dicionário valor
        jogos[key] = input('\nDigite o nº de jogos:'+key+'\t')
        if jogos[key] != '0':
           tab[key] = contador 
           total = total + int(jogos[key])*valor[key]
        else:
            tab[key] = 0
        contador = contador + 1
    for key in tab:
        if tab[key] != 0:
            print(swith(tab[key]))
    jog.write('\nO total é: '+str(total))
    print('\nO total é: ',total)
    
global jog
t = '.txt'#adicionar a extenção à string concatenada
agora = datetime.datetime.now()#guarda a data e o tempo desse momento
formato = agora.strftime('%d-%m-%y_%H-%M-%S')#formata a data guardada em agora no estilo entre parêntesis
p = formato+t#concatena as strings para se encaixar no estilo arquivo.txt
jog = open(p,'w')#abre gravação do arquivo.txt
def jogo():
    global total
    global contador
    global valor
    global tab
    global jogos#dicionário para receber o tipo e a quantidade de jogos
    jogos = dict()
    tab = dict()#dicionário com os jogos válidos para acionar o switch
    faz_jogo()
    jog.close()#fecha a gravação do arquivo
   
jogo()
