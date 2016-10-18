def trukatu (a, b):
    aux = b
    b = a
    a = aux
    return a,b

def ordenatuBI (a, b):
    if a < b:
        a,b=trukatu(a, b)
    return a,b

#
# Hiru zenbaki ordenatzen ditu handienetik txikienera.
#
def ordenatuHIRU (a, b, c):
    # Pasadak honela jarri
    atera = False
    while not atera:
        a,b=ordenatuBI(a, b)
        b,c=ordenatuBI(b, c)
        a,c=ordenatuBI(a, c)
        if a >= b & b >= c:
            atera = True
    
    return a,b,c

def proba():
	#guztiz desordenatuta
	# 1, 2, 3
	n1=1
	n2=2
	n3=3
	n1,n2,n3=ordenatuHIRU(n1,n2,n3)
	print "1,2,3 Zuen programak idatzi behar du 3 2 1 eta idazten du: %d %d %d" %(n1,n2,n3)
    
    # 1, 3, 2
    n1=1
    n2=3
    n3=2
    n1,n2,n3=ordenatuHIRU(n1,n2,n3)
    print "1,3,2 Zuen programak idatzi behar du 3 2 1 eta idazten du: %d %d %d" %(n1,n2,n3)

    # 2, 1, 3
    n1=1
    n2=1
    n3=3
    n1,n2,n3=ordenatuHIRU(n1,n2,n3)
    print "2,1,3 Zuen programak idatzi behar du 3 2 1 eta idazten du: %d %d %d" %(n1,n2,n3)

    # 2, 3, 1
    n1=2;
    n2=3;
    n3=1;
    n1,n2,n3=ordenatuHIRU(n1,n2,n3)
    print "2,3,1 Zuen programak idatzi behar du 3 2 1 eta idazten du: %d %d %d" %(n1,n2,n3)

    # 3, 1, 2
    n1=3;
    n2=1;
    n3=2;
    n1,n2,n3=ordenatuHIRU(n1,n2,n3)
    print "3,1,2 Zuen programak idatzi behar du 3 2 1 eta idazten du: %d %d %d" %(n1,n2,n3)

    # 3, 2, 1
    n1=3;
    n2=2;
    n3=1;
    n1,n2,n3=ordenatuHIRU(n1,n2,n3)
    print "3,2,1 Zuen programak idatzi behar du 3 2 1 eta idazten du: %d %d %d" %(n1,n2,n3)

    """
        Nire proba kasuak (jon):
        
        HIRU ZENBAKI EZBERDIN
        n1    n2    n3
        1     2     3     <-     desordenatuta
        1     3     2     <-     desordenatuta
        2     1     3     <-     desordenatuta
        2     3     1     <-     desordenatuta
        3     1     2     <-     desordenatuta
        3     2     1     <-     ordenatuta
        
        BI ZENBAKI EZBERDIN
        
    """

proba()
