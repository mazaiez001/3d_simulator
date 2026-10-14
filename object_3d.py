from definition_3d import *
from turtle import *



class vecteur (object):

    def __init__(self,x,y,z):

        self.x = x
        self.y = y
        self.z = z



class point (object):
    
    def __init__(self,x,y,z):
        
        self.x = x
        self.y = y
        self.z = z



class ligne (object):

    def __init__(self,point1,point2):

        self.point1 = point1
        self.point2 = point2
        x,y,z = donne_vecteur (self.point1,self.point2)
        self.vecteur = vecteur(x,y,z)



class plan (object):

    def __init__(self,vecteur,point):

        self.vecteur = vecteur
        self.point = point
        self.d = - ( (self.point.x * self.vecteur.x) + (self.point.y * self.vecteur.y) + (self.point.z * self.vecteur.z) ) 



class carre (object): 
    
    def __init__(self,point1,point2,point3,point4):

        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        x,y,z = donne_vecteur(self.point1,self.point2)
        self.vecteur1 = vecteur(x,y,z)
        x,y,z = donne_vecteur(self.point2,self.point3)
        self.vecteur2 = vecteur(x,y,z)
        x,y,z = donne_produit_vectoriel(self.vecteur1, self.vecteur2)
        self.vecteur_normal = vecteur(x,y,z)
        self.plan = plan(self.vecteur_normal,self.point1)



def donne_intersection_tirangle_plan(ligne,carre,point_centre):



    les_points = []
    x,y,z = donne_vecteur(carre.point1,carre.point2)
    v_p1_p2 = vecteur(x,y,z)
    x,y,z = donne_vecteur(point_centre,carre.point1)
    v_pc_p1 = vecteur(x,y,z)
    x,y,z = donne_produit_vectoriel(v_pc_p1,v_p1_p2)
    n_p1 = vecteur(x,y,z)
    p1 = plan(n_p1,point_centre)

    x,y,z = donne_vecteur(carre.point2,carre.point3)
    v_p2_p3 = vecteur(x,y,z)
    x,y,z = donne_vecteur(point_centre,carre.point2)
    v_pc_p2 = vecteur(x,y,z)
    x,y,z = donne_produit_vectoriel(v_pc_p2,v_p2_p3)
    n_p2 = vecteur(x,y,z)
    p2 = plan(n_p2,point_centre)
    
    x,y,z = donne_vecteur(carre.point3,carre.point4)
    v_p3_p4 = vecteur(x,y,z)
    x,y,z = donne_vecteur(point_centre,carre.point3)
    v_pc_p3 = vecteur(x,y,z)
    x,y,z = donne_produit_vectoriel(v_pc_p3,v_p3_p4)
    n_p3 = vecteur(x,y,z)
    p3 = plan(n_p3,point_centre)
    
    x,y,z = donne_vecteur(carre.point4,carre.point1)
    v_p4_p1 = vecteur(x,y,z)
    x,y,z = donne_vecteur(point_centre,carre.point4)
    v_pc_p4 = vecteur(x,y,z)
    x,y,z = donne_produit_vectoriel(v_pc_p4,v_p4_p1)
    n_p4 = vecteur(x,y,z)
    p4 = plan(n_p4,point_centre)

    n_p0 = vecteur(0,0,0)

    if n_p1 == n_p0 or n_p2 == n_p0 or n_p3 == n_p0 or n_p4 == n_p0 :
        
        
        return les_points
    
    if donne_ver_inter_ligne_plan(ligne,p1) :

        print ("inter1")

        x_inter,y_inter,z_inter = donne_inter_ligne_plan(ligne,p1)
        point_intersection = point(x_inter,y_inter,z_inter)
        
        distance = 1000
        
        d_pt1 = donne_distance_entre_points(point_centre,carre.point1)
        d_pt2 = donne_distance_entre_points(point_centre,carre.point2)

        rapport1 = distance / d_pt1
        rapport2 = distance / d_pt2

        pt1 = point(carre.point1.x * rapport1, carre.point1.y * rapport1, carre.point1.z * rapport1)
        pt2 = point(carre.point2.x * rapport2, carre.point2.y * rapport2, carre.point2.z * rapport2)

        if ver_point_dans_triangle(point_intersection,point_centre,pt1,pt2) == True and ver_point_dans_triangle(point_intersection,point_centre,carre.point1,carre.point2) == False:

            les_points.append(point_intersection)
            print ("test1")
    

    if donne_ver_inter_ligne_plan(ligne,p2) :
       
        print ("inter2")

        x_inter,y_inter,z_inter = donne_inter_ligne_plan(ligne,p2)
        point_intersection = point(x_inter,y_inter,z_inter)
        
        distance = 1000
        
        d_pt2 = donne_distance_entre_points(point_centre,carre.point2)
        d_pt3 = donne_distance_entre_points(point_centre,carre.point3)

        rapport1 = distance / d_pt2
        rapport2 = distance / d_pt3

        pt2 = point(carre.point2.x * rapport1, carre.point2.y * rapport1, carre.point2.z * rapport1)
        pt3 = point(carre.point3.x * rapport2, carre.point3.y * rapport2, carre.point3.z * rapport2)

        if ver_point_dans_triangle(point_intersection,point_centre,pt2,pt3) == True and ver_point_dans_triangle(point_intersection,point_centre,carre.point2,carre.point3) == False:

            les_points.append(point_intersection)
            print ("test2")
    

    if donne_ver_inter_ligne_plan(ligne,p3) :

        print ("inter3")

        x_inter,y_inter,z_inter = donne_inter_ligne_plan(ligne,p3)
        point_intersection = point(x_inter,y_inter,z_inter)
        
        distance = 1000
        
        d_pt3 = donne_distance_entre_points(point_centre,carre.point3)
        d_pt4 = donne_distance_entre_points(point_centre,carre.point4)

        rapport1 = distance / d_pt3
        rapport2 = distance / d_pt4

        pt3 = point(carre.point3.x * rapport1, carre.point3.y * rapport1, carre.point3.z * rapport1)
        pt4 = point(carre.point4.x * rapport2, carre.point4.y * rapport2, carre.point4.z * rapport2)

        if ver_point_dans_triangle(point_intersection,point_centre,pt3,pt4) == True and ver_point_dans_triangle(point_intersection,point_centre,carre.point3,carre.point4) == False:

            les_points.append(point_intersection)
            print ("test3")
    

    if donne_ver_inter_ligne_plan(ligne,p4) :

        print ("inter4")

        x_inter,y_inter,z_inter = donne_inter_ligne_plan(ligne,p4)
        point_intersection = point(x_inter,y_inter,z_inter)
        
        distance = 1000
        
        d_pt4 = donne_distance_entre_points(point_centre,carre.point4)
        d_pt1 = donne_distance_entre_points(point_centre,carre.point1)

        rapport1 = distance / d_pt4
        rapport2 = distance / d_pt1

        pt4 = point(carre.point4.x * rapport1, carre.point4.y * rapport1, carre.point4.z * rapport1)
        pt1 = point(carre.point1.x * rapport2, carre.point1.y * rapport2, carre.point1.z * rapport2)

        if ver_point_dans_triangle(point_intersection,point_centre,pt4,pt1) == True and ver_point_dans_triangle(point_intersection,point_centre,carre.point4,carre.point1) == False:

            les_points.append(point_intersection)
            print ("test4")
    
    return les_points



