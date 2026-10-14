from object_3d import *
from definition_3d import *
 
t1 = point(-50,0,10)
t2 = point(50,0,10)
t3 = point(50,100,10)
t4 = point(-50,100,10)

test = carre(t1,t2,t3,t4)

p1 = point(-100,-50,100)
p2 = point(100,150,10)

l1 = ligne(t1,t2)
l2 = ligne(t2,t3)
l3 = ligne(t3,t4)
l4 = ligne(t4,t1)

listes2 = [l1, l2, l3, l4]


l = ligne(p1,p2)

centre = point(0,0,0)

listes = donne_ligne_transformer(l,test,centre)


affichage_liste(listes)

affichage_liste(listes2)


