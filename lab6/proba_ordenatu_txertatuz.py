def idatzi_bektorea(L):
#jarri kodea
    
def eskuinera_mugitu_posetik(L,posHas,posBuk):
#aurre: posHas <= posBuk
#post: posHas-etik posBuk-era dauden elementu guztiak eskmara desplazauak izan dira
#gogoratu eskumara desplazatzeko eskumatik hasi
#jarri kodea  
    return(L);

def txertatu_zenbakia_pos(L,egungoPos,posean):
#aurre: egungoPos >= posean
#post: egungoPos-ean dagoen elementua posean txertatuta geldituko da
#      horretarako egungoPos-eko elementua aux batetan gorde eta eskuinera desplazatu posetik egungoPosera dauden elemtuak
#jarri kodea
    aux=????
    L=eskuinera_mugitu_posetik(??????);
    ??????
    ?????
    return(L);

def txertatzeko_posizioa_bilatu(L,egungoPos):
#aurre: egungoPos < len(L)
#post: egungo elementuaren posizioa eta bektorea emanda esan ze posizioan txertatu beharko litzatekeen egungo elementua bueltatuko du
#      0 <=emaitza <=egungoPos 
#gogoratu Python-ez bektoreen lehenengo posizioa 0 dela
#jarri kodea
        ?????
        
def ordenatu_txertatuz(L):
#jarri kodea
    ????
    
    return(L);

def proba_ordenatu_txertatuz():
     #1. poba kasua
     bektor1 = [9, 5, 3, 4, 10, 8, 13, 24, 15, 11]
     
     print("Sarrerako bektorea (9,5,3,4,10,8,13,24,15,11):")
     idatzi_bektorea(bektor1)

     bektor1=ordenatu_txertatuz(bektor1)
     print("emaitza egokia (3,4,5,8,9,10,11,13,15,24) da eta zure azpiprogramak :")
     idatzi_bektorea(bektor1)
     print(" lortzen du")
     
     #beste proba kasurik

proba_ordenatu_txertatuz();
