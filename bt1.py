def getHijos(edo ,proble):
    return proble[edo]

def siguiente(lEdos ,lTabu ,hs):
    hmejor =1000
    mejor=' '
    listo=False
    indi=0
    donde=0
    for edo in lEdos:
        if hs[edo]<hmejor:
            mejor=edo
            hmejor=hs[edo]
            donde=indi
        indi=indi+1
    if mejor not in lTabu:
        soln=(mejor ,hmejor)
    else:
        del lEdos[donde]
        soln=siguiente(lEdos ,lTabu ,hs)
    return soln

def tabu(actual ,lTabu ,proble ,hs):
    print(actual)
    hactual=hs[actual]
    hijos=getHijos(actual ,proble)
    nuevo ,hnuevo=siguiente(hijos ,lTabu ,hs)
    if hactual <hnuevo:
        soln=actual
    else:
        lTabu.append(actual)
        soln=tabu(nuevo,lTabu,proble,hs)
    return soln

def main():
    """
    proble={'A':['B','C','D'],'B':['A','C','E'],'C':['A','B','D','E'],
    'D':['A','C','F'],'E':['B','C','F'],'F':['D','E']}
    hs={'A':45,'B':40,'C':35,'D':37,'E':23,'F':15}
    """
    proble={
        'A':['B','C','D','E','F'],
        'B':['A','C'],
        'C':['A','B','D','G','H'],
        'D':['A','C','E','I'],
        'E':['A','D','F','J','K'],
        'F':['A','E'],
        'G':['C','H'],
        'H':['C','G','I','L'],
        'I':['D','H','J','L','M'],
        'J':['E','I','K','Ñ'],
        'K':['E','J'],
        'L':['H','I','M','O'],
        'M':['I','L','N','O'],
        'N':['I','M','Ñ','O'],
        'Ñ':['J','N'],
        'O':['L','M','N']
    }
    hs={'A':10,'B':10,'C':10.5,'D':10.25,'E':8,'F':12,'G':9,
    'H':7.5,'I':10,'J':12.25,'K':12,'L':9,'M':7,'N':10,'Ñ':11,
    'O':8.5
    }
    inicial=input("Dame el nodo de inicio: ")
    soln=tabu(inicial,[],proble ,hs)
    print('SOLUCION ENCONTRADA:'+soln)

if __name__ =='__main__':
    main()

