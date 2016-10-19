def matrizean_badago(M,zenb):
#Sarrera: 10*10 dimentsioatako matrize bat
#Aurre: M zenbaki osoz eratuta dago, zenb zenbaki oso bat da
#Irteera: zenb elementuaren posizioa bilatuko da, beraz lerro eta zutabe bat bueltatuko dira
#Post: lerroa (0..9) arteko balio bat hartuko du, baita zutabea ere.
#      Bai lerroa eta bai zutabea -1 balioko dute zenb ez bada M-ren balio bat

    lerroBat=[None]*10;	
    x=-1;
    y=-1;
    ?????



    return(x,y);
    
    
def proba_matrizean_badago():
    lerro=[None]*10;
    Matrize=[lerro]*10;
    
    #badago elementua hasieran
    print("Matrizea hurrengoa da: ");
    Matrize[0]=[1,2,3,4,5,6,7,8,9,10];
    Matrize[1]=[11,12,13,14,15,16,17,18,19,20];
    Matrize[2]=[21,22,23,24,25,26,27,28,29,30];
    Matrize[3]=[31,32,33,34,35,36,37,38,39,40];
    Matrize[4]=[41,2,3,4,55,6,7,8,9,10];
    Matrize[5]=[51,2,3,4,5,67,7,8,9,10];
    Matrize[6]=[61,2,3,4,5,6,79,8,9,10];
    Matrize[7]=[71,2,3,4,5,6,7,83,9,10];
    Matrize[8]=[81,2,3,4,5,6,73,8,93,10];
    Matrize[9]=[91,2,3,4,5,6,7,85,93,10];
    for ind in range(0,10):
        print(Matrize[ind]);
    print("matrizean_badago(Matrize,1) deiak \n(0,0) bueltatu beharko luke");
    print("Eta zure azpiprogramak bueltatzen du:");
    (nunX,nunY)=matrizean_badago(Matrize,1);
    print(nunX,nunY);
    
    #badago elementua erdian
    print("Matrizea hurrengoa da: ");
    Matrize[0]=[1,2,3,4,5,6,7,8,9,10];
    Matrize[1]=[11,12,13,14,15,16,17,18,19,20];
    Matrize[2]=[21,22,23,24,25,26,27,28,29,30];
    Matrize[3]=[31,32,33,34,35,36,37,38,39,40];
    Matrize[4]=[41,2,3,4,55,6,7,8,9,10];
    Matrize[5]=[51,2,3,4,5,67,7,8,9,10];
    Matrize[6]=[61,2,3,4,5,6,79,8,9,10];
    Matrize[7]=[71,2,3,4,5,6,7,83,9,10];
    Matrize[8]=[81,2,3,4,5,6,73,8,93,10];
    Matrize[9]=[91,2,3,4,5,6,7,85,93,10];
    for ind in range(0,10):
        print(Matrize[ind]);
    print("matrizean_badago(Matrize,21) deiak \n(2,0) bueltatu beharko luke");
    print("Eta zure azpiprogramak bueltatzen du:");
    (nunX,nunY)=matrizean_badago(Matrize,21);
    print(nunX,nunY);
    
      #badago elementua bukaeran
    print("Matrizea hurrengoa da: ");
    Matrize[0]=[1,2,3,4,5,6,7,8,9,10];
    Matrize[1]=[11,12,13,14,15,16,17,18,19,20];
    Matrize[2]=[21,22,23,24,25,26,27,28,29,30];
    Matrize[3]=[31,32,33,34,35,36,37,38,39,40];
    Matrize[4]=[41,2,3,4,55,6,7,8,9,10];
    Matrize[5]=[51,2,3,4,5,67,7,8,9,10];
    Matrize[6]=[61,2,3,4,5,6,79,8,9,10];
    Matrize[7]=[71,2,3,4,5,6,7,83,9,10];
    Matrize[8]=[81,2,3,4,5,6,73,8,93,10];
    Matrize[9]=[91,2,3,4,5,6,7,85,93,100];
    for ind in range(0,10):
        print(Matrize[ind]);
        
    print("matrizean_badago(Matrize,100) deiak \n(9,9) bueltatu beharko luke");
    print("Eta zure azpiprogramak bueltatzen du:");
    (nunX,nunY)=matrizean_badago(Matrize,100);
    print(nunX,nunY);
    
       #ez dago elementua
    print("Matrizea hurrengoa da: ");
    Matrize[0]=[1,2,3,4,5,6,7,8,9,10];
    Matrize[1]=[11,12,13,14,15,16,17,18,19,20];
    Matrize[2]=[21,22,23,24,25,26,27,28,29,30];
    Matrize[3]=[31,32,33,34,35,36,37,38,39,40];
    Matrize[4]=[41,2,3,4,55,6,7,8,9,10];
    Matrize[5]=[51,2,3,4,5,67,7,8,9,10];
    Matrize[6]=[61,2,3,4,5,6,79,8,9,10];
    Matrize[7]=[71,2,3,4,5,6,7,83,9,10];
    Matrize[8]=[81,2,3,4,5,6,73,8,93,10];
    Matrize[9]=[91,2,3,4,5,6,7,85,93,100];
    for ind in range(0,10):
        print(Matrize[ind]);
        
    print("matrizean_badago(Matrize,200) deiak \n(-1,-1) bueltatu beharko luke");
    print("Eta zure azpiprogramak bueltatzen du:");
    (nunX,nunY)=matrizean_badago(Matrize,200);
    print(nunX,nunY);
  
proba_matrizean_badago()
