import pandas as pd
import openpyxl

fservicio =0
def init():
    while True:
        try:
            fservicio = float(input("digite el factor de servicio entre 1 y 3: "))
        except ValueError:
            print ("Solo se adminten números")   
            continue
        if (fservicio >=1 and fservicio <=3):
            cal(fservicio)
        else:
            print("El factor de servicio no coincide con los requerimentos")
        init()
def cal (parametro):
    while True:
        try:
            caudal = float(input("digite caudal: "))  
        except ValueError:
            print ("Solo se adminten números")   
            continue
        break
    while True:
        try:
            tentrada = float(input("digite temperatura de entrada: "))  
        except ValueError:
            print ("Solo se adminten números")   
            continue
        break
    while True:
        try:
            tsalida = float(input("digite temperatura de salida: "))  
        except ValueError:
            print ("Solo se adminten números")   
            continue
        break    
    cons1 = 1000
    cons2 = 0.0003069
    
    tdt = round (caudal*(tentrada - tsalida)*parametro*cons1*cons2)
    print ("el distrito mide: ", tdt, '\n')
    chillers(tdt)
def chillers (tamt):
    print ("\n Tamaños de chillers centrifugos y de adsorcion 500TR, 750TR, 1000TR \n")
    print ("Por favor leer con detenimiento e indicar la cantidad \n")
    print ("______________________________________________________________________ \n")

    while True:
        try:
            c500= int(input("Digite la cantidad para 500TR centrifugos: "))  
        except ValueError:
            print ("Solo se adminten números")   
            continue 
        if c500 < 0:
            print("Solo se adminten numeros positivos")
            continue
        else:
            break 
    while True:
        try:
            c750= int(input("Digite la cantidad para 750TR centrifugos: "))  
        except ValueError:
            print ("Solo se adminten números")   
            continue
        if c750 < 0:
            print("Solo se adminten numeros positivos")
            continue
        else:
            break
    while True:
        try:
            c1000= int(input("Digite la cantidad para 1000TR centrifugos: "))  
        except ValueError:
            print ("Solo se adminten números")   
            continue
        if c1000 < 0:
            print("Solo se adminten numeros positivos")
            continue
        else:
            break
    while True:
        try:
            a500= int(input("Digite la cantidad para 500TR absorción: "))  
        except ValueError:
            print ("Solo se adminten números")   
            continue
        if a500 < 0:
            print("Solo se adminten numeros positivos")
            continue
        else:
            break
    while True:
        try:
            a750= int(input("Digite la cantidad para 750TR absorción: "))  
        except ValueError:
            print ("Solo se adminten números")   
            continue
        if a750 < 0:
            print("Solo se adminten numeros positivos")
            continue
        else:
            break
    while True:
        try:
            a1000= int(input("Digite la cantidad para 1000TR absorción: ")) 
        except ValueError:
            print ("Solo se adminten números")   
            continue
        if a1000 < 0:
            print("Solo se adminten numeros positivos")
            continue
        else:
            break   
    #operacion para calcular los tr centrifugos y tr absorcion 

    totalc=(500*c500)+(750*c750)+(1000*c1000)
    totala=(500*a500)+(750*a750)+(1000*a1000)
    total=totalc + totala

    #comprobacion del tamaño maximo de TR
    tmax= tamt + (tamt*0.5)

    if total<=tamt:
        print ("Las tecnologias selecionadas no suministran el tamaño del DT \n")
        print ("_____________________________________________________________\n")
        chillers(tamt)
    elif total>=tmax: 
        print ("Las tecnologias selecionadas superan el tope del DT \n")
        print ("_____________________________________________________________\n")
        chillers(tamt)
    else : 
        centrifugos(totalc)
        absorcion(totala)

def centrifugos(parametro1):
    rp=parametro1*0.3190995427365
    g=(parametro1*511.13199046407)/1000
    c=(parametro1*0.0035174111853)*(1925000/0.88)
    o=c*0.3

    capex=parametro1*0.0035174111853
    ft=capex*1000000
    e=capex*1700000
    b=capex*2000000
    # Se crea la tabla centrífugos

    centrifu = {'Energia': ['Red Publica', 'Microturbina Gas', 'Solar Foto Voltaica', 'Energia Eolica','Energia Biomasa','TR de los chillers centrifugos es:'],
              'Emisiones CO2(tco2 al mes)':[e,rp,b,ft,c,0.0003069],
                'CAPEX(dolares megavatios)':[g,o,b,ft,capex,""],
            'opex(do-año)': [ft,rp,e,c,g,1000]}
    tc = pd.DataFrame(centrifu)
    print("__________________________________________________________ \n")

    #exportar excel
    tc.to_excel ('D:\Usuario\Desktop\Ing. de Sistemas\Octavo Semestre/Linea de enfasis /centrifugo.xlsx',index=False)
    
    print(tc)

    crearTablas('centrifu')

def absorcion(parametro2):
    g=(parametro2*511.13199046407)/1000
    c=((parametro2*0.0035174111853)*(1925000/0.88)) 
    o=c*0.3

    capex=parametro2*0.0035174111853
    ft=(capex*1000000)*1.015
    b=capex*2000000
    # Se crea la tabla absorción

    abso= {'Energia': ['Microturbina Gas', 'Solar Termica', 'Energia biomasa', 'TR de los chillers de absorcion es:'],
             'Emisiones CO2(TCO2 al mes)':[g,capex,b,""],
             'Capex(dolares megavatios)':[g,capex,b,""],
            'Opex (do-año)': [g,capex,b,1000] 
            }
    tablaabsor = pd.DataFrame(abso)
    print("__________________________________________________________ \n")
    
    #exportar excel
    tablaabsor.to_excel ('D:\Usuario\Desktop\Ing. de Sistemas\Octavo Semestre/Linea de enfasis/absorcion.xlsx',index=False)
    
    print(tablaabsor)		
    crearTablas('abso')

def crearTablas(resp):
    if resp=='centri':
        print("\n Tabla centrifugos")
    elif resp=='abso':       
        print("\n Tabla de absorcion")        

init()    