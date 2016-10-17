def zifraKop(???):
#Espezifikazioa:
#Sarrera: zenbaki osoko bat. 
#   Aurre: zenbakiaren balioa > 0.
#Irteera: zenbaki bat
#   Post: zenbaki bat, sarrerako zenbakiaren digitu kopurua 
    kont=0;
    
    return(???);

def kodeaEgokiaDa(???):
#Espezifikazioa:
#Sarrera: zenbaki osoko bat. 
#   Aurre: 0 baino handiagoa den zenbaki bat .
#Irteera: boolear bat
#   Post: Zenbakiak 4 zifra izanez gero, aurreneko zifrak 1 eta 9 arteko balioa izango du
#   Zenbakiak 5 zifra izanez gero, aurreneko bi zifren balioak 10 eta 52 artekoa izango da      
    emaitza=False;
   


    return(???);

def hiriarenKodea(???):
#Espezifikazioa:
#Sarrera: bi zenbaki. lehenengoa posta kodea da eta bigarrena posta kodearen digitu kopurua
#   Aurre: zenbakiak osokoak dira.
#Irteera: zenbaki bat
#   Post: zenbaki bat, sarrerako digitu kopuruaren arabera, zifra bat edo bi itzuliko ditu
   


    return(???);

def posta_kodea_eta_probintzia_bera_dira(kod1,kod2):
 #Espezifikazioa:
 #Sarrera: 2 zenbaki osokoak
 #Aurre: cod1 eta cod2 >0
 #Irteera: boolear bat kodeak diren esateko
 #         eta kod1 eta kod2-ren herriei dagozkien kodeak berdinak diren esateko   
 #Post: 1. boolearrak true balioko du kod1 eta kod2 posta kode egokiak badira
 #      bestela false
 #      kodX 4 zenbakiz osatuta dagoenean herriari dagkion kodea
 #      01-09 tarteko zenbaki bat izango da kode egokia izateko
 #      kodX 5 zenbakiz osatuta dogoenean herriaren kodea
 #      10-52 artean egongo da kode egokia izateko 
 #      2. boolearrak true balioko du kod1 eta kod2 hiri berdineko posta kodeak badira
 #      bestela false

    
    berdinak=False;
    egokiak=False;

	???
   
    return(egokiak,berdinak);

def proba():
    kode1=48004;
    kode2=48002;
    (egokiak,berdinak)=posta_kodea_eta_probintzia_bera_dira(kode1,kode2);
    print "48004 eta 48002 kode egokiak eta herri berdinekoak dira,";
    print "eta zure programak esaten du: "; 
    if(egokiak):
        print "egokiak dira";
        if(berdinak):
            print " eta herri berdinekoak direla";
        else:
            print " baina herri desberdinekoak direla";
    else:
        print "biak (edo bat) ez dira egokiak";
    print "\n\n";
    
    kode1=50004;
    kode2=48002;
    (egokiak,berdinak)=posta_kodea_eta_probintzia_bera_dira(kode1,kode2);
    print "50004 eta 48002 kode egokiak baina herri desberdinekoak dira,";
    print "eta zure programak esaten du: "; 
    if(egokiak):
        print "egokiak dira";
        if(berdinak):
            print " eta herri berdinekoak direla";
        else:
            print " baina herri desberdinekoak direla";
    else:
        print "biak (edo bat) ez dira egokiak";
    print "\n\n";
    
    
    kode1=1004;
    kode2=1002;
    (egokiak,berdinak)=posta_kodea_eta_probintzia_bera_dira(kode1,kode2);
    print "1004 eta 1002 kode egokiak eta herri berdinekoak dira,";
    print "eta zure programak esaten du: "; 
    if(egokiak):
        print "egokiak dira";
        if(berdinak):
            print " eta herri berdinekoak direla";
        else:
            print " baina herri desberdinekoak direla";
    else:
        print "biak (edo bat) ez dira egokiak";
    print "\n\n";
    
    
    kode1=2004;
    kode2=1002;
    (egokiak,berdinak)=posta_kodea_eta_probintzia_bera_dira(kode1,kode2);
    print "2004 eta 1002 kode egokiak baina herri desberdinekoak dira,";
    print "eta zure programak esaten du: "; 
    if(egokiak):
        print "egokiak dira";
        if(berdinak):
            print " eta herri berdinekoak direla";
        else:
            print " baina herri desberdinekoak direla";
    else:
        print "biak (edo bat) ez dira egokiak";
    print "\n\n";
    
    
    kode1=204;
    kode2=1002;
    (egokiak,berdinak)=posta_kodea_eta_probintzia_bera_dira(kode1,kode2);
    print "204 ez da kode egokia";
    print "eta zure programak esaten du: "; 
    if(egokiak):
        print "egokiak dira";
        if(berdinak):
            print " eta herri berdinekoak direla";
        else:
            print " baina herri desberdinekoak direla";
    else:
        print "biak (edo bat) ez dira egokiak";
    print "\n\n";
    
proba()

