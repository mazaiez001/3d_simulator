from object_3d_2 import *
from definition_3d_2 import *
from turtle import *

 
# carre1 = carre(point(-50,100,2), point(50,100,2), point(50,-100,2), point(-50,-100,2))

# carre3 = carre(point(-200,100,10), point(-100,100,10), point(-100,-100,10), point(-200,-100,10))

#carre21 = carre(point(-20+a,10,2), point(-10+a,10,3), point(-10+a,-10,3), point(-20+a,-10,2))
#carre22 = carre(point(-10+a,10,3), point(10+a,10,3), point(10+a,-10,3), point(-10+a,-10,3))
#carre23 = carre(point(10+a,10,3), point(20+a,10,2), point(20+a,-10,2), point(10+a,-10,3))
#carre24 = carre(point(-28+a,15,2.4),point(-10+a,15,2.4),point(-10+a,-15,2.4),point(-28+a,-15,2.4))
#carre2 = carre(point(-30+a,5,2.5), point(30+a,5,2.5), point(30+a,-5,2.5), point(-30+a,-5,2.5))
#liste_carre = [carre21,carre22,carre23,carre24,carre2]
# carre21 = carre(point(-20+a,10+c,2+b), point(-10+a,10+c,3+b), point(-10+a,-10+c,3 +b), point(-20+a,-10+c,2+b))
# carre22 = carre(point(-10+a,10+c,3+b), point(10+a,10+c,3+b), point(10+a,-10+c,3 +b), point(-10+a,-10+c,3+b))
# carre23 = carre(point(10+a,10+c,3+b), point(20+a,10+c,2+b), point(20+a,-10+c,2 +b), point(10+a,-10+c,3+b))
# carre24 = carre(point(-28+a,15+c,2.4+b),point(-10+a,15+c,2.4+b),point(-10+a,-15+c,2.4 +b),point(-28+a,-15+c,2.4+b))
# carre2 = carre(point(-30+a,5+c,2.5 +b), point(30+a,5+c,2.5+b), point(30+a,-5+c,2.5 +b), point(-30+a,-5+c,2.5+b))

# carre21 = carre(point(-20,10,2), point(-10,10,3), point(-10,-10,3), point(-20,-10,2))
# carre22 = carre(point(-10,10,3), point(10,10,3), point(10,-10,3), point(-10,-10,3))
# carre23 = carre(point(10,10,3), point(20,10,2), point(20,-10,2 ), point(10,-10,3))
# carre24 = carre(point(-28,15,2.4),point(-10,15,2.4),point(-10,-15,2.4 ),point(-28,-15,2.4))
# carre2 = carre(point(-30,5,2.5), point(30,5,2.5), point(30,-5,2.5), point(-30,-5,2.5))    
# liste_carre = [carre2,carre22,carre23,carre24,carre21] 

b = 0
a = 0
while True:
    b += 0.001
    a += b
    a += 0.01
    carre21 = carre(point(-2,1,23), point(-1-0.1,1,26), point(-1-0.1,-1,26), point(-2,-1,23))
    carre22 = carre(point(-1,1,26.4), point(1,1,26.1), point(1,-1,26.1), point(-1,-1,26.4))
    carre23 = carre(point(1+0.1,1,26), point(2,1,23), point(2,-1,23 ), point(1+0.1,-1,26))
    carre24 = carre(point(-2.8,1.5,24),point(-1,1.5,24),point(-1,-1.5,24 ),point(-2.8,-1.5,24))
    carre2 = carre(point(-3,0.5,25), point(3,0.5,25), point(3,-0.5,25), point(-3,-0.5,25))    
    liste_carre = [carre2,carre22,carre23,carre24,carre21]
    for i in liste_carre:
    
        i.donne_rotation_carre(point(0,5,26), a )
   

    for n,k in enumerate(liste_carre):
        ##print("carre = ",n+21)
        liste_points = [k.point1, k.point2, k.point3, k.point4]
        
        for j in liste_points :

            ##print("x = ",j.x,"y = ",j.y,"z = ",j.z)
            pass


        
    affichage_liste(liste_carre)
    
    
    




a = input()


