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
	# 2, 5, 7
	n1=2;
	n2=5;
	n3=7;
	n1,n2,n3=ordenatuHIRU(n1,n2,n3)
	print "2,5,7 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3);

	# 2, 7, 5
	n1=2;
	n2=7;
	n3=5;
	n1,n2,n3=ordenatuHIRU(n1,n2,n3)
	print "2,7,5 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3);

	# 7, 2, 5
	n1=7;
	n2=2;
	n3=5;
	n1,n2,n3=ordenatuHIRU(n1,n2,n3)
	print "7,2,5 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3);

	# 7, 5, 2
	n1=7;
	n2=5;
	n3=2;
	n1,n2,n3=ordenatuHIRU(n1,n2,n3)
	print "7,5,2 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3);

	# 2, 5, 7
	n1=2;
	n2=5;
	n3=7;
	n1,n2,n3=ordenatuHIRU(n1,n2,n3)
	print "2,5,7 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3);

	# 2, 7, 5
	n1=2;
	n2=7;
	n3=5;
	n1,n2,n3=ordenatuHIRU(n1,n2,n3)
	print "2,7,5 Zuen programak idatzi behar du 7 5 2 eta idazten du: %d %d %d" %(n1,n2,n3);

proba()