def donne_ligne_transformer(ligne_choisie,carre,point_centre):

    ligne_transformer = []
    
    les_intersection = donne_intersection_tirangle_plan(ligne_choisie,carre,point_centre)
    
    n = len(les_intersection)

    distance_ligne = donne_distance_entre_points(ligne_choisie.point1,ligne_choisie.point2)
    distance_intersection = donne_distance_entre_points(les_intersection[0],les_intersection[1])
    
    d_i1_p1 = donne_distance_entre_points(les_intersection[0],ligne_choisie.point1)
    d_i1_p2 = donne_distance_entre_points(les_intersection[0],ligne_choisie.point2)

    d_i2_p1 = donne_distance_entre_points(les_intersection[1],ligne_choisie.point1)
    d_i2_p2 = donne_distance_entre_points(les_intersection[1],ligne_choisie.point2)
    
    if n >= 2 and n < 5 :
        

        if (( d_i1_p1 + d_i1_p2 ) == distance_ligne) and ( ( d_i2_p1 + d_i2_p2 ) == distance_ligne) :

            
            if d_i2_p2 < d_i1_p2 :
            
                ligne1 = ligne(ligne_choisie.point1,les_intersection[0])
                ligne2 = ligne(ligne_choisie.point2,les_intersection[1])

            else:
        
                ligne1 = ligne(ligne_choisie.point1,les_intersection[1])
                ligne2 = ligne(ligne_choisie.point2,les_intersection[0])
           
            
            ligne_transformer = [ligne1,ligne2]
 

        elif (( d_i1_p1 + d_i1_p2 ) == distance_ligne) and ( ( d_i2_p1 + d_i2_p2 ) != distance_ligne) :
           

            if (d_i1_p1 + d_i1_p1) == distance_intersection :
                
                ligne1 = ligne(ligne_choisie.point2,les_intersection[0])


            else : 
                
                ligne1 = ligne(ligne_choisie.point1,les_intersection[0])
            

            ligne_transformer = [ligne1]
        
        elif (( d_i1_p1 + d_i1_p2 ) != distance_ligne) and ( ( d_i2_p1 + d_i2_p2 ) == distance_ligne):


            if (d_i1_p2 + d_i2_p1) == distance_intersection :
                
                ligne2 = ligne(ligne_choisie.point1,les_intersection[1])


            else : 
                
                ligne2 = ligne(ligne_choisie.point2,les_intersection[1])
            

            ligne_transformer = [ligne2]

        return ligne_transformer


    else:
       
        ligne_transformer = [ligne_choisie]
       
        return ligne_transformer



def affichage_liste(liste_affichage):
    
    
    vn_p = vecteur(0,0,1)
    point_p = point(0,0,9)
    p = plan(vn_p,point_p)
    centre = point(0,0,0)

    for lignes in liste_affichage:

        l1 = ligne(centre,lignes.point1)
        l2 = ligne(centre,lignes.point2)
        
        x,y,z = donne_inter_ligne_plan(l1,p)
        p1 = point(x,y,z)

        x,y,z = donne_inter_ligne_plan(l2,p)
        p2 = point(x,y,z)

        penup()
        goto(p1.x,p1.y)
        pendown()
        goto(p2.x,p2.y)
        penup()

     


        
    











    





