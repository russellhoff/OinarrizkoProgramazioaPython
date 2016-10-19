def idatzi_lista(L):
    for ind in range(0,10):
        print(L[ind]);



def ordenatu_burbuilaz(L):
    ????
    
    return(L);

def proba_ordenatu_burbuilaz():
     #hasieratu
     Lista1=[None]*10
     Lista1[0]=1;
     Lista1[1]=5;
     Lista1[2]=3;
     Lista1[3]=4;
     Lista1[4]=10;
     Lista1[5]=8;
     Lista1[6]=13;
     Lista1[7]=24;
     Lista1[8]=15;
     Lista1[9]=11;
     
     ###txertatu hasieran
     print("Hasierako zerrendak (1,5,3,4,10,8,13,24,15,11) zenbakiz osatuta dago:");
     idatzi_lista(Lista1);

     Lista1=ordenatu_burbuilaz(Lista1);
     print("zerrenda (1,3,4,5,8,10,11,13,15,24) eman beharko luke eta ematen du:");
     idatzi_lista(Lista1);
        
proba_ordenatu_burbuilaz();
