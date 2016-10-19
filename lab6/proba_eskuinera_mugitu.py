def idatzi_Lista(L):
#Sarrera: zenbaki osoz eratutako array bat
#Aurre:-
#Irteera: array eratzen duten elementuak pantailaratuko dira
#Post:
    for ind in ...
       


def eskuinera_mugitu_posetik(L,posHas,posBuk):
#aurre: posHas <= posBuk
#post: posHas-etik posBuk-era dauden elementu guztiak eskmara desplazauak izan dira
#gogoratu eskumara desplazatzeko eskumatik hasi
#jarri kodea  
    return(L);
   

def proba_eskuinera_mugitu():     
    #10 elementuzko zerrenda batekin
    Lista1=[1,2,3,4,5,6,7,8,9,10];
 
    print("1 kasua: 10 elementuko zerrenda bat: \n [1,2,3,4,5,6,7,8,9,10]");
    print(" Hasierako zerrendaren elementuak hauek dira: ");
    idatzi_Lista(Lista1);

    print("eta zure programak atera beharko luke [1,2,3,4,5,5,6,7,9,10]");
    #ohartu 8 zapaldu dela eta 0an hasten direla posizioak
    Lista1=eskuinera_mugitu(Lista1,4,7);
    idatzi_Lista(Lista1);
    
    #proba kasu gehiago
proba_eskuinera_mugitu();
