from _ast import Num
#
# Hamartarretik bitarrera. Irakasleak emaniko funtzioa.
#
def hamartarretik_bitarrera(num):
    aux=num
    bitar=0
    kont=0
    
    while aux >= 1:
        bitar += aux % 2 * (10**kont)
        aux = aux / 2
        kont += 1
    
    return(bitar)

#
# Ni neuk idatzitako funtzioa, zeinek aldagai bat gutxiago erabiltzen duen.
#
def hamartarretik_bitarrera_jon(num):
    aux=num
    bitar=""
    
    while aux >= 1:
        bitar = str(aux % 2) + bitar
        aux = aux / 2
        
    return(bitar)

#
# Main funtzioa.
#
def proba():
    #1. Proba
    hamartar=1
    emaitza=hamartarretik_bitarrera_jon(hamartar)
    pantaila='Hamartarra ' + str(hamartar) + ' da eta programak 1 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)
    #2. Proba
    hamartar=2
    emaitza=hamartarretik_bitarrera_jon(hamartar)
    pantaila='Hamartarra ' + str(hamartar) + ' da eta programak 10 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)
    #3. Proba
    hamartar=5
    emaitza=hamartarretik_bitarrera_jon(hamartar)
    pantaila='Hamartarra ' + str(hamartar) + ' da eta programak 101 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)
    #3. Proba
    hamartar=24
    emaitza=hamartarretik_bitarrera_jon(hamartar)
    pantaila='Hamartarra ' + str(hamartar) + ' da eta programak 11000 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)
    #4. Proba
    hamartar=127
    emaitza=hamartarretik_bitarrera_jon(hamartar)
    pantaila='Hamartarra ' + str(hamartar) + ' da eta programak 1111111 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)
    #4. Proba
    hamartar=146
    emaitza=hamartarretik_bitarrera_jon(hamartar)
    pantaila='Hamartarra ' + str(hamartar) + ' da eta programak 10010010 bueltatu behar du. '+str(emaitza)+' bueltatzen du.'
    print(pantaila)

proba()
