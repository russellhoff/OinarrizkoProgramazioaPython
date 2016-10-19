def idatzi_lista(L):
    for ind in range(0,L['kopurua']):
        print(L['zenbakiak'][ind]);

def minimoaren_posizioa_topatu(L,nundik_hasi):
#Sarrera: zenbaki osoz eratutako zerrenda bat
#Aurre: 0 <= nundik_hasi < len(L)
#Irteera: nundik_hasi posiziotik hasita 
#nun dago elementurik txikiena
#Post: 0 <= emaitza < len(L)
        ?????
    return(L);

def ordezkatu(L,egungoPos,txikienaPos):
#Sarrera: zenbaki osoz eratutako zerrenda bat
#Aurre: 0 <= egungoPos,txikienaPos < len(L)
# eta egungoPos<=txikienaPos
#Irteera: L[egungoPos]-ean
#L[egungoPos..azkena]
#tarteko elementurik txikiena egongo da 
#Post: L[egungoPos] <= L[txikienaPos]

    ??????
    ?????


def ordenazioa_hautaketaz(L):
    ????
    
    return(L);

def proba_ordenazioa_hautaketaz():
     #hasieratu
     Lista1=[1,5,3,4,10,8,13,24,15,11]
     
     
     ###txertatu hasieran
     print("Hasierako zerrendak (1,5,3,4,10,8,13,24,15,11) zenbakiz osatuta dago:");
     idatzi_lista(Lista1);

     Lista1=ordenazioa_hautaketaz(Lista1);
     print("zerrenda (1,3,4,5,8,10,11,13,15,24) eman beharko luke eta ematen du:");
     idatzi_lista(Lista1);
        
proba_ordenazioa_hautaketaz();
